# step16_heatmap.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "final_dataset_for_ml.csv"
)

meta_cols = [
    "Sample Name",
    "Patient_ID",
    "Factor Value[time point]"
]

feature_cols = [
    c for c in df.columns
    if c not in meta_cols
]

corr = df[feature_cols].corr()

plt.figure(figsize=(12,10))

im = plt.imshow(
    corr,
    aspect="auto"
)

plt.colorbar(im)

plt.xticks(
    range(len(feature_cols)),
    feature_cols,
    rotation=90
)

plt.yticks(
    range(len(feature_cols)),
    feature_cols
)

plt.title(
    "Metabolite Correlation Heatmap"
)

plt.tight_layout()

plt.savefig(
    "Correlation_Heatmap.png",
    dpi=300
)

plt.show()