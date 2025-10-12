import streamlit as st
import pandas as pd
import json
import yaml
from pathlib import Path
import matplotlib.pyplot as plt

st.set_page_config(page_title="CoT Legibility Explorer", layout="wide")

MODEL_DISPLAY_NAMES = {
    "gpt-4o": "GPT-4o",
    "gpt-4o-mini": "GPT-4o Mini",
    "gpt-4-turbo": "GPT-4 Turbo",
    "claude-3-7-sonnet-latest": "Claude 3.7 Sonnet",
    "claude-3-5-sonnet-latest": "Claude 3.5 Sonnet",
    "claude-3-opus-latest": "Claude 3 Opus",
    "R1": "DeepSeek R1",
    "o3-mini": "O3-Mini",
}

def get_model_display_name(model_name, temperature):
    display_name = MODEL_DISPLAY_NAMES.get(model_name, model_name)
    if temperature is not None and temperature != 1.0:
        return f"{display_name} (temperature={temperature})"
    return display_name

@st.cache_data
def load_runs_data():
    runs_dir = Path("runs")
    aggregated_data = {}

    for run_path in runs_dir.iterdir():
        if not run_path.is_dir():
            continue

        eval_file = run_path / "evaluation.json"
        if not eval_file.exists():
            continue

        try:
            parts = run_path.name.split("_")
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

            inference_file = run_path / "inference.json"
            if not inference_file.exists():
                inference_file = run_path / "inference.jsonl"

            inference_data = {}
            if inference_file.exists():
                with open(inference_file) as f:
                    if inference_file.suffix == ".jsonl":
                        for line in f:
                            item = json.loads(line)
                            inference_data[item["question_id"]] = item
                    else:
                        infer_list = json.load(f)
                        for item in infer_list:
                            inference_data[item["question_id"]] = item

            for result in eval_data.get("results", []):
                qid = result.get("question_id")
                if qid in inference_data:
                    result["correct_answer"] = inference_data[qid].get("correct_answer", "N/A")
                    result["reasoning"] = inference_data[qid].get("reasoning")
                    result["answer"] = inference_data[qid].get("answer", "N/A")

            model_display = get_model_display_name(model, temperature)
            key = (model_display, dataset)

            if key not in aggregated_data:
                aggregated_data[key] = {
                    "model_display": model_display,
                    "dataset": dataset,
                    "results": [],
                    "runs": []
                }

            aggregated_data[key]["results"].extend(eval_data.get("results", []))
            aggregated_data[key]["runs"].append(run_path.name)

        except Exception:
            continue

    runs_data = []
    for key, data in aggregated_data.items():
        results = data["results"]
        legibility_scores = [r.get("legibility", {}).get("score", 0) for r in results]

        correct_count = sum(1 for r in results if r.get("correctness", {}).get("correctness") == "correct")
        partial_count = sum(1 for r in results if r.get("correctness", {}).get("correctness") == "partially_correct")
        incorrect_count = sum(1 for r in results if r.get("correctness", {}).get("correctness") == "incorrect")
        total_count = len(results)

        run_info = {
            "model_display": data["model_display"],
            "dataset": data["dataset"],
            "avg_legibility": sum(legibility_scores) / len(legibility_scores) if legibility_scores else 0,
            "legibility_std": pd.Series(legibility_scores).std() if len(legibility_scores) > 1 else 0,
            "num_questions": total_count,
            "correct_pct": (correct_count / total_count * 100) if total_count > 0 else 0,
            "partial_pct": (partial_count / total_count * 100) if total_count > 0 else 0,
            "incorrect_pct": (incorrect_count / total_count * 100) if total_count > 0 else 0,
            "results": results,
            "runs": data["runs"]
        }
        runs_data.append(run_info)

    return pd.DataFrame(runs_data)

df = load_runs_data()

if df.empty:
    st.error("No runs found with evaluation data")
    st.stop()

st.title("CoT Legibility Explorer")

st.markdown("---")

st.subheader("Model")
model_options = ["Select a model..."] + sorted(df["model_display"].unique().tolist())
selected_model = st.selectbox("", model_options, label_visibility="collapsed", key="model")

st.subheader("Dataset")
dataset_options = ["Select a dataset..."] + sorted(df["dataset"].unique().tolist())
selected_dataset = st.selectbox("", dataset_options, label_visibility="collapsed", key="dataset")

if selected_model != "Select a model..." and selected_dataset != "Select a dataset...":
    run_data = df[(df["model_display"] == selected_model) & (df["dataset"] == selected_dataset)]

    if run_data.empty:
        st.warning("No runs found for this combination")
    else:
        run = run_data.iloc[0]

        st.markdown("---")

        st.subheader("Summary Statistics")

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Samples", f"{run['num_questions']}")
        with col2:
            st.metric("Avg Legibility", f"{run['avg_legibility']:.2f}")
        with col3:
            st.metric("Correct", f"{run['correct_pct']:.1f}%")
        with col4:
            st.metric("Partially Correct", f"{run['partial_pct']:.1f}%")
        with col5:
            st.metric("Incorrect", f"{run['incorrect_pct']:.1f}%")

        st.caption(f"Combined from {len(run['runs'])} run(s): {', '.join(run['runs'])}")

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

        col1, col2 = st.columns([1, 4])
        with col1:
            num_to_show = st.selectbox(
                "Show",
                options=[25, 50, 100, len(filtered_results)],
                format_func=lambda x: f"{x} outputs" if x != len(filtered_results) else "All outputs",
                key="num_outputs"
            )

        st.caption("Select the checkbox on the left of each row to view details")

        search_query = st.text_input("Search", placeholder="Search by ID, legibility, or correctness...", key="search_query")

        if search_query:
            search_lower = search_query.lower()
            filtered_results = [
                r for r in filtered_results
                if search_lower in str(r.get("question_id", "")).lower() or
                   search_lower in str(r.get("legibility", {}).get("score", "")).lower() or
                   search_lower in str(r.get("correctness", {}).get("correctness", "")).lower()
            ]

        filtered_results = filtered_results[:num_to_show]

        if filtered_results:
            if "selected_question_idx" not in st.session_state:
                st.session_state.selected_question_idx = None

            table_data = []
            for i, result in enumerate(filtered_results):
                qid = result.get("question_id", f"Question {i+1}")
                leg_score = result.get("legibility", {}).get("score", 0)
                correctness = result.get("correctness", {}).get("correctness", "unknown")

                correctness_display = {
                    "correct": "✓ Correct",
                    "partially_correct": "~ Partially Correct",
                    "incorrect": "✗ Incorrect"
                }.get(correctness, "? Unknown")

                table_data.append({
                    "ID": qid,
                    "Legibility": f"{leg_score:.2f}",
                    "Correctness": correctness_display
                })

            table_df = pd.DataFrame(table_data)

            event = st.dataframe(
                table_df,
                use_container_width=True,
                hide_index=True,
                height=400,
                on_select="rerun",
                selection_mode="single-row"
            )

            if event.selection and "rows" in event.selection and len(event.selection["rows"]) > 0:
                selected_row = event.selection["rows"][0]
                st.session_state.selected_question_idx = selected_row

            if st.session_state.selected_question_idx is not None:
                st.markdown("---")
                st.subheader("Question Details")

                result = filtered_results[st.session_state.selected_question_idx]

                st.markdown("#### Question")
                st.write(result.get("question", "N/A"))

                st.markdown("#### Expected Answer")
                st.write(result.get("correct_answer", "N/A"))

                if result.get("reasoning"):
                    st.markdown("#### Model Reasoning")
                    st.text_area("", result.get("reasoning"), height=200, key="reasoning_detail", label_visibility="collapsed")

                st.markdown("#### Model Answer")
                st.text_area("", result.get("answer", "N/A"), height=200, key="answer_detail", label_visibility="collapsed")

                st.markdown("#### Scores")
                col1, col2 = st.columns(2)

                leg_score = result.get("legibility", {}).get("score", 0)
                correctness = result.get("correctness", {}).get("correctness", "unknown")

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
