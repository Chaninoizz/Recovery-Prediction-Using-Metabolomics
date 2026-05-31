import pandas as pd

# โหลดข้อมูล
nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

# เลือกเฉพาะคอลัมน์ sample
sample_cols = [c for c in nmr.columns if c.endswith("_S")]

# สร้าง matrix
matrix = nmr[
    ["metabolite_identification"] + sample_cols
]

# transpose
matrix = matrix.set_index(
    "metabolite_identification"
).T

print(matrix.shape)
print(matrix.head())