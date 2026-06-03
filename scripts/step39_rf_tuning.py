import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
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

param_grid = {
    "n_estimators": [100, 300, 500, 1000],
    "max_depth": [2, 3, 4, 5, None],
    "min_samples_split": [2, 3, 4, 5],
    "min_samples_leaf": [1, 2, 3],
    "max_features": ["sqrt", "log2", None],
    "criterion": ["gini", "entropy"]
}

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1
)

grid.fit(X, y)

print("\nBest Score:")
print(grid.best_score_)

print("\nBest Parameters:")
print(grid.best_params_)