# Testing Custom Models via OpenRouter

This guide explains how to test any model available on OpenRouter with the existing analysis pipeline.

## Prerequisites

1. Ensure you have your OpenRouter API key set in the environment:
   ```bash
   export OPENROUTER_API_KEY="your_openrouter_api_key"
   ```

2. Make sure you have the GPQA dataset downloaded:
   ```bash
   python get_gpqa_d.py
   ```

## Step 1: Run Your Model

Use the `custom_model_run.py` script to test any model available on OpenRouter:

```bash
python custom_model_run.py \
  --model "anthropic/claude-3.5-sonnet" \
  --model-display-name "claude35" \
  --num_questions 200 \
  --temperature 1.0 \
  --logprobs  # Optional: only if the model supports logprobs
```

### Parameters:
- `--model`: The model identifier on OpenRouter (check OpenRouter docs for available models)
- `--model-display-name`: A short name for your model (used in filenames and plots)
- `--num_questions`: Number of questions to process (default: 200)
- `--temperature`: Temperature setting for the model (default: 1.0)
- `--max_workers`: Number of parallel workers (default: 30)
- `--output_dir`: Custom output directory (default: auto-generated based on model name)
- `--logprobs`: Request logprobs if supported by the model

### Example Models on OpenRouter:
- `anthropic/claude-3.5-sonnet`
- `openai/gpt-4-turbo`
- `google/gemini-pro`
- `mistralai/mixtral-8x7b-instruct`
- `meta-llama/llama-3-70b-instruct`

## Step 2: Grade the Results

Use the custom autograder to analyze your model's outputs:

```bash
python autograder_custom.py \
  --dir "r1_rollouts/claude35_temp_1.0" \
  --model-display-name "claude35"
```

This will generate:
- `scores/claude35_temp_1.0_scores.json`: Detailed scoring data
- `answers/claude35_temp_1.0_answers.md`: Human-readable analysis

## Step 3: Generate Plots

To include your model in the analysis plots, run:

```bash
python analyze_scores.py --dir scores --pattern "*_scores.json" --plots
```

The plots will automatically include your custom model with appropriate labels and colors.

## Example: Testing Claude 3.5 Sonnet

```bash
# 1. Run Claude 3.5 on 50 questions as a test
python custom_model_run.py \
  --model "anthropic/claude-3.5-sonnet" \
  --model-display-name "claude35" \
  --num_questions 50 \
  --temperature 0.7

# 2. Grade the outputs
python autograder_custom.py \
  --dir "r1_rollouts/claude35_temp_0.7" \
  --model-display-name "claude35"

# 3. Generate plots including all models
python analyze_scores.py --dir scores --pattern "*_scores.json" --plots
```

## Notes

1. The analysis pipeline will automatically handle models that don't have a "reasoning" section (only DeepSeek R1-style models have this).

2. Colors for new models are automatically assigned. You can customize colors by adding your model to the `get_model_colors()` function in `utils/analysis_utils.py`.

3. The autograder uses Claude for grading legibility and correctness. Make sure you have your Anthropic API key set:
   ```bash
   export ANTHROPIC_API_KEY="your_anthropic_api_key"
   ```

4. For best results, use consistent naming for your model throughout the pipeline (same `--model-display-name` in both scripts).

## Troubleshooting

- If you get API errors, check your OpenRouter API key and model availability
- For rate limiting issues, reduce `--max_workers`
- If autograding fails, ensure your Anthropic API key is set correctly
- Check that output files follow the expected naming pattern: `{model_display_name}_response_{timestamp}_{question}.md`