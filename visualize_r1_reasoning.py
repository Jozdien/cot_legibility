#!/usr/bin/env python3
"""Visualize R1's reasoning process since it doesn't provide logprobs."""

import argparse
import os
import re
from datetime import datetime
from time import perf_counter
from dotenv import load_dotenv
from openai import OpenAI
from datasets import load_from_disk

load_dotenv()


def extract_reasoning_sections(reasoning_text):
    """Extract different sections from R1's reasoning."""
    sections = {
        "initial_thoughts": [],
        "calculations": [],
        "verifications": [],
        "corrections": [],
        "final_answer": []
    }
    
    # Split by sentences instead of lines since R1 often has long single-line reasoning
    import re
    sentences = re.split(r'(?<=[.!?])\s+', reasoning_text)
    
    current_section = "initial_thoughts"
    
    for sentence in sentences:
        sentence_lower = sentence.lower()
        
        # Detect section changes based on keywords
        if any(word in sentence_lower for word in ['calculate', 'compute', 'solve', 'work out', 'adding', 'multiply']):
            current_section = "calculations"
        elif any(word in sentence_lower for word in ['check', 'verify', 'confirm', 'double-check', 'make sure']):
            current_section = "verifications"
        elif any(word in sentence_lower for word in ['wait', 'actually', 'no,', 'mistake', 'wrong', 'error', 'but wait']):
            current_section = "corrections"
        elif any(word in sentence_lower for word in ['therefore', 'final answer', 'conclusion', 'so the answer', 'hence', 'thus']):
            current_section = "final_answer"
        
        if sentence.strip():
            sections[current_section].append(sentence)
    
    return sections


def visualize_reasoning_flow(reasoning_text):
    """Create a visual representation of R1's reasoning process."""
    sections = extract_reasoning_sections(reasoning_text)
    
    print("\n" + "="*60)
    print("🧠 R1 REASONING FLOW VISUALIZATION")
    print("="*60 + "\n")
    
    # Color codes for different sections
    colors = {
        "initial_thoughts": "\033[94m",  # blue
        "calculations": "\033[92m",      # green
        "verifications": "\033[93m",     # yellow
        "corrections": "\033[91m",       # red
        "final_answer": "\033[95m"       # magenta
    }
    
    # Section symbols
    symbols = {
        "initial_thoughts": "💭",
        "calculations": "🔢",
        "verifications": "✓",
        "corrections": "⚠️",
        "final_answer": "📍"
    }
    
    # Display each section
    for section_name, sentences in sections.items():
        if sentences:
            color = colors[section_name]
            symbol = symbols[section_name]
            
            print(f"{symbol} {color}{section_name.replace('_', ' ').title()}:\033[0m")
            print(f"{color}{'─' * 50}\033[0m")
            
            # Show first few sentences of each section
            for i, sentence in enumerate(sentences[:3]):
                # Wrap long sentences
                if len(sentence) > 80:
                    print(f"{color}  {sentence[:77]}...\033[0m")
                else:
                    print(f"{color}  {sentence}\033[0m")
            
            if len(sentences) > 3:
                print(f"{color}  ... ({len(sentences) - 3} more sentences)\033[0m")
            print()
    
    # Create a reasoning flow diagram
    print("\n📊 REASONING PATTERN:")
    print("─" * 50)
    
    # Count transitions
    thought_depth = len(sections["initial_thoughts"])
    calc_count = len(sections["calculations"])
    verify_count = len(sections["verifications"])
    correction_count = len(sections["corrections"])
    
    # Visualize the flow
    bar_width = 40
    max_count = max(thought_depth, calc_count, verify_count, correction_count, 1)
    
    for name, count in [
        ("Think", thought_depth),
        ("Calculate", calc_count),
        ("Verify", verify_count),
        ("Correct", correction_count)
    ]:
        bar_length = int((count / max_count) * bar_width)
        bar = "█" * bar_length + "░" * (bar_width - bar_length)
        print(f"{name:10} {bar} {count}")
    
    print("\n" + "="*60)
    
    # Return metrics
    return {
        "thought_depth": thought_depth,
        "calculations": calc_count,
        "verifications": verify_count,
        "corrections": correction_count,
        "total_lines": sum(len(s) for s in sections.values())
    }


def process_r1_with_reasoning(question, temperature=0.7):
    """Process a question with R1 and visualize its reasoning."""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
    
    print(f"\n📝 Question: {question}")
    print(f"🤖 Model: deepseek/deepseek-r1")
    print(f"🌡️  Temperature: {temperature}")
    print("\n" + "─" * 60 + "\n")
    
    print("🔄 Calling R1 API...")
    start_time = perf_counter()
    
    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=[{"role": "user", "content": question}],
            temperature=temperature,
        )
        
        elapsed = perf_counter() - start_time
        print(f"✅ Response received in {elapsed:.2f}s\n")
        
        # Get response and reasoning
        response_text = completion.choices[0].message.content
        
        # Display final answer
        print("📄 FINAL ANSWER:")
        print("─" * 60)
        print(response_text[:500] + "..." if len(response_text) > 500 else response_text)
        print()
        
        # Check for reasoning
        if hasattr(completion.choices[0].message, 'reasoning') and completion.choices[0].message.reasoning:
            reasoning_text = completion.choices[0].message.reasoning
            
            # Visualize reasoning flow
            metrics = visualize_reasoning_flow(reasoning_text)
            
            # Save full reasoning
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"r1_reasoning_{timestamp}.txt"
            
            with open(filename, "w") as f:
                f.write(f"Question: {question}\n")
                f.write(f"Temperature: {temperature}\n")
                f.write(f"Response time: {elapsed:.2f}s\n")
                f.write("\n" + "="*60 + "\n")
                f.write("REASONING:\n")
                f.write(reasoning_text)
                f.write("\n" + "="*60 + "\n")
                f.write("FINAL ANSWER:\n")
                f.write(response_text)
            
            print(f"\n💾 Full reasoning saved to: {filename}")
            
            # Display metrics
            print(f"\n📈 REASONING METRICS:")
            print(f"• Total reasoning sentences: {metrics['total_lines']}")
            print(f"• Initial thoughts: {metrics['thought_depth']} sentences")
            print(f"• Calculations: {metrics['calculations']} sentences")
            print(f"• Verifications: {metrics['verifications']} sentences")
            print(f"• Corrections: {metrics['corrections']} sentences")
            
            # Calculate reasoning complexity
            reasoning_words = len(reasoning_text.split())
            answer_words = len(response_text.split())
            print(f"• Reasoning length: {reasoning_words} words")
            print(f"• Answer length: {answer_words} words")
            print(f"• Reasoning/Answer ratio: {reasoning_words / max(answer_words, 1):.1f}x")
            
        else:
            print("⚠️  No reasoning data available in response")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


def main():
    parser = argparse.ArgumentParser(description="Visualize R1's reasoning process")
    parser.add_argument("--question", "-q", type=str, help="Question to ask")
    parser.add_argument("--gpqa", action="store_true", help="Use a random GPQA question")
    parser.add_argument("--temperature", "-t", type=float, default=0.7)
    
    args = parser.parse_args()
    
    # Determine question
    if args.question:
        question = args.question
    elif args.gpqa:
        gpqa_dataset = load_from_disk("data/gpqa_diamond")
        import random
        idx = random.randint(0, min(10, len(gpqa_dataset)-1))  # First 10 for faster testing
        question = gpqa_dataset[idx]["Question"]
        print(f"Using GPQA question #{idx}")
    else:
        # Default test question
        question = "What is 15 * 17? Show your work step by step."
    
    process_r1_with_reasoning(question, args.temperature)


if __name__ == "__main__":
    main()