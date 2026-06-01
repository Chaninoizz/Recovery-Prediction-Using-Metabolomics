import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

# Load dataset
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

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Champion Model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    min_samples_leaf=1,
    min_samples_split=2,
    random_state=42
)

model.fit(X_train, y_train)

# Plot Confusion Matrix
ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test
)

plt.title(
    "Champion Model Confusion Matrix"
)

plt.tight_layout()

plt.savefig(
    "results/confusion_matrix.png",
    dpi=300
)

plt.show()

print(
    "\nSaved: results/confusion_matrix.png"
)