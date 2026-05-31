final_cols = [
    "Sample Name",
    "Patient_ID",
    "Factor Value[time point]"
] + metabolite_cols

merged[final_cols].to_csv(
    "final_dataset_for_ml.csv",
    index=False
)