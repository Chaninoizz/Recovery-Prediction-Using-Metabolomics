# step20_volcano.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind

# =====================
# Load Data
# =====================

df = pd.read_csv("final_dataset_for_ml.csv")

# =====================
# Feature Columns
# =====================

exclude_cols = [
    "Sample Name",
    "Patient_ID",
    "Factor Value[time point]"
]

metabolites = [
    c for c in df.columns
    if c not in exclude_cols
]

# =====================
# Groups
# =====================

preop = df[
    df["Factor Value[time point]"] == "preop"
]

postop = df[
    df["Factor Value[time point]"] != "preop"
]

# =====================
# Volcano Data
# =====================

results = []

for metabolite in metabolites:

    pre = preop[metabolite]

    post = postop[metabolite]

    # Fold Change

    fc = post.mean() - pre.mean()

    # T-Test

    stat, p = ttest_ind(
        post,
        pre,
        equal_var=False
    )

    results.append([
        metabolite,
        fc,
        p
    ])

volcano = pd.DataFrame(
    results,
    columns=[
        "Metabolite",
        "FoldChange",
        "PValue"
    ]
)

volcano["MinusLog10P"] = -np.log10(
    volcano["PValue"]
)

# =====================
# Plot
# =====================

plt.figure(figsize=(10,7))

plt.scatter(
    volcano["FoldChange"],
    volcano["MinusLog10P"]
)

# Label Top 5

top5 = volcano.nlargest(
    5,
    "MinusLog10P"
)

for _, row in top5.iterrows():

    plt.text(
        row["FoldChange"],
        row["MinusLog10P"],
        row["Metabolite"],
        fontsize=8
    )

plt.axhline(
    -np.log10(0.05),
    linestyle="--"
)

plt.xlabel("Fold Change")

plt.ylabel("-log10(P-value)")

plt.title(
    "Volcano Plot: Preop vs Postop"
)

plt.tight_layout()

plt.savefig(
    "Volcano_Plot.png",
    dpi=300
)

plt.show()

print("\nTop Significant Metabolites")
print(
    volcano.sort_values(
        "PValue"
    ).head(10)
)

print("\nVolcano_Plot.png saved!")