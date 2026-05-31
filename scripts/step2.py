import pandas as pd

df = pd.read_csv("Domain_2_sample_table_MTBLS242.tsv", sep="\t")

print(df.shape)

print(df.head())

print(df.columns)

print(df["Characteristics[Variant]"].value_counts())

print(df.isnull().sum())

print("\nSample Names")
print(df["Sample Name"].head(20))

print("\nFactor Value")
print(df["Factor Value[time point]"].value_counts())