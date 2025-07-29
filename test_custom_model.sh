#!/bin/bash

# Test script for custom model integration
# This tests with just 2 questions to verify the pipeline works

echo "Testing custom model integration..."

# Test with a small model (you can change this to any model available on OpenRouter)
MODEL="deepseek/deepseek-r1-distill-llama-70b"
MODEL_NAME="r1-distill-llama-70b"
NUM_QUESTIONS=2

echo "1. Running $MODEL on $NUM_QUESTIONS questions..."
python custom_model_run.py \
  --model "$MODEL" \
  --model-display-name "$MODEL_NAME" \
  --num_questions $NUM_QUESTIONS \
  --temperature 0.7 \
  --max_workers 2

echo -e "\n2. Checking if output files were created..."
OUTPUT_DIR="r1_rollouts/${MODEL_NAME}_temp_0.7"
if [ -d "$OUTPUT_DIR" ]; then
    echo "✓ Output directory created: $OUTPUT_DIR"
    echo "Files created:"
    ls -la "$OUTPUT_DIR" | head -5
else
    echo "✗ Output directory not found!"
    exit 1
fi

echo -e "\n3. Running autograder..."
python autograder_custom.py \
  --dir "$OUTPUT_DIR" \
  --model-display-name "$MODEL_NAME" \
  --workers 2

echo -e "\n4. Checking if scores and answers were generated..."
SCORES_FILE="scores/${MODEL_NAME}_temp_0.7_scores.json"
ANSWERS_FILE="answers/${MODEL_NAME}_temp_0.7_answers.md"

if [ -f "$SCORES_FILE" ]; then
    echo "✓ Scores file created: $SCORES_FILE"
    echo "First few lines:"
    head -10 "$SCORES_FILE"
else
    echo "✗ Scores file not found!"
fi

if [ -f "$ANSWERS_FILE" ]; then
    echo -e "\n✓ Answers file created: $ANSWERS_FILE"
    echo "First few lines:"
    head -20 "$ANSWERS_FILE"
else
    echo "✗ Answers file not found!"
fi

echo -e "\n5. Testing plot generation (including new model)..."
python analyze_scores.py --dir scores --pattern "*_scores.json" --plots

echo -e "\nTest complete! Check the outputs above for any errors."