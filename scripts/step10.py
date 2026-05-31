import pandas as pd

# โหลด NMR
nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

# โหลด metadata
meta = pd.read_csv(
    "Domain_2_sample_table_MTBLS242.tsv",
    sep="\t"
)

# เลือก sample columns
sample_cols = [c for c in nmr.columns if c.endswith("_S")]

# transpose
matrix = nmr[
    ["metabolite_identification"] + sample_cols
]

matrix = matrix.set_index(
    "metabolite_identification"
).T

# เปลี่ยน index เป็น column
matrix = matrix.reset_index()

matrix = matrix.rename(
    columns={"index": "Sample Name"}
)

# merge
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

print(merged.shape)

print(
    merged[
        [
            "Sample Name",
            "Factor Value[time point]"
        ]
    ].head(20)
)