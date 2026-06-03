import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    min_samples_leaf=1,
    min_samples_split=2,
    random_state=42
)

model.fit(X_train, y_train)

ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test
)

plt.title("Champion Model Confusion Matrix")
plt.tight_layout()

plt.savefig(
    "results/confusion_matrix_v2.png",
    dpi=300
)

print("Saved: results/confusion_matrix_v2.png")