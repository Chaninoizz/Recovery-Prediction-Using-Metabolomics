import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.preprocessing import StandardScaler

import xgboost as xgb

# ================== Load Data ==================

meta = pd.read_csv(
    "raw_data/Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t",
    low_memory=False
)

sample_info = pd.read_csv(
    "raw_data/Domain_2_sample_table_MTBLS242.tsv",
    sep="\t"
)

# ================== Prepare Metabolite Matrix ==================

abundance = meta.iloc[:, 17:].T

metabolites = (
    meta["metabolite_identification"]
    .fillna("unknown")
    .astype(str)
    .values
)

abundance.columns = metabolites

abundance = (
    abundance
    .apply(pd.to_numeric, errors="coerce")
    .fillna(0)
)

abundance.index = (
    abundance.index
    .astype(str)
    .str.strip()
)

sample_info["Sample Name"] = (
    sample_info["Sample Name"]
    .astype(str)
    .str.strip()
)

df = abundance.merge(
    sample_info[
        [
            "Sample Name",
            "Factor Value[time point]"
        ]
    ],
    left_index=True,
    right_on="Sample Name"
)

# ================== Create Labels ==================

important_features = [
    "L-tyrosine",
    "L-alanine"
]

for feature in important_features:
    if feature not in df.columns:
        raise ValueError(
            f"Missing feature: {feature}"
        )

if "lipoproteins" not in df.columns:
    df["lipoproteins"] = 0

df["recovery_score"] = (
    df["L-tyrosine"]
    + df["L-alanine"]
    + df["lipoproteins"]
)

median_score = (
    df["recovery_score"]
    .median()
)

df["label"] = (
    df["recovery_score"] > median_score
).astype(int)

print("\nNumber of Samples:")
print(len(df))

print("\nLabel Distribution:")
print(
    df["label"]
    .value_counts()
)

# ================== Train Data ==================

feature_columns = abundance.columns

X = df[feature_columns].values
y = df["label"].values

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ================== Models ==================

rf = RandomForestClassifier(
    n_estimators=500,
    max_depth=5,
    random_state=42
)

xgb_model = xgb.XGBClassifier(
    n_estimators=300,
    max_depth=3,
    learning_rate=0.05,
    eval_metric="logloss",
    random_state=42
)

ensemble = VotingClassifier(
    estimators=[
        ("rf", rf),
        ("xgb", xgb_model)
    ],
    voting="soft"
)

# ================== Cross Validation ==================

min_class = np.bincount(y).min()

n_splits = min(
    5,
    min_class
)

if n_splits < 2:
    raise ValueError(
        "Not enough samples for cross validation."
    )

cv = StratifiedKFold(
    n_splits=n_splits,
    shuffle=True,
    random_state=42
)

print("\nX shape:", X.shape)
print("y shape:", y.shape)

scores = cross_val_score(
    ensemble,
    X_scaled,
    y,
    cv=cv,
    scoring="accuracy"
)

print("\nFold Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())

# ================== Train Final ==================

ensemble.fit(
    X_scaled,
    y
)

feature_importance = pd.Series(
    rf.fit(X_scaled, y).feature_importances_,
    index=abundance.columns
)

print("\nTop 10 Important Metabolites:")

print(
    feature_importance
    .sort_values(ascending=False)
    .head(10)
)

