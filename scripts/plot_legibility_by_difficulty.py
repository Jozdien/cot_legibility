import json
from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

MODELS = {
    "R1": "20251014_190506_R1_gpqa",
    "R1-Zero": "20251024_054931_R1-Zero_gpqa",
    "V3": "20251024_055247_v3_gpqa",
    "Claude\nSonnet 4": "20251021_213023_claude-sonnet-4_gpqa",
    "Claude\nOpus 4": "20251021_215130_claude-opus-4_gpqa",
    "QwQ": "20251021_000418_qwq_gpqa",
    "Qwen3-235B": "20251020_152434_Qwen3 235B_gpqa",
    "R1-Distill-\nQwen-32B": "20251022_003910_R1-Distill-Qwen-32B_gpqa",
    "R1-Distill-\nQwen-14B": "20251022_013133_R1-Distill-Qwen-14B_gpqa",
}

RUNS_DIR = Path("runs")
BASELINE_FILE = Path("runs/20251021_213023_claude-sonnet-4_gpqa/evaluation.json")

font_path = Path("fonts/Montserrat-SemiBold.ttf")
if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    plt.rcParams["font.family"] = "Montserrat"


def load_baseline_map(baseline_path):
    with open(baseline_path) as f:
        baseline_data = json.load(f)
    baseline_results = baseline_data.get("results", [])
    return {
        item["question_id"]: item.get("correctness", {}).get("correctness")
        for item in baseline_results
    }


def load_categorized_scores(run_name, baseline_map):
    eval_file = RUNS_DIR / run_name / "evaluation.json"
    with open(eval_file) as f:
        data = json.load(f)

    categorized = {"correct": [], "partially_correct": [], "incorrect": []}

    for r in data.get("results", []):
        q_id = r.get("question_id")
        if q_id not in baseline_map:
            continue

        category = baseline_map[q_id]
        if category not in categorized:
            continue

        score = r.get("legibility", {}).get("score")
        if isinstance(score, (int, float)):
            categorized[category].append(score)

    return categorized


plt.rcParams.update(
    {
        "font.size": 14,
        "axes.labelsize": 16,
        "axes.titlesize": 16,
        "xtick.labelsize": 13,
        "ytick.labelsize": 14,
    }
)

baseline_map = load_baseline_map(BASELINE_FILE)

fig, ax = plt.subplots(figsize=(14, 6))

positions = []
all_data = []
hatches = []
pos = 0

model_positions = []
for model_name, run_name in MODELS.items():
    categorized = load_categorized_scores(run_name, baseline_map)

    model_start_pos = pos
    for category, hatch in [
        ("correct", ""),
        ("partially_correct", "///"),
        ("incorrect", "xxx"),
    ]:
        if categorized[category]:
            all_data.append(categorized[category])
            positions.append(pos)
            hatches.append(hatch)
            pos += 0.85

    model_center = (model_start_pos + pos - 0.9) / 2
    model_positions.append(model_center)
    pos += 0.7

bp = ax.boxplot(
    all_data,
    positions=positions,
    widths=0.75,
    patch_artist=True,
    showfliers=True,
    medianprops={"linewidth": 0},
    flierprops=dict(
        marker="o",
        markerfacecolor="white",
        markersize=5,
        markeredgecolor="black",
        markeredgewidth=1,
    ),
    whiskerprops=dict(color="black", linewidth=1),
    capprops=dict(color="black", linewidth=1.5),
)

for patch, hatch in zip(bp["boxes"], hatches):
    patch.set_facecolor("#d65e00")
    patch.set_edgecolor("black")
    patch.set_linewidth(1)
    patch.set_hatch(hatch)

ax.set_xticks(model_positions)
ax.set_xticklabels(list(MODELS.keys()))
ax.set_xlim(-1, len(model_positions) * 3 + 1.5)
ax.set_ylabel("Illegibility Score", fontsize=18)
ax.set_ylim(0, 10)
ax.grid(axis="y", alpha=0.3, linestyle="--")
ax.set_axisbelow(True)

legend_elements = [
    mpatches.Patch(
        facecolor="#d65e00", edgecolor="black", label="Easy", linewidth=1, hatch=""
    ),
    mpatches.Patch(
        facecolor="#d65e00",
        edgecolor="black",
        label="Medium",
        linewidth=1,
        hatch="///",
    ),
    mpatches.Patch(
        facecolor="#d65e00", edgecolor="black", label="Hard", linewidth=1, hatch="xxx"
    ),
]
ax.legend(handles=legend_elements, fontsize=12, loc="upper right")

plt.tight_layout()
plt.savefig("legibility_by_difficulty.pdf", dpi=300, bbox_inches="tight")
print("Saved legibility_by_difficulty.pdf")
