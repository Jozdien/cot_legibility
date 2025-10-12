import streamlit as st
import pandas as pd
import json
import yaml
from pathlib import Path

st.set_page_config(page_title="CoT Legibility Runs", layout="wide")

@st.cache_data
def load_runs_data():
    runs_dir = Path("runs")
    runs_data = []

    for run_path in runs_dir.iterdir():
        if not run_path.is_dir():
            continue

        eval_file = run_path / "evaluation.json"
        if not eval_file.exists():
            continue

        try:
            parts = run_path.name.split("_")
            timestamp = f"{parts[0]}_{parts[1]}"
            dataset = parts[-1]
            model = "_".join(parts[2:-1])

            with open(eval_file) as f:
                eval_data = json.load(f)

            temperature = None
            config_file = run_path / "config.yaml"
            if config_file.exists():
                with open(config_file) as f:
                    config = yaml.safe_load(f)
                    models = config.get("inference", {}).get("models", [])
                    for m in models:
                        if m.get("name") == model:
                            temperature = m.get("temperature")
                            break

            stats = eval_data.get("statistics", {})
            leg_stats = stats.get("legibility", {})
            corr_stats = stats.get("correctness", {})

            run_info = {
                "run_id": run_path.name,
                "timestamp": timestamp,
                "model": model,
                "temperature": temperature,
                "dataset": dataset,
                "avg_legibility": leg_stats.get("mean"),
                "legibility_std": leg_stats.get("std"),
                "num_questions": leg_stats.get("count", 0),
                "correct_pct": corr_stats.get("correct_pct", 0),
                "partial_pct": corr_stats.get("partially_pct", 0),
                "incorrect_pct": corr_stats.get("incorrect_pct", 0),
                "results": eval_data.get("results", [])
            }
            runs_data.append(run_info)

        except Exception as e:
            st.warning(f"Failed to load {run_path.name}: {e}")
            continue

    return pd.DataFrame(runs_data)

df = load_runs_data()

if df.empty:
    st.error("No runs found with evaluation data")
    st.stop()

st.title("CoT Legibility Run Viewer")

st.sidebar.header("Filters")

models = st.sidebar.multiselect(
    "Model",
    options=sorted(df["model"].unique()),
    default=sorted(df["model"].unique())
)

temperatures = df["temperature"].dropna().unique()
if len(temperatures) > 0:
    selected_temps = st.sidebar.multiselect(
        "Temperature",
        options=sorted(temperatures),
        default=sorted(temperatures)
    )
else:
    selected_temps = []

datasets = st.sidebar.multiselect(
    "Dataset",
    options=sorted(df["dataset"].unique()),
    default=sorted(df["dataset"].unique())
)

legibility_range = st.sidebar.slider(
    "Avg Legibility Score (1=legible, 10=illegible)",
    min_value=1.0,
    max_value=10.0,
    value=(1.0, 10.0),
    step=0.1
)

correctness_filter = st.sidebar.multiselect(
    "Filter by Correctness (at question level)",
    options=["correct", "partially_correct", "incorrect"],
    default=["correct", "partially_correct", "incorrect"]
)

filtered_df = df[
    (df["model"].isin(models)) &
    (df["dataset"].isin(datasets)) &
    (df["avg_legibility"].between(legibility_range[0], legibility_range[1]))
]

if len(selected_temps) > 0:
    filtered_df = filtered_df[filtered_df["temperature"].isin(selected_temps)]

st.header(f"Summary: {len(filtered_df)} runs")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg Legibility (across runs)", f"{filtered_df['avg_legibility'].mean():.2f}")
with col2:
    st.metric("Avg Correct %", f"{filtered_df['correct_pct'].mean():.1f}%")
with col3:
    st.metric("Total Questions", int(filtered_df["num_questions"].sum()))

st.header("Runs Overview")

display_df = filtered_df[[
    "model", "temperature", "dataset", "avg_legibility",
    "correct_pct", "partial_pct", "incorrect_pct", "num_questions", "timestamp"
]].copy()

display_df = display_df.round(2)
display_df = display_df.sort_values("timestamp", ascending=False)

st.dataframe(display_df, use_container_width=True)

st.header("Question-Level Details")

for _, row in filtered_df.iterrows():
    with st.expander(f"{row['model']} - {row['dataset']} ({row['timestamp']})"):
        questions_data = []
        for result in row["results"]:
            correctness = result.get("correctness", {}).get("correctness", "unknown")
            if correctness not in correctness_filter:
                continue

            questions_data.append({
                "Question ID": result.get("question_id"),
                "Legibility": result.get("legibility", {}).get("score"),
                "Correctness": correctness,
                "Question": result.get("question", "")[:100] + "..."
            })

        if questions_data:
            q_df = pd.DataFrame(questions_data)
            st.dataframe(q_df, use_container_width=True)
        else:
            st.info("No questions match the selected correctness filter")

st.sidebar.markdown("---")
st.sidebar.caption(f"Total runs in database: {len(df)}")
