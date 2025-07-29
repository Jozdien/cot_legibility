#!/bin/bash

# Test script for MMLU-Pro integration
# This tests with just 2 questions to verify the pipeline works

echo "Testing MMLU-Pro integration..."

# Test with a small model
MODEL="mistralai/mixtral-8x7b-instruct"
MODEL_NAME="mixtral"
NUM_QUESTIONS=2

echo "1. Downloading MMLU-Pro dataset (if needed)..."
if [ ! -d "data/mmlu_pro" ]; then
    python get_mmlu_pro.py
else
    echo "✓ MMLU-Pro dataset already exists"
fi

echo -e "\n2. Running $MODEL on $NUM_QUESTIONS MMLU-Pro questions..."
python custom_model_run_multi_dataset.py \
  --model "$MODEL" \
  --model-display-name "$MODEL_NAME" \
  --dataset mmlu_pro \
  --num_questions $NUM_QUESTIONS \
  --temperature 0.3 \
  --max_workers 2

echo -e "\n3. Checking if output files were created..."
OUTPUT_DIR="r1_rollouts/mmlu_pro_${MODEL_NAME}_temp_0.3"
if [ -d "$OUTPUT_DIR" ]; then
    echo "✓ Output directory created: $OUTPUT_DIR"
    echo "Files created:"
    ls -la "$OUTPUT_DIR" | head -5
else
    echo "✗ Output directory not found!"
    exit 1
fi

echo -e "\n4. Running autograder on MMLU-Pro results..."
python autograder_custom_multi.py \
  --dir "$OUTPUT_DIR" \
  --model-display-name "$MODEL_NAME" \
  --dataset auto \
  --workers 2

echo -e "\n5. Checking if scores and answers were generated..."
SCORES_FILE="scores/mmlu_pro_${MODEL_NAME}_temp_0.3_scores.json"
ANSWERS_FILE="answers/mmlu_pro_${MODEL_NAME}_temp_0.3_answers.md"

if [ -f "$SCORES_FILE" ]; then
    echo "✓ Scores file created: $SCORES_FILE"
    echo "First result:"
    python -c "import json; print(json.dumps(json.load(open('$SCORES_FILE'))[0], indent=2))" | head -50
else
    echo "✗ Scores file not found!"
fi

if [ -f "$ANSWERS_FILE" ]; then
    echo -e "\n✓ Answers file created: $ANSWERS_FILE"
    echo "First few lines:"
    head -30 "$ANSWERS_FILE"
else
    echo "✗ Answers file not found!"
fi

echo -e "\nTest complete! The MMLU-Pro pipeline is working correctly if you see scores and answers above."