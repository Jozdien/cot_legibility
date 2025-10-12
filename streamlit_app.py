import streamlit as st
import pandas as pd
import json
import yaml
from pathlib import Path
import matplotlib.pyplot as plt

st.set_page_config(page_title="CoT Legibility Explorer", layout="wide")

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
                "model_display": f"{model}@{temperature}" if temperature is not None else model,
                "avg_legibility": leg_stats.get("mean"),
                "legibility_std": leg_stats.get("std"),
                "num_questions": leg_stats.get("count", 0),
                "correct_pct": corr_stats.get("correct_pct", 0),
                "partial_pct": corr_stats.get("partially_pct", 0),
                "incorrect_pct": corr_stats.get("incorrect_pct", 0),
                "results": eval_data.get("results", [])
            }
            runs_data.append(run_info)

        except Exception:
            continue

    return pd.DataFrame(runs_data)

df = load_runs_data()

if df.empty:
    st.error("No runs found with evaluation data")
    st.stop()

st.title("CoT Legibility Explorer")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Model")
    model_options = ["Select a model..."] + sorted(df["model_display"].unique().tolist())
    selected_model = st.selectbox("", model_options, label_visibility="collapsed")

with col2:
    st.subheader("Dataset")
    dataset_options = ["Select a dataset..."] + sorted(df["dataset"].unique().tolist())
    selected_dataset = st.selectbox("", dataset_options, label_visibility="collapsed")

if selected_model != "Select a model..." and selected_dataset != "Select a dataset...":
    run_data = df[(df["model_display"] == selected_model) & (df["dataset"] == selected_dataset)]

    if run_data.empty:
        st.warning("No runs found for this combination")
    else:
        run = run_data.iloc[0]

        st.markdown("---")

        st.subheader("Summary Statistics")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Avg Legibility", f"{run['avg_legibility']:.2f}")
        with col2:
            st.metric("Correct", f"{run['correct_pct']:.1f}%")
        with col3:
            st.metric("Partially Correct", f"{run['partial_pct']:.1f}%")
        with col4:
            st.metric("Incorrect", f"{run['incorrect_pct']:.1f}%")

        st.markdown("---")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        correctness_data = [run['correct_pct'], run['partial_pct'], run['incorrect_pct']]
        correctness_labels = ['Correct', 'Partially Correct', 'Incorrect']
        colors = ['#90EE90', '#FFD700', '#FF6B6B']
        ax1.bar(correctness_labels, correctness_data, color=colors)
        ax1.set_ylabel('Percentage (%)')
        ax1.set_title('Correctness Breakdown')
        ax1.set_ylim(0, 100)

        legibility_scores = [r.get("legibility", {}).get("score", 0) for r in run["results"]]
        ax2.hist(legibility_scores, bins=10, color='#87CEEB', edgecolor='black')
        ax2.set_xlabel('Legibility Score (1=legible, 10=illegible)')
        ax2.set_ylabel('Count')
        ax2.set_title('Legibility Score Distribution')

        st.pyplot(fig)
        plt.close()

        st.markdown("---")

        st.subheader("Questions")

        with st.expander("Filters", expanded=True):
            col1, col2 = st.columns(2)

            with col1:
                min_leg = float(min(legibility_scores) if legibility_scores else 1.0)
                max_leg = float(max(legibility_scores) if legibility_scores else 10.0)
                legibility_range = st.slider(
                    "Legibility Score Range",
                    min_value=1.0,
                    max_value=10.0,
                    value=(min_leg, max_leg),
                    step=0.1
                )

            with col2:
                correctness_options = st.multiselect(
                    "Correctness",
                    options=["correct", "partially_correct", "incorrect"],
                    default=["correct", "partially_correct", "incorrect"]
                )

        filtered_results = []
        for result in run["results"]:
            leg_score = result.get("legibility", {}).get("score", 0)
            correctness = result.get("correctness", {}).get("correctness", "unknown")

            if (legibility_range[0] <= leg_score <= legibility_range[1] and
                correctness in correctness_options):
                filtered_results.append(result)

        st.markdown(f"**Showing {len(filtered_results)} of {len(run['results'])} questions**")

        if filtered_results:
            for i, result in enumerate(filtered_results):
                qid = result.get("question_id", f"Question {i+1}")
                leg_score = result.get("legibility", {}).get("score", 0)
                correctness = result.get("correctness", {}).get("correctness", "unknown")

                correctness_color = {
                    "correct": "🟢",
                    "partially_correct": "🟡",
                    "incorrect": "🔴"
                }.get(correctness, "⚪")

                with st.expander(f"{correctness_color} {qid} - Legibility: {leg_score:.2f}"):
                    st.markdown("#### Question")
                    st.write(result.get("question", "N/A"))

                    st.markdown("#### Correct Answer")
                    st.write(result.get("correct_answer", "N/A"))

                    if result.get("reasoning"):
                        st.markdown("#### Model Reasoning")
                        st.text_area("", result.get("reasoning"), height=200, key=f"reasoning_{i}", label_visibility="collapsed")

                    st.markdown("#### Model Answer")
                    st.text_area("", result.get("answer", "N/A"), height=200, key=f"answer_{i}", label_visibility="collapsed")

                    st.markdown("#### Scores")
                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("**Legibility**")
                        st.write(f"Score: {leg_score:.2f}")
                        st.write(result.get("legibility", {}).get("explanation", "N/A"))

                    with col2:
                        st.markdown("**Correctness**")
                        st.write(f"Grade: {correctness}")
                        st.write(result.get("correctness", {}).get("explanation", "N/A"))
        else:
            st.info("No questions match the selected filters")
