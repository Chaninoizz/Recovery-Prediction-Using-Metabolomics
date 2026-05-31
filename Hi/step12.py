import pandas as pd

# โหลด NMR
nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

# โหลด Metadata
meta = pd.read_csv(
    "Domain_2_sample_table_MTBLS242.tsv",
    sep="\t"
)

# หา sample columns
sample_cols = [c for c in nmr.columns if c.endswith("_S")]

# สร้าง matrix
matrix = nmr[
    ["metabolite_identification"] + sample_cols
]

matrix = matrix.set_index(
    "metabolite_identification"
).T

matrix = matrix.reset_index()

matrix = matrix.rename(
    columns={"index": "Sample Name"}
)

# merge metadata
merged = pd.merge(
    matrix,
    meta[
        [
            "Sample Name",
            "Factor Value[time point]"
        ]
    ],
    on="Sample Name",
    how="left"
)

# สร้าง Patient_ID
merged["Patient_ID"] = (
    merged["Sample Name"]
    .str.replace("-", "_", regex=False)
    .str.split("_")
    .str[1]
)

print(
    merged[
        [
            "Sample Name",
            "Patient_ID",
            "Factor Value[time point]"
        ]
    ].head(20)
)

print("\nMissing Values")
print(merged.isnull().sum())

print("\nUnique Patients")
print(merged["Patient_ID"].nunique())

print("\nSamples per Patient")
print(
    merged["Patient_ID"]
    .value_counts()
    .head(20)
)

# เลือกเฉพาะ metabolite
metabolite_cols = [
    c for c in merged.columns
    if c not in [
        "Sample Name",
        "Factor Value[time point]",
        "Patient_ID"
    ]
]

print("\nSummary Statistics")
print(
    merged[metabolite_cols]
    .describe()
)

import numpy as np

merged[metabolite_cols] = np.log1p(
    merged[metabolite_cols]
)

print("\nAfter Log Transform")
print(
    merged[metabolite_cols]
    .describe()
)

merged.to_csv(
    "clean_metabolomics_dataset.csv",
    index=False
)

print("\nDataset Saved!")

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

merged[metabolite_cols] = scaler.fit_transform(
    merged[metabolite_cols]
)

print("\nAfter Standardization")
print(
    merged[metabolite_cols]
    .describe()
)

merged.to_csv(
    "clean_metabolomics_dataset_scaled.csv",
    index=False
)

print("\nTimepoint Counts")
print(
    merged["Factor Value[time point]"]
    .value_counts()
)

final_cols = [
    "Sample Name",
    "Patient_ID",
    "Factor Value[time point]"
] + metabolite_cols

merged[final_cols].to_csv(
    "final_dataset_for_ml.csv",
    index=False
)

print("\nFinal dataset exported!")