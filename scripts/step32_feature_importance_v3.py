import pandas as pd

from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(
    "data/recovery_prediction_dataset_v4.csv"
)

X = df.drop(
    columns=["Patient_ID", "Label"]
)

y = df["Label"]

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X, y)

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 20 Features\n")
print(
    importance_df.head(20)
)