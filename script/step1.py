import pandas as pd

df = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

print(df.shape)
print(df.head())
print(df.columns)