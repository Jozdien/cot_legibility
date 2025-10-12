import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

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


def plot_correctness_vs_legibility(scores_path, output_path, model="deepseek", metric="reasoning", use_normalized=False):
    setup_matplotlib()

    data = read_json(scores_path)

    correctness_scores, legibility_scores = [], []

    for item in data:
        if "legibility" not in item or "correctness" not in item:
            continue

        metric_data = item["legibility"].get(f"{model}_{metric}", {})
        score = metric_data.get("normalized_score" if use_normalized else "score")
        correctness = item["correctness"].get(model, {}).get("correctness")

        if not isinstance(score, (int, float)) or not correctness:
            continue

        correctness_scores.append(score_correctness(correctness))
        legibility_scores.append(score)

    correctness_scores = np.array(correctness_scores)
    legibility_scores = np.array(legibility_scores)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.boxplot(
        [legibility_scores[correctness_scores == x] for x in [0, 0.5, 1]],
        positions=[0, 0.5, 1],
        widths=0.1
    )

    for x_val in [0, 0.5, 1]:
        mask = correctness_scores == x_val
        if not mask.any():
            continue

        y = legibility_scores[mask]
        x_jitter = np.random.normal(0, 0.02, size=len(y)) + x_val

        xy = np.vstack([x_jitter, y])
        density = stats.gaussian_kde(xy)(xy)
        density_scaled = (density - density.min()) / (density.max() - density.min())

        ax.scatter(x_jitter, y, c=plt.cm.viridis(density_scaled), alpha=0.6, s=30)

    ax.set_xticks([0, 0.5, 1])
    ax.set_xticklabels(["Incorrect", "Partial", "Correct"])
    ax.set_ylabel(f"{'Normalized ' if use_normalized else ''}Illegibility Score", fontsize=12)
    ax.set_title(f"Correctness vs {'Normalized ' if use_normalized else ''}Illegibility ({model}_{metric})", fontsize=14)
    ax.set_ylim(0, 10)
    ax.grid(True, linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python plot_density_scatter.py <scores_file> <output_file> [model] [metric] [use_normalized]")
        sys.exit(1)

    scores_path = sys.argv[1]
    output_path = sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "deepseek"
    metric = sys.argv[4] if len(sys.argv) > 4 else "reasoning"
    use_normalized = sys.argv[5].lower() == "true" if len(sys.argv) > 5 else False

    plot_correctness_vs_legibility(scores_path, output_path, model, metric, use_normalized)
