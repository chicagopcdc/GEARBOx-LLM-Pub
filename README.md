# GEARBOx LLM

## Prerequisites

- Create `.env` file on the root directory used for accessing Azure OpenAI service

```bash
export AZURE_OPENAI_API_KEY="[YOUR_API_KEY_VALUE]"
export AZURE_OPENAI_API_BASE="[YOUR_AZURE_API_BASE_ADDRESS]"
export AZURE_OPENAI_API_TYPE="azure"
export AZURE_OPENAI_API_DEPLOYMENT="gpt-4o"
export AZURE_OPENAI_API_MODEL="gpt-4o"
export AZURE_OPENAI_API_VERSION="2024-05-01-preview"
```

- `source .env` to load environmental variables on your local system
- Python libraries required for the GEARBOx LLM task are listed in `[requirements.txt](./requirements.txt)`
- `openai`, `instructor`, and `pydantic` are core libraries.
- Google Sheets API

## Access Google Sheet with Sheets API

- Enable Google Sheets API: A simple code for creating user's access and refresh tokens is in [google_drive_quickstart.py](google_drive_quickstart.py). Once you execute [google_drive_quickstart.py](google_drive_quickstart.py), a browser window will popup to signin to your google profile. `credentials.json` and `token.json` will be created after successfully login to Google. The file `token.json` stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.

See reference: [Google Sheets API Overview](https://developers.google.com/sheets/api/reference/rest)

## Generate Entity Classes based on GEARBOx knowledge base in Google Sheet

- Update variables in `generate_entity_classes.sh`

```bash
export GOOGLE_SPREADSHEET_ID="1hpPyjNbRXZFSSo6YwOYaDEZRhE43SROI6A6fs3rgoXc"
export GOOGLE_RANGE_NAME="'GEARBOx v5 - Complex - Revised'!A1:I113"
export CLASS_OUTPUT_PATH="src/"
export OUTPUT_IC_PATH="Entity_IC.py"
export OUTPUT_EC_PATH="Entity_EC.py"
```

- `[generate_entity_classes.sh](./generate_entity_classes.sh)` 1. Read Google spreadsheet using Sheets API, 2. generate response models for LLM task extracting inclusion criteria (`./src/Entity_IC.py`) and exclusion criteria (`./src/Entity_EC.py`).

## Execute GEARBOx LLM

- `Entity_IC.py` and `Entity_EC.py` should be generated using `[generate_entity_classes.sh](./generate_entity_classes.sh)` before executing GEARBOx LLM.
- Update variables in `[run_gearbox_llm.sh](./run_gearbox_llm.sh)`. The input/output path will be changed to cloud storage (TBD).
- `GOOGLE_SPREADSHEET_ID` and `GOOGLE_RANGE_NAME` are used in dynamic generation of entity classes on runtime.

```bash
export GOOGLE_SPREADSHEET_ID="1hpPyjNbRXZFSSo6YwOYaDEZRhE43SROI6A6fs3rgoXc"
export GOOGLE_RANGE_NAME="'GEARBOx v5 - Complex - Revised'!A1:I113"
export INPUT_DATA_PATH="input/"
export OUTPUT_DATA_PATH="output/"
# Chunk size of LLM processing
export CHUNK_SIZE=2
```
