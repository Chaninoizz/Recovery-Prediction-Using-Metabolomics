import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

champion_features = [
    "L-tyrosine_3m",
    "lipoproteins_preop",
    "L-allo-Isoleucine_preop",
    "creatinine_preop",
    "glycine_preop",
    "lipoproteins_delta",
    "L-glutamine_delta"
]

y = df["Label"]

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

print("\nChampion Accuracy = 0.8556\n")

for feature_to_remove in champion_features:

    selected = [
        f for f in champion_features
        if f != feature_to_remove
    ]

    X = df[selected]

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    print("-" * 50)
    print("Removed:", feature_to_remove)
    print("Accuracy:", scores.mean())