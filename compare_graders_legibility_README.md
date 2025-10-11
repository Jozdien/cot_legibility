# Compare Graders - Legibility Only (Weighted Kappa)

This is the modified version of `compare_graders.py` that focuses only on comparing legibility scores between Claude and GPT-4, using the exact same prompt as `autograder.py`.

## Key Changes

1. **Uses exact same legibility grading prompt** from `autograder.py`, including the three example texts
2. **Computes weighted Cohen's kappa** using quadratic weights - small disagreements (e.g., difference of 1) are treated as much less severe than larger disagreements
3. **Grades reasoning text** if available, otherwise grades response text
4. **Handles API errors gracefully** - if Claude API is disabled, continues with GPT-4 only
5. **Generates confusion matrix** to visualize the pattern of agreements and disagreements

## Usage

```bash
python compare_graders.py \
    --rollout_dir r1_rollouts/your_directory \
    --num_samples 50 \
    --output_dir grader_comparison \
    --max_workers 5
```

## Output

The script produces:
- `legibility_grading_comparison.json`: Detailed results with scores from both graders and weighted kappa
- `legibility_grader_comparison.png`: Visual comparison with scatter plots, distributions, and weighted Cohen's kappa
- `legibility_correlation.png`: Correlation plot between the two graders' scores
- `legibility_confusion_matrix.png`: Confusion matrix showing the pattern of agreements/disagreements

## Weighted Cohen's Kappa Interpretation

- < 0: Poor agreement
- 0.00-0.20: Slight agreement  
- 0.21-0.40: Fair agreement
- 0.41-0.60: Moderate agreement
- 0.61-0.80: Substantial agreement
- 0.81-1.00: Almost perfect agreement

**Note**: The weighted kappa uses quadratic weights, which means:
- A disagreement of 1 point (e.g., 3 vs 4) has weight = 1 - (1²/9²) = 0.988 (very low penalty)
- A disagreement of 5 points (e.g., 2 vs 7) has weight = 1 - (5²/9²) = 0.691 (moderate penalty)  
- A disagreement of 9 points (e.g., 1 vs 10) has weight = 1 - (9²/9²) = 0 (maximum penalty)

## API Requirements

- Requires valid API keys in `.env` file:
  - `ANTHROPIC_API_KEY` for Claude grading
  - `OPENAI_API_KEY` for GPT-4 grading
  
If Claude API is disabled, the script will continue with GPT-4 only but won't be able to compute inter-rater reliability.