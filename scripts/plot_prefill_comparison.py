import json
from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

RUN_NAME = "20251019_202534_qwq_gpqa"

FONT_FAMILY = "Montserrat-SemiBold.ttf"
TITLE_FONTSIZE = 14
LABEL_FONTSIZE = 14
TICK_FONTSIZE = 14
TEXT_FONTSIZE = 9
FIGSIZE = (10, 6)
DPI = 300

font_path = Path(f"fonts/{FONT_FAMILY}")
if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    plt.rcParams["font.family"] = "Montserrat"

eval_file = Path(f"runs/{RUN_NAME}/prefill_evaluation.json")

with open(eval_file) as f:
    data = json.load(f)

stats = data["statistics"]
prefill_stats = stats.get("prefill_correctness")
original_stats = stats.get("original_correctness")

if not prefill_stats or not original_stats:
    print("No prefill or original correctness stats found")
    exit(1)

categories = ["Correct", "Partially Correct", "Incorrect"]
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

fig, ax = plt.subplots(figsize=FIGSIZE)
bars1 = ax.bar(
    x - width / 2, original_pcts, width, label="Original", alpha=0.8, color=colors
)
bars2 = ax.bar(
    x + width / 2,
    prefill_pcts,
    width,
    label="Prefilled",
    alpha=0.8,
    color=colors,
    hatch="///",
)

for bars, pcts in [(bars1, original_pcts), (bars2, prefill_pcts)]:
    for bar, pct in zip(bars, pcts):
        if pct > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                pct + 2,
                f"{pct:.1f}%",
                ha="center",
                fontsize=TEXT_FONTSIZE,
            )

ax.set_ylabel("Percentage (%)", fontsize=LABEL_FONTSIZE)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=TICK_FONTSIZE)
ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)
ax.set_ylim(0, 110)
ax.legend(fontsize=LABEL_FONTSIZE)
ax.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.savefig("prefill_correctness_comparison.pdf", dpi=DPI, bbox_inches="tight")
plt.savefig("prefill_correctness_comparison.png", dpi=150)
print("Saved prefill_correctness_comparison.pdf and .png")
