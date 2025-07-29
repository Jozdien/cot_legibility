#!/bin/bash

# Test script for science dataset integration
# Tests ScienceQA and ChemBench with 2 questions each

echo "Testing science dataset integration..."

# Configuration
MODEL="deepseek/deepseek-r1"
MODEL_NAME="R1"
NUM_QUESTIONS=2

echo "=== Testing ScienceQA ==="

echo "1. Downloading ScienceQA dataset (if needed)..."
if [ ! -d "data/scienceqa_hard" ]; then
    python get_scienceqa.py
else
    echo "✓ ScienceQA dataset already exists"
fi

echo -e "\n2. Running $MODEL on $NUM_QUESTIONS ScienceQA chemistry questions..."
python custom_model_run_science.py \
  --model "$MODEL" \
  --model-display-name "$MODEL_NAME" \
  --dataset scienceqa \
  --num_questions $NUM_QUESTIONS \
  --temperature 0.7 \
  --subject-filter "chemistry" \
  --max_workers 2

echo -e "\n3. Checking ScienceQA output..."
SCIENCEQA_DIR="r1_rollouts/scienceqa_${MODEL_NAME}_temp_0.7"
if [ -d "$SCIENCEQA_DIR" ]; then
    echo "✓ Output directory created: $SCIENCEQA_DIR"
    echo "Files created:"
    ls -la "$SCIENCEQA_DIR" | head -5
else
    echo "✗ ScienceQA output directory not found!"
fi

echo -e "\n4. Running autograder on ScienceQA results..."
python autograder_custom_multi.py \
  --dir "$SCIENCEQA_DIR" \
  --model-display-name "$MODEL_NAME" \
  --dataset auto \
  --workers 2

echo -e "\n=== Testing ChemBench ==="

echo -e "\n5. Downloading ChemBench dataset (if needed)..."
if [ ! -d "data/chembench" ]; then
    python get_chembench.py
else
    echo "✓ ChemBench dataset already exists"
fi

echo -e "\n6. Running $MODEL on $NUM_QUESTIONS ChemBench questions..."
python custom_model_run_science.py \
  --model "$MODEL" \
  --model-display-name "$MODEL_NAME" \
  --dataset chembench \
  --num_questions $NUM_QUESTIONS \
  --temperature 0.5 \
  --max_workers 2

echo -e "\n7. Checking ChemBench output..."
CHEMBENCH_DIR="r1_rollouts/chembench_${MODEL_NAME}_temp_0.5"
if [ -d "$CHEMBENCH_DIR" ]; then
    echo "✓ Output directory created: $CHEMBENCH_DIR"
    echo "Files created:"
    ls -la "$CHEMBENCH_DIR" | head -5
else
    echo "✗ ChemBench output directory not found!"
fi

echo -e "\n8. Running autograder on ChemBench results..."
python autograder_custom_multi.py \
  --dir "$CHEMBENCH_DIR" \
  --model-display-name "$MODEL_NAME" \
  --dataset auto \
  --workers 2

echo -e "\n9. Checking generated score files..."
SCIENCEQA_SCORES="scores/scienceqa_${MODEL_NAME}_temp_0.7_scores.json"
CHEMBENCH_SCORES="scores/chembench_${MODEL_NAME}_temp_0.5_scores.json"

if [ -f "$SCIENCEQA_SCORES" ]; then
    echo "✓ ScienceQA scores created: $SCIENCEQA_SCORES"
    echo "Preview:"
    python -c "import json; data=json.load(open('$SCIENCEQA_SCORES')); print(f'Total questions: {len(data)}'); print(f'First result: {data[0] if data else None}')" | head -20
else
    echo "✗ ScienceQA scores not found!"
fi

if [ -f "$CHEMBENCH_SCORES" ]; then
    echo -e "\n✓ ChemBench scores created: $CHEMBENCH_SCORES"
    echo "Preview:"
    python -c "import json; data=json.load(open('$CHEMBENCH_SCORES')); print(f'Total questions: {len(data)}'); print(f'First result: {data[0] if data else None}')" | head -20
else
    echo "✗ ChemBench scores not found!"
fi

echo -e "\n10. Testing plot generation..."
if [ -f "$SCIENCEQA_SCORES" ]; then
    python analyze_scores_flexible.py --file "$SCIENCEQA_SCORES" --plots
    echo "Check plots/all/ for ScienceQA plots"
fi

echo -e "\nTest complete! Science dataset pipelines are working if you see scores and plots above."