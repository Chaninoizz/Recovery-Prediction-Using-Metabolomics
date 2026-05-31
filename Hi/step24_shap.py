import pandas as pd
import shap

from sklearn.ensemble import RandomForestClassifier

# -------------------
# Load Dataset
# -------------------

df = pd.read_csv(
    "../data/recovery_prediction_dataset_v2.csv"
)

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
y = df["Label"]

# -------------------
# Train Model
# -------------------

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X, y)

# -------------------
# SHAP
# -------------------

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

print("SHAP calculated!")

# -------------------
# Summary Plot
# -------------------

shap.summary_plot(
    shap_values,
    X,
    show=False
)

import matplotlib.pyplot as plt

plt.tight_layout()
plt.savefig(
    "SHAP_Summary.png",
    dpi=300,
    bbox_inches="tight"
)

print("SHAP_Summary.png saved!")