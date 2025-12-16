#!/usr/bin/env bash
# ./run_gearbox_llm.sh

# export DATA_SOURCE="local_file" # "google_sheet"

# export GOOGLE_SPREADSHEET_ID="1hpPyjNbRXZFSSo6YwOYaDEZRhE43SROI6A6fs3rgoXc"
# export GOOGLE_RANGE_NAME="'GEARBOx v5'!A1:F113"

# export EXCEL_FILE_PATH="GEARBOx Ontology for LLM.xlsx"
# export EXCEL_SHEET_NAME="GEARBOx v5"

export RESPONSE_MODEL_OUTPUT_PATH="src/"
export OUTPUT_IC_PATH="Response_Model_IC.py"
export OUTPUT_EC_PATH="Response_Model_EC.py"
# export OUTPUT_IC_PATH="Response_Model_IC_test.py"
# export OUTPUT_EC_PATH="Response_Model_EC_test.py"

export INPUT_DATA_PATH="input_test/"
export OUTPUT_DATA_PATH="output/"
export OUTPUT_MULTIRUN_PATH="output/multi_run"

export N_REPEATS=1

# CFG Parser Config
CMD="./src/extract_w_instructor.py"

# Run CFG Parser
if ! python $CMD
then
  # rm -f "$OUTFILE"
  echo "Failed to run GEARBOx LLM."
  exit 1
fi
