import os
from os.path import join

import json


BUILD_DIR = "build"

results = "model,fps,lut,bram18k,dsp,mac_efficiency\n"
models = os.listdir(BUILD_DIR)
models.sort()
for model in models:
    if model.startswith("lutestimates_"):
        try:
            resources_json = join(BUILD_DIR, model, "report", "estimate_layer_resources.json")
            with open(resources_json, "r") as f:
                resources = json.load(f)
            performance_json = join(BUILD_DIR, model, "report", "estimate_network_performance.json")
            with open(performance_json, "r") as f:
                performance = json.load(f)
            resources = resources["total"]
            fps = performance["estimated_throughput_fps"]
            mac_efficiency = performance["mac_efficiency"]
            model_name = model.removeprefix("lutestimates_")
            print(model_name)
            results += "{},{},{},{},{},{}%\n".format(
                model_name,
                fps,
                resources["LUT"],
                resources["BRAM_18K"],
                resources["DSP"],
                round(mac_efficiency, 2)
            )
        except FileNotFoundError as e:
            print(e)

with open("summary_lut.csv", "w") as f:
    f.write(results)