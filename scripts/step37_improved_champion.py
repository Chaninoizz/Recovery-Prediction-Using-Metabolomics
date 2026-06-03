import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import VotingClassifier
import warnings
warnings.filterwarnings('ignore')

# ====================== โหลดข้อมูล ======================
df = pd.read_csv("data/recovery_prediction_dataset_v3.csv")

# ====================== Feature Engineering ======================
# ปรับชื่อคอลัมน์ให้ตรงกับข้อมูลจริงของคุณ
selected_features = [
    "L-tyrosine_3m", 
    "lipoproteins_preop", 
    "L-allo-Isoleucine_preop",
    "creatinine_preop", 
    "glycine_preop", 
    "lipoproteins_delta", 
    "L-glutamine_delta",
    "L-valine_preop", 
    "L-leucine_preop", 
    "Dimethyl sulfone_3m",      # แก้ไขชื่อคอลัมน์
    "L-alanine_3m", 
    "L-tyrosine_delta", 
    "pyruvic_acid_preop"
]

# ตรวจสอบว่าคอลัมน์มีจริงหรือไม่
available_features = [col for col in selected_features if col in df.columns]
print(f"ใช้ Features: {len(available_features)} / {len(selected_features)}")

X = df[available_features].copy()
y = df["Label"].map({"Fast Recovery": 0, "Poor Recovery": 1})

print(f"จำนวนผู้ป่วย: {len(df)}")

# ====================== Ensemble Model ======================
xgb1 = XGBClassifier(
    n_estimators=500,
    max_depth=4,
    learning_rate=0.04,
    subsample=0.85,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss"
)

xgb2 = XGBClassifier(
    n_estimators=300,
    max_depth=3,
    learning_rate=0.07,
    subsample=0.9,
    random_state=123,
    eval_metric="logloss"
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

# Final Training + Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
ensemble.fit(X_train, y_train)

pred = ensemble.predict(X_test)
print(f"\n✅ Test Accuracy: {accuracy_score(y_test, pred):.4f}")

print("\nClassification Report:")
print(classification_report(y_test, pred, target_names=["Fast Recovery", "Poor Recovery"]))

# Feature Importance
final_xgb = ensemble.estimators_[0]
importances = pd.Series(final_xgb.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n🔥 Top 10 Important Features:")
print(importances.head(10))