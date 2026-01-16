import os
from os.path import join
import argparse
import shutil
import torch

# build steps
from qonnx.core.datatype import DataType
from qonnx.core.modelwrapper import ModelWrapper
from qonnx.util.config import extract_model_config_to_json
from qonnx.util.cleanup import cleanup_model
from qonnx.transformation.merge_onnx_models import MergeONNXModels
from brevitas.export import export_qonnx
from finn.util.pytorch import ToTensor
from finn.transformation.qonnx.convert_qonnx_to_finn import ConvertQONNXtoFINN
# streamline
from qonnx.transformation.lower_convs_to_matmul import LowerConvsToMatMul
from qonnx.transformation.general import (
    GiveReadableTensorNames,
    GiveUniqueNodeNames,
    ApplyConfig,
)
from qonnx.transformation.infer_data_layouts import InferDataLayouts
from qonnx.transformation.infer_datatypes import InferDataTypes
from finn.transformation.streamline import Streamline
import finn.transformation.streamline.absorb as absorb
import finn.transformation.streamline.reorder as reorder
# to hw
from qonnx.transformation.infer_shapes import InferShapes
import finn.transformation.fpgadataflow.convert_to_hw_layers as to_hw

# build
import finn.builder.build_dataflow as build
import finn.builder.build_dataflow_config as build_cfg


def step_yolov8_tidy_up(model: ModelWrapper, cfg: build_cfg.DataflowBuildConfig):
    model = model.transform(ConvertQONNXtoFINN())
    global_inp_name = model.graph.input[0].name
    ishape = model.get_tensor_shape(global_inp_name)
    chkpt_preproc_name = join(cfg.output_dir, "preproc.onnx")
    export_qonnx(ToTensor(), torch.randn(ishape), chkpt_preproc_name)
    pre_model = ModelWrapper(chkpt_preproc_name)
    pre_model = cleanup_model(pre_model)
    pre_model = pre_model.transform(ConvertQONNXtoFINN())
    model = model.transform(MergeONNXModels(pre_model))
    model.set_tensor_datatype(global_inp_name, DataType["UINT8"])
    return model


def step_yolov8_streamline(model: ModelWrapper, cfg: build_cfg.DataflowBuildConfig):
    model = model.transform(Streamline())
    model = model.transform(reorder.MoveAddPastJoinConcat())
    additional_streamline_transformations = [
        # Affine ops
        reorder.MoveScalarLinearPastSplit(),
        reorder.MoveLinearPastFork(),
        reorder.MoveMulPastJoinAdd(),
        reorder.MoveMulPastJoinConcat(),
        Streamline(),
        # Affine ops in SPPF
        reorder.MoveLinearPastFork(),
        reorder.MoveMulPastMaxPool(),
        reorder.MoveLinearPastFork(),
        reorder.MoveMulPastMaxPool(),
        reorder.MoveMulPastJoinConcat(),
        Streamline(),
        # Transposes
        LowerConvsToMatMul(),
        absorb.AbsorbTransposeIntoMultiThreshold(),
        absorb.AbsorbConsecutiveTransposes(),
        reorder.MakeScaleResizeNHWC(),
        reorder.MoveTransposePastSplit(),
        reorder.MoveTransposePastFork(),
        reorder.MoveTransposePastJoinAdd(),
        reorder.MoveTransposePastJoinConcat(),
        absorb.AbsorbConsecutiveTransposes(),
        # Transposes in SPPF
        reorder.MakeMaxPoolNHWC(),
        reorder.MoveTransposePastJoinConcat(),
        absorb.AbsorbConsecutiveTransposes()
    ]
    for trn in additional_streamline_transformations:
        model = model.transform(trn)
        model = model.transform(GiveUniqueNodeNames())
        model = model.transform(GiveReadableTensorNames())
        model = model.transform(InferDataTypes())
        model = model.transform(InferDataLayouts())
    return model


def step_yolov8_convert_to_hw_layers(model: ModelWrapper, cfg: build_cfg.DataflowBuildConfig):
    if cfg.standalone_thresholds:
        model = model.transform(to_hw.InferThresholdingLayer())
    model = model.transform(to_hw.InferQuantizedMatrixVectorActivation())
    model = model.transform(to_hw.InferPool())
    model = model.transform(to_hw.InferConvInpGen())
    model = model.transform(to_hw.InferAddStreamsLayer())
    model = model.transform(to_hw.InferConcatLayer())
    model = model.transform(to_hw.InferSplitLayer())
    model = model.transform(to_hw.InferUpsample())
    model = model.transform(to_hw.InferDuplicateStreamsLayer()) 
    
    model = model.transform(InferShapes())
    model = model.transform(InferDataTypes())
    model = model.transform(InferDataLayouts())
    model = model.transform(GiveUniqueNodeNames())
    model = model.transform(GiveReadableTensorNames())
    return model


def step_slr_floorplan(model: ModelWrapper, cfg: build_cfg.DataflowBuildConfig):
    if cfg.shell_flow_type == build_cfg.ShellFlowType.VITIS_ALVEO:
        ins = [x.name for x in model.graph.input]
        outs = [x.name for x in model.graph.output]
        last_nodes = [model.find_producer(out).name for out in outs]
        first_nodes = [model.find_consumer(inp).name for inp in ins]
        inout_nodes = first_nodes + last_nodes
        default_slr = 0
        indices = []
        floorplan_dict = {"Defaults": {}}
        print('FLOORPLANNING, nodes that are anchored to slr 0:')
        for i, node in enumerate(model.graph.node):
            if node.name in inout_nodes:
                indices.append(i)
                node_dict = {"slr": default_slr}
                floorplan_dict[node.name] = node_dict
                print(node.name, i)

        model = model.transform(ApplyConfig(floorplan_dict))
        hw_attrs = [
            "PE",
            "SIMD",
            "parallel_window",
            "ram_style",
            "depth",
            "impl_style",
            "resType",
            "mem_mode",
            "runtime_writeable_weights",
            "inFIFODepths",
            "outFIFODepths",
            "depth_trigger_uram",
            "depth_trigger_bram",
            "slr",
        ]
        extract_model_config_to_json(model, cfg.output_dir + "/final_hw_config_floorplan.json", hw_attrs)
        print("SLR floorplanning applied")
        # except Exception:
        #     print("No SLR floorplanning applied")
    return model


# determine which shell flow to use for a given platform
def platform_to_shell(platform):
    if platform in zynq_platforms:
        return build_cfg.ShellFlowType.VIVADO_ZYNQ
    elif platform in alveo_platforms:
        return build_cfg.ShellFlowType.VITIS_ALVEO
    else:
        raise Exception("Unknown platform, can't determine ShellFlowType")
    

def mhz_to_clk_ns(clk_mhz):
    clk_hz = clk_mhz * 10**6
    clk_s = 1 / clk_hz
    clk_ns = clk_s * 10**9
    return clk_ns


def cycles_to_fps(cycles, synth_clk_period_ns):
    n_clock_cycles_per_sec = 10**9 / synth_clk_period_ns
    fps = n_clock_cycles_per_sec / cycles
    return fps


build_steps_full = [
    step_yolov8_tidy_up,
    step_yolov8_streamline,
    step_yolov8_convert_to_hw_layers,
    "step_create_dataflow_partition",
    "step_specialize_layers",
    "step_target_fps_parallelization",
    "step_apply_folding_config",
    "step_minimize_bit_width",
    "step_generate_estimate_reports",
    "step_hw_codegen",
    "step_hw_ipgen",
    "step_set_fifo_depths",
    "step_create_stitched_ip",
    step_slr_floorplan,
    "step_measure_rtlsim_performance",
    "step_out_of_context_synthesis",
    "step_synthesize_bitfile",
    "step_make_pynq_driver",
    "step_deployment_package",
]

build_steps_estimates = [
    step_yolov8_tidy_up,
    step_yolov8_streamline,
    step_yolov8_convert_to_hw_layers,
    "step_create_dataflow_partition",
    "step_specialize_layers",
    "step_target_fps_parallelization",
    "step_apply_folding_config",
    "step_minimize_bit_width",
    "step_generate_estimate_reports",
]

build_steps_set_folding = [
    "step_target_fps_parallelization",
    "step_apply_folding_config",
    "step_minimize_bit_width",
    "step_generate_estimate_reports",
]

build_type_to_steps = {
    "analysis": build_steps_estimates,
    "set_folding": build_steps_set_folding,
    "full": build_steps_full,
}


parser = argparse.ArgumentParser()
parser.add_argument('--EXP_NAME', type=str, default='test')
parser.add_argument('--BOARD', type=str, default='ZCU104')
parser.add_argument('--MODEL_ONNX', type=str)
parser.add_argument('--FOLDING_CONFIG', type=str, default=None)
parser.add_argument('--TARGET_FPS', type=float, default=None)
# parser.add_argument('--TARGET_CYCLES', type=int, default=None)
parser.add_argument('--CLK_MHZ', type=float, default=300)
parser.add_argument('--BUILD_TYPE', type=str, default="analysis")
parser.add_argument('--ANALYZE_MAC_EFFICIENCY', action="store_true")
args = parser.parse_args()

# if args.TARGET_CYCLES is not None:
#     args.TARGET_FPS = cycles_to_fps(args.TARGET_CYCLES, mhz_to_clk_ns(args.CLK_MHZ))
#     print("TARGET_CYCLES set to {}, which gives {} fps".format(args.TARGET_CYCLES, args.TARGET_FPS))
specialize_layers_config_file = None
auto_fifo_depths = False

# which platforms to build the networks for
zynq_platforms = ["ZCU104", "ZCU102"]
alveo_platforms = ["U250", "U55C"]
BUILD_DIR = os.environ["FINN_BUILD_DIR"]
OUTPUT_DIR = join(BUILD_DIR, args.EXP_NAME)
build_steps = build_type_to_steps[args.BUILD_TYPE]


cfg = build.DataflowBuildConfig(
    output_dir=OUTPUT_DIR,
    verbose=True,
    standalone_thresholds=True,
    folding_config_file=args.FOLDING_CONFIG,
    specialize_layers_config_file=specialize_layers_config_file,
    auto_fifo_depths=auto_fifo_depths,
    split_large_fifos=True,
    synth_clk_period_ns=mhz_to_clk_ns(args.CLK_MHZ),
    target_fps=args.TARGET_FPS,
    analyze_mac_efficiency=args.ANALYZE_MAC_EFFICIENCY,
    board=args.BOARD,
    shell_flow_type=platform_to_shell(args.BOARD),
    steps=build_steps,
    generate_outputs=[
        build_cfg.DataflowOutputType.ESTIMATE_REPORTS,
        build_cfg.DataflowOutputType.BITFILE,
        build_cfg.DataflowOutputType.PYNQ_DRIVER,
        build_cfg.DataflowOutputType.DEPLOYMENT_PACKAGE,
    ],
)
build.build_dataflow_cfg(args.MODEL_ONNX, cfg)