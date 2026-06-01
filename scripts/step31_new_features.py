import pandas as pd

df = pd.read_csv(
    "../data/recovery_prediction_dataset_v2.csv"
)

# Percent Change
df["tyrosine_pct"] = (
    df["L-tyrosine_delta"]
    /
    (abs(df["L-tyrosine_preop"]) + 0.001)
)

df["lipoproteins_pct"] = (
    df["lipoproteins_delta"]
    /
    (abs(df["lipoproteins_preop"]) + 0.001)
)

# Clinical Score
df["clinical_score"] = (
    df["L-tyrosine_3m"]
    +
    df["lipoproteins_preop"]
    +
    df["L-allo-Isoleucine_preop"]
)

# Interaction
df["tyrosine_x_lipo"] = (
    df["L-tyrosine_3m"]
    *
    df["lipoproteins_preop"]
)

df = pd.read_csv(
    "../data/recovery_prediction_dataset_v3.csv"
)

print(df.shape)
print("Saved!")