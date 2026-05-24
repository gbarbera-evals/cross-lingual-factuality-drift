import pandas as pd


def load_prompts(filepath):
    """
    Load multilingual factuality prompts dataset.
    """

    df = pd.read_csv(filepath)

    required_columns = [
        "case_id",
        "pair_id",
        "topic",
        "language",
        "prompt",
        "expected_facts"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return df


if __name__ == "__main__":

    filepath = "data/prompts/factuality_prompts.csv"

    df = load_prompts(filepath)

    print("\nDataset loaded successfully.\n")

    print(df.head())

    print("\nDataset shape:")
    print(df.shape)