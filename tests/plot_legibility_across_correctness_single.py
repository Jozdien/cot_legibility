import json
import os

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def setup_matplotlib():
    fm.fontManager.addfont("../fonts/Montserrat-Regular.ttf")
    plt.rcParams["font.family"] = "Montserrat"
    plt.rcParams["hatch.linewidth"] = 1


def score_correctness(correctness):
    return {"correct": 1, "partially_correct": 0.5, "incorrect": 0}.get(correctness, 0)


def get_reasoning_length(filename):
    try:
        with open(os.path.join("../r1_rollouts/q_repeat_temp_1.0", filename), "r") as f:
            content = f.read()
            # Find the start of reasoning section
            reasoning_start = content.find("DeepSeek reasoning (via openrouter)")
            if reasoning_start == -1:
                return None
            reasoning = content[reasoning_start:].strip()
            return len(reasoning) / 10000
    except Exception as e:
        print(f"Error in get_reasoning_length: {e}")
        return None


def analyze_distributions(correctness_scores, legibility_scores):
    # Convert to numpy arrays and group
    correct = np.array(legibility_scores)[np.array(correctness_scores) == 1]
    incorrect = np.array(legibility_scores)[np.array(correctness_scores) == 0]

    # Mann-Whitney U test (non-parametric)
    u_stat, p_value = stats.mannwhitneyu(correct, incorrect, alternative="two-sided")

    # Cohen's d effect size
    cohens_d = (np.mean(correct) - np.mean(incorrect)) / np.sqrt(
        (
            (len(correct) - 1) * np.var(correct)
            + (len(incorrect) - 1) * np.var(incorrect)
        )
        / (len(correct) + len(incorrect) - 2)
    )

    print(f"Mann-Whitney U p-value: {p_value:.4f}")
    print(f"Cohen's d: {cohens_d:.4f}")


def process_data(data):
    correctness_scores = []
    normalized_legibility_scores = []

    for item in data:
        if not item["correctness"] or not item["legibility"]:
            continue
        if not item["file"].startswith("q140_"):
            continue

        # Get reasoning length
        reasoning_length = get_reasoning_length(item["file"])
        if not reasoning_length:
            continue

        correctness = score_correctness(item["correctness"]["deepseek"]["correctness"])
        legibility = item["legibility"]["deepseek_reasoning"]["score"]

        # Normalize legibility score by reasoning length
        # normalized_legibility = (legibility / reasoning_length) * 4
        # if normalized_legibility > 10:
        #     continue
        normalized_legibility = legibility

        correctness_scores.append(correctness)
        normalized_legibility_scores.append(normalized_legibility)

    return correctness_scores, normalized_legibility_scores


def create_plot(correctness_scores, legibility_scores):
    plt.figure(figsize=(10, 6))

    # Convert to numpy for easier grouping
    correctness = np.array(correctness_scores)
    legibility = np.array(legibility_scores)

    # Box plot
    plt.boxplot(
        [legibility[correctness == x] for x in [0, 0.5, 1]],
        positions=[0, 0.5, 1],
        widths=0.1,
    )

    # Scatter plot with jitter
    for x in [0, 0.5, 1]:
        if not any(correctness == x):
            continue
        y = legibility[correctness == x]
        x_jitter = np.random.normal(0, 0.02, size=len(y)) + x
        xy = np.vstack([x_jitter, y])
        z = stats.gaussian_kde(xy)(xy)
        idx = z.argsort()
        x_jitter, y, z = x_jitter[idx], y[idx], z[idx]
        plt.scatter(x_jitter, y, c=z, cmap="viridis", alpha=0.5)

    analyze_distributions(correctness_scores, legibility_scores)

    # plt.xlabel('Correctness (0=incorrect, 0.5=partial, 1=correct)')
    plt.xticks([0, 1], ["Incorrect", "Correct"])
    plt.ylabel("Normalized Illegibility Score (higher means less legible)")
    # plt.legend()
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.ylim(0, 9.5)
    plt.colorbar(label="Point density")
    plt.tight_layout()
    return plt


def main():
    setup_matplotlib()
    with open("../scores/q_repeat_temp_1.0_scores.json", "r") as f:
        data = json.load(f)

    correctness_scores, normalized_legibility_scores = process_data(data)
    plt = create_plot(correctness_scores, normalized_legibility_scores)
    plt.savefig("q_repeat_temp_1.0_correctness_vs_normalized_legibility_temp.png")


if __name__ == "__main__":
    main()
