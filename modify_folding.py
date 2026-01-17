import os
from os.path import join

import json


FOLDING_DIR = "folding_configs"

configs = os.listdir(FOLDING_DIR)
configs = [c for c in configs if not os.path.isdir(join(FOLDING_DIR, c))]
for config_name in configs:
    print(config_name)
    with open(join(FOLDING_DIR, config_name), "r") as f:
        dict = json.load(f)
    for module_name, module_dict in dict.items():
        if "MVAU" in module_name:
            module_dict["ram_style"] = "distributed"
            module_dict["resType"] = "lut"
    with open(join(FOLDING_DIR, config_name.removesuffix(".json") + "_alllut.json"), "w") as f:
        json.dump(dict, f, indent=2)