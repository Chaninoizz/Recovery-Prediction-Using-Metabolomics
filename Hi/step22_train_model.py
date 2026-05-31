import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# -------------------
# Load Dataset
# -------------------

df = pd.read_csv(
    "../data/recovery_prediction_dataset_v2.csv"
)

# -------------------
# Features
# -------------------

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

# -------------------
# Label
# -------------------

y = df["Label"]

# -------------------
# Split
# -------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# -------------------
# Random Forest
# -------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# -------------------
# Predict
# -------------------

y_pred = model.predict(
    X_test
)

# -------------------
# Metrics
# -------------------

acc = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(acc)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)

# -------------------
# Feature Importance
# -------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)

print("\nTop 10 Features")

print(
    importance.head(10)
)

print("Using Top 10 Features")
print(top_features)