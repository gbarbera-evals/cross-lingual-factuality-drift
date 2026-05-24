import pandas as pd
import matplotlib.pyplot as plt

provider = pd.read_csv(
    "../reports/provider_drift.csv"
)

plt.figure(figsize=(5,4))

plt.bar(
    provider["provider"],
    provider["drift_rate"]
)

plt.ylabel("Drift Rate (%)")
plt.title("Drift Candidate Rate by Model")

plt.tight_layout()

plt.savefig(
    "../visuals/provider_drift.png",
    dpi=300
)

plt.close()

print("Saved provider_drift.png")