import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.svm import SVC

from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score,
    GridSearchCV
)

# Load dataset
df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

# Target
y = df["Label"]

# Features
X = df.drop(
    columns=["Label"]
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("selector", SelectKBest(f_classif)),
    ("clf", SVC(kernel="rbf"))
])

param_grid = {
    "selector__k": [3, 5, 7, 10, 15],
    "clf__C": [0.1, 1, 5, 10, 20],
    "clf__gamma": ["scale", 0.1, 0.01]
}

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

grid = GridSearchCV(
    pipeline,
    param_grid=param_grid,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1
)

grid.fit(X, y)

print("\nBest Accuracy")
print(grid.best_score_)

print("\nBest Parameters")
print(grid.best_params_)

scores = cross_val_score(
    grid.best_estimator_,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

print("\nFold Scores")
print(scores)

print("\nMean Accuracy")
print(scores.mean())