#!/usr/bin/env python3
"""Inline entropy visualization for R1 responses - shows entropy next to each token."""

import argparse
import json
import math
import os
from datetime import datetime

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def calculate_entropy(top_logprobs):
    """Calculate entropy from top logprobs."""
    if not top_logprobs:
        return 0.0
    # Handle both dict and object formats
    probs = []
    for item in top_logprobs:
        if hasattr(item, 'logprob'):
            probs.append(math.exp(item.logprob))
        else:
            probs.append(math.exp(item["logprob"]))
    total = sum(probs)
    if total == 0:
        return 0.0
    probs = [p / total for p in probs]
    return -sum(p * math.log(p) for p in probs if p > 0)


def get_entropy_indicator(entropy, max_entropy=3.0):
    """Get a visual indicator for entropy level."""
    if entropy < 0.5:
        return "▁"
    elif entropy < 1.0:
        return "▃"
    elif entropy < 1.5:
        return "▅"
    elif entropy < 2.0:
        return "▇"
    else:
        return "█"


def visualize_inline(question="What is 2 + 2?", model="deepseek/deepseek-r1", temperature=0.7):
    """Process question and show inline entropy visualization."""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
    
    print(f"\n\033[1mQuestion:\033[0m {question}")
    print(f"\033[1mModel:\033[0m {model} (temp={temperature})\n")
    
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            temperature=temperature,
            logprobs=True,
            top_logprobs=20,
        )
        
        logprobs_data = completion.choices[0].logprobs
        if not logprobs_data or not logprobs_data.content:
            print("No logprobs data available")
            return
        
        print("\033[1mResponse with entropy indicators:\033[0m")
        print("(▁=low ▃=med-low ▅=medium ▇=med-high █=high entropy)\n")
        
        # Process tokens
        max_entropy = 0
        tokens_data = []
        
        for token_data in logprobs_data.content:
            entropy = calculate_entropy(token_data.top_logprobs)
            max_entropy = max(max_entropy, entropy)
            
            # Extract top alternatives
            top_alts = []
            if token_data.top_logprobs:
                for alt in token_data.top_logprobs[:3]:
                    if hasattr(alt, 'token'):
                        top_alts.append({'token': alt.token, 'logprob': alt.logprob})
                    else:
                        top_alts.append(alt)
            
            tokens_data.append({
                "token": token_data.token,
                "entropy": entropy,
                "logprob": token_data.logprob,
                "top_alts": top_alts
            })
        
        # Display inline
        line_buffer = ""
        for i, data in enumerate(tokens_data):
            token = data["token"]
            entropy = data["entropy"]
            indicator = get_entropy_indicator(entropy)
            
            # Color based on entropy
            if entropy < 0.5:
                color = "\033[94m"  # blue
            elif entropy < 1.0:
                color = "\033[92m"  # green
            elif entropy < 1.5:
                color = "\033[93m"  # yellow
            else:
                color = "\033[91m"  # red
            
            # Format token with entropy
            if "\n" in token:
                # Handle newlines
                parts = token.split("\n")
                for j, part in enumerate(parts):
                    if part:
                        line_buffer += f"{color}{part}{indicator}\033[0m"
                    if j < len(parts) - 1:
                        print(line_buffer)
                        line_buffer = ""
            else:
                line_buffer += f"{color}{token}{indicator}\033[0m"
                
                # Word boundary detection (simplified)
                if len(line_buffer) > 80 or i == len(tokens_data) - 1:
                    print(line_buffer)
                    line_buffer = ""
        
        if line_buffer:
            print(line_buffer)
        
        # Summary stats
        avg_entropy = sum(d["entropy"] for d in tokens_data) / len(tokens_data)
        high_entropy_tokens = [d for d in tokens_data if d["entropy"] > 1.5]
        
        print(f"\n\033[1mStats:\033[0m")
        print(f"• Total tokens: {len(tokens_data)}")
        print(f"• Average entropy: {avg_entropy:.3f}")
        print(f"• Max entropy: {max_entropy:.3f}")
        print(f"• High entropy tokens: {len(high_entropy_tokens)} ({len(high_entropy_tokens)/len(tokens_data)*100:.1f}%)")
        
        # Show some high entropy examples
        if high_entropy_tokens:
            print(f"\n\033[1mHighest entropy tokens:\033[0m")
            sorted_tokens = sorted(high_entropy_tokens, key=lambda x: x["entropy"], reverse=True)[:5]
            for t in sorted_tokens:
                alts = []
                for alt in t["top_alts"]:
                    token = alt['token'] if isinstance(alt, dict) else alt.token
                    logprob = alt['logprob'] if isinstance(alt, dict) else alt.logprob
                    alts.append(f"{token} ({math.exp(logprob)*100:.0f}%)")
                print(f"• \"{t['token']}\" (H={t['entropy']:.3f}) → alternatives: {', '.join(alts)}")
        
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", "-q", type=str, help="Question to ask")
    parser.add_argument("--temperature", "-t", type=float, default=0.7)
    parser.add_argument("--model", "-m", type=str, default="deepseek/deepseek-r1")
    
    args = parser.parse_args()
    
    # Default questions for quick testing
    if not args.question:
        args.question = "What is the capital of France? Think step by step."
    
    visualize_inline(args.question, args.model, args.temperature)


if __name__ == "__main__":
    main()