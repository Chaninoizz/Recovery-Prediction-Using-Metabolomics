import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูล
df = pd.read_csv("final_dataset_for_ml.csv")

# แปลง Patient_ID ให้เป็น string 4 หลัก
df["Patient_ID"] = (
    df["Patient_ID"]
    .astype(str)
    .str.zfill(4)
)

# ดูว่ามี Patient_ID อะไรบ้าง
print("\nPatients available:")
print(df["Patient_ID"].value_counts().head(20))

# เลือกคนไข้
patient = "0100"

patient_df = df[
    df["Patient_ID"] == patient
].copy()

print("\nPatient Data Shape:")
print(patient_df.shape)

print("\nPatient Records:")
print(
    patient_df[
        ["Sample Name", "Patient_ID", "Factor Value[time point]"]
    ]
)

# ถ้าไม่มีข้อมูลให้หยุด
if len(patient_df) == 0:
    print(f"\nPatient {patient} not found!")
    exit()

# เรียงลำดับเวลา
time_order = {
    "preop": 0,
    "3 months after surgery": 1,
    "6 months after surgery": 2,
    "9 months after surgery": 3,
    "12 months after surgery": 4
}

patient_df["time_num"] = (
    patient_df["Factor Value[time point]"]
    .map(time_order)
)

patient_df = patient_df.sort_values("time_num")

# เลือก metabolite
metabolite = "L-Lactic acid"

# วาดกราฟ
plt.figure(figsize=(8,5))

plt.plot(
    patient_df["Factor Value[time point]"],
    patient_df[metabolite],
    marker="o",
    linewidth=2
)

plt.title(
    f"Patient {patient}: {metabolite}"
)

plt.ylabel("Standardized Abundance")
plt.xlabel("Time Point")

plt.xticks(rotation=20)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "Patient_Journey.png",
    dpi=300
)

plt.show()