# step22_prepare_ml.py

import pandas as pd

# -------------------
# Load files
# -------------------

df = pd.read_csv("final_dataset_for_ml.csv")
labels = pd.read_csv("patient_recovery_labels.csv")

# -------------------
# เอาเฉพาะ Fast/Poor
# -------------------

labels = labels[
    labels["Recovery_Group"].isin(
        ["Fast Recovery", "Poor Recovery"]
    )
]

print("Patients:")
print(labels["Recovery_Group"].value_counts())

# -------------------
# เลือกข้อมูล
# preop + 3 months
# -------------------

early_data = df[
    df["Factor Value[time point]"].isin([
        "preop",
        "3 months after surgery"
    ])
]

# -------------------
# สร้าง row ต่อ patient
# -------------------

rows = []

feature_cols = [
    c for c in df.columns
    if c not in [
        "Sample Name",
        "Patient_ID",
        "Factor Value[time point]"
    ]
]

for pid in labels["Patient_ID"]:

    patient = early_data[
        early_data["Patient_ID"] == pid
    ]

    if len(patient) < 2:
        continue

    preop = patient[
        patient["Factor Value[time point]"] == "preop"
    ]

    m3 = patient[
        patient["Factor Value[time point]"]
        == "3 months after surgery"
    ]

    if len(preop) == 0 or len(m3) == 0:
        continue

    preop = preop.iloc[0]
    m3 = m3.iloc[0]

    row = {
        "Patient_ID": pid
    }

    for metabolite in feature_cols:

        row[f"{metabolite}_preop"] = preop[metabolite]

        row[f"{metabolite}_3m"] = m3[metabolite]

        row[f"{metabolite}_delta"] = (
            m3[metabolite]
            - preop[metabolite]
        )

    label = labels[
        labels["Patient_ID"] == pid
    ]["Recovery_Group"].values[0]

    row["Label"] = label

    rows.append(row)

ml_df = pd.DataFrame(rows)

print("\nML Dataset Shape")
print(ml_df.shape)

print("\nLabel Counts")
print(ml_df["Label"].value_counts())

ml_df.to_csv(
    "../data/recovery_prediction_dataset_v2.csv",
    index=False
)

print(
    "\nrecovery_prediction_dataset_v2.csv saved!"
)