#!/usr/bin/env bash
# ./generate_pydantic_classes.sh

# export DATA_SOURCE="google_sheet"
export DATA_SOURCE="local_file"

export GOOGLE_SPREADSHEET_ID="1hpPyjNbRXZFSSo6YwOYaDEZRhE43SROI6A6fs3rgoXc"
export GOOGLE_RANGE_NAME="'GEARBOx v5'!A1:F113"

export EXCEL_FILE_PATH="GEARBOx Ontology for LLM.xlsx"
export EXCEL_SHEET_NAME="GEARBOx v5"
# export EXCEL_SHEET_NAME="Test"

export RESPONSE_MODEL_OUTPUT_PATH="src/"
export OUTPUT_IC_PATH="Response_Model_IC.py"
export OUTPUT_EC_PATH="Response_Model_EC.py"

# CFG Parser Configß
CMD="./src/sheet_to_model.py"

# Run CFG Parser
if ! python $CMD
then
  rm -f "$OUTFILE"
  echo "Failed to generate Entity Classes."
  exit 1
fi