import pandas as pd
import shap
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

features = [
    "clinical_score",
    "L-allo-Isoleucine_preop",
    "creatinine_preop",
    "glycine_preop",
    "lipoproteins_ratio"
]

X = df[features]
y = df["Label"]

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

model.fit(X, y)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

if isinstance(shap_values, list):
    shap.summary_plot(
        shap_values[1],
        X,
        show=False
    )
else:
    shap.summary_plot(
        shap_values[:, :, 1],
        X,
        show=False
    )

plt.tight_layout()

plt.savefig(
    "results/champion_shap_v2.png",
    dpi=300,
    bbox_inches="tight"
)

print(
    "Saved: results/champion_shap_v2.png"
)