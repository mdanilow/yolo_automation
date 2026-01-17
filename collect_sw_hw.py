import pandas as pd


hw_summary_file = "summary_lut.csv"
eval_results_file = "collected_eval_results.csv"

collected_results = {}
# with open(hw_summary_file, "r") as file


with open(hw_summary_file, "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        print(line)
        line = line.split(",")
        model = line[0].removesuffix("_30fps_hls")
        fps = float(line[1])
        lut = int(float(line[2]))
        mac_eff = float(line[5].removesuffix("%\n"))
        collected_results[model] = [fps, lut, mac_eff]

with open(eval_results_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.split(",")
        collected_results[line[0]] += [float(line[1])]

results = "model,fps,lut,mac_efficiency,mAP\n"
keys = list(collected_results.keys())
for k in keys:
    data = collected_results[k]
    if len(data) == 3:
        data.append("XXX")
    line = ",".join(["{}"] * 5) + "\n"
    line = line.format(
        k,
        *data
    )
    results += line
print(results)
with open("collected_results.csv", "w") as file:
    file.write(results)
# print(collected_results)
# print(hw_summary)