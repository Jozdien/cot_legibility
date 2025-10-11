#!/bin/bash
set -e

if [ $# -lt 1 ]; then
    echo "Usage: ./run.sh <config_path>"
    echo ""
    echo "Examples:"
    echo "  ./run.sh config/default.yaml"
    echo "  ./run.sh config/quick_test.yaml"
    echo "  ./run.sh config/examples/analysis_only.yaml"
    exit 1
fi

CONFIG_PATH="$1"

if [ ! -f "$CONFIG_PATH" ]; then
    echo "Error: Config file not found: $CONFIG_PATH"
    exit 1
fi

echo "Running pipeline with config: $CONFIG_PATH"
echo ""

python -m src.main "$CONFIG_PATH"
