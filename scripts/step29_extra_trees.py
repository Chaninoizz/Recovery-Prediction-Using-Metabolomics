import pandas as pd

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

df = pd.read_csv(
    "data/recovery_prediction_dataset_v2.csv"
)

features = [
    "L-tyrosine_3m",
    "lipoproteins_preop",
    "L-allo-Isoleucine_preop"
]

X = df[features]
y = df["Label"]

model = ExtraTreesClassifier(
    n_estimators=500,
    max_depth=2,
    min_samples_leaf=2,
    min_samples_split=6,
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