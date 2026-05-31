import pandas as pd

nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

# ใช้ชื่อ metabolite เป็น index
nmr = nmr.set_index("metabolite_identification")

# transpose
nmr_t = nmr.T

print(nmr_t.shape)
print(nmr_t.head())