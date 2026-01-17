import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('collected_results_xd.csv')

# Clean data
df['mAP'] = pd.to_numeric(df['mAP'], errors='coerce')
df['lut'] = pd.to_numeric(df['lut'], errors='coerce')
df = df.dropna(subset=['mAP', 'lut'])

# Parse 'model' column to extract features
def parse_model_name(name):
    parts = name.split('_')
    if len(parts) >= 3:
        quant = parts[0]
        arch = parts[1]
        res = parts[2]
        return quant, arch, res
    else:
        return name, name, name

df[['Kwantyzacja', 'Architektura', 'Resolution']] = df['model'].apply(
    lambda x: pd.Series(parse_model_name(x))
)

# Define custom RGB palette for Architectures
# We sort them to ensure consistent assignment: n->red, p->green, s->blue
unique_archs = sorted(df['Architektura'].unique())
palette_mapping = {
    unique_archs[0]: 'red',
    unique_archs[1]: 'green',
    unique_archs[2]: 'blue'
}

# Calculate Pareto Front
df_sorted = df.sort_values(by=['lut', 'mAP'], ascending=[True, False])
pareto_front = []
current_max_map = -float('inf')

for index, row in df_sorted.iterrows():
    if row['mAP'] > current_max_map:
        pareto_front.append(row)
        current_max_map = row['mAP']

pareto_df = pd.DataFrame(pareto_front)

# Create plot
plt.figure(figsize=(12, 8))

# Scatter plot using custom palette
sns.scatterplot(
    data=df,
    x='lut',
    y='mAP',
    hue='Architektura',
    style='Kwantyzacja',
    s=150,
    palette=palette_mapping,
    zorder=2
)

# Annotate points
for i, row in df.iterrows():
    plt.text(
        row['lut'], 
        row['mAP'], 
        f" {row['Resolution']}", 
        fontsize=9, 
        ha='left', 
        va='bottom'
    )

# Draw Pareto Front line
plt.plot(
    pareto_df['lut'], 
    pareto_df['mAP'], 
    color='black', 
    linestyle='--', 
    linewidth=1, 
    label='Front Pareto', 
    zorder=1
)

plt.title('Jakość detekcji (mAP) vs zużycie zasobów FPGA LUT')
plt.xlabel('LUT')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.savefig('map_vs_lut_rgb.png')
plt.show()