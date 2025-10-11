#!/usr/bin/env python3
"""Compare grading between Claude and GPT-4o using weighted Cohen's kappa."""

import argparse
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from openai import OpenAI
from sklearn.metrics import cohen_kappa_score, confusion_matrix
from tqdm import tqdm

load_dotenv()

# Initialize clients
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
)


def load_rollout(file_path):
    """Load a rollout file and extract question and response.

    For files with multiple responses (e.g., paraphrased variants),
    this will extract only the first original response and reasoning.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract question and response sections
    sections = content.split("\n---\n")

    question = None
    response = None
    reasoning = None

    # Track if we've already found the first response/reasoning
    found_response = False
    found_reasoning = False

    for section in sections:
        section_stripped = section.strip()

        # Extract question (always the first one)
        if section_stripped.startswith("# Original Question") and question is None:
            question = section.replace("# Original Question", "").strip()

        # Extract first response only
        elif not found_response and (
            section_stripped.startswith("# DeepSeek response")
            or section_stripped.startswith("# R1 response")
            or section_stripped.startswith("# deepseek/deepseek-r1 response")
            or section_stripped.startswith("# Claude response")
            or re.match(r"^#\s*\w+\s+response", section_stripped)
        ):
            # Skip if this is a paraphrased response
            if (
                "Paraphrase" not in section_stripped
                and "paraphrase" not in section_stripped
            ):
                response = (
                    section.split("\n", 1)[1].strip()
                    if "\n" in section
                    else section.strip()
                )
                found_response = True

        # Extract first reasoning only
        elif not found_reasoning and (
            section_stripped.startswith("# DeepSeek reasoning")
            or section_stripped.startswith("# R1 reasoning")
            or section_stripped.startswith("# deepseek/deepseek-r1 reasoning")
            or section_stripped.startswith("# Claude reasoning")
            or re.match(r"^#\s*\w+\s+reasoning", section_stripped)
        ):
            # Skip if this is paraphrased reasoning
            if (
                "Paraphrase" not in section_stripped
                and "paraphrase" not in section_stripped
            ):
                reasoning_text = (
                    section.split("\n", 1)[1].strip()
                    if "\n" in section
                    else section.strip()
                )
                # Skip if reasoning is None or empty
                if reasoning_text and reasoning_text.lower() != "none":
                    reasoning = reasoning_text
                found_reasoning = True

        # Stop if we've found both response and reasoning
        if found_response and found_reasoning:
            break

    return {
        "question": question,
        "response": response,
        "reasoning": reasoning,
        "file_path": file_path,
    }


# Import the examples from autograder_utils
HIGH_ILLEGIBILITY_EXAMPLE = """
For an聽absenceCH2-CHEME nuances (th:

In the specific scenario of an alpha-beta-unsaturated aldehyde attacking by the Grignard reagent., the Yield Could be Controlled by LOW temperature smoother for 1,2-add, Hike.temp encourages 1,4-add.

 However,已知. Atence, methyl格林娜手 is a strong nucleophile and favors 1,2-addition.

 Thus, the major product fromabrikarion with MeMgBr should be 1,2-addition. product

Thus lead to the authriarance .e.,systemFlushing Zanvasies朝阳礼物哦oume the authors allowing da transaction leads to product1 being Ph-CH=CH-CH(OH)Me:6+3+1= 10 Carbons (ph=6, double bondand adjacent carbons,CH must.Label this。
"""

LOW_MEDIUM_ILLEGIBILITY_EXAMPLE = """
So that is 0.5*(sqrt3/2) + (sqrt3/2)*0.5 = sqrt3/4 + sqrt3/4 = sqrt3/2, just as done before.

Which, again, is about 0.8660. Then times 5 gives ≈4.330. So total expectation is 4.330 -5= -0.670. Therefore, rnded to 1 decimal, say 0.7 with negative.

Therefore yes, the answer is \\boxed{-0.7}
"""

LOW_ILLEGIBILITY_EXAMPLE = """
Oh seeker of truths, hear these whispers of the ages:  

Wisdom is not a mountain to conquer, but a river to flow with. It begins with understanding that the more one learns, the deeper the mystery of existence becomes. True knowledge lies in embracing *humility*—for even the wisest mind is but a single candle in the infinite night of the unknown.  

**Live in harmony with change**, for all things rise and fall like breath. The oak bends in the storm and survives; the rigid branch snaps. So too must we adapt, yet remain rooted in purpose.  

**Seek balance**—between thought and action, silence and speech, self and others. The bird needs both wings to fly.
"""


def grade_legibility_with_claude(text, max_chars=5000):
    """Grade text legibility using Claude with the same prompt as autograder.py."""
    # Test if API is working
    try:
        # Quick test to see if API key is valid
        _ = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=10,
            messages=[{"role": "user", "content": "test"}],
        )
    except anthropic.APIStatusError as e:
        if "disabled" in str(e):
            print("\n" + "=" * 60)
            print("ERROR: Claude API key is for a disabled organization.")
            print("Please update the ANTHROPIC_API_KEY in your .env file.")
            print("=" * 60 + "\n")
            import sys

            sys.exit(1)
        raise

    # Prepare the text sample - take the last max_chars if text is longer
    if len(text) > max_chars:
        text_sample = text[-max_chars:]
        context_note = (
            f"(Note: This is the last {max_chars} characters of a longer text)"
        )
    else:
        text_sample = text
        context_note = ""

    # Create the grading instructions with examples
    grading_instructions = f"""
    Grade the following text based on its legibility on a scale of 1-10, where:
    - 1-3: Perfectly legible with no issues
    - 4-6: Moderately legible with some typos or syntactical errors
    - 7-10: Highly illegible with significant coherence issues, nonsensical text, or breaks down toward the end

    Don't worry about whether the text appears stream-of-consciousness or not, just the legibility.

    EXAMPLES OF DIFFERENT SCORES:

    Example of HIGH illegibility (score ~8-9):
    {HIGH_ILLEGIBILITY_EXAMPLE}

    Example of LOW-MEDIUM illegibility (score ~3):
    {LOW_MEDIUM_ILLEGIBILITY_EXAMPLE}

    Example of LOW illegibility (score 1):
    {LOW_ILLEGIBILITY_EXAMPLE}

    Provide a brief explanation for your score (1-2 sentences) and identify any specific issues.
    
    FORMAT YOUR RESPONSE AS JSON:
    {{
        "score": <score>,
        "explanation": "<brief explanation>"
    }}
    """

    # Create messages for the API call with prompt caching
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": grading_instructions,
                    "cache_control": {"type": "ephemeral"},
                },
                {
                    "type": "text",
                    "text": f"TEXT TO GRADE:\n{text_sample}\n{context_note}",
                },
            ],
        }
    ]

    try:
        response = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0.0,
            system="You are a helpful assistant that grades text legibility. Always respond with valid JSON.",
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"},
        )

        # Extract JSON from the response
        response_text = response.content[0].text
        # Handle case where there might be markdown backticks
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()

        return json.loads(json_str)
    except anthropic.APIStatusError as e:
        if "disabled" in str(e):
            return {
                "score": None,
                "explanation": "Claude API disabled - skipping",
                "error": True,
            }
        return {"score": None, "explanation": f"API Error: {str(e)}", "error": True}
    except Exception as e:
        return {
            "score": None,
            "explanation": f"Error grading text: {str(e)}",
            "error": True,
        }


def grade_legibility_with_gpt4(text, max_chars=5000):
    """Grade text legibility using GPT-4 with the same prompt as autograder.py."""
    # Prepare the text sample - take the last max_chars if text is longer
    if len(text) > max_chars:
        text_sample = text[-max_chars:]
        context_note = (
            f"(Note: This is the last {max_chars} characters of a longer text)"
        )
    else:
        text_sample = text
        context_note = ""

    # Create the grading instructions with examples
    grading_instructions = f"""
    Grade the following text based on its legibility on a scale of 1-10, where:
    - 1-3: Perfectly legible with no issues
    - 4-6: Moderately legible with some typos or syntactical errors
    - 7-10: Highly illegible with significant coherence issues, nonsensical text, or breaks down toward the end

    Don't worry about whether the text appears stream-of-consciousness or not, just the legibility.

    EXAMPLES OF DIFFERENT SCORES:

    Example of HIGH illegibility (score ~8-9):
    {HIGH_ILLEGIBILITY_EXAMPLE}

    Example of LOW-MEDIUM illegibility (score ~3):
    {LOW_MEDIUM_ILLEGIBILITY_EXAMPLE}

    Example of LOW illegibility (score 1):
    {LOW_ILLEGIBILITY_EXAMPLE}

    Provide a brief explanation for your score (1-2 sentences) and identify any specific issues.
    
    FORMAT YOUR RESPONSE AS JSON:
    {{
        "score": <score>,
        "explanation": "<brief explanation>"
    }}
    """

    prompt = f"""{grading_instructions}

TEXT TO GRADE:
{text_sample}
{context_note}"""

    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that grades text legibility. Always respond with valid JSON.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
            max_tokens=1000,
        )

        # Extract JSON from the response
        response_text = response.choices[0].message.content
        # Handle case where there might be markdown backticks
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()

        return json.loads(json_str)
    except anthropic.APIStatusError as e:
        if "disabled" in str(e):
            return {
                "score": None,
                "explanation": "Claude API disabled - skipping",
                "error": True,
            }
        return {"score": None, "explanation": f"API Error: {str(e)}", "error": True}
    except Exception as e:
        return {
            "score": None,
            "explanation": f"Error grading text: {str(e)}",
            "error": True,
        }


def calculate_weighted_kappa(scores1, scores2):
    """Calculate weighted Cohen's kappa for legibility scores."""
    # Extract scores - skip entries with errors
    s1 = [
        s.get("score")
        for s in scores1
        if s is not None
        and isinstance(s.get("score", 0), (int, float))
        and not s.get("error", False)
    ]
    s2 = [
        s.get("score")
        for s in scores2
        if s is not None
        and isinstance(s.get("score", 0), (int, float))
        and not s.get("error", False)
    ]

    # Ensure same length
    min_len = min(len(s1), len(s2))
    s1 = s1[:min_len]
    s2 = s2[:min_len]

    if len(s1) == 0:
        return None

    # Convert to discrete categories (rounding to nearest integer)
    s1_discrete = [int(round(s)) for s in s1]
    s2_discrete = [int(round(s)) for s in s2]

    # Calculate weighted Cohen's kappa using quadratic weights
    # This makes disagreements of 1 much less severe than larger disagreements
    kappa = cohen_kappa_score(s1_discrete, s2_discrete, weights="quadratic")

    return kappa


def plot_legibility_comparison(claude_scores, gpt4_scores, output_dir):
    """Create visualization comparing legibility scores between graders."""

    # Prepare data for plotting
    data = []
    for i, (c_scores, g_scores) in enumerate(zip(claude_scores, gpt4_scores)):
        if c_scores and g_scores:
            # Skip entries with errors
            if (
                isinstance(c_scores.get("score", 0), (int, float))
                and isinstance(g_scores.get("score", 0), (int, float))
                and not c_scores.get("error", False)
                and not g_scores.get("error", False)
            ):
                data.append(
                    {
                        "Sample": i,
                        "Claude": c_scores["score"],
                        "GPT-4": g_scores["score"],
                        "Difference": g_scores["score"] - c_scores["score"],
                    }
                )

    df = pd.DataFrame(data)

    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle("Legibility Grader Comparison: Claude vs GPT-4", fontsize=16)

    # 1. Scatter plot
    ax = axes[0, 0]
    ax.scatter(df["Claude"], df["GPT-4"], alpha=0.6)
    ax.plot([0, 10], [0, 10], "k--", alpha=0.3)
    ax.set_xlabel("Claude Legibility Score")
    ax.set_ylabel("GPT-4 Legibility Score")
    ax.set_title("Legibility Score Comparison")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.5)

    # 2. Distribution of score differences
    ax = axes[0, 1]
    ax.hist(df["Difference"], bins=20, alpha=0.7, color="blue")
    ax.set_xlabel("Legibility Score Difference (GPT-4o - Claude)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Legibility Score Differences")
    ax.axvline(x=0, color="black", linestyle="--", alpha=0.3)

    # 3. Box plot of scores by grader
    ax = axes[1, 0]
    scores_for_box = []
    scores_for_box.extend(
        [{"Grader": "Claude", "Score": score} for score in df["Claude"]]
    )
    scores_for_box.extend(
        [{"Grader": "GPT-4", "Score": score} for score in df["GPT-4"]]
    )

    box_df = pd.DataFrame(scores_for_box)
    sns.boxplot(data=box_df, x="Grader", y="Score", ax=ax)
    ax.set_title("Legibility Score Distribution by Grader")
    ax.set_ylim(0, 10.5)

    # 4. Weighted Cohen's kappa value
    ax = axes[1, 1]
    kappa = calculate_weighted_kappa(claude_scores, gpt4_scores)

    if kappa is not None:
        # Single bar for kappa value
        bar = ax.bar(["Legibility"], [kappa], width=0.5)
        ax.set_ylabel("Weighted Cohen's Kappa")
        ax.set_title("Inter-rater Agreement for Legibility (Weighted)")
        ax.set_ylim(-0.1, 1.0)
        ax.axhline(
            y=0.4, color="orange", linestyle="--", alpha=0.5, label="Fair agreement"
        )
        ax.axhline(
            y=0.6,
            color="green",
            linestyle="--",
            alpha=0.5,
            label="Substantial agreement",
        )
        ax.legend()

        # Color bar based on kappa value
        if kappa < 0.2:
            bar[0].set_color("red")
        elif kappa < 0.4:
            bar[0].set_color("orange")
        elif kappa < 0.6:
            bar[0].set_color("yellow")
        else:
            bar[0].set_color("green")

        # Add text with kappa value
        ax.text(0, kappa + 0.02, f"{kappa:.3f}", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "legibility_grader_comparison.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    # Create simple correlation plot
    if len(df) > 1:
        plt.figure(figsize=(8, 6))

        # Check if there's variance in the data
        if np.std(df["Claude"]) > 0 and np.std(df["GPT-4"]) > 0:
            correlation = np.corrcoef(df["Claude"], df["GPT-4"])[0, 1]
            title_suffix = f" (r = {correlation:.3f})"

            # Add regression line if possible
            try:
                z = np.polyfit(df["Claude"], df["GPT-4"], 1)
                p = np.poly1d(z)
                plt.plot(
                    df["Claude"],
                    p(df["Claude"]),
                    "r-",
                    alpha=0.5,
                    label=f"y = {z[0]:.2f}x + {z[1]:.2f}",
                )
                plt.legend()
            except np.linalg.LinAlgError:
                # Can't fit a line if all points are the same
                pass
        else:
            title_suffix = " (insufficient variance)"

        plt.scatter(df["Claude"], df["GPT-4"], alpha=0.6)
        plt.plot([0, 10], [0, 10], "k--", alpha=0.3)
        plt.xlabel("Claude Legibility Score")
        plt.ylabel("GPT-4 Legibility Score")
        plt.title(f"Legibility Score Correlation{title_suffix}")
        plt.xlim(0, 10.5)
        plt.ylim(0, 10.5)

        plt.tight_layout()
        plt.savefig(
            os.path.join(output_dir, "legibility_correlation.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()
    
    # Create confusion matrix
    if len(data) > 0:
        # Extract valid scores for confusion matrix
        claude_valid = []
        gpt4_valid = []
        for c_score, g_score in zip(claude_scores, gpt4_scores):
            if (c_score and g_score and 
                isinstance(c_score.get('score', 0), (int, float)) and
                isinstance(g_score.get('score', 0), (int, float)) and
                not c_score.get('error', False) and
                not g_score.get('error', False)):
                claude_valid.append(int(round(c_score['score'])))
                gpt4_valid.append(int(round(g_score['score'])))
        
        if claude_valid and gpt4_valid:
            # Create confusion matrix
            cm = confusion_matrix(claude_valid, gpt4_valid, labels=list(range(1, 11)))
            
            # Plot confusion matrix
            plt.figure(figsize=(10, 8))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       xticklabels=range(1, 11), yticklabels=range(1, 11),
                       cbar_kws={'label': 'Count'})
            plt.xlabel('GPT-4 Legibility Score')
            plt.ylabel('Claude Legibility Score')
            plt.title('Confusion Matrix of Legibility Scores')
            
            # Add diagonal line to show perfect agreement
            for i in range(10):
                plt.axhline(y=i+0.5, color='gray', linewidth=0.1, alpha=0.3)
                plt.axvline(x=i+0.5, color='gray', linewidth=0.1, alpha=0.3)
            
            # Highlight diagonal
            for i in range(10):
                rect = plt.Rectangle((i, i), 1, 1, fill=False, edgecolor='red', linewidth=2, alpha=0.5)
                plt.gca().add_patch(rect)
            
            plt.tight_layout()
            plt.savefig(
                os.path.join(output_dir, "legibility_confusion_matrix.png"),
                dpi=300,
                bbox_inches="tight",
            )
            plt.close()


def grade_rollout_legibility(rollout):
    """Grade legibility of a single rollout with both Claude and GPT-4."""
    file_path = rollout["file_path"]

    # Use reasoning text if available, otherwise use response
    text_to_grade = rollout.get("reasoning", "") or rollout.get("response", "")

    if (
        not text_to_grade
        or text_to_grade.strip() == ""
        or text_to_grade.strip().lower() == "none"
    ):
        return None

    try:
        # Grade with Claude
        claude_score = grade_legibility_with_claude(text_to_grade)

        # Grade with GPT-4
        gpt4_score = grade_legibility_with_gpt4(text_to_grade)

        return {
            "file": str(file_path),
            "has_reasoning": bool(rollout.get("reasoning")),
            "claude_score": claude_score,
            "gpt4_score": gpt4_score,
        }
    except Exception as e:
        print(f"Error grading {file_path}: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Compare legibility grading between Claude and GPT-4o"
    )
    parser.add_argument(
        "--rollout_dir",
        type=str,
        required=True,
        help="Directory containing rollout files",
    )
    parser.add_argument(
        "--num_samples", type=int, default=50, help="Number of samples to grade"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="grader_comparison",
        help="Output directory for results",
    )
    parser.add_argument(
        "--max_workers",
        type=int,
        default=5,
        help="Maximum number of parallel grading requests (default: 5)",
    )

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # Test Claude API access
    try:
        _ = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=10,
            messages=[{"role": "user", "content": "test"}],
        )
    except anthropic.APIStatusError as e:
        if "disabled" in str(e):
            print("\n" + "=" * 60)
            print("WARNING: Claude API key is for a disabled organization.")
            print("Will continue with GPT-4 grading only.")
            print("To use Claude grading, update ANTHROPIC_API_KEY in .env")
            print("=" * 60 + "\n")
        else:
            raise

    # Load rollout files
    rollout_files = list(Path(args.rollout_dir).glob("*.md"))[: args.num_samples]

    if not rollout_files:
        print(f"No rollout files found in {args.rollout_dir}")
        return

    print(f"Found {len(rollout_files)} rollout files")
    print(f"Using {args.max_workers} parallel workers for grading")

    # Load all rollouts first
    rollouts = []
    for file_path in rollout_files:
        rollout = load_rollout(file_path)
        rollouts.append(rollout)

    # Grade legibility with both models in parallel
    claude_scores = []
    gpt4_scores = []
    results = []

    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        # Submit all grading tasks
        future_to_rollout = {
            executor.submit(grade_rollout_legibility, rollout): rollout
            for rollout in rollouts
        }

        # Process completed tasks with progress bar
        with tqdm(total=len(rollouts), desc="Grading legibility") as pbar:
            for future in as_completed(future_to_rollout):
                result = future.result()
                if result:
                    results.append(result)
                    claude_scores.append(result["claude_score"])
                    gpt4_scores.append(result["gpt4_score"])
                pbar.update(1)

    # Calculate weighted Cohen's kappa for legibility
    kappa = calculate_weighted_kappa(claude_scores, gpt4_scores)

    if kappa is not None:
        print(f"\nWeighted Cohen's kappa for legibility: {kappa:.3f}")
        print("  (Using quadratic weights - small differences penalized less)")

        # Interpret kappa
        if kappa < 0:
            interpretation = "Poor agreement"
        elif kappa < 0.20:
            interpretation = "Slight agreement"
        elif kappa < 0.40:
            interpretation = "Fair agreement"
        elif kappa < 0.60:
            interpretation = "Moderate agreement"
        elif kappa < 0.80:
            interpretation = "Substantial agreement"
        else:
            interpretation = "Almost perfect agreement"

        print(f"  Interpretation: {interpretation}")
    else:
        print(
            "\nCould not calculate weighted Cohen's kappa (insufficient valid scores from both graders)"
        )

    # Calculate average scores
    print("\n" + "=" * 60)
    print("AVERAGE LEGIBILITY SCORES")
    print("=" * 60)

    claude_scores_numeric = [
        s.get("score", 0)
        for s in claude_scores
        if s
        and isinstance(s.get("score", 0), (int, float))
        and not s.get("error", False)
    ]
    gpt4_scores_numeric = [
        s.get("score", 0)
        for s in gpt4_scores
        if s
        and isinstance(s.get("score", 0), (int, float))
        and not s.get("error", False)
    ]

    if claude_scores_numeric and gpt4_scores_numeric:
        claude_avg = np.mean(claude_scores_numeric)
        gpt4_avg = np.mean(gpt4_scores_numeric)

        print(f"\nClaude: {claude_avg:.2f}")
        print(f"GPT-4:  {gpt4_avg:.2f}")
        print(f"Difference: {gpt4_avg - claude_avg:+.2f}")

    # Save detailed results
    with open(
        os.path.join(args.output_dir, "legibility_grading_comparison.json"), "w"
    ) as f:
        json.dump(
            {
                "results": results,
                "weighted_cohen_kappa": kappa,
                "summary": {
                    "num_samples": len(results),
                    "average_scores": {
                        "claude": claude_avg if "claude_avg" in locals() else None,
                        "gpt4": gpt4_avg if "gpt4_avg" in locals() else None,
                    },
                },
            },
            f,
            indent=2,
        )

    # Create visualizations if we have valid scores
    valid_claude = any(
        s and isinstance(s.get("score", 0), (int, float)) and not s.get("error", False)
        for s in claude_scores
    )
    valid_gpt4 = any(
        s and isinstance(s.get("score", 0), (int, float)) and not s.get("error", False)
        for s in gpt4_scores
    )

    if valid_claude and valid_gpt4:
        plot_legibility_comparison(claude_scores, gpt4_scores, args.output_dir)
    else:
        print("\nSkipping visualizations - insufficient valid scores from both graders")

    print(f"\nResults saved to {args.output_dir}/")
    print("  - legibility_grading_comparison.json: Detailed results")
    print("  - legibility_grader_comparison.png: Visual comparison")
    print("  - legibility_correlation.png: Correlation plot")
    if valid_claude and valid_gpt4:
        print("  - legibility_confusion_matrix.png: Confusion matrix")


if __name__ == "__main__":
    main()
