# Multi-Dataset Support for Model Testing

This guide explains how to test models on different datasets (GPQA-Diamond and MMLU-Pro) using the updated pipeline.

## Dataset Differences

### GPQA-Diamond (Original)
- **Format**: Open-ended graduate-level science questions
- **Answer Type**: Free-form text answers
- **Grading**: Supports correct/partially_correct/incorrect
- **Questions**: ~200 challenging physics, chemistry, and biology questions

### MMLU-Pro (New)
- **Format**: Multiple-choice questions with 10 options (A-J)
- **Answer Type**: Single letter (A-J)
- **Grading**: Binary correct/incorrect only
- **Questions**: 12,032 questions across various subjects
- **Note**: More challenging than original MMLU with 10 choices instead of 4

## Setup

### 1. Download MMLU-Pro Dataset
```bash
python get_mmlu_pro.py
```

This downloads the MMLU-Pro dataset to `data/mmlu_pro/`.

### 2. Run a Model on MMLU-Pro

Use the multi-dataset version of the custom model runner:

```bash
python custom_model_run_multi_dataset.py \
  --model "anthropic/claude-3.5-sonnet" \
  --model-display-name "claude35" \
  --dataset mmlu_pro \
  --num_questions 100 \
  --temperature 0.7
```

### Parameters:
- `--dataset`: Choose between "gpqa" (default) or "mmlu_pro"
- All other parameters remain the same as before

### Output Directory Structure:
- GPQA: `r1_rollouts/gpqa_{model_name}_temp_{temperature}/`
- MMLU-Pro: `r1_rollouts/mmlu_pro_{model_name}_temp_{temperature}/`

## 3. Grade the Results

Use the multi-dataset autograder:

```bash
python autograder_custom_multi.py \
  --dir "r1_rollouts/mmlu_pro_claude35_temp_0.7" \
  --model-display-name "claude35" \
  --dataset auto
```

### Parameters:
- `--dataset`: Choose "gpqa", "mmlu_pro", or "auto" (auto-detects from directory name)

### Output Files:
- Scores: `scores/mmlu_pro_claude35_temp_0.7_scores.json`
- Analysis: `answers/mmlu_pro_claude35_temp_0.7_answers.md`

## 4. Generate Plots

For custom models or models not in the predefined list (deepseek, anthropic, openai, cutoff), use the flexible analyzer:

```bash
# For custom models like R1, use the flexible analyzer
python analyze_scores_flexible.py --dir scores --pattern "*_scores.json" --plots

# Or analyze a specific file
python analyze_scores_flexible.py --file scores/mmlu_pro_R1_temp_1.0_scores.json --plots
```

For standard models, the original analyzer still works:
```bash
python analyze_scores.py --dir scores --pattern "*_scores.json" --plots
```

## Complete Examples

### Example 1: Test GPT-4 on MMLU-Pro
```bash
# Download dataset (if not already done)
python get_mmlu_pro.py

# Run GPT-4 on 50 MMLU-Pro questions
python custom_model_run_multi_dataset.py \
  --model "openai/gpt-4-turbo" \
  --model-display-name "gpt4" \
  --dataset mmlu_pro \
  --num_questions 50 \
  --temperature 0.3

# Grade the results
python autograder_custom_multi.py \
  --dir "r1_rollouts/mmlu_pro_gpt4_temp_0.3" \
  --model-display-name "gpt4"

# Generate plots
python analyze_scores.py --dir scores --pattern "*_scores.json" --plots
```

### Example 2: Compare Same Model on Both Datasets
```bash
# Run on GPQA
python custom_model_run_multi_dataset.py \
  --model "mistralai/mixtral-8x7b-instruct" \
  --model-display-name "mixtral" \
  --dataset gpqa \
  --num_questions 50

# Run on MMLU-Pro
python custom_model_run_multi_dataset.py \
  --model "mistralai/mixtral-8x7b-instruct" \
  --model-display-name "mixtral" \
  --dataset mmlu_pro \
  --num_questions 50

# Grade both
python autograder_custom_multi.py \
  --dir "r1_rollouts/gpqa_mixtral_temp_1.0" \
  --model-display-name "mixtral"

python autograder_custom_multi.py \
  --dir "r1_rollouts/mmlu_pro_mixtral_temp_1.0" \
  --model-display-name "mixtral"

# Plots will show both results
python analyze_scores.py --dir scores --pattern "*_scores.json" --plots
```

## Key Changes from Original Pipeline

### Necessary Changes:
1. **Question Formatting**: MMLU-Pro questions are formatted with options A-J
2. **Answer Extraction**: Added logic to extract letter answers (A-J) for MMLU-Pro
3. **Correctness Grading**: MMLU-Pro uses binary grading (no partial credit)
4. **Dataset Detection**: Auto-detects dataset type from question format or directory name

### Unchanged:
- Legibility scoring remains the same
- File naming conventions preserved
- Plot generation works identically
- API interfaces unchanged
- Output directory structure follows same pattern

## Tips

1. **Dataset Auto-Detection**: The autograder can auto-detect the dataset type from:
   - Directory name (if it contains "mmlu_pro")
   - Question format (presence of A-J options)

2. **Mixing Datasets**: Keep GPQA and MMLU-Pro results in separate directories for cleaner analysis

3. **Temperature Settings**: MMLU-Pro might benefit from lower temperatures (0.0-0.3) since it's multiple choice

4. **Batch Processing**: MMLU-Pro has many more questions, so consider processing in batches

## Troubleshooting

- **Dataset Not Found**: Make sure to run `python get_mmlu_pro.py` first
- **Answer Extraction Issues**: MMLU-Pro expects single letter answers (A-J)
- **Grading Differences**: Remember MMLU-Pro doesn't support "partially_correct"
- **"No valid scores found" Error**: If using custom model names (not deepseek/anthropic/openai/cutoff), use `analyze_scores_flexible.py` instead of `analyze_scores.py`
- **Empty Plots**: The flexible analyzer handles any model name and creates all plots correctly, including illegibility by correctness