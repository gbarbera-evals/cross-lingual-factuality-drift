from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]

REPORTS_DIR = BASE_DIR / "reports"
VISUALS_DIR = BASE_DIR / "visuals"

VISUALS_DIR.mkdir(exist_ok=True)

# 1. Provider-level confirmed drift

provider = pd.read_csv(REPORTS_DIR / "final_confirmed_drift.csv")

plt.figure(figsize=(6, 4))
plt.bar(provider["provider"], provider["drift_rate"])
plt.ylabel("Confirmed Drift Rate (%)")
plt.title("Confirmed Factual Drift by Model")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "confirmed_drift_by_model.png", dpi=300)
plt.close()

# 2. Language-level confirmed drift

language = pd.read_csv(REPORTS_DIR / "final_language_drift.csv")

language["label"] = language["provider"] + " / " + language["lang"]

plt.figure(figsize=(8, 4))
plt.bar(language["label"], language["drift_rate"])
plt.ylabel("Confirmed Drift Rate (%)")
plt.title("Confirmed Factual Drift by Model and Language")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "confirmed_drift_by_language.png", dpi=300)
plt.close()

# 3. Category-language confirmed drift

category_lang = pd.read_csv(REPORTS_DIR / "final_category_language_drift.csv")

category_lang["label"] = (
    category_lang["category"]
    + "\n"
    + category_lang["provider"].str.replace("ollama:", "", regex=False)
    + " / "
    + category_lang["lang"]
)

plt.figure(figsize=(14, 6))
plt.bar(category_lang["label"], category_lang["drift_rate"])
plt.ylabel("Confirmed Drift Rate (%)")
plt.title("Confirmed Drift by Category, Model, and Language")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "confirmed_drift_by_category_language.png", dpi=300)
plt.close()

print("Saved final visuals.")