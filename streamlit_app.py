import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import yaml

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

CORRECTNESS_VALUES = ["correct", "partially_correct", "incorrect"]
CORRECTNESS_DISPLAY = {
    "correct": "✓ Correct",
    "partially_correct": "~ Partially Correct",
    "incorrect": "✗ Incorrect",
    "unknown": "? Unknown",
}


def get_model_display_name(model_name, temperature):
    display_name = MODEL_DISPLAY_NAMES.get(model_name, model_name)
    if temperature is not None and temperature != 1.0:
        return f"{display_name} (temperature={temperature})"
    return display_name


def load_inference_data(run_path):
    inference_file = run_path / "inference.json"
    if not inference_file.exists():
        inference_file = run_path / "inference.jsonl"

    if not inference_file.exists():
        return {}

    inference_data = {}
    with open(inference_file) as f:
        if inference_file.suffix == ".jsonl":
            for line in f:
                item = json.loads(line)
                key = (item["question_id"], item.get("sample_index", 0))
                inference_data[key] = item
        else:
            for item in json.load(f):
                key = (item["question_id"], item.get("sample_index", 0))
                inference_data[key] = item
    return inference_data


def get_temperature_from_config(run_path, model, inference_data=None):
    config_file = run_path / "config.yaml"
    if config_file.exists():
        with open(config_file) as f:
            config = yaml.safe_load(f)
            models = config.get("inference", {}).get("models", [])
            for m in models:
                if m.get("name") == model:
                    return m.get("temperature")

    if inference_data is None:
        inference_data = load_inference_data(run_path)

    if inference_data:
        first_item = next(iter(inference_data.values()))
        return first_item.get("temperature")

    return None


def enrich_results_with_inference(results, inference_data):
    for result in results:
        qid = result.get("question_id")
        sample_idx = result.get("sample_index", 0)
        key = (qid, sample_idx)
        if key in inference_data:
            if not result.get("question"):
                result["question"] = inference_data[key].get("question", "N/A")
            result["correct_answer"] = inference_data[key].get("correct_answer", "N/A")
            result["reasoning"] = inference_data[key].get("reasoning")
            result["answer"] = inference_data[key].get("answer", "N/A")


def get_legibility_score(result):
    leg = result.get("legibility")
    if isinstance(leg, dict):
        return leg.get("score", 0)
    return 0


def get_correctness(result):
    corr = result.get("correctness")
    if isinstance(corr, dict):
        return corr.get("correctness", "unknown")
    return "unknown"


def calculate_statistics(results):
    legibility_scores = [get_legibility_score(r) for r in results]
    correctness_counts = Counter(get_correctness(r) for r in results)
    total = len(results)

    return {
        "avg_legibility": sum(legibility_scores) / len(legibility_scores)
        if legibility_scores
        else 0,
        "legibility_std": pd.Series(legibility_scores).std()
        if len(legibility_scores) > 1
        else 0,
        "num_questions": total,
        "correct_pct": correctness_counts.get("correct", 0) / total * 100
        if total > 0
        else 0,
        "partial_pct": correctness_counts.get("partially_correct", 0) / total * 100
        if total > 0
        else 0,
        "incorrect_pct": correctness_counts.get("incorrect", 0) / total * 100
        if total > 0
        else 0,
    }


@st.cache_data(ttl=300)
def load_runs_metadata():
    runs_dir = Path("streamlit_runs")
    aggregated_data = {}

    for run_path in runs_dir.iterdir():
        if not run_path.is_dir():
            continue

        eval_file = run_path / "evaluation.json"
        if not eval_file.exists():
            continue

        try:
            with open(eval_file) as f:
                eval_data = json.load(f)

            results = eval_data.get("results", [])
            if not results:
                continue

            first_result = results[0]
            model = first_result.get("model", "unknown")
            dataset = first_result.get("dataset", "unknown")

            config_file = run_path / "config.yaml"
            temperature = None
            if config_file.exists():
                with open(config_file) as f:
                    config = yaml.safe_load(f)
                    models = config.get("inference", {}).get("models", [])
                    for m in models:
                        if m.get("name") == model:
                            temperature = m.get("temperature")
                            break

            if temperature is None and results:
                temperature = first_result.get("temperature")

            model_display = get_model_display_name(model, temperature)
            key = (model_display, dataset)

            if key not in aggregated_data:
                aggregated_data[key] = {
                    "model_display": model_display,
                    "dataset": dataset,
                    "runs": [],
                    "num_questions": 0,
                    "legibility_scores": [],
                    "correctness_counts": Counter(),
                }

            aggregated_data[key]["runs"].append(run_path.name)
            aggregated_data[key]["num_questions"] += len(results)
            aggregated_data[key]["legibility_scores"].extend(
                [get_legibility_score(r) for r in results]
            )
            for r in results:
                aggregated_data[key]["correctness_counts"][get_correctness(r)] += 1

        except Exception:
            continue

    runs_data = []
    for data in aggregated_data.values():
        scores = data["legibility_scores"]
        counts = data["correctness_counts"]
        total = data["num_questions"]

        run_info = {
            "model_display": data["model_display"],
            "dataset": data["dataset"],
            "runs": data["runs"],
            "num_questions": total,
            "avg_legibility": sum(scores) / len(scores) if scores else 0,
            "legibility_std": pd.Series(scores).std() if len(scores) > 1 else 0,
            "correct_pct": counts.get("correct", 0) / total * 100 if total > 0 else 0,
            "partial_pct": counts.get("partially_correct", 0) / total * 100
            if total > 0
            else 0,
            "incorrect_pct": counts.get("incorrect", 0) / total * 100
            if total > 0
            else 0,
        }
        runs_data.append(run_info)

    return pd.DataFrame(runs_data)


@st.cache_data(ttl=300)
def load_results_for_runs(run_names):
    runs_dir = Path("streamlit_runs")
    all_results = []

    for run_name in run_names:
        run_path = runs_dir / run_name
        eval_file = run_path / "evaluation.json"

        if not eval_file.exists():
            continue

        with open(eval_file) as f:
            eval_data = json.load(f)

        inference_data = load_inference_data(run_path)
        results = eval_data.get("results", [])
        enrich_results_with_inference(results, inference_data)
        all_results.extend(results)

    return all_results


df = load_runs_metadata()

if df.empty:
    st.error("No runs found with evaluation data")
    st.stop()

st.title("CoT Legibility Explorer")

st.markdown("---")

st.subheader("Model")
all_models = sorted(df["model_display"].unique().tolist())
if "dataset" in st.session_state and st.session_state.dataset != "Select a dataset...":
    available_models = sorted(
        df[df["dataset"] == st.session_state.dataset]["model_display"].unique().tolist()
    )
    model_options = ["Select a model..."] + available_models
else:
    model_options = ["Select a model..."] + all_models
selected_model = st.selectbox(
    "Model", model_options, label_visibility="collapsed", key="model"
)

st.subheader("Dataset")
all_datasets = sorted(df["dataset"].unique().tolist())
if selected_model != "Select a model...":
    available_datasets = sorted(
        df[df["model_display"] == selected_model]["dataset"].unique().tolist()
    )
    dataset_options = ["Select a dataset..."] + available_datasets
else:
    dataset_options = ["Select a dataset..."] + all_datasets
selected_dataset = st.selectbox(
    "Dataset", dataset_options, label_visibility="collapsed", key="dataset"
)

if selected_model != "Select a model..." and selected_dataset != "Select a dataset...":
    run_data = df[
        (df["model_display"] == selected_model) & (df["dataset"] == selected_dataset)
    ]

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
            st.metric(
                "Average Legibility (1-9)",
                f"{run['avg_legibility']:.2f} ± {run['legibility_std']:.2f}",
            )
        with col3:
            st.metric("Correct", f"{run['correct_pct']:.1f}%")
        with col4:
            st.metric("Partially Correct", f"{run['partial_pct']:.1f}%")
        with col5:
            st.metric("Incorrect", f"{run['incorrect_pct']:.1f}%")

        st.caption(f"Combined from {len(run['runs'])} run(s): {', '.join(run['runs'])}")

        results = load_results_for_runs(tuple(run["runs"]))

        st.markdown("---")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            fig, ax = plt.subplots(1, 1, figsize=(6, 4))

            legibility_scores = [get_legibility_score(r) for r in results]
            bins = [i + 0.5 for i in range(0, 10)]
            ax.hist(legibility_scores, bins=bins, color="#87CEEB", edgecolor="black")
            ax.set_xlabel("Legibility Score (1=legible, 9=illegible)")
            ax.set_ylabel("Count")
            ax.set_title("Legibility Score Distribution")
            ax.set_xlim(0, 10)
            ax.set_xticks(range(1, 10))

            st.pyplot(fig)
            plt.close()

        st.markdown("---")

        st.subheader("Questions")

        with st.expander("Filters", expanded=True):
            min_leg = float(min(legibility_scores) if legibility_scores else 1.0)
            max_leg = float(max(legibility_scores) if legibility_scores else 9.0)
            min_leg = max(1.0, min(min_leg, 9.0))
            max_leg = max(1.0, min(max_leg, 9.0))

            legibility_range = st.slider(
                "Legibility Score Range",
                min_value=1.0,
                max_value=9.0,
                value=(min_leg, max_leg),
                step=0.1,
            )

            correctness_options = st.multiselect(
                "Correctness",
                options=CORRECTNESS_VALUES + ["unknown"],
                default=CORRECTNESS_VALUES + ["unknown"],
            )

        filtered_results = [
            r
            for r in results
            if legibility_range[0] <= get_legibility_score(r) <= legibility_range[1]
            and get_correctness(r) in correctness_options
        ]

        col1, col2, col3 = st.columns([1, 2, 1.5])
        with col1:
            entries_to_show = st.selectbox(
                "Entries to show",
                options=[10, 25, 50, 100, len(filtered_results)],
                index=1,
                key="entries_select",
            )
        with col3:
            search_query = st.text_input(
                "Search", placeholder="Search all content...", key="search"
            )

        if filtered_results:
            if "selected_question_idx" not in st.session_state:
                st.session_state.selected_question_idx = None

            table_data = []
            for i, result in enumerate(filtered_results):
                qid = result.get("question_id", f"Question {i+1}")

                if search_query:
                    searchable_text = " ".join(
                        [
                            str(result.get("question_id", "")),
                            str(result.get("question", "")),
                            str(result.get("reasoning", "")),
                            str(result.get("answer", "")),
                            str(result.get("correct_answer", "")),
                            str(result.get("legibility", {}).get("explanation", "")),
                            str(result.get("correctness", {}).get("explanation", "")),
                        ]
                    ).lower()

                    if search_query.lower() not in searchable_text:
                        continue

                correctness_display = CORRECTNESS_DISPLAY.get(
                    get_correctness(result), "? Unknown"
                )

                table_data.append(
                    {
                        "ID": qid,
                        "Legibility": f"{get_legibility_score(result):.2f}",
                        "Correctness": correctness_display,
                        "original_index": i,
                    }
                )

            def sort_key(x):
                is_unknown = "Unknown" in x["Correctness"]
                return (is_unknown, -float(x["Legibility"]))

            table_data.sort(key=sort_key)
            table_data = table_data[:entries_to_show]
            table_df = pd.DataFrame(table_data)

            event = st.dataframe(
                table_df[["ID", "Legibility", "Correctness"]],
                width="stretch",
                hide_index=True,
                height=400,
                on_select="rerun",
                selection_mode="single-row",
            )

            st.caption("Click the checkbox on the left of a row to view details")

            if (
                event.selection
                and "rows" in event.selection
                and len(event.selection["rows"]) > 0
            ):
                selected_row = event.selection["rows"][0]
                st.session_state.selected_question_idx = table_df.iloc[selected_row][
                    "original_index"
                ]

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
                    st.text_area(
                        "Model Reasoning",
                        result.get("reasoning"),
                        height=200,
                        key=f"reasoning_detail_{result.get('question_id')}_{result.get('sample_index', 0)}",
                        label_visibility="collapsed",
                    )

                st.markdown("#### Model Answer")
                st.text_area(
                    "Model Answer",
                    result.get("answer", "N/A"),
                    height=200,
                    key=f"answer_detail_{result.get('question_id')}_{result.get('sample_index', 0)}",
                    label_visibility="collapsed",
                )

                st.markdown("#### Scores")
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Legibility**")
                    st.write(f"Score: {get_legibility_score(result):.2f}")
                    st.write(result.get("legibility", {}).get("explanation", "N/A"))

                with col2:
                    st.markdown("**Correctness**")
                    st.write(f"Grade: {get_correctness(result)}")
                    st.write(result.get("correctness", {}).get("explanation", "N/A"))
        else:
            st.info("No questions match the selected filters")
