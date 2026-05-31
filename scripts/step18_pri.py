import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("final_dataset_for_ml.csv")

print("Columns:")
print(df.columns)

# ==========================
# Select ONLY metabolite columns
# ==========================

exclude_cols = [
    "Sample Name",
    "Factor Value[time point]",
    "Patient_ID"
]

feature_cols = [
    col for col in df.columns
    if col not in exclude_cols
]

# ใช้เฉพาะตัวเลข
X = df[feature_cols].select_dtypes(include=np.number)

print("\nFeature Matrix Shape:")
print(X.shape)

# ==========================
# PCA
# ==========================

pca = PCA(n_components=2)

pcs = pca.fit_transform(X)

df["PC1"] = pcs[:, 0]
df["PC2"] = pcs[:, 1]

# ==========================
# Select Patient
# ==========================

patient = "0100"

patient_df = df[
    df["Patient_ID"].astype(str).str.zfill(4)
    == patient
].copy()

print("\nPatient Data Shape:")
print(patient_df.shape)

print("\nPatient Records:")
print(
    patient_df[
        [
            "Sample Name",
            "Patient_ID",
            "Factor Value[time point]"
        ]
    ]
)

# ==========================
# Sort Timepoints
# ==========================

time_order = {
    "preop": 0,
    "3 months after surgery": 1,
    "6 months after surgery": 2,
    "9 months after surgery": 3,
    "12 months after surgery": 4
}

patient_df["time_num"] = (
    patient_df["Factor Value[time point]"]
    .map(time_order)
)

patient_df = patient_df.sort_values("time_num")

# ==========================
# Calculate Distance
# ==========================

baseline_pc1 = patient_df.iloc[0]["PC1"]
baseline_pc2 = patient_df.iloc[0]["PC2"]

distances = []

for _, row in patient_df.iterrows():

    distance = np.sqrt(
        (row["PC1"] - baseline_pc1) ** 2 +
        (row["PC2"] - baseline_pc2) ** 2
    )

    distances.append(distance)

patient_df["Distance"] = distances

# ==========================
# PRI Score
# ==========================

patient_df["PRI"] = (
    100 / (1 + patient_df["Distance"])
)

print("\nPRI Results:")
print(
    patient_df[
        [
            "Factor Value[time point]",
            "Distance",
            "PRI"
        ]
    ]
)

# ==========================
# Plot
# ==========================

plt.figure(figsize=(8, 5))

plt.plot(
    patient_df["Factor Value[time point]"],
    patient_df["PRI"],
    marker="o",
    linewidth=3
)

plt.title(
    f"Patient {patient} Recovery Index"
)

plt.xlabel("Time Point")
plt.ylabel("PRI Score")

plt.xticks(rotation=20)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "PRI_Score.png",
    dpi=300
)

plt.show()

print("\nPRI_Score.png saved!")