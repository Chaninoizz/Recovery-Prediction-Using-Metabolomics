import pandas as pd

nmr = pd.read_csv(
    "Domain_2_NMR_results_MTBLS242.tsv",
    sep="\t"
)

print(nmr["metabolite_identification"])
print(nmr.columns[:15])

