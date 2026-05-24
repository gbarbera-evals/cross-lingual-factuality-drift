# Cross-Lingual Factuality Drift Benchmark

![Python](https://img.shields.io/badge/Python-Data%20Pipeline-blue)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL%20Analysis-yellow)
![Promptfoo](https://img.shields.io/badge/Promptfoo-Evaluation-purple)
![Ollama](https://img.shields.io/badge/Ollama-Local%20Inference-black)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Manual Review](https://img.shields.io/badge/Manual%20Review-200%20Outputs-orange)
![Cross Lingual](https://img.shields.io/badge/Cross--Lingual-EN%20%7C%20IT-blueviolet)
![Benchmark](https://img.shields.io/badge/Benchmark-Factuality-success)
[![Live Dashboard](https://img.shields.io/badge/Live-Dashboard-red)](https://cross-lingual-factuality-drift-7t8f8rcjwulous7ldrrcfb.streamlit.app/)

![Confirmed Drift by Language](visuals/confirmed_drift_by_language.png)

### Interactive Dashboard

🔗 **[Open Streamlit Dashboard](https://cross-lingual-factuality-drift-7t8f8rcjwulous7ldrrcfb.streamlit.app/)**


Benchmark evaluating cross-lingual factual consistency across English and Italian prompts in local language models.

The project investigates whether factual accuracy changes across languages, combining automated evaluation pipelines with full manual adjudication.

Models evaluated:

- llama3.2 (Ollama)
- mistral (Ollama)

Scope:

- 200 manually reviewed outputs
- English + Italian
- Cross-lingual factual consistency
- Full manual evaluation workflow

## Motivation

Cross-lingual robustness remains an important challenge for language models.

Models may preserve factual accuracy in one language while introducing factual distortions, omissions, or unsupported additions in another.

This benchmark evaluates whether factual reliability remains stable across English and Italian prompts.

## Methodology

Pipeline:

Prompt generation
→ Ollama inference
→ Annotation pipeline
→ Initial candidate detection heuristics
→ Full manual adjudication (200 outputs)
→ SQL analysis (DuckDB)
→ Visualization generation
→ Streamlit dashboard

## Benchmark Categories

- Historical events
- Biographies
- Geopolitics
- Environmental disasters
- Public health
- Science communication

## Models

| Model | Runtime |
|--------|----------|
| llama3.2 | Ollama |
| mistral | Ollama |

## Dashboard

Interactive Streamlit dashboard for benchmark exploration.

![Dashboard](visuals/dashboard.png)

## Key Findings

- Both evaluated local models showed substantially elevated confirmed factual drift rates in Italian compared to English.

- Llama 3.2 demonstrated stronger cross-lingual degradation overall (28% EN → 72% IT).

- Mistral also exhibited Italian vulnerability (18% EN → 52% IT).

- Historical events emerged as the highest-risk category for confirmed cross-lingual factual drift.

- Biographies and environmental disasters also showed elevated cross-lingual drift.

## Visualizations

### Confirmed Drift by Model

![Model Drift](visuals/confirmed_drift_by_model.png)

### Drift by Language

![Language Drift](visuals/confirmed_drift_by_language.png)

### Drift by Category + Language

![Category Drift](visuals/confirmed_drift_by_category_language.png)

## Tech Stack

- Python
- Pandas
- DuckDB
- SQL
- Promptfoo
- Ollama
- Streamlit
- Matplotlib

## Future Improvements

- Additional languages
- Additional local models
- Expanded factual categories
- Automated drift detection improvements