import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "final_dataset_for_ml.csv"
)

time_order = {
    "preop":0,
    "3 months after surgery":1,
    "6 months after surgery":2,
    "9 months after surgery":3,
    "12 months after surgery":4
}

df["time_num"] = (
    df["Factor Value[time point]"]
    .map(time_order)
)

metabolite = "L-Lactic acid"

mean_values = (
    df.groupby(
        "Factor Value[time point]"
    )[metabolite]
    .mean()
)

mean_values = mean_values.reindex(
    time_order.keys()
)

plt.figure(figsize=(8,5))

plt.plot(
    mean_values.index,
    mean_values.values,
    marker="o"
)

plt.xticks(rotation=20)

plt.ylabel("Mean Standardized Value")

plt.title(
    f"{metabolite} Recovery Trajectory"
)

plt.tight_layout()

plt.savefig(
    "Recovery_Trajectory.png",
    dpi=300
)

plt.show()