import pandas as pd

nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

# เลือกเฉพาะคอลัมน์ sample ที่ลงท้ายด้วย _S
sample_cols = [c for c in nmr.columns if c.endswith("_S")]

print("Number of samples:", len(sample_cols))
print(sample_cols[:10])