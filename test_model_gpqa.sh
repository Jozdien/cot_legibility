#!/bin/bash

# Test any model on GPQA dataset
# Usage: ./test_model_gpqa.sh <model_id> <display_name> [num_questions]
# Note: display_name can contain hyphens, they'll be preserved in directory names

MODEL=${1:-"anthropic/claude-3.5-sonnet"}
MODEL_NAME=${2:-"claude35"}
NUM_QUESTIONS=${3:-50}
TEMPERATURE="1.0"

echo "Testing $MODEL ($MODEL_NAME) on $NUM_QUESTIONS GPQA questions..."

# 1. Run the model
echo -e "\n1. Running model..."
python custom_model_run.py \
  --model "$MODEL" \
  --model-display-name "$MODEL_NAME" \
  --num_questions $NUM_QUESTIONS \
  --temperature $TEMPERATURE \
  --max_workers 10

# 2. Check output
OUTPUT_DIR="r1_rollouts/${MODEL_NAME}_temp_${TEMPERATURE}"
echo "Looking for output directory: $OUTPUT_DIR"
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Error: Output directory not created!"
    echo "Available directories:"
    ls -la r1_rollouts | grep "$MODEL_NAME"
    exit 1
fi

echo -e "\n2. Running autograder..."
python autograder_custom.py \
  --dir "$OUTPUT_DIR" \
  --model-display-name "$MODEL_NAME" \
  --workers 5

# 3. Analyze results
SCORES_FILE="scores/${MODEL_NAME}_temp_${TEMPERATURE}_scores.json"
echo -e "\n3. Analyzing results..."
python analyze_scores_flexible.py \
  --file "$SCORES_FILE" \
  --plots

echo -e "\nComplete! Results:"
echo "- Rollouts: $OUTPUT_DIR"
echo "- Scores: $SCORES_FILE"
echo "- Plots: plots/all/${MODEL_NAME}_temp_${TEMPERATURE}_*.png"