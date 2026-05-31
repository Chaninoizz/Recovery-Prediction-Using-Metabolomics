import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("final_dataset_for_ml.csv")

# ==========================
# Metabolite Columns
# ==========================

exclude_cols = [
    "Sample Name",
    "Patient_ID",
    "Factor Value[time point]"
]

metabolites = [
    col for col in df.columns
    if col not in exclude_cols
]

# ==========================
# Preop vs Postop
# ==========================

preop = df[
    df["Factor Value[time point]"] == "preop"
]

postop = df[
    df["Factor Value[time point]"] != "preop"
]

# ==========================
# Mean Difference
# ==========================

results = []

for metabolite in metabolites:

    pre_mean = preop[metabolite].mean()

    post_mean = postop[metabolite].mean()

    diff = post_mean - pre_mean

    abs_diff = abs(diff)

    results.append([
        metabolite,
        pre_mean,
        post_mean,
        diff,
        abs_diff
    ])

ranking = pd.DataFrame(
    results,
    columns=[
        "Metabolite",
        "Preop_Mean",
        "Postop_Mean",
        "Difference",
        "Absolute_Difference"
    ]
)

ranking = ranking.sort_values(
    "Absolute_Difference",
    ascending=False
)

print("\nTop Biomarkers")
print(
    ranking[
        [
            "Metabolite",
            "Difference"
        ]
    ].head(10)
)

# ==========================
# Plot Top 10
# ==========================

top10 = ranking.head(10)

plt.figure(figsize=(10,6))

plt.barh(
    top10["Metabolite"],
    top10["Absolute_Difference"]
)

plt.xlabel("Magnitude of Change")

plt.title(
    "Top 10 Metabolites Changed After Surgery"
)

plt.tight_layout()

plt.savefig(
    "Top_Biomarkers.png",
    dpi=300
)

plt.show()

print("\nTop_Biomarkers.png saved!")