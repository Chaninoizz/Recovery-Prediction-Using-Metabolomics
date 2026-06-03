import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import VotingClassifier
import warnings
warnings.filterwarnings('ignore')

# ====================== โหลดข้อมูล ======================
df = pd.read_csv("data/recovery_prediction_dataset_v3.csv")

# ====================== Top Features + Engineering ======================
selected_features = [
    "L-tyrosine_3m",
    "lipoproteins_preop",
    "L-allo-Isoleucine_preop",     # สำคัญมาก
    "creatinine_preop",
    "glycine_preop",
    "lipoproteins_delta",
    "L-leucine_preop",
    "L-valine_preop",
    "Dimethyl sulfone_3m",
    "L-tyrosine_delta"
]

X = df[selected_features].copy()

# Feature Engineering (เพิ่มความสามารถโมเดล)
X['tyrosine_lipoprotein_ratio'] = X['L-tyrosine_3m'] / (X['lipoproteins_preop'] + 1e-5)
X['bcaa_total'] = X['L-leucine_preop'] + X['L-valine_preop'] + X['L-allo-Isoleucine_preop']
X['amino_acid_index'] = X['glycine_preop'] + X['L-tyrosine_3m']

print(f"ใช้ Features ทั้งหมด: {X.shape[1]}")

y = df["Label"].map({"Fast Recovery": 0, "Poor Recovery": 1})

# ====================== Strong Ensemble ======================
xgb1 = XGBClassifier(
    n_estimators=800,
    max_depth=4,
    learning_rate=0.03,
    subsample=0.8,
    colsample_bytree=0.75,
    random_state=42,
    eval_metric='logloss'
)

xgb2 = XGBClassifier(
    n_estimators=500,
    max_depth=3,
    learning_rate=0.05,
    subsample=0.85,
    random_state=123,
    eval_metric='logloss'
)

ensemble = VotingClassifier(
    estimators=[('xgb1', xgb1), ('xgb2', xgb2)],
    voting='soft',
    weights=[2, 1]
)

# ====================== Evaluation ======================
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(ensemble, X, y, cv=cv, scoring='accuracy')

print(f"5-Fold CV Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# Final Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

ensemble.fit(X_train, y_train)
pred = ensemble.predict(X_test)

print(f"\n✅ Test Accuracy: {accuracy_score(y_test, pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, pred, target_names=["Fast Recovery", "Poor Recovery"]))

# Top Features
importances = pd.Series(ensemble.estimators_[0].feature_importances_, 
                       index=X.columns).sort_values(ascending=False)
print("\n🔥 Top 10 Important Features:")
print(importances.head(12))