import pandas as pd

df = pd.read_csv(
    "../data/recovery_prediction_dataset_v2.csv"
)

# -----------------------
# Ratio Features
# -----------------------

df["tyrosine_ratio"] = (
    df["L-tyrosine_3m"] /
    (df["L-tyrosine_preop"] + 0.0001)
)

df["lipoproteins_ratio"] = (
    df["lipoproteins_3m"] /
    (df["lipoproteins_preop"] + 0.0001)
)

# -----------------------
# Save
# -----------------------

df.to_csv(
    "recovery_prediction_dataset_v2.csv",
    index=False
)

print("Saved!")
print(df.head())