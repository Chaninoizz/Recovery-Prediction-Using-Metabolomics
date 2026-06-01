import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

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

rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

svm = SVC(
    probability=True,
    kernel="rbf",
    C=10,
    gamma=0.1
)

xgb = XGBClassifier(
    n_estimators=200,
    max_depth=2,
    learning_rate=0.05,
    eval_metric="logloss",
    random_state=42
)

ensemble = VotingClassifier(
    estimators=[
        ("rf", rf),
        ("svm", svm),
        ("xgb", xgb)
    ],
    voting="soft"
)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    ensemble,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

print("Fold Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())