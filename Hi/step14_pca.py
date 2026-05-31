import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv(
    "final_dataset_for_ml.csv"
)

# สร้าง group

df["Group"] = df[
    "Factor Value[time point]"
].apply(
    lambda x:
    "Preop"
    if x == "preop"
    else "Postop"
)

meta_cols = [
    "Sample Name",
    "Patient_ID",
    "Factor Value[time point]",
    "Group"
]

feature_cols = [
    c for c in df.columns
    if c not in meta_cols
]

X = df[feature_cols]

pca = PCA(n_components=2)

pcs = pca.fit_transform(X)

plt.figure(figsize=(8,6))

for g in ["Preop","Postop"]:

    idx = df["Group"] == g

    plt.scatter(
        pcs[idx,0],
        pcs[idx,1],
        label=g,
        alpha=0.7
    )

plt.xlabel("PC1")
plt.ylabel("PC2")

plt.title(
    "PCA: Preop vs Postop"
)

plt.legend()

plt.savefig(
    "PCA_Preop_vs_Postop.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()