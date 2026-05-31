import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score


df = pd.read_csv(
    "../data/recovery_prediction_dataset_v2.csv"
)

top_features = [
    "lipoproteins_preop",
    "L-allo-Isoleucine_preop",
    "L-tyrosine_3m",
    "L-alanine_preop",
    "L-tyrosine_preop",
    "lipoproteins_3m",
    "methanol_delta",
    "citrate_delta",
    "L-valine_preop",
    "isopropanol_3m"
]

X = df[top_features]

y = df["Label"]

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

print("Fold Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())

print("\nStd:")
print(scores.std())