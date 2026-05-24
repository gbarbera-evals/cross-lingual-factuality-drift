import pandas as pd


def load_results(filepath):
    df = pd.read_csv(filepath)

    required_columns = [
        "case_id",
        "pair_id",
        "topic",
        "language",
        "model",
        "prompt",
        "expected_facts",
        "response",
        "factuality_label",
        "drift_label",
        "drift_type",
        "severity",
        "notes",
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return df


def summarize_results(df):
    print("\nDataset shape:")
    print(df.shape)

    print("\nFactuality label distribution:")
    print(df["factuality_label"].value_counts(dropna=False))

    print("\nDrift label distribution:")
    print(df["drift_label"].value_counts(dropna=False))

    print("\nDrift type distribution:")
    print(df["drift_type"].value_counts(dropna=False))


if __name__ == "__main__":
    filepath = "data/processed/labeled_results.csv"

    df = load_results(filepath)

    print("\nLabeled results loaded successfully.")
    summarize_results(df)