#!/usr/bin/env python3
"""Visualize token entropy from R1 responses with colored terminal output."""

import argparse
import json
import math
import os
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
    probs = []
    for item in top_logprobs:
        if hasattr(item, 'logprob'):
            probs.append(math.exp(item.logprob))
        else:
            probs.append(math.exp(item["logprob"]))
    
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


def get_bar_for_entropy(entropy, max_entropy, width=20):
    """Get a bar visualization for entropy."""
    if max_entropy == 0:
        return "━" * width
    
    filled = int((entropy / max_entropy) * width)
    return "█" * filled + "░" * (width - filled)


def process_and_visualize(question, model="deepseek/deepseek-r1", temperature=0.7):
    """Process a question with R1 and visualize token entropy."""
    # Initialize OpenRouter client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
    
    print(f"\n\033[1m📝 Question:\033[0m {question}")
    print(f"\n\033[1m🤖 Model:\033[0m {model}")
    print(f"\033[1m🌡️  Temperature:\033[0m {temperature}")
    print("\n" + "─" * 80 + "\n")
    
    # Make API call
    print("🔄 Calling R1 API...")
    start_time = perf_counter()
    
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            temperature=temperature,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            logprobs=True,
            top_logprobs=20,
        )
        
        elapsed = perf_counter() - start_time
        print(f"✅ Response received in {elapsed:.2f}s\n")
        
        # Process response
        response_text = completion.choices[0].message.content
        logprobs_data = completion.choices[0].logprobs
        
        if not logprobs_data or not logprobs_data.content:
            print("❌ No logprobs data available in response")
            return
        
        # Calculate entropy for each token
        tokens_with_entropy = []
        max_entropy = 0
        
        for token_data in logprobs_data.content:
            entropy = calculate_entropy(token_data.top_logprobs)
            max_entropy = max(max_entropy, entropy)
            
            # Extract top logprobs handling both dict and object formats
            top_logprobs = []
            if token_data.top_logprobs:
                for item in token_data.top_logprobs[:5]:
                    if hasattr(item, 'token'):
                        top_logprobs.append({
                            'token': item.token,
                            'logprob': item.logprob
                        })
                    else:
                        top_logprobs.append(item)
            
            tokens_with_entropy.append({
                "token": token_data.token,
                "logprob": token_data.logprob,
                "entropy": entropy,
                "top_logprobs": top_logprobs
            })
        
        # Display response with entropy visualization
        print("\033[1m📊 Token Entropy Visualization:\033[0m")
        print("(Higher entropy = more uncertainty in the model's prediction)\n")
        
        # Legend
        print("Entropy scale: \033[94m█ Low\033[0m \033[92m█ Medium-Low\033[0m \033[93m█ Medium-High\033[0m \033[91m█ High\033[0m\n")
        
        # Display tokens with entropy
        current_text = ""
        for i, item in enumerate(tokens_with_entropy):
            token = item["token"]
            entropy = item["entropy"]
            color = get_color_for_entropy(entropy, max_entropy)
            
            # Print token with color
            print(f"{color}{token}\033[0m", end="")
            current_text += token
            
            # Every 10 tokens or at newlines, show entropy details
            if (i + 1) % 10 == 0 or "\n" in token or i == len(tokens_with_entropy) - 1:
                print()  # New line
        
        print("\n" + "─" * 80 + "\n")
        
        # Detailed entropy analysis
        print("\033[1m📈 Entropy Statistics:\033[0m")
        entropies = [item["entropy"] for item in tokens_with_entropy]
        avg_entropy = sum(entropies) / len(entropies) if entropies else 0
        
        print(f"• Average entropy: {avg_entropy:.4f}")
        print(f"• Max entropy: {max_entropy:.4f}")
        print(f"• Min entropy: {min(entropies):.4f}")
        
        # Show highest entropy tokens
        print(f"\n\033[1m🔥 Top 10 Highest Entropy Tokens:\033[0m")
        sorted_tokens = sorted(tokens_with_entropy, key=lambda x: x["entropy"], reverse=True)[:10]
        
        for i, item in enumerate(sorted_tokens, 1):
            bar = get_bar_for_entropy(item["entropy"], max_entropy)
            print(f"{i:2d}. {bar} {item['entropy']:.4f} │ \"{item['token']}\"")
            
            # Show top alternatives
            if item["top_logprobs"]:
                print("    └─ Top alternatives: ", end="")
                alts = []
                for alt in item["top_logprobs"][:3]:
                    token = alt['token'] if isinstance(alt, dict) else alt.token
                    logprob = alt['logprob'] if isinstance(alt, dict) else alt.logprob
                    alts.append(f"\"{token}\" ({math.exp(logprob)*100:.1f}%)")
                print(", ".join(alts))
        
        # Save detailed results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"entropy_analysis_{timestamp}.jsonl"
        
        with open(output_file, "w") as f:
            for item in tokens_with_entropy:
                json.dump(item, f)
                f.write("\n")
        
        print(f"\n💾 Detailed results saved to: {output_file}")
        
        # Check for reasoning tokens if present
        if hasattr(completion.choices[0].message, 'reasoning') and completion.choices[0].message.reasoning:
            print(f"\n\033[1m💭 Reasoning:\033[0m")
            print(completion.choices[0].message.reasoning[:500] + "..." if len(completion.choices[0].message.reasoning) > 500 else completion.choices[0].message.reasoning)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


def main():
    parser = argparse.ArgumentParser(description="Visualize token entropy from R1 responses")
    parser.add_argument("--question", type=str, help="Question to ask (default: simple test question)")
    parser.add_argument("--gpqa", action="store_true", help="Use a random GPQA question")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature for generation")
    parser.add_argument("--model", type=str, default="deepseek/deepseek-r1", 
                       help="Model to use (default: deepseek/deepseek-r1)")
    
    args = parser.parse_args()
    
    # Determine question
    if args.question:
        question = args.question
    elif args.gpqa:
        # Load a GPQA question
        gpqa_dataset = load_from_disk("data/gpqa_diamond")
        import random
        question = random.choice(gpqa_dataset)["Question"]
        print(f"Using GPQA question (truncated): {question[:200]}...")
    else:
        # Default simple question
        question = "What is the capital of France? Please explain your reasoning step by step."
    
    # Process and visualize
    process_and_visualize(question, args.model, args.temperature)


if __name__ == "__main__":
    main()