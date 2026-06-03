import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

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
y = df["Label"]

rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

svm = SVC(
    kernel="rbf",
    C=10,
    gamma=0.1,
    probability=True
)

estimators = [
    ("rf", rf),
    ("svm", svm)
]

stack = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(),
    cv=5
)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    stack,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

print("Fold Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())