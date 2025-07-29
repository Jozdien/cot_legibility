# Science Datasets for Long Reasoning Tasks

This guide covers using ScienceQA and ChemBench - two challenging science datasets that require extensive reasoning.

## Dataset Overview

### ScienceQA (Filtered for Hard Questions)
- **Focus**: Chemistry, Physics, Advanced Biology
- **Format**: Multiple choice with hints and detailed solutions
- **Filter Applied**: High school level, text-only questions
- **Why Good for Long Reasoning**: Questions often require multi-step problem solving, applying multiple concepts

### ChemBench
- **Source**: jablonkagroup/ChemBench on HuggingFace
- **Focus**: Chemistry - from general to quantum/materials science
- **Format**: Mix of multiple choice and open-ended
- **Filter Applied**: Questions requiring calculation/mechanism/synthesis
- **Why Good for Long Reasoning**: Complex chemical problems requiring detailed work

## Setup

### 1. Download Datasets

```bash
# Download ScienceQA (filtered for hard science questions)
python get_scienceqa.py

# Download ChemBench
python get_chembench.py
```

### 2. Run Models on Science Datasets

Use the specialized science dataset runner:

```bash
# Example: Run R1 on ScienceQA chemistry questions
python custom_model_run_science.py \
  --model "deepseek/deepseek-r1" \
  --model-display-name "R1" \
  --dataset scienceqa \
  --num_questions 100 \
  --temperature 0.7 \
  --subject-filter "chemistry"

# Example: Run Claude on ChemBench
python custom_model_run_science.py \
  --model "anthropic/claude-3.5-sonnet" \
  --model-display-name "claude35" \
  --dataset chembench \
  --num_questions 50 \
  --temperature 0.3
```

### Parameters:
- `--dataset`: Choose from "scienceqa", "chembench", "gpqa", "mmlu_pro"
- `--subject-filter`: Filter ScienceQA by subject (chemistry, physics, biology)
- `--topic-filter`: Filter ScienceQA by specific topic
- Other parameters same as before

## 3. Grade Results

The multi-dataset autograder handles all science datasets:

```bash
# Grade ScienceQA results
python autograder_custom_multi.py \
  --dir "r1_rollouts/scienceqa_R1_temp_0.7" \
  --model-display-name "R1" \
  --dataset auto

# Grade ChemBench results  
python autograder_custom_multi.py \
  --dir "r1_rollouts/chembench_claude35_temp_0.3" \
  --model-display-name "claude35" \
  --dataset auto
```

## 4. Analyze Results

Use the flexible analyzer for custom models:

```bash
python analyze_scores_flexible.py \
  --file scores/scienceqa_R1_temp_0.7_scores.json \
  --plots
```

## Complete Examples

### Example 1: Chemistry Deep Dive with R1
```bash
# 1. Download ScienceQA if needed
python get_scienceqa.py

# 2. Run R1 on chemistry questions
python custom_model_run_science.py \
  --model "deepseek/deepseek-r1" \
  --model-display-name "R1" \
  --dataset scienceqa \
  --num_questions 100 \
  --temperature 0.7 \
  --subject-filter "chemistry"

# 3. Grade
python autograder_custom_multi.py \
  --dir "r1_rollouts/scienceqa_R1_temp_0.7" \
  --model-display-name "R1"

# 4. Analyze
python analyze_scores_flexible.py \
  --file scores/scienceqa_R1_temp_0.7_scores.json \
  --plots
```

### Example 2: Compare Models on ChemBench
```bash
# Run multiple models
for model in "deepseek/deepseek-r1" "anthropic/claude-3.5-sonnet" "openai/gpt-4-turbo"
do
  python custom_model_run_science.py \
    --model "$model" \
    --model-display-name "${model##*/}" \
    --dataset chembench \
    --num_questions 50 \
    --temperature 0.5
done

# Grade all
for model in "deepseek-r1" "claude-3.5-sonnet" "gpt-4-turbo"
do
  python autograder_custom_multi.py \
    --dir "r1_rollouts/chembench_${model}_temp_0.5" \
    --model-display-name "$model"
done

# Compare results
python analyze_scores_flexible.py --dir scores --pattern "chembench_*_scores.json" --plots
```

## What Makes These Good for Testing

### ScienceQA Strengths:
- **Multi-step reasoning**: Many problems require sequential steps
- **Conceptual depth**: Questions test understanding, not just recall
- **Hints system**: Tests if models can use hints effectively
- **Detailed solutions**: Ground truth includes full explanations

### ChemBench Strengths:
- **Technical complexity**: Includes advanced topics like quantum chemistry
- **Calculation-heavy**: Tests numerical reasoning abilities
- **Mechanism problems**: Requires spatial/sequential reasoning
- **Real-world relevance**: Problems from actual chemistry practice

## Expected Reasoning Patterns

For these datasets, you should see models:
1. **Breaking down problems** into steps
2. **Applying formulas** and principles
3. **Showing calculations** (especially ChemBench)
4. **Explaining chemical mechanisms** step-by-step
5. **Using given hints** effectively (ScienceQA)
6. **Checking answers** through alternative methods

## Tips for Best Results

1. **Temperature Settings**: 
   - ScienceQA: 0.5-0.7 (balance creativity with accuracy)
   - ChemBench: 0.3-0.5 (more deterministic for calculations)

2. **Filtering Options**:
   ```bash
   # Focus on specific topics
   --subject-filter "physics" --topic-filter "quantum"
   ```

3. **Sample Sizes**: Start with 50-100 questions to test, these can be computationally intensive

4. **Model Selection**: Frontier models (R1, GPT-4, Claude) shine on these datasets due to complexity

## Interpreting Results

- **High Illegibility + Correct**: Model is "thinking hard" but getting it right
- **Low Illegibility + Incorrect**: Model is confidently wrong (concerning!)
- **Chemistry vs Physics**: Models may show different patterns across subjects
- **Hint Usage**: Check if models that use hints perform better

## Dataset Statistics

After downloading, you'll see:
- **ScienceQA Hard**: ~500-1000 filtered questions (from 21k total)
- **ChemBench**: Varies, but typically 1000+ chemistry problems

Both datasets avoid saturation even with frontier models due to their complexity.