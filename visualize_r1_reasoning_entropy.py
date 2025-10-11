#!/usr/bin/env python3
"""Analyze entropy and uncertainty patterns in R1's reasoning text."""

import argparse
import os
import re
from collections import Counter
from datetime import datetime
from time import perf_counter
from dotenv import load_dotenv
from openai import OpenAI
from datasets import load_from_disk
import math

load_dotenv()


def analyze_reasoning_uncertainty(reasoning_text):
    """Analyze uncertainty indicators in R1's reasoning."""
    
    # Uncertainty phrases and their weights
    uncertainty_indicators = {
        # High uncertainty (weight 3)
        "i'm not sure": 3,
        "not entirely sure": 3,
        "could be wrong": 3,
        "might be mistaken": 3,
        "i don't know": 3,
        "hard to say": 3,
        
        # Medium uncertainty (weight 2)
        "maybe": 2,
        "perhaps": 2,
        "possibly": 2,
        "probably": 2,
        "i think": 2,
        "it seems": 2,
        "might be": 2,
        "could be": 2,
        "or maybe": 2,
        "alternatively": 2,
        
        # Low uncertainty/verification (weight 1)
        "let me check": 1,
        "wait": 1,
        "actually": 1,
        "hmm": 1,
        "uh": 1,
        "um": 1,
        "well": 1,
        
        # Corrections (weight 3)
        "no, wait": 3,
        "actually, no": 3,
        "that's wrong": 3,
        "mistake": 3,
        "error": 3,
        "incorrect": 3,
    }
    
    # Confidence indicators (negative weight)
    confidence_indicators = {
        "definitely": -2,
        "certainly": -2,
        "clearly": -2,
        "obviously": -2,
        "must be": -2,
        "has to be": -2,
        "for sure": -2,
        "without doubt": -2,
        "confirmed": -1,
        "correct": -1,
        "right": -1,
        "yes": -1,
    }
    
    # Split into sentences
    sentences = re.split(r'[.!?]+', reasoning_text.lower())
    
    uncertainty_scores = []
    highlighted_sentences = []
    
    for sentence in sentences:
        if not sentence.strip():
            continue
            
        score = 0
        highlights = []
        
        # Check uncertainty indicators
        for phrase, weight in uncertainty_indicators.items():
            if phrase in sentence:
                score += weight
                highlights.append((phrase, weight))
        
        # Check confidence indicators
        for phrase, weight in confidence_indicators.items():
            if phrase in sentence:
                score += weight
                highlights.append((phrase, weight))
        
        uncertainty_scores.append((sentence.strip(), score, highlights))
    
    return uncertainty_scores


def visualize_reasoning_entropy(reasoning_text):
    """Create entropy-like visualization of reasoning uncertainty."""
    
    uncertainty_scores = analyze_reasoning_uncertainty(reasoning_text)
    
    print("\n" + "="*70)
    print("🧠 R1 REASONING UNCERTAINTY ANALYSIS")
    print("="*70 + "\n")
    
    # Calculate max score for normalization
    max_score = max(abs(score) for _, score, _ in uncertainty_scores) if uncertainty_scores else 1
    
    # Group by score levels
    high_uncertainty = [(s, sc, h) for s, sc, h in uncertainty_scores if sc >= 3]
    medium_uncertainty = [(s, sc, h) for s, sc, h in uncertainty_scores if 1 <= sc < 3]
    low_uncertainty = [(s, sc, h) for s, sc, h in uncertainty_scores if -1 <= sc < 1]
    high_confidence = [(s, sc, h) for s, sc, h in uncertainty_scores if sc < -1]
    
    # Display uncertainty heat map
    print("📊 UNCERTAINTY HEAT MAP:")
    print("(Red = high uncertainty, Yellow = medium, Green = low, Blue = confident)")
    print("─" * 70)
    
    # Create visual representation
    for i, (sentence, score, highlights) in enumerate(uncertainty_scores[:30]):  # First 30 sentences
        # Color based on score
        if score >= 3:
            color = "\033[91m"  # red
            symbol = "█"
        elif score >= 1:
            color = "\033[93m"  # yellow
            symbol = "▓"
        elif score >= -1:
            color = "\033[92m"  # green
            symbol = "▒"
        else:
            color = "\033[94m"  # blue
            symbol = "░"
        
        # Create bar
        bar_length = int(abs(score) / max_score * 20) if max_score > 0 else 0
        bar = symbol * max(bar_length, 1)
        
        # Truncate sentence for display
        display_sentence = sentence[:60] + "..." if len(sentence) > 60 else sentence
        
        print(f"{color}{bar:<20}\033[0m {display_sentence}")
    
    if len(uncertainty_scores) > 30:
        print(f"\n... and {len(uncertainty_scores) - 30} more sentences")
    
    # Show most uncertain sentences
    if high_uncertainty:
        print(f"\n\n🔴 HIGHEST UNCERTAINTY SENTENCES (score ≥ 3):")
        print("─" * 70)
        for sentence, score, highlights in high_uncertainty[:5]:
            print(f"\n• Score {score}: \"{sentence[:100]}{'...' if len(sentence) > 100 else ''}\"")
            if highlights:
                print(f"  Indicators: {', '.join([f'{p} ({w})' for p, w in highlights])}")
    
    # Show corrections
    corrections = [(s, sc, h) for s, sc, h in uncertainty_scores 
                   if any(word in s for word in ['wait', 'actually', 'mistake', 'wrong', 'error'])]
    
    if corrections:
        print(f"\n\n⚠️  CORRECTIONS & REVISIONS:")
        print("─" * 70)
        for sentence, score, _ in corrections[:5]:
            print(f"• \"{sentence[:100]}{'...' if len(sentence) > 100 else ''}\"")
    
    # Statistics
    print(f"\n\n📈 UNCERTAINTY STATISTICS:")
    print("─" * 70)
    total_sentences = len(uncertainty_scores)
    if total_sentences > 0:
        avg_score = sum(score for _, score, _ in uncertainty_scores) / total_sentences
        print(f"• Total sentences analyzed: {total_sentences}")
        print(f"• Average uncertainty score: {avg_score:.2f}")
        print(f"• High uncertainty sentences: {len(high_uncertainty)} ({len(high_uncertainty)/total_sentences*100:.1f}%)")
        print(f"• Medium uncertainty: {len(medium_uncertainty)} ({len(medium_uncertainty)/total_sentences*100:.1f}%)")
        print(f"• Low uncertainty: {len(low_uncertainty)} ({len(low_uncertainty)/total_sentences*100:.1f}%)")
        print(f"• High confidence: {len(high_confidence)} ({len(high_confidence)/total_sentences*100:.1f}%)")
        print(f"• Contains corrections: {'Yes' if corrections else 'No'}")
    
    return uncertainty_scores


def calculate_reasoning_entropy_proxy(reasoning_text):
    """Calculate entropy-like metrics from reasoning text."""
    
    # Word frequency analysis
    words = re.findall(r'\b\w+\b', reasoning_text.lower())
    word_freq = Counter(words)
    
    # Calculate word entropy (diversity)
    total_words = len(words)
    word_probs = [count/total_words for count in word_freq.values()]
    word_entropy = -sum(p * math.log(p) for p in word_probs if p > 0)
    
    # Sentence length variance (complexity indicator)
    sentences = re.split(r'[.!?]+', reasoning_text)
    sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
    
    if sentence_lengths:
        avg_length = sum(sentence_lengths) / len(sentence_lengths)
        variance = sum((l - avg_length)**2 for l in sentence_lengths) / len(sentence_lengths)
        complexity_score = math.sqrt(variance)
    else:
        complexity_score = 0
    
    # Question frequency (uncertainty indicator)
    questions = len(re.findall(r'\?', reasoning_text))
    question_ratio = questions / len(sentences) if sentences else 0
    
    return {
        "word_entropy": word_entropy,
        "complexity_score": complexity_score,
        "question_ratio": question_ratio,
        "total_words": total_words,
        "unique_words": len(word_freq),
        "vocabulary_richness": len(word_freq) / total_words if total_words > 0 else 0
    }


def process_r1_with_entropy_analysis(question, temperature=0.7):
    """Process question with R1 and analyze reasoning entropy."""
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
    
    print(f"\n📝 Question: {question}")
    print(f"🤖 Model: deepseek/deepseek-r1")
    print(f"🌡️  Temperature: {temperature}")
    print("\n" + "─" * 70 + "\n")
    
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
        
        response_text = completion.choices[0].message.content
        
        # Check for reasoning
        if hasattr(completion.choices[0].message, 'reasoning') and completion.choices[0].message.reasoning:
            reasoning_text = completion.choices[0].message.reasoning
            
            # Analyze uncertainty
            uncertainty_scores = visualize_reasoning_entropy(reasoning_text)
            
            # Calculate entropy proxy metrics
            print(f"\n\n🎲 ENTROPY-LIKE METRICS:")
            print("─" * 70)
            metrics = calculate_reasoning_entropy_proxy(reasoning_text)
            
            print(f"• Word entropy (diversity): {metrics['word_entropy']:.3f}")
            print(f"• Sentence complexity: {metrics['complexity_score']:.3f}")
            print(f"• Question ratio: {metrics['question_ratio']:.3f}")
            print(f"• Vocabulary richness: {metrics['vocabulary_richness']:.3f}")
            print(f"• Total words: {metrics['total_words']}")
            print(f"• Unique words: {metrics['unique_words']}")
            
            # Save analysis
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"r1_reasoning_entropy_{timestamp}.txt"
            
            with open(filename, "w") as f:
                f.write(f"Question: {question}\n")
                f.write(f"Temperature: {temperature}\n")
                f.write(f"Response time: {elapsed:.2f}s\n")
                f.write("\n" + "="*70 + "\n")
                f.write("UNCERTAINTY ANALYSIS:\n\n")
                
                for sentence, score, highlights in uncertainty_scores[:50]:
                    f.write(f"Score {score}: {sentence}\n")
                    if highlights:
                        f.write(f"  Indicators: {highlights}\n")
                    f.write("\n")
                
                f.write("\n" + "="*70 + "\n")
                f.write("FULL REASONING:\n")
                f.write(reasoning_text)
                f.write("\n" + "="*70 + "\n")
                f.write("FINAL ANSWER:\n")
                f.write(response_text)
            
            print(f"\n💾 Full analysis saved to: {filename}")
            
            # Show final answer
            print(f"\n\n📄 FINAL ANSWER:")
            print("─" * 70)
            print(response_text[:300] + "..." if len(response_text) > 300 else response_text)
            
        else:
            print("⚠️  No reasoning data available")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


def main():
    parser = argparse.ArgumentParser(description="Analyze entropy-like patterns in R1's reasoning")
    parser.add_argument("--question", "-q", type=str, help="Question to ask")
    parser.add_argument("--gpqa", action="store_true", help="Use a GPQA question")
    parser.add_argument("--temperature", "-t", type=float, default=0.7)
    
    args = parser.parse_args()
    
    if args.question:
        question = args.question
    elif args.gpqa:
        gpqa_dataset = load_from_disk("data/gpqa_diamond")
        import random
        idx = random.randint(0, min(10, len(gpqa_dataset)-1))
        question = gpqa_dataset[idx]["Question"]
        print(f"Using GPQA question #{idx}")
    else:
        # Test question with some complexity
        question = "Explain why water expands when it freezes, unlike most other substances. What are the implications?"
    
    process_r1_with_entropy_analysis(question, args.temperature)


if __name__ == "__main__":
    main()