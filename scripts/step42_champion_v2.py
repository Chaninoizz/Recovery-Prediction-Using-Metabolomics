import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

# Load v4 dataset
df = pd.read_csv(
    "data/recovery_prediction_dataset_v4.csv"
)

# New Champion Features
selected_features = [
    "clinical_score",
    "lipoproteins_preop",
    "glycine_x_lipo",
    "L-allo-Isoleucine_preop",
    "glycine_ratio",
    "glycine_preop",
    "creatinine_preop",
    "L-tyrosine_3m"
]

X = df[selected_features]
y = df["Label"]

# Champion RF
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    min_samples_leaf=1,
    min_samples_split=2,
    random_state=42
)

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

print("Selected Features:")
print(selected_features)

print("\nFold Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())