import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

# =========================
# Load Dataset
# =========================

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)
# =========================
# Features Ranked by Importance
# =========================

ranked_features = [
    "clinical_score",
    "L-allo-Isoleucine_preop",
    "lipoproteins_preop",
    "creatinine_preop",
    "glycine_preop",
    "L-tyrosine_3m",
    "lipoproteins_delta",
    "L-glutamine_delta",
    "L-leucine_preop",
    "tyrosine_pct"
]

# =========================
# Labels
# =========================

y = df["Label"]

# =========================
# CV Setup
# =========================

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# =========================
# Test Different Feature Sets
# =========================

feature_sizes = [3, 5, 7, 10]

results = []

for n in feature_sizes:

    selected = ranked_features[:n]

    X = df[selected]

    model = RandomForestClassifier(
        n_estimators=1000,
        max_depth=5,
        min_samples_leaf=2,
        min_samples_split=4,
        random_state=42
    )

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    mean_acc = scores.mean()

    results.append({
        "Features": n,
        "Accuracy": mean_acc
    })

    print("\n===================")
    print(f"Top {n} Features")
    print(selected)

    print("Fold Scores:")
    print(scores)

    print("Mean Accuracy:")
    print(mean_acc)

# =========================
# Summary
# =========================

results_df = pd.DataFrame(results)

print("\n===================")
print("FINAL RESULTS")
print(results_df)

best = results_df.loc[
    results_df["Accuracy"].idxmax()
]

print("\nBEST MODEL")

print(best)