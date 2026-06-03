import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

from itertools import combinations

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

top_features = [
    "clinical_score",
    "L-allo-Isoleucine_preop",
    "lipoproteins_preop",
    "creatinine_preop",
    "glycine_preop",
    "L-tyrosine_3m",
    "lipoproteins_delta",
    "L-glutamine_delta",
    "L-leucine_preop",
    "Dimethyl sulfone_3m",
    "tyrosine_x_lipo",
    "lipoproteins_ratio"
]

missing = [f for f in top_features if f not in df.columns]

if missing:
    print("Missing Features:")
    print(missing)
    exit()

y = df["Label"]

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

best_score = 0
best_features = None

for n_features in [5, 6, 7]:

    for combo in combinations(top_features, n_features):

        X = df[list(combo)]

        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=3,
            random_state=42
        )

        score = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring="accuracy"
        ).mean()

        if score > best_score:

            best_score = score
            best_features = combo

            print("\nNEW BEST")
            print("Score:", round(score, 4))
            print("Features:")
            print(combo)

print("\n" + "=" * 50)
print("FINAL BEST")
print("=" * 50)

print("Accuracy:")
print(best_score)

print("\nFeatures:")
print(best_features)

print("All features found:",
      all(f in df.columns for f in top_features))