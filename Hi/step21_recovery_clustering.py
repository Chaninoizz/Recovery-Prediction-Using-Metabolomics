# step21_recovery_clustering.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("final_dataset_for_ml.csv")

# ==========================
# Feature Columns
# ==========================

exclude_cols = [
    "Sample Name",
    "Patient_ID",
    "Factor Value[time point]"
]

feature_cols = [
    c for c in df.columns
    if c not in exclude_cols
]

# ==========================
# PCA
# ==========================

X = df[feature_cols]

pca = PCA(n_components=2)

pcs = pca.fit_transform(X)

df["PC1"] = pcs[:,0]
df["PC2"] = pcs[:,1]

# ==========================
# Calculate PRI
# ==========================

preop_center = (
    df[
        df["Factor Value[time point]"] == "preop"
    ][["PC1","PC2"]]
    .mean()
)

pri_results = []

for patient in df["Patient_ID"].unique():

    patient_df = df[
        df["Patient_ID"] == patient
    ]

    last_visit = patient_df.iloc[-1]

    distance = np.sqrt(
        (last_visit["PC1"] - preop_center["PC1"])**2 +
        (last_visit["PC2"] - preop_center["PC2"])**2
    )

    pri_results.append([
        patient,
        distance
    ])

pri_df = pd.DataFrame(
    pri_results,
    columns=[
        "Patient_ID",
        "Distance"
    ]
)

# ==========================
# KMeans
# ==========================

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

pri_df["Cluster"] = kmeans.fit_predict(
    pri_df[["Distance"]]
)

# ==========================
# Rename Clusters
# ==========================

cluster_means = (
    pri_df.groupby("Cluster")["Distance"]
    .mean()
    .sort_values()
)

cluster_order = cluster_means.index.tolist()

mapping = {
    cluster_order[0]: "Fast Recovery",
    cluster_order[1]: "Moderate Recovery",
    cluster_order[2]: "Poor Recovery"
}

pri_df["Recovery_Group"] = (
    pri_df["Cluster"]
    .map(mapping)
)

# ==========================
# Summary
# ==========================

print("\nRecovery Groups")

print(
    pri_df["Recovery_Group"]
    .value_counts()
)

# ==========================
# Plot
# ==========================

counts = (
    pri_df["Recovery_Group"]
    .value_counts()
)

plt.figure(figsize=(8,5))

counts.plot(
    kind="bar"
)

plt.ylabel("Number of Patients")

plt.title(
    "Recovery Clusters"
)

plt.tight_layout()

plt.savefig(
    "Recovery_Clusters.png",
    dpi=300
)

plt.show()

print("\nRecovery_Clusters.png saved!")

# Save labels

pri_df.to_csv(
    "patient_recovery_labels.csv",
    index=False
)

print("\npatient_recovery_labels.csv saved!")