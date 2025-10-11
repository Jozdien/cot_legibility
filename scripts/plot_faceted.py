import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy import stats

from src.utils.io import read_json


def setup_matplotlib(font_path="fonts/Montserrat-Regular.ttf"):
    if Path(font_path).exists():
        fm.fontManager.addfont(font_path)
        plt.rcParams["font.family"] = "Montserrat"


def score_correctness(correctness):
    return {"correct": 1, "partially_correct": 0.5, "incorrect": 0}.get(correctness, np.nan)


def extract_question_index(filename):
    match = re.match(r"q(\d+)_", filename)
    return int(match.group(1)) if match else None


def plot_faceted_by_question(scores_path, output_path, model="deepseek", metric="reasoning"):
    setup_matplotlib()

    data = read_json(scores_path)

    by_question = {}

    for item in data:
        if "legibility" not in item or "correctness" not in item or "file" not in item:
            continue

        q_idx = extract_question_index(item["file"])
        if q_idx is None:
            continue

        score = item["legibility"].get(f"{model}_{metric}", {}).get("score")
        correctness = item["correctness"].get(model, {}).get("correctness")

        if not isinstance(score, (int, float)) or not correctness:
            continue

        if q_idx not in by_question:
            by_question[q_idx] = {"correctness": [], "legibility": []}

        by_question[q_idx]["correctness"].append(score_correctness(correctness))
        by_question[q_idx]["legibility"].append(score)

    n_questions = len(by_question)
    n_cols = min(3, n_questions)
    n_rows = (n_questions + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
    axes = np.array([axes]).flatten() if n_questions == 1 else axes.flatten()

    for idx, (q_idx, q_data) in enumerate(sorted(by_question.items())):
        ax = axes[idx]

        correctness = np.array(q_data["correctness"])
        legibility = np.array(q_data["legibility"])

        ax.boxplot(
            [legibility[correctness == x] for x in [0, 0.5, 1]],
            positions=[0, 0.5, 1],
            widths=0.1
        )

        for x_val in [0, 0.5, 1]:
            mask = correctness == x_val
            if not mask.any():
                continue

            y = legibility[mask]
            if len(y) > 1:
                x_jitter = np.random.normal(0, 0.02, size=len(y)) + x_val
                xy = np.vstack([x_jitter, y])
                density = stats.gaussian_kde(xy)(xy)
                density_scaled = (density - density.min()) / (density.max() - density.min())
                ax.scatter(x_jitter, y, c=plt.cm.viridis(density_scaled), alpha=0.5, s=20)

        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(["Incorrect", "Partial", "Correct"])
        ax.set_title(f"Question {q_idx}")
        ax.set_ylim(0, 10)
        ax.grid(True, linestyle="--", alpha=0.3)

    for idx in range(n_questions, len(axes)):
        axes[idx].set_visible(False)

    fig.supylabel("Illegibility Score")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python plot_faceted.py <scores_file> <output_file> [model] [metric]")
        sys.exit(1)

    scores_path = sys.argv[1]
    output_path = sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "deepseek"
    metric = sys.argv[4] if len(sys.argv) > 4 else "reasoning"

    plot_faceted_by_question(scores_path, output_path, model, metric)
