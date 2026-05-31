import pandas as pd

nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

meta = pd.read_csv(
    "Domain_2_sample_table_MTBLS242.tsv",
    sep="\t"
)

sample_cols = [c for c in nmr.columns if c.endswith("_S")]

meta_samples = set(meta["Sample Name"])

nmr_samples = set(sample_cols)

missing = meta_samples - nmr_samples

print("Missing samples:", len(missing))

for s in list(missing)[:50]:
    print(s)