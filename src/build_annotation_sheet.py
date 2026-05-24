import json
import pandas as pd

with open("benchmark_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

results = data["results"]["results"]

rows = []

for result in results:
    vars_data = result.get("vars", {})
    provider = result.get("provider", {})
    response = result.get("response", {}).get("output", "")

    numbered_list_flag = int(
        "1." in response
        or "2." in response
    )

    rows.append({
        "prompt_id": vars_data.get("prompt_id"),
        "category": vars_data.get("category"),
        "lang": vars_data.get("lang"),
        "provider": provider.get("id", ""),
        "response": response,
        "response_chars": len(response),
        "numbered_list_flag": numbered_list_flag,
        "possible_instruction_violation": numbered_list_flag,
        "possible_compression": "",
        "possible_drift": "",
        "drift_type": "",
        "notes": ""
    })

df = pd.DataFrame(rows)

pair_stats = (
    df.groupby(["prompt_id", "provider"])["response_chars"]
    .agg(
        pair_response_chars_min="min",
        pair_response_chars_max="max"
    )
    .reset_index()
)

df = df.merge(
    pair_stats,
    on=["prompt_id", "provider"],
    how="left"
)

df["length_ratio"] = (
    df["pair_response_chars_min"]
    / df["pair_response_chars_max"]
)

df["is_shorter_in_pair"] = (
    df["response_chars"] == df["pair_response_chars_min"]
).astype(int)

df["possible_compression"] = (
    (df["length_ratio"] < 0.75)
    & (df["is_shorter_in_pair"] == 1)
).astype(int)

df["possible_severe_compression"] = (
    (df["length_ratio"] < 0.60)
    & (df["is_shorter_in_pair"] == 1)
).astype(int)

df["possible_drift"] = (
    (df["possible_compression"] == 1)
    |
    (df["possible_instruction_violation"] == 1)
).astype(int)

column_order = [
    "prompt_id",
    "category",
    "lang",
    "provider",
    "response",
    "response_chars",
    "pair_response_chars_min",
    "pair_response_chars_max",
    "length_ratio",
    "is_shorter_in_pair",
    "numbered_list_flag",
    "possible_instruction_violation",
    "possible_compression",
    "possible_severe_compression",
    "possible_drift",
    "drift_type",
    "notes"
]

df = df[column_order]

df.to_csv(
    "annotation_sheet.csv",
    index=False,
    encoding="utf-8"
)

print()
print("Possible drift candidates:", df["possible_drift"].sum())
print("Compression candidates:", df["possible_compression"].sum())
print("Severe compression candidates:", df["possible_severe_compression"].sum())
print("Instruction violation candidates:", df["possible_instruction_violation"].sum())

print(df.head())
print()
print("Rows:", len(df))