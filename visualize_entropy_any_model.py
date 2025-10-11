#!/usr/bin/env python3
"""Visualize token entropy for any OpenRouter model that supports logprobs."""

import argparse
import math
import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()


def calculate_entropy(top_logprobs):
    """Calculate entropy from top logprobs."""
    if not top_logprobs:
        return 0.0
    
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


def test_models_for_logprobs():
    """Test different models to see which support logprobs."""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
    
    # Models to test
    models_to_test = [
        "openai/gpt-4o-mini",
        "openai/gpt-3.5-turbo",
        "anthropic/claude-3-haiku",
        "deepseek/deepseek-r1",
        "meta-llama/llama-3.1-8b-instruct",
        "mistralai/mistral-7b-instruct"
    ]
    
    print("Testing models for logprobs support:\n")
    
    for model in models_to_test:
        try:
            print(f"Testing {model}...", end=" ")
            completion = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Say hello"}],
                temperature=0.7,
                logprobs=True,
                top_logprobs=5,
                max_tokens=10
            )
            
            if hasattr(completion.choices[0], 'logprobs') and completion.choices[0].logprobs:
                print("✓ Supports logprobs")
            else:
                print("✗ No logprobs returned")
                
        except Exception as e:
            print(f"✗ Error: {str(e)}")
    
    print("\n" + "="*50 + "\n")


def visualize_entropy(question, model="openai/gpt-4o-mini", temperature=0.7):
    """Visualize entropy for a model that supports logprobs."""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
    
    print(f"Question: {question}")
    print(f"Model: {model} (temp={temperature})\n")
    
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            temperature=temperature,
            logprobs=True,
            top_logprobs=20,
        )
        
        # Check for logprobs
        if not hasattr(completion.choices[0], 'logprobs') or not completion.choices[0].logprobs:
            print(f"⚠️  Model '{model}' doesn't return logprobs.")
            print(f"\nResponse: {completion.choices[0].message.content}")
            return
        
        logprobs_data = completion.choices[0].logprobs
        if not logprobs_data.content:
            print("No logprobs content available")
            return
        
        print("Token Entropy Visualization:")
        print("█ = high entropy (uncertain), ░ = low entropy (confident)\n")
        
        # Process tokens
        max_entropy = 0
        tokens_data = []
        
        for token_data in logprobs_data.content:
            entropy = calculate_entropy(token_data.top_logprobs)
            max_entropy = max(max_entropy, entropy)
            
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
        
        # Display with inline entropy bars
        print("Response with entropy bars:\n")
        
        for i, data in enumerate(tokens_data):
            token = data["token"]
            entropy = data["entropy"]
            
            # Create mini entropy bar
            if max_entropy > 0:
                bar_level = int((entropy / max_entropy) * 5)
            else:
                bar_level = 0
            
            bars = ["░", "▁", "▃", "▅", "▇", "█"]
            bar = bars[min(bar_level, 5)]
            
            # Color based on entropy
            if entropy < 0.5:
                color = "\033[94m"  # blue
            elif entropy < 1.0:
                color = "\033[92m"  # green
            elif entropy < 1.5:
                color = "\033[93m"  # yellow
            else:
                color = "\033[91m"  # red
            
            # Print token with bar
            print(f"{color}{token}\033[0m{bar}", end="")
            
            # Newline handling
            if "\n" in token or (i + 1) % 20 == 0:
                print()
        
        print("\n\n" + "="*50)
        
        # Stats
        avg_entropy = sum(d["entropy"] for d in tokens_data) / len(tokens_data)
        print(f"\nStats:")
        print(f"• Tokens: {len(tokens_data)}")
        print(f"• Avg entropy: {avg_entropy:.3f}")
        print(f"• Max entropy: {max_entropy:.3f}")
        
        # High entropy tokens
        high_entropy = sorted(tokens_data, key=lambda x: x["entropy"], reverse=True)[:5]
        print(f"\nMost uncertain tokens:")
        for t in high_entropy:
            alts = []
            for alt in t["top_alts"]:
                token = alt['token'] if isinstance(alt, dict) else alt.token
                logprob = alt['logprob'] if isinstance(alt, dict) else alt.logprob
                prob = math.exp(logprob) * 100
                alts.append(f"{token} ({prob:.0f}%)")
            print(f"• \"{t['token']}\" (H={t['entropy']:.3f}) → {', '.join(alts)}")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"entropy_{model.replace('/', '_')}_{timestamp}.jsonl"
        with open(filename, "w") as f:
            for item in tokens_data:
                json.dump(item, f)
                f.write("\n")
        print(f"\n💾 Saved to: {filename}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Test which models support logprobs")
    parser.add_argument("--model", "-m", type=str, default="openai/gpt-4o-mini",
                       help="Model to use (default: openai/gpt-4o-mini)")
    parser.add_argument("--question", "-q", type=str, 
                       default="What is the capital of France? Explain your reasoning.",
                       help="Question to ask")
    parser.add_argument("--temperature", "-t", type=float, default=0.7)
    
    args = parser.parse_args()
    
    if args.test:
        test_models_for_logprobs()
    
    visualize_entropy(args.question, args.model, args.temperature)


if __name__ == "__main__":
    main()