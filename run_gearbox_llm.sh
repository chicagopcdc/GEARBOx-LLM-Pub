#!/usr/bin/env bash
# ./run_gearbox_llm.sh

export GOOGLE_SPREADSHEET_ID="1hpPyjNbRXZFSSo6YwOYaDEZRhE43SROI6A6fs3rgoXc"
export GOOGLE_RANGE_NAME="'GEARBOx v5 - Complex - Revised'!A1:I113"
export INPUT_DATA_PATH="input/"
export OUTPUT_DATA_PATH="output/"

# CFG Parser Config
CMD="./src/extract_w_instructor.py"

# Run CFG Parser
if ! python $CMD
then
  # rm -f "$OUTFILE"
  echo "Failed to run GEARBOx LLM."
  exit 1
fi
