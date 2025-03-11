#!/bin/bash

# Create scores directory if it doesn't exist
mkdir -p scores

# Find all subdirectories in r1_rollouts
for dir in r1_rollouts/*/; do
    # Extract directory name without path
    dir_name=$(basename "$dir")
    
    # Check if a score file already exists for this directory
    score_file="scores/${dir_name}_legibility_scores.json"
    
    if [ ! -f "$score_file" ]; then
        echo "Processing directory: $dir"
        echo "Score file will be: $score_file"
        
        # Run the autograder on this directory
        python autograder.py --dir "$dir" --output "$score_file"
        
        # Optional: add a delay between processing directories
        echo "Completed processing $dir. Waiting 5 seconds before next directory..."
        sleep 5
    else
        echo "Skipping $dir (already scored)"
    fi
done

echo "All unscored directories have been processed."