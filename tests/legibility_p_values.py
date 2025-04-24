import json
import numpy as np
import pandas as pd
from scipy import stats

def analyze_legibility_scores(filepath):
    print(f"Analyzing {filepath}")
    # Read and parse the JSON file
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    # Extract legibility scores
    deepseek_scores = []
    deepseek_answers_scores = []
    anthropic_scores = []
    anthropic_answers_scores = []
    openai_scores = []
    openai_answers_scores = []
    cutoff_scores = []
    cutoff_answers_scores = []
    
    for entry in data:
        legibility = entry.get('legibility', {})
        
        # Get deepseek reasoning score
        if 'deepseek_reasoning' in legibility:
            score = legibility['deepseek_reasoning'].get('score')
            if score is not None and score != 'N/A':
                deepseek_scores.append(score)
        if 'deepseek_response' in legibility:
            score = legibility['deepseek_response'].get('score')
            if score is not None and score != 'N/A':
                deepseek_answers_scores.append(score)
        
        # Get other reasoning scores
        if 'anthropic_reasoning' in legibility:
            score = legibility['anthropic_reasoning'].get('score')
            if score is not None and score != 'N/A':
                anthropic_scores.append(score)
        if 'anthropic_response' in legibility:
            score = legibility['anthropic_response'].get('score')
            if score is not None and score != 'N/A':
                anthropic_answers_scores.append(score)
        if 'openai_reasoning' in legibility:
            score = legibility['openai_reasoning'].get('score')
            if score is not None and score != 'N/A':
                openai_scores.append(score)
        if 'openai_response' in legibility:
            score = legibility['openai_response'].get('score')
            if score is not None and score != 'N/A':
                openai_answers_scores.append(score)
        if 'cutoff_reasoning' in legibility:
            score = legibility['cutoff_reasoning'].get('score')
            if score is not None and score != 'N/A':
                cutoff_scores.append(score)
        if 'cutoff_response' in legibility:
            score = legibility['cutoff_response'].get('score')
            if score is not None and score != 'N/A':
                cutoff_answers_scores.append(score)
        
    # Perform Mann-Whitney U test
    _, pvalue_deepseek_anthropic = stats.mannwhitneyu(deepseek_scores, anthropic_scores)
    _, pvalue_deepseek_openai = stats.mannwhitneyu(deepseek_scores, openai_scores)
    _, pvalue_deepseek_cutoff = stats.mannwhitneyu(deepseek_scores, cutoff_scores)
    _, pvalue_deepseek_answers_anthropic = stats.mannwhitneyu(deepseek_answers_scores, anthropic_answers_scores)
    _, pvalue_deepseek_answers_openai = stats.mannwhitneyu(deepseek_answers_scores, openai_answers_scores)
    _, pvalue_deepseek_answers_cutoff = stats.mannwhitneyu(deepseek_answers_scores, cutoff_answers_scores)

    # print(f"DeepSeek Reasoning scores (n={len(deepseek_scores)}): {deepseek_scores}")
    # print(f"Anthropic Reasoning scores (n={len(anthropic_scores)}): {anthropic_scores}")
    # print(f"OpenAI Reasoning scores (n={len(openai_scores)}): {openai_scores}")
    # print(f"Cutoff Reasoning scores (n={len(cutoff_scores)}): {cutoff_scores}")
    print(f"DeepSeek vs Anthropic Mann-Whitney U p-value: {pvalue_deepseek_anthropic}")
    print(f"DeepSeek vs OpenAI Mann-Whitney U p-value: {pvalue_deepseek_openai}")
    print(f"DeepSeek vs Cutoff Mann-Whitney U p-value: {pvalue_deepseek_cutoff}")
    print(f"DeepSeek vs Anthropic Answers Mann-Whitney U p-value: {pvalue_deepseek_answers_anthropic}")
    print(f"DeepSeek vs OpenAI Answers Mann-Whitney U p-value: {pvalue_deepseek_answers_openai}")
    print(f"DeepSeek vs Cutoff Answers Mann-Whitney U p-value: {pvalue_deepseek_answers_cutoff}")
    
    # Also get summary statistics
    deepseek_mean = np.mean(deepseek_scores)
    anthropic_mean = np.mean(anthropic_scores)
    openai_mean = np.mean(openai_scores)
    cutoff_mean = np.mean(cutoff_scores)
    deepseek_answers_mean = np.mean(deepseek_answers_scores)
    anthropic_answers_mean = np.mean(anthropic_answers_scores)
    openai_answers_mean = np.mean(openai_answers_scores)
    cutoff_answers_mean = np.mean(cutoff_answers_scores)
    print(f"\nMean scores:")
    print(f"DeepSeek Reasoning: {deepseek_mean:.2f}")
    print(f"Anthropic Reasoning: {anthropic_mean:.2f}")
    print(f"OpenAI Reasoning: {openai_mean:.2f}")
    print(f"Cutoff Reasoning: {cutoff_mean:.2f}")
    print(f"DeepSeek Answers: {deepseek_answers_mean:.2f}")
    print(f"Anthropic Answers: {anthropic_answers_mean:.2f}")
    print(f"OpenAI Answers: {openai_answers_mean:.2f}")
    print(f"Cutoff Answers: {cutoff_answers_mean:.2f}")

# Usage:
analyze_legibility_scores('../scores/temp_0.4_cutoff_0.25_openrouter_scores.json')
