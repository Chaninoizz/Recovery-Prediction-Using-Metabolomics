import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

# ==========================
# Champion Features
# ==========================
selected_features = [
    "L-tyrosine_3m",
    "lipoproteins_preop",
    "L-allo-Isoleucine_preop",
    "creatinine_preop",
    "glycine_preop",
    "lipoproteins_delta",
    "L-glutamine_delta"
]

X = df[selected_features]
y = df["Label"]

# ==========================
# Champion RF (Balanced)
# ==========================
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    min_samples_leaf=1,
    min_samples_split=2,
    class_weight="balanced",
    random_state=42
)

# ==========================
# Cross Validation
# ==========================
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

# ==========================
# Fit Final Model
# ==========================
model.fit(X, y)

print("\nChampion Model Saved In M