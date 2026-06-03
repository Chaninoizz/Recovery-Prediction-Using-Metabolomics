import pandas as pd

from itertools import combinations

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

# ==========================
# Top Features
# ==========================

top_features = [

    "clinical_score",
    "lipoproteins_preop",
    "L-allo-Isoleucine_preop",
    "glycine_preop",
    "L-leucine_preop",
    "creatinine_preop",
    "L-tyrosine_3m",
    "lipoproteins_delta",
    "L-allo-Isoleucine_3m",
    "L-glutamine_3m",

    "lipoproteins_pct",
    "(R)-3-Hydroxybutyric acid_3m",
    "L-glutamine_delta",
    "tyrosine_pct",
    "L-valine_preop",
    "L-alanine_3m",
    "lipoproteins_3m",
    "L-alanine_preop",
    "Dimethyl sulfone_3m",
    "lipoproteins_ratio"
]

# เช็คว่ามีทุก feature

top_features = [
    f for f in top_features
    if f in df.columns
]

print(
    "Available Features:",
    len(top_features)
)

# ==========================
# Data
# ==========================

y = df["Label"]

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

best_score = 0
best_features = None

# ==========================
# Search
# ==========================

for n_features in [4, 5, 6, 7]:

    print(
        f"\nSearching {n_features} features..."
    )

    for combo in combinations(
        top_features,
        n_features
    ):

        X = df[list(combo)]

        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=3,
            min_samples_leaf=1,
            min_samples_split=2,
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
            print(
                "Score:",
                round(score, 4)
            )

            print(
                "Features:"
            )

            print(combo)

# ==========================
# Final
# ==========================

print("\n" + "=" * 50)

print("FINAL BEST")

print("=" * 50)

print(
    "\nAccuracy:"
)

print(best_score)

print(
    "\nFeatures:"
)

print(best_features)