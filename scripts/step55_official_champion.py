import pandas as pd

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
# Official Champion Features
# ==========================

selected_features = [
    "clinical_score",
    "glycine_preop",
    "creatinine_preop",
    "L-allo-Isoleucine_3m",
    "L-glutamine_3m",
    "(R)-3-Hydroxybutyric acid_3m",
    "L-valine_preop"
]

# ==========================
# X / y
# ==========================

X = df[selected_features]

y = df["Label"]

# Encode labels

y = y.map({
    "Poor Recovery": 0,
    "Fast Recovery": 1
})

# ==========================
# Champion Model
# ==========================

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
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

# ==========================
# Results
# ==========================

print("=" * 50)
print("OFFICIAL CHAMPION MODEL")
print("=" * 50)

print("\nFeatures:")
print(selected_features)

print("\nFold Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())

print("\nStd:")
print(scores.std())

print("\nFinal Accuracy:")
print(f"{scores.mean()*100:.2f}%")