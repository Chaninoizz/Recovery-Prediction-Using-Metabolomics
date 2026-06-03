import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

feature_columns = [
    col for col in df.columns
    if col not in [
        "Patient_ID",
        "Label"
    ]
]

X = df[feature_columns]

y = df["Label"]

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

selector = RFECV(
    estimator=model,
    step=1,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1
)

selector.fit(X, y)

print("\nBest Number of Features:")
print(selector.n_features_)

selected_features = X.columns[
    selector.support_
]

print("\nSelected Features:")
print(selected_features.tolist())

print("\nBest CV Score:")
print(max(selector.cv_results_["mean_test_score"]))