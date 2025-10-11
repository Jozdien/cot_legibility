#!/usr/bin/env python3
"""Visualize token entropy from R1 with proper provider configuration."""

import argparse
import json
import math
import os
import time
from datetime import datetime
from time import perf_counter

from datasets import load_from_disk
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def calculate_entropy(top_logprobs):
    """Calculate entropy from top logprobs."""
    if not top_logprobs:
        return 0.0

    # Convert log probabilities to probabilities
    probs = [math.exp(lp["logprob"]) for lp in top_logprobs]

    # Normalize (should already sum to ~1, but just in case)
    total = sum(probs)
    if total == 0:
        return 0.0
    probs = [p / total for p in probs]

    # Calculate entropy: -sum(p * log(p))
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return entropy


def get_color_for_entropy(entropy, max_entropy):
    """Get ANSI color code based on entropy level."""
    if max_entropy == 0:
        return "\033[90m"  # gray

    # Normalize entropy to 0-1 range
    normalized = min(entropy / max_entropy, 1.0)

    # Color scale: blue (low) -> green -> yellow -> red (high)
    if normalized < 0.25:
        return "\033[94m"  # blue
    elif normalized < 0.5:
        return "\033[92m"  # green
    elif normalized < 0.75:
        return "\033[93m"  # yellow
    else:
        return "\033[91m"  # red


def visualize_r1_entropy(
    question, temperature=1.0, provider="Nebius", show_mode="both"
):
    """Process question with R1 using proper provider to get logprobs."""

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
    )

    print(f"\n\033[1m📝 Question:\033[0m {question}")
    print("\033[1m🤖 Model:\033[0m deepseek/deepseek-r1")
    print(f"\033[1m🌡️  Temperature:\033[0m {temperature}")
    print(f"\033[1m📡 Provider:\033[0m {provider}")
    print("\n" + "─" * 80 + "\n")

    print("🔄 Calling R1 API with logprobs enabled...")
    start_time = perf_counter()

    # Try up to 3 times with different approaches
    attempt = 0
    completion = None
    last_error = None

    while attempt < 1 and completion is None:
        try:
            if attempt == 0:
                # First attempt: with specified provider
                print(f"   → Attempt {attempt + 1}: Using {provider} provider...")
                extra_body = {
                    "include_reasoning": True,
                    "provider": {"order": [provider], "allow_fallbacks": False},
                }
            elif attempt == 1:
                # Second attempt: allow fallbacks
                print(f"   → Attempt {attempt + 1}: Allowing provider fallbacks...")
                extra_body = {
                    "include_reasoning": True,
                    "provider": {"order": [provider], "allow_fallbacks": True},
                }
            else:
                # Third attempt: no provider specification
                print(f"   → Attempt {attempt + 1}: Auto-selecting provider...")
                extra_body = {"include_reasoning": True}

            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1",
                messages=[{"role": "user", "content": question}],
                temperature=temperature,
                logprobs=True,
                top_logprobs=20,
                extra_body=extra_body,
            )

            elapsed = perf_counter() - start_time
            print(f"✅ Response received in {elapsed:.2f}s\n")

        except json.JSONDecodeError as e:
            last_error = f"JSON decode error: {e}"
            print("   ⚠️  JSON decode error, likely rate limit or timeout")
            attempt += 1
            if attempt < 3:
                print("   ⏳ Waiting 2 seconds before retry...")
                time.sleep(2)
        except Exception as e:
            last_error = str(e)
            print(f"   ⚠️  Error: {str(e)}")
            attempt += 1
            if attempt < 3:
                print("   ⏳ Waiting 2 seconds before retry...")
                time.sleep(2)

    if completion is None:
        print(f"\n❌ Failed after 3 attempts. Last error: {last_error}")
        return

    try:
        # Check for logprobs
        if (
            not hasattr(completion.choices[0], "logprobs")
            or not completion.choices[0].logprobs
        ):
            print(f"⚠️  No logprobs returned with provider '{provider}'")
            print("Try using --provider Together or --provider Nebius")
            return

        logprobs_data = completion.choices[0].logprobs

        if not logprobs_data.content:
            print("❌ No logprobs content available")
            return

        print(f"✅ Got logprobs for {len(logprobs_data.content)} tokens!\n")

        # Process tokens with entropy
        tokens_with_entropy = []
        max_entropy = 0

        for token_data in logprobs_data.content:
            # Convert to dict format for consistency
            top_logprobs = []
            if token_data.top_logprobs:
                for lp in token_data.top_logprobs:
                    top_logprobs.append({"token": lp.token, "logprob": lp.logprob})

            entropy = calculate_entropy(top_logprobs)
            max_entropy = max(max_entropy, entropy)

            tokens_with_entropy.append(
                {
                    "token": token_data.token,
                    "logprob": token_data.logprob,
                    "entropy": entropy,
                    "top_logprobs": top_logprobs[:5],  # Keep top 5 for display
                }
            )

        # Display response with entropy visualization
        print("\033[1m📊 Token Entropy Visualization:\033[0m")
        print("(Higher entropy = more uncertainty in the model's prediction)\n")

        # Legend
        print(
            "Entropy scale: \033[94m█ Low\033[0m \033[92m█ Medium-Low\033[0m \033[93m█ Medium-High\033[0m \033[91m█ High\033[0m\n"
        )

        # Display tokens with entropy - clean up tokenizer artifacts
        current_line = ""
        in_reasoning = True
        reasoning_ended = False

        for i, item in enumerate(tokens_with_entropy):
            token = item["token"]
            entropy = item["entropy"]
            color = get_color_for_entropy(entropy, max_entropy)

            # Clean up tokenizer artifacts
            display_token = token.replace("Ġ", " ").replace("Ċ", "\n")

            # Check for end of reasoning
            if "</think>" in display_token:
                in_reasoning = False
                if show_mode in ["both", "reasoning"]:
                    print(current_line)
                    print("\n" + "─" * 40 + " END OF REASONING " + "─" * 22 + "\n")
                current_line = ""
                continue

            # Skip special end token
            if "<｜end▁of▁sentence｜>" in display_token:
                continue

            # Skip tokens based on show mode
            if show_mode == "reasoning" and not in_reasoning:
                continue
            elif show_mode == "answer" and in_reasoning:
                continue

            # Check if we need a new line
            if "\n" in display_token:
                # Split by newlines and handle each part
                parts = display_token.split("\n")
                for j, part in enumerate(parts):
                    if part:  # Only add non-empty parts
                        current_line += f"{color}{part}\033[0m"
                    if j < len(parts) - 1:  # Add newline except for last part
                        print(current_line)
                        current_line = ""
            else:
                # Add token to current line
                current_line += f"{color}{display_token}\033[0m"

                # Word wrap at reasonable length
                # Remove ANSI codes for length calculation
                clean_line = current_line
                for code in [
                    "\033[94m",
                    "\033[92m",
                    "\033[93m",
                    "\033[91m",
                    "\033[90m",
                    "\033[0m",
                ]:
                    clean_line = clean_line.replace(code, "")

                if len(clean_line) > 80:
                    print(current_line)
                    current_line = ""

        if current_line:
            print(current_line)

        print("\n" + "─" * 80 + "\n")

        # Detailed entropy analysis
        print("\033[1m📈 Entropy Statistics:\033[0m")
        entropies = [item["entropy"] for item in tokens_with_entropy]
        avg_entropy = sum(entropies) / len(entropies) if entropies else 0

        print(f"• Average entropy: {avg_entropy:.4f}")
        print(f"• Max entropy: {max_entropy:.4f}")
        print(f"• Min entropy: {min(entropies):.4f}")

        # Show highest entropy tokens
        print("\n\033[1m🔥 Top 10 Highest Entropy Tokens:\033[0m")
        sorted_tokens = sorted(
            tokens_with_entropy, key=lambda x: x["entropy"], reverse=True
        )[:10]

        for i, item in enumerate(sorted_tokens, 1):
            # Clean up token display
            clean_token = item["token"].replace("Ġ", " ").replace("Ċ", "\\n")
            print(f'\n{i:2d}. Entropy: {item["entropy"]:.4f} │ Token: "{clean_token}"')

            # Show top alternatives
            if item["top_logprobs"]:
                print("    └─ Top alternatives: ", end="")
                alts = []
                for alt in item["top_logprobs"][:3]:
                    clean_alt = alt["token"].replace("Ġ", " ").replace("Ċ", "\\n")
                    alts.append(
                        f'"{clean_alt}" ({math.exp(alt["logprob"]) * 100:.1f}%)'
                    )
                print(", ".join(alts))

        # Save detailed results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logprobs_file = f"r1_entropy_{timestamp}.jsonl"

        with open(logprobs_file, "w") as f:
            for item in tokens_with_entropy:
                # Save in same format as original R1 rollouts
                json.dump(
                    {
                        "token": item["token"],
                        "logprob": item["logprob"],
                        "entropy": item["entropy"],
                        "top_logprobs": item["top_logprobs"],
                    },
                    f,
                )
                f.write("\n")

        print(f"\n💾 Detailed logprobs saved to: {logprobs_file}")

        # Show reasoning if available
        if (
            hasattr(completion.choices[0].message, "reasoning")
            and completion.choices[0].message.reasoning
        ):
            print("\n\033[1m💭 Reasoning Preview:\033[0m")
            reasoning = completion.choices[0].message.reasoning
            print(reasoning[:500] + "..." if len(reasoning) > 500 else reasoning)

        # Show final answer
        print("\n\033[1m📄 Final Answer:\033[0m")
        answer = completion.choices[0].message.content
        print(answer[:500] + "..." if len(answer) > 500 else answer)

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback

        traceback.print_exc()


def main():
    parser = argparse.ArgumentParser(
        description="Visualize R1 token entropy with proper provider"
    )
    parser.add_argument("--question", "-q", type=str, help="Question to ask")
    parser.add_argument(
        "--gpqa", action="store_true", help="Use a random GPQA question"
    )
    parser.add_argument("--temperature", "-t", type=float, default=1.0)
    parser.add_argument(
        "--provider",
        "-p",
        type=str,
        default="Nebius",
        choices=["Together", "Nebius"],
        help="Provider to use for R1 (default: Nebius)",
    )
    parser.add_argument(
        "--show",
        "-s",
        type=str,
        default="both",
        choices=["both", "reasoning", "answer"],
        help="What to display: both, reasoning only, or answer only (default: both)",
    )

    args = parser.parse_args()

    # Determine question
    if args.question:
        question = args.question
    elif args.gpqa:
        # Load a GPQA question
        gpqa_dataset = load_from_disk("data/gpqa_diamond")
        import random

        idx = random.randint(0, min(10, len(gpqa_dataset) - 1))
        question = gpqa_dataset[idx]["Question"]
        print(f"Using GPQA question #{idx}")
    else:
        # Default simple question
        question = "What is the capital of France? Please think step by step."

    # Process and visualize
    visualize_r1_entropy(question, args.temperature, args.provider, args.show)


if __name__ == "__main__":
    main()
