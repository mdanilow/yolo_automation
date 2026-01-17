# 4-bit
python build_yolov8.py --EXP_NAME build_4w4a_yolov8p_640_30fps_hls --MODEL_ONNX exports/4w4a_yolov8p_640.onnx --FOLDING_CONFIG folding_configs/yolov8p_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
python build_yolov8.py --EXP_NAME build_4w4a_yolov8p_480_30fps_hls --MODEL_ONNX exports/4w4a_yolov8p_480.onnx --FOLDING_CONFIG folding_configs/yolov8p_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
python build_yolov8.py --EXP_NAME build_4w4a_yolov8p_320_30fps_hls --MODEL_ONNX exports/4w4a_yolov8p_320.onnx --FOLDING_CONFIG folding_configs/yolov8p_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

python build_yolov8.py --EXP_NAME build_4w4a_yolov8n_640_30fps_hls --MODEL_ONNX exports/4w4a_yolov8n_640.onnx --FOLDING_CONFIG folding_configs/yolov8n_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
python build_yolov8.py --EXP_NAME build_4w4a_yolov8n_480_30fps_hls --MODEL_ONNX exports/4w4a_yolov8n_480.onnx --FOLDING_CONFIG folding_configs/yolov8n_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
python build_yolov8.py --EXP_NAME build_4w4a_yolov8n_320_30fps_hls --MODEL_ONNX exports/4w4a_yolov8n_320.onnx --FOLDING_CONFIG folding_configs/yolov8n_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

python build_yolov8.py --EXP_NAME build_4w4a_yolov8s_640_30fps_hls --MODEL_ONNX exports/4w4a_yolov8s_640.onnx --FOLDING_CONFIG folding_configs/yolov8s_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
python build_yolov8.py --EXP_NAME build_4w4a_yolov8s_480_30fps_hls --MODEL_ONNX exports/4w4a_yolov8s_480.onnx --FOLDING_CONFIG folding_configs/yolov8s_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
python build_yolov8.py --EXP_NAME build_4w4a_yolov8s_320_30fps_hls --MODEL_ONNX exports/4w4a_yolov8s_320.onnx --FOLDING_CONFIG folding_configs/yolov8s_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
