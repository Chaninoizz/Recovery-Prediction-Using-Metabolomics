import pandas as pd

from boruta import BorutaPy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

# Load dataset
df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

# Features
X = df.drop(
    columns=["Patient_ID", "Label"]
)

# Label
y = df["Label"]

# Convert label to numeric
y = y.map({
    "Fast Recovery": 1,
    "Poor Recovery": 0
})

# Random Forest
rf = RandomForestClassifier(
    n_estimators=1000,
    random_state=42,
    n_jobs=-1
)

# Boruta
boruta = BorutaPy(
    estimator=rf,
    n_estimators="auto",
    random_state=42,
    verbose=2
)

boruta.fit(
    X.values,
    y.values
)

selected_features = X.columns[
    boruta.support_
]

print("\nSelected Features:")
print(list(selected_features))

# Evaluate selected features
X_selected = X[selected_features]

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

scores = cross_val_score(
    model,
    X_selected,
    y,
    cv=cv,
    scoring="accuracy"
)

print("\nFold Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())