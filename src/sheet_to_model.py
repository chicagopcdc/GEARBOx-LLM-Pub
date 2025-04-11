import os
import pandas as pd
from exec_response_model import generate_class_fields_and_enums
from text_util import export_response_model_to_file
from itertools import islice

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
CREDENTIAL_PATH = "../credentials.json"

creds = None
# Only perform Google Sheets authentication if the data source is 'google_sheet'
if os.environ.get('DATA_SOURCE') == 'google_sheet':
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIAL_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

def read_google_sheet(sheet_id: str, sheet_range: str) -> pd.DataFrame:
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    values = result.get("values", [])
    return pd.DataFrame(values[1:], columns=values[0])

def read_excel_file(file_path: str, sheet_name: str) -> pd.DataFrame:
    """
    Reads data from a local Excel file and returns it as a pandas DataFrame.
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)

# generate_entity_class("Entity_IC.py", class_definition_ic)
# generate_entity_class("Entity_EC.py", class_definition_ec)

# Helper function to get dictionary chunks of size 2
def dict_chunk(dictionary:dict, size:int = 2):
    iterator = iter(dictionary.items())
    for chunk in iter(lambda: list(islice(iterator, size)), []):
        yield chunk

def generate_entity_class(gearbox_df:pd.DataFrame, chunk_size:int=2) -> str:
# Generate class fields from the DataFrame
    class_fields_ic, enum_classes = generate_class_fields_and_enums(gearbox_df, "included")
    class_fields_ec, _ = generate_class_fields_and_enums(gearbox_df, "excluded")

    class_definition = (
        "from enum import Enum\n"
        "from pydantic import BaseModel, Field, model_validator, ValidationInfo\n"
        "from typing import Optional, List\n"
        "import re\n\n"
    )

    # Define the Fact class
    class_definition += (
        "class Fact(BaseModel):\n"
        "    fact: str = Field(...)\n"
        "    substring_quote: List[str] = Field(...)\n\n"
        "    @model_validator(mode=\"after\")\n"
        "    def validate_sources(self, info: ValidationInfo) -> \"Fact\":\n"
        "        text_chunks = info.context.get(\"text_chunk\", None)\n"
        "        spans = list(self.get_spans(text_chunks))\n"
        "        self.substring_quote = [text_chunks[span[0] : span[1]] for span in spans]\n"
        "        return self\n\n"
        "    def get_spans(self, context):\n"
        "        for quote in self.substring_quote:\n"
        "            yield from self._get_span(quote, context)\n\n"
        "    def _get_span(self, quote, context):\n"
        "        for match in re.finditer(re.escape(quote), context):\n"
        "            yield match.span()\n\n"
    )

    for enum_name, enum_definition in enum_classes.items():
        class_definition += f"{enum_definition}\n"

    # Generating the ic class as a string
    class_definition_ic = class_definition
    for i, chunk in enumerate(dict_chunk(class_fields_ic, size=chunk_size)):
        class_definition_ic += f"class Entity{i}(BaseModel):\n"    
        for field_name, field_definition in chunk:
            class_definition_ic += f"    {field_name}: {field_definition}\n"
        class_definition_ic += f"    answer_facts: List[Fact] = Field(..., description=\"Exact fact quotes from the note supporting the answer.\")\n"

    # Generating the ec class as a string
    class_definition_ec = class_definition
    for i, chunk in enumerate(dict_chunk(class_fields_ec, size=chunk_size)):
        class_definition_ec += f"class Entity{i}(BaseModel):\n"
        for field_name, field_definition in chunk:
            class_definition_ec += f"    {field_name}: {field_definition}\n"
        class_definition_ec += f"    answer_facts: List[Fact] = Field(..., description=\"Exact fact quotes from the note supporting the answer.\")\n"


    return class_definition_ic, class_definition_ec

def main():
    # Determine the data source (Google Sheet or local Excel file)
    data_source = os.environ.get('DATA_SOURCE', 'google_sheet')  # Default to Google Sheet
    response_model_output_path = os.environ.get('RESPONSE_MODEL_OUTPUT_PATH')
    output_ic_path = os.environ.get('OUTPUT_IC_PATH')
    output_ec_path = os.environ.get('OUTPUT_EC_PATH')

    if data_source == 'google_sheet':
        google_spreadsheet_id = os.environ.get('GOOGLE_SPREADSHEET_ID')
        google_range_name = os.environ.get('GOOGLE_RANGE_NAME')

        print("Generating entity classes from Google Sheet")
        print("Google spreadsheet ID:", google_spreadsheet_id)
        print("Google sheet range:", google_range_name)

        gearbox_df = read_google_sheet(google_spreadsheet_id, google_range_name)

    elif data_source == 'local_file':
        excel_file_path = os.environ.get('EXCEL_FILE_PATH')
        excel_sheet_name = os.environ.get('EXCEL_SHEET_NAME')

        print("Generating entity classes from local Excel file")
        print("Excel file path:", excel_file_path)
        print("Excel sheet name:", excel_sheet_name)

        gearbox_df = read_excel_file(excel_file_path, excel_sheet_name)

    else:
        print("Invalid data source. Please set DATA_SOURCE to 'google_sheet' or 'local_file'.")
        return

    # Generate entity classes
    class_definition_ic, class_definition_ec = generate_entity_class(gearbox_df)

    # Save the class definitions to files
    export_response_model_to_file(response_model_output_path + output_ic_path, class_definition_ic)
    export_response_model_to_file(response_model_output_path + output_ec_path, class_definition_ec)

    print("Entity classes saved to file")

if __name__ == "__main__":
    main()
