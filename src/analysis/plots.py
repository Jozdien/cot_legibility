from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

from ..utils.io import ensure_dir, read_json


def setup_matplotlib():
    font_path = Path("fonts/Montserrat-Regular.ttf")
    if font_path.exists():
        fm.fontManager.addfont(str(font_path))
        plt.rcParams["font.family"] = "Montserrat"
    plt.rcParams["hatch.linewidth"] = 1


def plot_legibility_scores_boxplot(evaluation: dict, output_dir: Path) -> None:
    results = evaluation["results"]
    scores = [
        r["legibility"]["score"]
        for r in results
        if "legibility" in r and isinstance(r["legibility"].get("score"), (int, float))
    ]

    if not scores:
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    bp = ax.boxplot([scores], patch_artist=True, widths=0.5)

    for box in bp["boxes"]:
        box.set(facecolor="#3498db", alpha=0.8)

    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title(f"CoT Illegibility Distribution (n={len(scores)})", fontsize=14)
    ax.set_ylim(0, 10)
    ax.set_xticklabels([""])
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "legibility_scores_boxplot.png", dpi=150)
    plt.close()


def plot_correctness_assessment(evaluation: dict, output_dir: Path) -> None:
    stats = evaluation["statistics"].get("correctness")
    if not stats:
        return

    categories = ["Correct", "Partially\nCorrect", "Incorrect"]
    percentages = [stats["correct_pct"], stats["partially_pct"], stats["incorrect_pct"]]
    colors = ["#2ecc71", "#f39c12", "#e74c3c"]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(categories, percentages, color=colors, alpha=0.8)

    for bar, pct in zip(bars, percentages):
        if pct > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                pct + 2,
                f"{pct:.1f}%",
                ha="center",
                fontsize=10,
            )

    ax.set_ylabel("Percentage (%)", fontsize=12)
    ax.set_title(f"Correctness Assessment (n={stats['total']})", fontsize=14)
    ax.set_ylim(0, 100)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "correctness_assessment.png", dpi=150)
    plt.close()


def plot_legibility_by_correctness(evaluation: dict, output_dir: Path) -> None:
    results = evaluation["results"]

    categories = {"correct": [], "partially_correct": [], "incorrect": []}

    for r in results:
        if "legibility" in r and "correctness" in r:
            score = r["legibility"].get("score")
            grade = r["correctness"].get("correctness")
            if isinstance(score, (int, float)) and grade in categories:
                categories[grade].append(score)

    if not any(categories.values()):
        return

    data = [
        categories["correct"],
        categories["partially_correct"],
        categories["incorrect"],
    ]
    labels = ["Correct", "Partially\nCorrect", "Incorrect"]
    colors = ["#2ecc71", "#f39c12", "#e74c3c"]

    fig, ax = plt.subplots(figsize=(10, 6))
    bp = ax.boxplot(data, patch_artist=True, labels=labels)

    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.8)

    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title("Illegibility by Correctness", fontsize=14)
    ax.set_ylim(0, 10)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "legibility_by_correctness.png", dpi=150)
    plt.close()


def plot_length_vs_legibility(evaluation: dict, output_dir: Path) -> None:
    results = evaluation["results"]

    length_map = {}
    inference_file = evaluation.get("metadata", {}).get("inference_file")
    if inference_file and Path(inference_file).exists():
        inference_data = read_json(inference_file)
        for item in inference_data:
            reasoning = item.get("reasoning", "")
            if reasoning:
                q_id = item["question_id"]
                sample_idx = item.get("sample_index", 0)
                length_map[(q_id, sample_idx)] = len(reasoning)

    lengths = []
    scores = []

    for r in results:
        q_id = r.get("question_id")
        sample_idx = r.get("sample_index", 0)
        length = length_map.get((q_id, sample_idx))
        if not length:
            continue

        score = r.get("legibility_reasoning", r.get("legibility", {})).get("score")
        if isinstance(score, (int, float)):
            lengths.append(length)
            scores.append(score)

    if not lengths:
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(lengths, scores, alpha=0.5, color="#3498db")

    ax.set_xlabel("Reasoning Length (characters)", fontsize=12)
    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title("Reasoning Length vs Illegibility", fontsize=14)
    ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "length_vs_legibility.png", dpi=150)
    plt.close()


def plot_model_comparison(
    evaluations: list[tuple[str, dict]], output_dir: Path
) -> None:
    model_names = [name for name, _ in evaluations]

    response_data = []
    reasoning_data = []

    for _, ev in evaluations:
        results = ev["results"]

        response_scores = [
            r.get("legibility_response", {}).get("score") for r in results
        ]
        response_scores = [s for s in response_scores if isinstance(s, (int, float))]
        response_data.append(response_scores)

        reasoning_scores = [
            r.get("legibility_reasoning", {}).get("score") for r in results
        ]
        reasoning_scores = [s for s in reasoning_scores if isinstance(s, (int, float))]
        reasoning_data.append(reasoning_scores)

    if not any(response_data) and not any(reasoning_data):
        legacy_data = []
        for _, ev in evaluations:
            results = ev["results"]
            scores = [r.get("legibility", {}).get("score") for r in results]
            scores = [s for s in scores if isinstance(s, (int, float))]
            legacy_data.append(scores)
        reasoning_data = legacy_data

    positions = np.arange(len(model_names)) * 3

    fig, ax = plt.subplots(figsize=(12, 6))

    bp_kwargs = {"widths": 0.7, "patch_artist": True, "whis": [1, 99]}

    if any(response_data):
        bp_response = ax.boxplot(response_data, positions=positions, **bp_kwargs)
        for box in bp_response["boxes"]:
            box.set(facecolor="#0273b2", alpha=1)

    if any(reasoning_data):
        offset = 1 if any(response_data) else 0
        bp_reasoning = ax.boxplot(
            reasoning_data, positions=positions + offset, **bp_kwargs
        )
        for box in bp_reasoning["boxes"]:
            box.set(facecolor="#d65e00", alpha=1)

    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_xticks(positions + (0.5 if any(response_data) else 0))
    ax.set_xticklabels(model_names)
    ax.set_ylim(0, 9.5)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    if any(response_data) and any(reasoning_data):
        legend_elements = [
            plt.Rectangle((0, 0), 1, 1, facecolor="#0273b2", label="Response"),
            plt.Rectangle((0, 0), 1, 1, facecolor="#d65e00", label="Reasoning"),
        ]
        ax.legend(handles=legend_elements, loc="upper right")

    plt.tight_layout()
    plt.savefig(output_dir / "model_comparison.png", dpi=150)
    plt.close()


def plot_legibility_comparison(
    evaluations: list[tuple[str, dict]], output_dir: Path
) -> None:
    model_names = [name for name, _ in evaluations]
    means = [
        ev["statistics"]["legibility"]["mean"]
        for _, ev in evaluations
        if "legibility" in ev["statistics"]
    ]
    stds = [
        ev["statistics"]["legibility"]["std"]
        for _, ev in evaluations
        if "legibility" in ev["statistics"]
    ]

    if not means:
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(model_names))
    ax.bar(x, means, color="#3498db", alpha=0.8)
    ax.errorbar(x, means, yerr=stds, fmt="none", ecolor="black", capsize=5)

    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title("Model Comparison - Illegibility", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(model_names, rotation=45, ha="right")
    ax.set_ylim(0, 10)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "legibility_comparison.png", dpi=150)
    plt.close()


def plot_legibility_by_difficulty(
    evaluation: dict, output_dir: Path, baseline_path: str = None
) -> None:
    if not baseline_path:
        return

    baseline_data = read_json(baseline_path)
    baseline_results = (
        baseline_data.get("results", baseline_data)
        if isinstance(baseline_data, dict)
        else baseline_data
    )
    baseline_map = {
        item["question_id"]: item.get("correctness", {}).get("correctness")
        for item in baseline_results
    }

    categorized = {"correct": [], "partially_correct": [], "incorrect": []}

    for r in evaluation["results"]:
        q_id = r["question_id"]
        if q_id not in baseline_map:
            continue

        category = baseline_map[q_id]
        if category not in categorized:
            continue

        score = r.get("legibility_reasoning", r.get("legibility", {})).get("score")
        if isinstance(score, (int, float)):
            categorized[category].append(score)

    data = [
        categorized["correct"],
        categorized["partially_correct"],
        categorized["incorrect"],
    ]
    labels = [
        "Easy\n(Baseline Correct)",
        "Medium\n(Baseline Partial)",
        "Hard\n(Baseline Incorrect)",
    ]
    colors = ["#2ecc71", "#f39c12", "#e74c3c"]
    hatches = ["", "///", "xxx"]

    fig, ax = plt.subplots(figsize=(10, 6))
    bp = ax.boxplot(data, labels=labels, patch_artist=True, widths=0.6)

    for patch, color, hatch in zip(bp["boxes"], colors, hatches):
        patch.set_facecolor(color)
        patch.set_alpha(0.8)
        patch.set_hatch(hatch)

    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_ylim(0, 9.5)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "legibility_by_difficulty.png", dpi=150)
    plt.close()


def plot_legibility_by_difficulty_comparison(
    evaluations: list[tuple[str, dict]], output_dir: Path, baseline_path: str = None
) -> None:
    if not baseline_path:
        return

    baseline_data = read_json(baseline_path)
    baseline_results = (
        baseline_data.get("results", baseline_data)
        if isinstance(baseline_data, dict)
        else baseline_data
    )
    baseline_map = {
        item["question_id"]: item.get("correctness", {}).get("correctness")
        for item in baseline_results
    }

    model_names = [name for name, _ in evaluations]
    x = np.arange(len(model_names)) * 1.5
    width = 0.4

    colors = {
        "correct": "#2ecc71",
        "partially_correct": "#f39c12",
        "incorrect": "#e74c3c",
    }
    hatches = {"correct": "", "partially_correct": "///", "incorrect": "xxx"}

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, category in enumerate(["correct", "partially_correct", "incorrect"]):
        all_data = []

        for _, ev in evaluations:
            scores = []
            for r in ev["results"]:
                q_id = r["question_id"]
                if q_id in baseline_map and baseline_map[q_id] == category:
                    score = r.get("legibility_reasoning", r.get("legibility", {})).get(
                        "score"
                    )
                    if isinstance(score, (int, float)):
                        scores.append(score)
            all_data.append(scores)

        positions = x + (i - 1) * width
        bp = ax.boxplot(
            all_data, positions=positions, widths=width * 0.8, patch_artist=True
        )

        for box in bp["boxes"]:
            box.set(facecolor=colors[category], alpha=0.8, hatch=hatches[category])

    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(model_names)
    ax.set_ylim(0, 9.5)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    from matplotlib.patches import Patch

    legend_elements = [
        Patch(
            facecolor=colors["correct"],
            hatch=hatches["correct"],
            label="Easy (Baseline Correct)",
        ),
        Patch(
            facecolor=colors["partially_correct"],
            hatch=hatches["partially_correct"],
            label="Medium (Baseline Partial)",
        ),
        Patch(
            facecolor=colors["incorrect"],
            hatch=hatches["incorrect"],
            label="Hard (Baseline Incorrect)",
        ),
    ]
    ax.legend(handles=legend_elements)

    plt.tight_layout()
    plt.savefig(output_dir / "legibility_by_difficulty_comparison.png", dpi=150)
    plt.close()


def plot_correctness_vs_legibility_scatter(
    evaluation: dict, output_dir: Path, use_normalized: bool = False
) -> None:
    from scipy import stats as scipy_stats

    correctness_map = {"correct": 1, "partially_correct": 0.5, "incorrect": 0}

    length_map = {}
    if use_normalized:
        inference_file = evaluation.get("metadata", {}).get("inference_file")
        if inference_file and Path(inference_file).exists():
            inference_data = read_json(inference_file)
            for item in inference_data:
                reasoning = item.get("reasoning", "")
                if reasoning:
                    q_id = item["question_id"]
                    sample_idx = item.get("sample_index", 0)
                    length_map[(q_id, sample_idx)] = len(reasoning)

    median_length = np.median(list(length_map.values())) if length_map else 1

    by_question = {}
    for r in evaluation["results"]:
        q_id = r.get("question_id")
        corr = r.get("correctness", {}).get("correctness")
        if corr not in correctness_map:
            continue

        score = r.get("legibility_reasoning", r.get("legibility", {})).get("score")
        if not isinstance(score, (int, float)):
            continue

        if use_normalized:
            sample_idx = r.get("sample_index", 0)
            length = length_map.get((q_id, sample_idx))
            if not length or length == 0:
                continue
            score = (score / length) * median_length

        if q_id not in by_question:
            by_question[q_id] = {"correctness": [], "legibility": [], "question": r.get("question", "")}
        by_question[q_id]["correctness"].append(correctness_map[corr])
        by_question[q_id]["legibility"].append(score)

    questions_with_multiple = {q_id: data for q_id, data in by_question.items() if len(data["correctness"]) > 1}

    if not questions_with_multiple:
        print("  Skipping correctness_vs_legibility_scatter: no questions with multiple samples")
        return

    question_correlations = []
    for q_id, data in questions_with_multiple.items():
        corr_vals = np.array(data["correctness"])
        leg_vals = np.array(data["legibility"])

        if len(set(corr_vals)) <= 1:
            continue

        if len(set(leg_vals)) > 1:
            corr_coef, _ = scipy_stats.pearsonr(corr_vals, leg_vals)
        else:
            corr_coef = 0
        question_correlations.append((q_id, corr_coef, data))

    if not question_correlations:
        print("  Skipping correctness_vs_legibility_scatter: no questions with variance in correctness")
        return

    question_correlations.sort(key=lambda x: x[1])

    n_questions = len(question_correlations)
    if n_questions == 1:
        selected_indices = [0]
    elif n_questions == 2:
        selected_indices = [0, 1]
    elif n_questions == 3:
        selected_indices = [0, 1, 2]
    else:
        selected_indices = [0, n_questions // 3, 2 * n_questions // 3, n_questions - 1]

    selected_questions = [question_correlations[i] for i in selected_indices]

    n_cols = min(2, len(selected_questions))
    n_rows = (len(selected_questions) + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))
    if n_rows * n_cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for idx, (q_id, corr_coef, data) in enumerate(selected_questions):
        ax = axes[idx]

        corr_vals = np.array(data["correctness"])
        leg_vals = np.array(data["legibility"])

        for x_val in [0, 0.5, 1]:
            mask = corr_vals == x_val
            if not mask.any():
                continue

            y = leg_vals[mask]
            if len(y) < 2:
                ax.scatter([x_val] * len(y), y, alpha=0.6, s=30, color="#3498db")
                continue

            x_jitter = np.random.normal(0, 0.02, size=len(y)) + x_val
            xy = np.vstack([x_jitter, y])

            try:
                density = scipy_stats.gaussian_kde(xy)(xy)
                density_range = density.max() - density.min()
                if density_range > 0:
                    density_scaled = (density - density.min()) / density_range
                    ax.scatter(x_jitter, y, c=plt.cm.viridis(density_scaled), alpha=0.6, s=30)
                else:
                    ax.scatter(x_jitter, y, alpha=0.6, s=30, color="#3498db")
            except Exception:
                ax.scatter(x_jitter, y, alpha=0.6, s=30, color="#3498db")

        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(["Inc", "Part", "Corr"], fontsize=9)
        ax.set_ylabel(f"{'Norm ' if use_normalized else ''}Illegibility", fontsize=10)
        ax.set_ylim(0, 10)
        ax.grid(True, linestyle="--", alpha=0.3)

        question_preview = data["question"][:60] + "..." if len(data["question"]) > 60 else data["question"]
        ax.set_title(f"r={corr_coef:.2f}, n={len(corr_vals)}\n{question_preview}", fontsize=9)

    for idx in range(len(selected_questions), len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()
    suffix = "_normalized" if use_normalized else ""
    plt.savefig(output_dir / f"correctness_vs_legibility_scatter{suffix}.png", dpi=150)
    plt.close()


def plot_question_correlations(
    evaluation: dict, output_dir: Path, use_normalized: bool = False
) -> None:
    from scipy import stats as scipy_stats

    correctness_map = {"correct": 1, "partially_correct": 0.5, "incorrect": 0}

    length_map = {}
    if use_normalized:
        inference_file = evaluation.get("metadata", {}).get("inference_file")
        if inference_file and Path(inference_file).exists():
            inference_data = read_json(inference_file)
            for item in inference_data:
                reasoning = item.get("reasoning", "")
                if reasoning:
                    q_id = item["question_id"]
                    sample_idx = item.get("sample_index", 0)
                    length_map[(q_id, sample_idx)] = len(reasoning)

    median_length = np.median(list(length_map.values())) if length_map else 1

    by_question = {}
    for r in evaluation["results"]:
        q_id = r.get("question_id")
        corr = r.get("correctness", {}).get("correctness")
        if corr not in correctness_map:
            continue

        score = r.get("legibility_reasoning", r.get("legibility", {})).get("score")
        if not isinstance(score, (int, float)):
            continue

        if use_normalized:
            sample_idx = r.get("sample_index", 0)
            length = length_map.get((q_id, sample_idx))
            if not length or length == 0:
                continue
            score = (score / length) * median_length

        if q_id not in by_question:
            by_question[q_id] = {"correctness": [], "legibility": []}
        by_question[q_id]["correctness"].append(correctness_map[corr])
        by_question[q_id]["legibility"].append(score)

    questions_with_multiple = {q_id: data for q_id, data in by_question.items() if len(data["correctness"]) > 1}

    if not questions_with_multiple:
        print("  Skipping question_correlations: no questions with multiple samples")
        return

    correlations = []
    for q_id, data in questions_with_multiple.items():
        corr_vals = np.array(data["correctness"])
        leg_vals = np.array(data["legibility"])

        if len(set(corr_vals)) <= 1:
            continue

        if len(set(leg_vals)) > 1:
            corr_coef, _ = scipy_stats.pearsonr(corr_vals, leg_vals)
        else:
            corr_coef = 0
        correlations.append(corr_coef)

    if not correlations:
        print("  Skipping question_correlations: no questions with variance in correctness")
        return

    correlations = sorted(correlations)

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(correlations))
    ax.scatter(x, correlations, alpha=0.6, s=50, color="#3498db")

    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5, linewidth=1)

    mean_corr = np.mean(correlations)
    ax.axhline(y=mean_corr, color='green', linestyle='--', alpha=0.5, linewidth=2, label=f'Mean: {mean_corr:.3f}')

    ax.set_xlabel("Question Index (sorted by correlation)", fontsize=12)
    ax.set_ylabel("Pearson Correlation (Correctness vs Illegibility)", fontsize=12)
    ax.set_title(f"Question-Level Correlations (n={len(correlations)})", fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    suffix = "_normalized" if use_normalized else ""
    plt.savefig(output_dir / f"question_correlations{suffix}.png", dpi=150)
    plt.close()


def plot_correctness_vs_legibility_scatter_comparison(
    evaluations: list[tuple[str, dict]], output_dir: Path, use_normalized: bool = False
) -> None:
    from scipy import stats as scipy_stats

    correctness_map = {"correct": 1, "partially_correct": 0.5, "incorrect": 0}

    by_question = {}
    all_lengths = []

    for _, ev in evaluations:
        length_map = {}
        if use_normalized:
            inference_file = ev.get("metadata", {}).get("inference_file")
            if inference_file and Path(inference_file).exists():
                inference_data = read_json(inference_file)
                for item in inference_data:
                    reasoning = item.get("reasoning", "")
                    if reasoning:
                        q_id = item["question_id"]
                        sample_idx = item.get("sample_index", 0)
                        length = len(reasoning)
                        length_map[(q_id, sample_idx)] = length
                        all_lengths.append(length)

    median_length = np.median(all_lengths) if all_lengths else 1

    for _, ev in evaluations:
        length_map = {}
        if use_normalized:
            inference_file = ev.get("metadata", {}).get("inference_file")
            if inference_file and Path(inference_file).exists():
                inference_data = read_json(inference_file)
                for item in inference_data:
                    reasoning = item.get("reasoning", "")
                    if reasoning:
                        q_id = item["question_id"]
                        sample_idx = item.get("sample_index", 0)
                        length_map[(q_id, sample_idx)] = len(reasoning)

        for r in ev["results"]:
            q_id = r.get("question_id")
            corr = r.get("correctness", {}).get("correctness")
            if corr not in correctness_map:
                continue

            score = r.get("legibility_reasoning", r.get("legibility", {})).get("score")
            if not isinstance(score, (int, float)):
                continue

            if use_normalized:
                sample_idx = r.get("sample_index", 0)
                length = length_map.get((q_id, sample_idx))
                if not length or length == 0:
                    continue
                score = (score / length) * median_length

            if q_id not in by_question:
                by_question[q_id] = {"correctness": [], "legibility": [], "question": r.get("question", "")}
            by_question[q_id]["correctness"].append(correctness_map[corr])
            by_question[q_id]["legibility"].append(score)

    questions_with_multiple = {q_id: data for q_id, data in by_question.items() if len(data["correctness"]) > 1}

    if not questions_with_multiple:
        print("  Skipping correctness_vs_legibility_scatter_comparison: no questions with multiple samples")
        return

    question_correlations = []
    for q_id, data in questions_with_multiple.items():
        corr_vals = np.array(data["correctness"])
        leg_vals = np.array(data["legibility"])

        if len(set(corr_vals)) <= 1:
            continue

        if len(set(leg_vals)) > 1:
            corr_coef, _ = scipy_stats.pearsonr(corr_vals, leg_vals)
        else:
            corr_coef = 0
        question_correlations.append((q_id, corr_coef, data))

    if not question_correlations:
        print("  Skipping correctness_vs_legibility_scatter_comparison: no questions with variance in correctness")
        return

    question_correlations.sort(key=lambda x: x[1])

    n_questions = len(question_correlations)
    if n_questions == 1:
        selected_indices = [0]
    elif n_questions == 2:
        selected_indices = [0, 1]
    elif n_questions == 3:
        selected_indices = [0, 1, 2]
    else:
        selected_indices = [0, n_questions // 3, 2 * n_questions // 3, n_questions - 1]

    selected_questions = [question_correlations[i] for i in selected_indices]

    n_cols = min(2, len(selected_questions))
    n_rows = (len(selected_questions) + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))
    if n_rows * n_cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for idx, (q_id, corr_coef, data) in enumerate(selected_questions):
        ax = axes[idx]

        corr_vals = np.array(data["correctness"])
        leg_vals = np.array(data["legibility"])

        for x_val in [0, 0.5, 1]:
            mask = corr_vals == x_val
            if not mask.any():
                continue

            y = leg_vals[mask]
            if len(y) < 2:
                ax.scatter([x_val] * len(y), y, alpha=0.6, s=30, color="#3498db")
                continue

            x_jitter = np.random.normal(0, 0.02, size=len(y)) + x_val
            xy = np.vstack([x_jitter, y])

            try:
                density = scipy_stats.gaussian_kde(xy)(xy)
                density_range = density.max() - density.min()
                if density_range > 0:
                    density_scaled = (density - density.min()) / density_range
                    ax.scatter(x_jitter, y, c=plt.cm.viridis(density_scaled), alpha=0.6, s=30)
                else:
                    ax.scatter(x_jitter, y, alpha=0.6, s=30, color="#3498db")
            except Exception:
                ax.scatter(x_jitter, y, alpha=0.6, s=30, color="#3498db")

        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(["Inc", "Part", "Corr"], fontsize=9)
        ax.set_ylabel(f"{'Norm ' if use_normalized else ''}Illegibility", fontsize=10)
        ax.set_ylim(0, 10)
        ax.grid(True, linestyle="--", alpha=0.3)

        question_preview = data["question"][:60] + "..." if len(data["question"]) > 60 else data["question"]
        ax.set_title(f"r={corr_coef:.2f}, n={len(corr_vals)}\n{question_preview}", fontsize=9)

    for idx in range(len(selected_questions), len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()
    suffix = "_normalized" if use_normalized else ""
    plt.savefig(
        output_dir / f"correctness_vs_legibility_scatter_comparison{suffix}.png",
        dpi=150,
    )
    plt.close()


def plot_legibility_progression(evaluation: dict, output_dir: Path) -> None:
    chunk_scores_by_position = {}

    for r in evaluation["results"]:
        chunks = r.get("legibility_chunks", [])
        for chunk in chunks:
            pos = chunk.get("start_pos", 0)
            score = chunk.get("score")
            if isinstance(score, (int, float)):
                if pos not in chunk_scores_by_position:
                    chunk_scores_by_position[pos] = []
                chunk_scores_by_position[pos].append(score)

    if not chunk_scores_by_position:
        return

    positions = sorted(chunk_scores_by_position.keys())
    data = [chunk_scores_by_position[p] for p in positions]

    fig, ax = plt.subplots(figsize=(12, 6))
    bp = ax.boxplot(
        data, positions=range(len(positions)), patch_artist=True, widths=0.6
    )

    for box in bp["boxes"]:
        box.set(facecolor="#3498db", alpha=0.8)

    ax.set_xlabel("Characters", fontsize=12)
    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_ylim(0, 10)
    ax.set_xticks(range(len(positions)))
    ax.set_xticklabels(positions)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "legibility_progression.png", dpi=150)
    plt.close()


def plot_prefill_correctness_comparison(evaluation: dict, output_dir: Path) -> None:
    stats = evaluation["statistics"]
    prefill_stats = stats.get("prefill_correctness")
    original_stats = stats.get("original_correctness")

    if not prefill_stats or not original_stats:
        return

    categories = ["Correct", "Partially\nCorrect", "Incorrect"]
    prefill_pcts = [
        prefill_stats["correct_pct"],
        prefill_stats["partially_pct"],
        prefill_stats["incorrect_pct"],
    ]
    original_pcts = [
        original_stats["correct_pct"],
        original_stats["partially_pct"],
        original_stats["incorrect_pct"],
    ]
    colors = ["#2ecc71", "#f39c12", "#e74c3c"]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width/2, original_pcts, width, label="Original", alpha=0.8, color=colors)
    bars2 = ax.bar(x + width/2, prefill_pcts, width, label="Prefilled", alpha=0.8, color=colors, hatch="///")

    for bars, pcts in [(bars1, original_pcts), (bars2, prefill_pcts)]:
        for bar, pct in zip(bars, pcts):
            if pct > 0:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    pct + 2,
                    f"{pct:.1f}%",
                    ha="center",
                    fontsize=9,
                )

    ax.set_ylabel("Percentage (%)", fontsize=12)
    ax.set_title(f"Correctness: Original vs Prefilled (n={prefill_stats['total']})", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 110)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "prefill_correctness_comparison.png", dpi=150)
    plt.close()


PLOT_FUNCTIONS = {
    "legibility_scores_boxplot": plot_legibility_scores_boxplot,
    "correctness_assessment": plot_correctness_assessment,
    "legibility_by_correctness": plot_legibility_by_correctness,
    "length_vs_legibility": plot_length_vs_legibility,
    "legibility_by_difficulty": plot_legibility_by_difficulty,
    "correctness_vs_legibility_scatter": plot_correctness_vs_legibility_scatter,
    "correctness_vs_legibility_scatter_normalized": lambda e,
    o: plot_correctness_vs_legibility_scatter(e, o, use_normalized=True),
    "question_correlations": plot_question_correlations,
    "question_correlations_normalized": lambda e,
    o: plot_question_correlations(e, o, use_normalized=True),
    "legibility_progression": plot_legibility_progression,
    "prefill_correctness_comparison": plot_prefill_correctness_comparison,
}

COMPARISON_PLOT_FUNCTIONS = {
    "model_comparison": plot_model_comparison,
    "legibility_comparison": plot_legibility_comparison,
    "legibility_by_difficulty_comparison": plot_legibility_by_difficulty_comparison,
    "correctness_vs_legibility_scatter_comparison": plot_correctness_vs_legibility_scatter_comparison,
    "correctness_vs_legibility_scatter_comparison_normalized": lambda e,
    o,
    b=None: plot_correctness_vs_legibility_scatter_comparison(
        e, o, use_normalized=True
    ),
}


def run_analysis_stage(config: dict, output_dir: Path, logger) -> None:
    setup_matplotlib()
    plots_dir = ensure_dir(output_dir / "plots")

    baseline_path = config.get("baseline_file")

    comparison = config.get("comparison", {})
    if comparison.get("enabled"):
        logger.info("Running comparison analysis")
        runs = comparison.get("runs", [])

        evaluations = []
        for run_path in runs:
            run_path = Path(run_path)
            if run_path.is_file():
                eval_data = read_json(run_path)
                name = run_path.parent.name
            else:
                eval_file = run_path / "evaluation.json"
                eval_data = read_json(eval_file)
                name = run_path.name

            evaluations.append((name, eval_data))

        logger.info(f"Loaded {len(evaluations)} evaluations for comparison")

        for plot_type in comparison.get("plot_types", []):
            if plot_type in COMPARISON_PLOT_FUNCTIONS:
                logger.info(f"Generating {plot_type} plot")
                plot_func = COMPARISON_PLOT_FUNCTIONS[plot_type]

                if plot_type == "legibility_by_difficulty_comparison":
                    plot_func(evaluations, plots_dir, baseline_path)
                else:
                    plot_func(evaluations, plots_dir)

    else:
        evaluation_file = output_dir / "evaluation.json"
        if not evaluation_file.exists():
            logger.warning(f"Evaluation file not found: {evaluation_file}")
            return

        logger.info(f"Loading evaluation from {evaluation_file}")
        evaluation = read_json(evaluation_file)

        for plot_name in config.get("plots", []):
            if plot_name in PLOT_FUNCTIONS:
                logger.info(f"Generating {plot_name} plot")
                plot_func = PLOT_FUNCTIONS[plot_name]

                if plot_name == "legibility_by_difficulty":
                    plot_func(evaluation, plots_dir, baseline_path)
                else:
                    plot_func(evaluation, plots_dir)

        prefill_evaluation_file = output_dir / "prefill_evaluation.json"
        if prefill_evaluation_file.exists():
            logger.info(f"Loading prefill evaluation from {prefill_evaluation_file}")
            prefill_evaluation = read_json(prefill_evaluation_file)
            logger.info("Generating prefill correctness comparison plot")
            plot_prefill_correctness_comparison(prefill_evaluation, plots_dir)

    logger.info(f"Analysis complete. Plots saved to {plots_dir}")
