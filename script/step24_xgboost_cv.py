import pandas as pd

from xgboost import XGBClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

# =========================
# Load Dataset
# =========================

df = pd.read_csv(
    "../data/recovery_prediction_dataset_v2.csv"
)

# =========================
# Features
# =========================

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

# =========================
# Encode Labels
# =========================

y = df["Label"].map({
    "Fast Recovery": 1,
    "Poor Recovery": 0
})

print("Dataset Shape:")
print(X.shape)

print("\nLabel Counts:")
print(y.value_counts())

# =========================
# XGBoost Model
# =========================

model = XGBClassifier(
    n_estimators=500,
    max_depth=3,
    learning_rate=0.03,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss"
)

# =========================
# 5 Fold CV
# =========================

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

print("\nFold Scores")
print(scores)

print("\nMean Accuracy")
print(scores.mean())

print("\nStd")
print(scores.std())