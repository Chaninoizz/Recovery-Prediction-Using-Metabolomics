import pandas as pd

from xgboost import XGBClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

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
y = df["Label"].map({
    "Fast Recovery": 0,
    "Poor Recovery": 1
})

# ==========================
# XGBoost Champion
# ==========================
model = XGBClassifier(
    n_estimators=1000,
    max_depth=2,
    learning_rate=0.01,
    subsample=0.7,
    colsample_bytree=0.9,
    min_child_weight=3,
    gamma=0.1,
    eval_metric="logloss",
    random_state=42,
    n_jobs=-1
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

print("=" * 50)
print("STEP 44 SUPER CHAMPION")
print("=" * 50)

print("\nFold Scores:")
print(scores)

print("\nMean Accuracy:")
print(f"{scores.mean():.4f}")

print("\nStd:")
print(f"{scores.std():.4f}")

print("\nFinal Result:")
print(f"Accuracy = {scores.mean()*100:.2f}% ± {scores.std()*100:.2f}%")