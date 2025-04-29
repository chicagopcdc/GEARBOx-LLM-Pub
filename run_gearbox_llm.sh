#!/usr/bin/env bash
# ./run_gearbox_llm.sh

export DATA_SOURCE="local file" # "google_sheet"

export GOOGLE_SPREADSHEET_ID="1hpPyjNbRXZFSSo6YwOYaDEZRhE43SROI6A6fs3rgoXc"
export GOOGLE_RANGE_NAME="'GEARBOx v5'!A1:F113"

export EXCEL_FILE_PATH="GEARBOx Ontology for LLM_In use.xlsx"
export EXCEL_SHEET_NAME="GEARBOx v4"

export INPUT_DATA_PATH="input/"
export OUTPUT_DATA_PATH="output/"
export CHUNK_SIZE=2

# CFG Parser Config
CMD="./src/extract_w_instructor.py"

# Run CFG Parser
if ! python $CMD
then
  # rm -f "$OUTFILE"
  echo "Failed to run GEARBOx LLM."
  exit 1
fi
