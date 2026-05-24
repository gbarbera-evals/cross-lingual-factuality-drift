import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

df = pd.read_csv(
    BASE_DIR
    / "data"
    / "prompts"
    / "annotation_sheet.csv"
)

st.title(
    "Cross-Lingual Factuality Drift Benchmark"
)

st.markdown("""

### Project Overview

This benchmark evaluates cross-lingual factual consistency in local language models across English and Italian prompts.

Two Ollama models (`llama3.2` and `mistral`) were evaluated on factual question-answering tasks spanning:

- Historical events
- Biographies
- Geopolitics
- Environmental disasters
- Public health
- Science communication

Responses were generated automatically and then manually reviewed for factual drift.

The benchmark focuses on identifying whether factual accuracy changes across languages, including:

- Hallucinated additions
- Cross-lingual factual inconsistencies
- Localization-related factual degradation

Dataset summary:

- 200 manually reviewed outputs
- 2 local models
- English + Italian evaluation
- Full manual adjudication pipeline

""")

# FILTERS

provider = st.selectbox(
    "Provider",
    ["All"]
    + sorted(
        df["provider"].unique()
    )
)

lang = st.selectbox(
    "Language",
    ["All"]
    + sorted(
        df["lang"].unique()
    )
)

category = st.selectbox(
    "Category",
    ["All"]
    + sorted(
        df["category"].unique()
    )
)

filtered = df.copy()

if provider != "All":
    filtered = filtered[
        filtered["provider"]
        == provider
    ]

if lang != "All":
    filtered = filtered[
        filtered["lang"]
        == lang
    ]

if category != "All":
    filtered = filtered[
        filtered["category"]
        == category
    ]

# METRICS

outputs = len(filtered)

drift = (
    filtered["drift_type"]
    != "no_drift"
).sum()

drift_rate = (
    drift
    / outputs
    * 100
    if outputs
    else 0
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Outputs",
    outputs
)

c2.metric(
    "Confirmed Drift",
    drift
)

c3.metric(
    "Drift Rate %",
    round(
        drift_rate,
        1
    )
)

# TABLE

show = filtered[
    [
        "prompt_id",
        "category",
        "lang",
        "provider",
        "drift_type",
        "notes"
    ]
]

st.dataframe(
    show,
    use_container_width=True
)

# INSPECTION

selected = st.selectbox(
    "Inspect Row",
    filtered.index
)

row = filtered.loc[
    selected
]

st.subheader(
    "Response"
)

st.write(
    row["response"]
)

st.subheader(
    "Notes"
)

st.write(
    row["notes"]
)