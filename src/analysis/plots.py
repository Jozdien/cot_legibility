import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path

from ..utils.io import read_json, ensure_dir


def setup_matplotlib():
    font_path = Path("fonts/Montserrat-Regular.ttf")
    if font_path.exists():
        fm.fontManager.addfont(str(font_path))
        plt.rcParams["font.family"] = "Montserrat"
    plt.rcParams["hatch.linewidth"] = 1


def plot_legibility_scores_boxplot(evaluation: dict, output_dir: Path) -> None:
    results = evaluation["results"]
    scores = [r["legibility"]["score"] for r in results if "legibility" in r and isinstance(r["legibility"].get("score"), (int, float))]

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
            ax.text(bar.get_x() + bar.get_width() / 2, pct + 2, f"{pct:.1f}%", ha="center", fontsize=10)

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

    data = [categories["correct"], categories["partially_correct"], categories["incorrect"]]
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

    lengths = []
    scores = []

    for r in results:
        if "legibility" in r and "answer" in r:
            score = r["legibility"].get("score")
            text = r.get("answer", "")
            if isinstance(score, (int, float)) and text:
                lengths.append(len(text))
                scores.append(score)

    if not lengths:
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(lengths, scores, alpha=0.5, color="#3498db")

    ax.set_xlabel("Text Length (characters)", fontsize=12)
    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title("Text Length vs Illegibility", fontsize=14)
    ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "length_vs_legibility.png", dpi=150)
    plt.close()


def plot_model_comparison(evaluations: list[tuple[str, dict]], output_dir: Path) -> None:
    model_names = [name for name, _ in evaluations]
    correct_pcts = [ev["statistics"]["correctness"]["correct_pct"] for _, ev in evaluations]
    partial_pcts = [ev["statistics"]["correctness"]["partially_pct"] for _, ev in evaluations]
    incorrect_pcts = [ev["statistics"]["correctness"]["incorrect_pct"] for _, ev in evaluations]

    x = np.arange(len(model_names))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x - width, correct_pcts, width, label="Correct", color="#2ecc71", alpha=0.8)
    ax.bar(x, partial_pcts, width, label="Partially Correct", color="#f39c12", alpha=0.8)
    ax.bar(x + width, incorrect_pcts, width, label="Incorrect", color="#e74c3c", alpha=0.8)

    ax.set_ylabel("Percentage (%)", fontsize=12)
    ax.set_title("Model Comparison - Correctness", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(model_names, rotation=45, ha="right")
    ax.set_ylim(0, 100)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_dir / "model_comparison.png", dpi=150)
    plt.close()


def plot_legibility_comparison(evaluations: list[tuple[str, dict]], output_dir: Path) -> None:
    model_names = [name for name, _ in evaluations]
    means = [ev["statistics"]["legibility"]["mean"] for _, ev in evaluations if "legibility" in ev["statistics"]]
    stds = [ev["statistics"]["legibility"]["std"] for _, ev in evaluations if "legibility" in ev["statistics"]]

    if not means:
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(model_names))
    bars = ax.bar(x, means, color="#3498db", alpha=0.8)
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


PLOT_FUNCTIONS = {
    "legibility_scores_boxplot": plot_legibility_scores_boxplot,
    "correctness_assessment": plot_correctness_assessment,
    "legibility_by_correctness": plot_legibility_by_correctness,
    "length_vs_legibility": plot_length_vs_legibility,
}

COMPARISON_PLOT_FUNCTIONS = {
    "model_comparison": plot_model_comparison,
    "legibility_comparison": plot_legibility_comparison,
}


def run_analysis_stage(config: dict, output_dir: Path, logger) -> None:
    setup_matplotlib()
    plots_dir = ensure_dir(output_dir / "plots")

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
                COMPARISON_PLOT_FUNCTIONS[plot_type](evaluations, plots_dir)

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
                PLOT_FUNCTIONS[plot_name](evaluation, plots_dir)

    logger.info(f"Analysis complete. Plots saved to {plots_dir}")
