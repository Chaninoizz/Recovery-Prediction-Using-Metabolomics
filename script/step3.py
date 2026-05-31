import pandas as pd

nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

meta = pd.read_csv(
    "Domain_2_sample_table_MTBLS242.tsv",
    sep="\t"
)

sample_names = meta["Sample Name"].tolist()

count = 0

for s in sample_names:
    if s in nmr.columns:
        count += 1

print("Matched:", count)
print("Total:", len(sample_names))