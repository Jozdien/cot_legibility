import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from src.utils.io import read_json


def setup_matplotlib(font_path="fonts/Montserrat-Regular.ttf"):
    if Path(font_path).exists():
        fm.fontManager.addfont(font_path)
        plt.rcParams["font.family"] = "Montserrat"
    plt.rcParams["hatch.linewidth"] = 1


def categorize_by_baseline(scores_path, baseline_path, model="deepseek"):
    data = read_json(scores_path)
    baseline = read_json(baseline_path)

    baseline_map = {
        item["question"]: item["correctness"][model]["correctness"]
        for item in baseline
        if "correctness" in item and model in item["correctness"]
    }

    categorized = {"correct": [], "partially_correct": [], "incorrect": []}

    for item in data:
        question = item.get("question")
        if question not in baseline_map:
            continue

        category = baseline_map[question]
        if category in categorized:
            categorized[category].append(item)

    return categorized


def plot_legibility_by_baseline(scores_paths, baseline_path, output_path, model="deepseek", metric="reasoning"):
    setup_matplotlib()

    fig, ax = plt.subplots(figsize=(12, 6))

    labels = []
    all_data = []

    for scores_path in scores_paths:
        categorized = categorize_by_baseline(scores_path, baseline_path, model)
        label = Path(scores_path).stem

        data = []
        for category in ["correct", "partially_correct", "incorrect"]:
            scores = [
                item["legibility"][f"{model}_{metric}"]["score"]
                for item in categorized[category]
                if "legibility" in item
                and f"{model}_{metric}" in item["legibility"]
                and isinstance(item["legibility"][f"{model}_{metric}"].get("score"), (int, float))
            ]
            data.append(scores)

        labels.append(label)
        all_data.append(data)

    x = np.arange(len(scores_paths)) * 1.5
    width = 0.4

    colors = {"correct": "#2ecc71", "partially_correct": "#f39c12", "incorrect": "#e74c3c"}
    hatches = {"correct": "", "partially_correct": "///", "incorrect": "xxx"}

    for i, category in enumerate(["correct", "partially_correct", "incorrect"]):
        data_for_category = [all_data[j][i] for j in range(len(scores_paths))]
        positions = x + (i - 1) * width

        bp = ax.boxplot(data_for_category, positions=positions, widths=width * 0.8, patch_artist=True)

        for box in bp["boxes"]:
            box.set(facecolor=colors[category], alpha=0.8, hatch=hatches[category])

    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title(f"Illegibility by Baseline Correctness ({model}_{metric})", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 10)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=colors["correct"], hatch=hatches["correct"], label="Easy (Baseline Correct)"),
        Patch(facecolor=colors["partially_correct"], hatch=hatches["partially_correct"], label="Medium (Baseline Partial)"),
        Patch(facecolor=colors["incorrect"], hatch=hatches["incorrect"], label="Hard (Baseline Incorrect)")
    ]
    ax.legend(handles=legend_elements)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python plot_with_baseline.py <baseline_file> <output_file> <scores_file1> [scores_file2 ...]")
        sys.exit(1)

    baseline_path = sys.argv[1]
    output_path = sys.argv[2]
    scores_paths = sys.argv[3:]

    plot_legibility_by_baseline(scores_paths, baseline_path, output_path)
