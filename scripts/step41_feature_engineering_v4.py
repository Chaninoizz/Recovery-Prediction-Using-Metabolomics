import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

# =========================
# New Interaction Features
# =========================

df["glycine_x_lipo"] = (
    df["glycine_preop"] *
    df["lipoproteins_preop"]
)

df["tyrosine_x_glycine"] = (
    df["L-tyrosine_3m"] *
    df["glycine_preop"]
)

df["glutamine_x_lipo"] = (
    df["L-glutamine_delta"] *
    df["lipoproteins_preop"]
)

df["glycine_ratio"] = (
    df["glycine_preop"] /
    (df["lipoproteins_preop"] + 1e-6)
)

# =========================
# Save New Dataset
# =========================

df.to_csv(
    "data/recovery_prediction_dataset_v4.csv",
    index=False
)

print("Saved!")
print(df.shape)