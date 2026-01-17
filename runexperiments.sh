# python build_yolov8.py --EXP_NAME estimates_3w3a_yolov8p_640_30fps --MODEL_ONNX build/test_3w3a_yolov8p_640/intermediate_models/step_specialize_layers.onnx --FOLDING_CONFIG folding_configs/9830400.json --BUILD_TYPE set_folding
# python build_yolov8.py --EXP_NAME analysis_3w3a_yolov8p_640_hls --MODEL_ONNX exports/3w3a_yolov8p_640.onnx --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --TARGET_FPS 30 --ANALYZE_MAC_EFFICIENCY --BUILD_TYPE analysis
# python build_yolov8.py --EXP_NAME analysis_3w3a_yolov8s_640_hls --MODEL_ONNX exports/3w3a_yolov8s_640.onnx --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --TARGET_FPS 30 --ANALYZE_MAC_EFFICIENCY --BUILD_TYPE analysis

# 3-bit
# python build_yolov8.py --EXP_NAME build_3w3a_yolov8p_640_30fps_hls --MODEL_ONNX exports/3w3a_yolov8p_640.onnx --FOLDING_CONFIG folding_configs/yolov8p_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_3w3a_yolov8p_480_30fps_hls --MODEL_ONNX exports/3w3a_yolov8p_480.onnx --FOLDING_CONFIG folding_configs/yolov8p_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# python build_yolov8.py --EXP_NAME build_3w3a_yolov8n_640_30fps_hls --MODEL_ONNX exports/3w3a_yolov8n_640.onnx --FOLDING_CONFIG folding_configs/yolov8n_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_3w3a_yolov8n_480_30fps_hls --MODEL_ONNX exports/3w3a_yolov8n_480.onnx --FOLDING_CONFIG folding_configs/yolov8n_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# python build_yolov8.py --EXP_NAME build_3w3a_yolov8s_640_30fps_hls --MODEL_ONNX exports/3w3a_yolov8s_640.onnx --FOLDING_CONFIG folding_configs/yolov8s_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_3w3a_yolov8s_480_30fps_hls --MODEL_ONNX exports/3w3a_yolov8s_480.onnx --FOLDING_CONFIG folding_configs/yolov8s_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# 4-bit
# python build_yolov8.py --EXP_NAME build_4w4a_yolov8p_640_30fps_hls --MODEL_ONNX exports/4w4a_yolov8p_640.onnx --FOLDING_CONFIG folding_configs/yolov8p_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_4w4a_yolov8p_480_30fps_hls --MODEL_ONNX exports/4w4a_yolov8p_480.onnx --FOLDING_CONFIG folding_configs/yolov8p_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_4w4a_yolov8p_320_30fps_hls --MODEL_ONNX exports/4w4a_yolov8p_320.onnx --FOLDING_CONFIG folding_configs/yolov8p_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# python build_yolov8.py --EXP_NAME build_4w4a_yolov8n_640_30fps_hls --MODEL_ONNX exports/4w4a_yolov8n_640.onnx --FOLDING_CONFIG folding_configs/yolov8n_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_4w4a_yolov8n_480_30fps_hls --MODEL_ONNX exports/4w4a_yolov8n_480.onnx --FOLDING_CONFIG folding_configs/yolov8n_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_4w4a_yolov8n_320_30fps_hls --MODEL_ONNX exports/4w4a_yolov8n_320.onnx --FOLDING_CONFIG folding_configs/yolov8n_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# python build_yolov8.py --EXP_NAME build_4w4a_yolov8s_640_30fps_hls --MODEL_ONNX exports/4w4a_yolov8s_640.onnx --FOLDING_CONFIG folding_configs/yolov8s_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_4w4a_yolov8s_480_30fps_hls --MODEL_ONNX exports/4w4a_yolov8s_480.onnx --FOLDING_CONFIG folding_configs/yolov8s_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_4w4a_yolov8s_320_30fps_hls --MODEL_ONNX exports/4w4a_yolov8s_320.onnx --FOLDING_CONFIG folding_configs/yolov8s_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# 8-bit
# python build_yolov8.py --EXP_NAME build_8w8a_yolov8p_640_30fps_hls --MODEL_ONNX exports/8w8a_yolov8p_640.onnx --FOLDING_CONFIG folding_configs/yolov8p_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_8w8a_yolov8p_480_30fps_hls --MODEL_ONNX exports/8w8a_yolov8p_480.onnx --FOLDING_CONFIG folding_configs/yolov8p_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_8w8a_yolov8p_320_30fps_hls --MODEL_ONNX exports/8w8a_yolov8p_320.onnx --FOLDING_CONFIG folding_configs/yolov8p_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# python build_yolov8.py --EXP_NAME build_8w8a_yolov8n_640_30fps_hls --MODEL_ONNX exports/8w8a_yolov8n_640.onnx --FOLDING_CONFIG folding_configs/yolov8n_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_8w8a_yolov8n_480_30fps_hls --MODEL_ONNX exports/8w8a_yolov8n_480.onnx --FOLDING_CONFIG folding_configs/yolov8n_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_8w8a_yolov8n_320_30fps_hls --MODEL_ONNX exports/8w8a_yolov8n_320.onnx --FOLDING_CONFIG folding_configs/yolov8n_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full

# python build_yolov8.py --EXP_NAME build_8w8a_yolov8s_640_30fps_hls --MODEL_ONNX exports/8w8a_yolov8s_640.onnx --FOLDING_CONFIG folding_configs/yolov8s_640_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_8w8a_yolov8s_480_30fps_hls --MODEL_ONNX exports/8w8a_yolov8s_480.onnx --FOLDING_CONFIG folding_configs/yolov8s_480_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full
# python build_yolov8.py --EXP_NAME build_8w8a_yolov8s_320_30fps_hls --MODEL_ONNX exports/8w8a_yolov8s_320.onnx --FOLDING_CONFIG folding_configs/yolov8s_320_30fps_hls.json --SPECIALIZE_LAYERS_CONFIG specialize_layers_configs/mvaus_hls.json --BUILD_TYPE full