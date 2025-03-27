#!/usr/bin/env bash
# ./generate_pydantic_classes.sh

export GOOGLE_SPREADSHEET_ID="1hpPyjNbRXZFSSo6YwOYaDEZRhE43SROI6A6fs3rgoXc"
export GOOGLE_RANGE_NAME="'GEARBOx v5 - Complex - Revised'!A1:I113"
export CLASS_OUTPUT_PATH="src/"
export OUTPUT_IC_PATH="Entity_IC.py"
export OUTPUT_EC_PATH="Entity_EC.py"

# CFG Parser Config
CMD="./src/sheet_to_class.py"

# Run CFG Parser
if ! python $CMD
then
  rm -f "$OUTFILE"
  echo "Failed to generate Entity Classes."
  exit 1
fi
