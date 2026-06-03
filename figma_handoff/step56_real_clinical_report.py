import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv(
    "data/recovery_prediction_dataset_v3.csv"
)

BIOMARKER_INFO = {

    "glycine_preop": {
        "description":
        "Glycine is involved in energy metabolism and recovery-associated pathways.",
        "conditions": [
            "Metabolic Dysregulation",
            "Recovery Risk Pattern"
        ]
    },

    "creatinine_preop": {
        "description":
        "Creatinine is commonly used as a marker of metabolic stress and physiological recovery.",
        "conditions": [
            "Metabolic Stress State",
            "Recovery Impairment Pattern"
        ]
    },

    "L-allo-Isoleucine_3m": {
        "description":
        "Altered branched-chain amino acid metabolism has been associated with impaired recovery.",
        "conditions": [
            "Amino Acid Dysregulation",
            "Metabolic Syndrome–Like Pattern"
        ]
    },

    "L-glutamine_3m": {
        "description":
        "Glutamine plays an important role in recovery and tissue repair.",
        "conditions": [
            "Recovery Pathway Alteration"
        ]
    },

    "(R)-3-Hydroxybutyric acid_3m": {
        "description":
        "This metabolite reflects changes in energy utilization and ketone metabolism.",
        "conditions": [
            "Energy Utilization Shift"
        ]
    },

    "L-valine_preop": {
        "description":
        "Valine is a branched-chain amino acid associated with metabolic regulation.",
        "conditions": [
            "Metabolic Adaptation Pattern"
        ]
    },

    "clinical_score": {
        "description":
        "Clinical score summarizes overall clinical recovery status.",
        "conditions": [
            "Recovery Risk Assessment"
        ]
    }
}

# ==========================
# Champion Features
# ==========================

selected_features = [
    "clinical_score",
    "glycine_preop",
    "creatinine_preop",
    "L-allo-Isoleucine_3m",
    "L-glutamine_3m",
    "(R)-3-Hydroxybutyric acid_3m",
    "L-valine_preop"
]

# ==========================
# Prepare Data
# ==========================

X = df[selected_features]

y = df["Label"].map({
    "Poor Recovery": 0,
    "Fast Recovery": 1
})

# ==========================
# Champion Model
# ==========================

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

# ==========================
# Cross Validation
# ==========================

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

accuracy = scores.mean() * 100

# ==========================
# Train Final Model
# ==========================

model.fit(X, y)

train_accuracy = model.score(X, y)

print("\nTraining Accuracy:")
print(f"{train_accuracy*100:.2f}%")

feature_importance = pd.DataFrame({
    "Feature": selected_features,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

# ==========================
# Select Patient
# ==========================

patient_id = int(
    input("Enter Patient ID: ")
)

print("\nGenerating Clinical AI Report...")
print("Analyzing Metabolomic Biomarkers...")

patient_row = df[
    df["Patient_ID"] == patient_id
]

if len(patient_row) == 0:

    print("Patient ID not found.")
    exit()

patient = patient_row[selected_features]

prediction = model.predict(patient)[0]

probabilities = model.predict_proba(patient)[0]

confidence = max(probabilities) * 100

if prediction == 0:
    prediction_text = "Poor Recovery"
else:
    prediction_text = "Fast Recovery"

# ==========================
# Report
# ==========================

print("=" * 50)
print("ADVANCED CLINICAL AI REPORT")
print("=" * 50)

print("\nPatient ID:")
print(f"PT-{patient_id:06d}")

from datetime import datetime

print("\nAnalysis Date:")
print(datetime.now().strftime("%Y-%m-%d"))

print("\nPrediction:")
print(prediction_text)

print("\nConfidence:")
print(f"{confidence:.2f}%")

if prediction_text == "Poor Recovery":
    risk_level = "HIGH"
else:
    risk_level = "LOW"

print("\nRisk Level:")
print(risk_level)

print("\nModel Accuracy:")
print(f"{accuracy:.2f}%")

print("\nCross Validation Scores:")
print(scores)

print("\n" + "=" * 50)
print("KEY CLINICAL DRIVERS")
print("=" * 50)

for i, row in enumerate(
    feature_importance.itertuples(),
    start=1
):

    print(
        f"{i}. {row.Feature} "
        f"({row.Importance*100:.1f}%)"
    )

# ==========================
# Reference Means
# ==========================

# ==========================
# Reference Means
# ==========================

reference_means = {}

for feature in selected_features:
    reference_means[feature] = X[feature].mean()

print("\n" + "=" * 50)
print("METABOLIC ALERTS")
print("=" * 50)

for feature in selected_features:

    value = float(patient[feature].iloc[0])

    mean = float(reference_means[feature])

    std = float(X[feature].std())

    difference = value - mean

    if std > 0:
        z_score = difference / std
    else:
        z_score = 0

    # Skip near-normal values
    if abs(difference) < 0.5:
        continue

    if difference > 0:
        status = "ABOVE POPULATION MEAN"
    else:
        status = "BELOW POPULATION MEAN"

    print("\nBiomarker:")
    print(feature)

    abs_z = abs(z_score)

    if abs_z < 0.5:
        significance = "MINIMAL DEVIATION"

    elif abs_z < 1.0:
        significance = "MILD DEVIATION"

    elif abs_z < 2.0:
        significance = "MODERATE DEVIATION"

    else:
        significance = "HIGH DEVIATION"

    print(f"Patient Value: {value:.3f}")
    print(f"Population Mean: {mean:.3f}")
    print(f"Z-Score: {z_score:.2f}")
    print(f"Status: {status}")

    print(
        f"Clinical Significance: {significance}"
    )

    abs_z = abs(z_score)

    if abs_z < 0.5:
        significance = "MINIMAL DEVIATION"

    elif abs_z < 1.0:
        significance = "MILD DEVIATION"

    elif abs_z < 2.0:
        significance = "MODERATE DEVIATION"

    else:
        significance = "HIGH DEVIATION"

    if feature in BIOMARKER_INFO:

        print("\nClinical Interpretation:")
        print(
            BIOMARKER_INFO[feature]["description"]
        )

        print("\nAssociated Conditions:")

        for condition in BIOMARKER_INFO[feature]["conditions"]:
            print(f"• {condition}")

    else:

        print("\nClinical Interpretation:")
        print(
            "Reference information not available."
        )



print("\n" + "=" * 50)

print("AI CONDITION STATEMENT")
print("-" * 50)

if prediction_text == "Poor Recovery":

    top3 = feature_importance.head(3)

    print(f"""
The strongest contributors to this prediction were:

• {top3.iloc[0]['Feature']} ({top3.iloc[0]['Importance']*100:.1f}%)

• {top3.iloc[1]['Feature']} ({top3.iloc[1]['Importance']*100:.1f}%)

• {top3.iloc[2]['Feature']} ({top3.iloc[2]['Importance']*100:.1f}%)

These biomarkers collectively support
the Poor Recovery classification.
""")

    for i in range(3):

        feature = top3.iloc[i]["Feature"]

        value = float(patient[feature].iloc[0])

        mean = float(reference_means[feature])

        if value > mean:
            direction = "ABOVE POPULATION MEAN"
        else:
            direction = "BELOW POPULATION MEAN"

        print(
            f"{feature} was {direction}."
        )

    print("""
The overall metabolomic profile shows
strong similarity to individuals within
the Poor Recovery cohort and suggests
increased recovery risk.
""")

else:

    top3 = feature_importance.head(3)

    print(f"""
The strongest contributors to this prediction were:

• {top3.iloc[0]['Feature']} ({top3.iloc[0]['Importance']*100:.1f}%)

• {top3.iloc[1]['Feature']} ({top3.iloc[1]['Importance']*100:.1f}%)

• {top3.iloc[2]['Feature']} ({top3.iloc[2]['Importance']*100:.1f}%)

These biomarkers collectively support
the Fast Recovery classification.
""")

    high_deviation_found = False

    for feature in selected_features:

        value = float(patient[feature].iloc[0])
        mean = float(reference_means[feature])
        std = float(X[feature].std())

        if std > 0:

            z_score = abs(
                (value - mean) / std
            )

            if z_score >= 2:
                high_deviation_found = True
                break

    if high_deviation_found:

        print("""
Note:

Although the overall prediction is Fast Recovery,
certain biomarkers demonstrated notable deviations
from the reference population and may warrant
further clinical review.
""")

    print("""
The overall metabolomic profile shows
strong similarity to individuals within
the Fast Recovery cohort and suggests
favorable recovery potential.
""")

if prediction_text == "Poor Recovery":

    if confidence >= 90:
        risk_level = "VERY HIGH"
    elif confidence >= 80:
        risk_level = "HIGH"
    elif confidence >= 70:
        risk_level = "MODERATE"
    else:
        risk_level = "LOW"

    severity = round(confidence / 10, 1)

    print("\n" + "=" * 50)
    print("CLINICAL RISK SUMMARY")
    print("=" * 50)

    print("\nRecovery Risk:")
    print(risk_level)

    print("\nMetabolic Risk:")
    print("HIGH")

    print("\nOverall Status:")
    print("ABNORMAL")

    print("\nAI Risk Score:")
    print(f"{severity}/10")

    print("\n" + "=" * 50)
    print("FINAL ASSESSMENT")
    print("=" * 50)

    print("""
The patient exhibits a metabolomic profile
consistent with the Poor Recovery cohort.

Multiple recovery-associated biomarkers
contributed to this prediction.

Enhanced monitoring may be beneficial.
""")

else:

    severity = round((100 - confidence) / 10, 1)

    print("\n" + "=" * 50)
    print("CLINICAL RISK SUMMARY")
    print("=" * 50)

    print("\nRecovery Risk:")
    print("LOW")

    print("\nMetabolic Risk:")
    print("LOW")

    print("\nOverall Status:")
    print("NORMAL")

    print("\nAI Risk Score:")
    print(f"{severity}/10")

    print("\n" + "=" * 50)
    print("FINAL ASSESSMENT")
    print("=" * 50)

    print("""
The patient exhibits a metabolomic profile
consistent with the Fast Recovery cohort.

The overall biomarker pattern suggests
favorable recovery potential.

Current metabolomic indicators are aligned
with patients who demonstrated faster
post-operative recovery.
""")
    
print("\nDISCLAIMER")
print("-" * 50)

print("""
This report is generated using a machine
learning model trained on metabolomics data.

The prediction is intended for research and
decision-support purposes only and should not
be used as a standalone clinical diagnosis.
""")

print("=" * 50)