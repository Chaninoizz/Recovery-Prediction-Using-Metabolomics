import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

features = [
    "glycine_preop",
    "creatinine_preop",
    "L-allo-Isoleucine_3m",
    "L-glutamine_3m",
    "(R)-3-Hydroxybutyric acid_3m",
    "L-valine_preop"
]

print("\nREFERENCE MEANS")
print("=" * 40)

for f in features:
    print(
        f,
        round(df[f].mean(), 4)
    )