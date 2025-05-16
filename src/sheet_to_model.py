import os
import pandas as pd
import re
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

# Function to generate class fields and enums
def generate_class_fields_and_enums(df, verb):
    fields = {}
    enum_classes = {}  # Dictionary to store generated enum classes as strings
    docstring = []

    for _, row in df.iterrows():
        param_name = row['Parameter Name']
        param_name_exist = f"{param_name}_exist"

        # Determine the field type based on 'Type' and 'Enum' columns
        if row['Type'] in ['integer', 'number']:
            field_type = 'Optional[int]'
        elif pd.notna(row['Enum']) and 'Yes' in row['Enum']:
            field_type = 'Optional[YesNo]'  # Assuming YesOrNo is a defined type elsewhere
        elif pd.notna(row['Enum']):
            field_type = f"Optional[List[{param_name.capitalize()}]]"
            
            # Create an enum class for this parameter
            enum_items = [item.strip().strip('"') for item in row['Enum'].split(',')]
            enum_class_str = f"class {param_name.capitalize()}(Enum):\n"
            for item in enum_items:
                if "(" in item and ")" in item:
                    enum_name = re.search(r"\((.*?)\)", item).group(1)
                    enum_name = enum_name.strip().replace(" ", "")
                    enum_name = enum_name.strip().replace("-", "").upper()
                else:
                    enum_name = item.strip().replace("-", "").replace(" ", "").upper()
                enum_class_str += f"    {enum_name} = \"{item}\"\n"
            
            enum_classes[param_name.capitalize()] = enum_class_str
            
        else:
            field_type = 'Optional[str]'

        # 
        description = row['Description']
        example = row['Examples']
        if pd.notna(example) and example.strip():
            example_str = f"    Extracted from the clinical trial eligibility document.\nExample: {example}"
        else:
            example_str = "    Extracted from the clinical trial eligibility document."
        docstring.append(f"    \'\'\'\n{example_str}\n    \'\'\'\n")
            
        parts = description.split('?')
        first_yesno = parts[0] + '?'
        second_criteria = parts[1].strip().replace("{verb}", verb) + '? '
        if len(parts) > 2:
            second_criteria = second_criteria + parts[2].replace('"', '\\"')
        
        fields[param_name_exist] = f"YesNo = Field(..., description=\"{first_yesno}\")"
        fields[param_name] = f"{field_type} = Field(\n        None, \n        description=\"{second_criteria}\")"
    
    enum_items = ["Yes","No"]
    enum_class_str = f"class YesNo(Enum):\n"
    for item in enum_items:
        enum_name = item.upper()
        enum_class_str += f"    {enum_name} = \"{item}\"\n"
    enum_classes["YesNo"] = enum_class_str

    return fields, enum_classes, docstring


# Helper function to get dictionary chunks of size 2
def dict_chunk(dictionary:dict, size:int = 2):
    iterator = iter(dictionary.items())
    for chunk in iter(lambda: list(islice(iterator, size)), []):
        yield chunk

# Function to generate the response model class
IMPORT_MODULE = """
from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationInfo, validator
from typing import Optional, List
import re
"""

FACT = """
class Fact(BaseModel):
    fact: str = Field(...)
    substring_quote: List[str] = Field(...)

    @model_validator(mode="after")
    def validate_sources(self, info: ValidationInfo) -> "Fact":
        text_chunks = info.context.get("text_chunk", None)
        spans = list(self.get_spans(text_chunks))
        self.substring_quote = [text_chunks[span[0] : span[1]] for span in spans]
        return self

    def get_spans(self, context):
        for quote in self.substring_quote:
            yield from self._get_span(quote, context)

    def _get_span(self, quote, context):
        for match in re.finditer(re.escape(quote), context):
            yield match.span()

"""

CONDITION_VALIDATOR = """
    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity{i}":
        if getattr(self, "{exist_field}") == YesNo.NO:
            if getattr(self, "{value_field}") is not None:
                raise ValueError("{value_field} must be None if {exist_field} is 'NO'")
            setattr(self, "{value_field}", None)
            self.answer_facts = []
        return self
"""

SOURCE_VALIDATOR = """  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity{i}":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

"""

def generate_entity_class(gearbox_df:pd.DataFrame, chunk_size:int=2) -> str:
# Generate class fields from the DataFrame
    class_fields_ic, enum_classes, docstring = generate_class_fields_and_enums(gearbox_df, "included")
    class_fields_ec, _, _ = generate_class_fields_and_enums(gearbox_df, "excluded")

    class_definition = IMPORT_MODULE
    class_definition += FACT
    
    for enum_name, enum_definition in enum_classes.items():
        class_definition += f"{enum_definition}\n"

    # Generating the ic class as a string
    class_definition_ic = class_definition
    for i, chunk in enumerate(dict_chunk(class_fields_ic, size=chunk_size)):
        class_definition_ic += f"class Entity{i}(BaseModel):\n"
        class_definition_ic += docstring[i]
        name_list = []
        for field_name, field_definition in chunk:
            class_definition_ic += f"    {field_name}: {field_definition}\n"
            name_list.append(field_name)
        class_definition_ic += f"    answer_facts: List[Fact] = Field(..., description=\"Exact fact quotes from the note supporting the answer.\")\n"
        class_definition_ic += CONDITION_VALIDATOR.format(
            i=i,
            exist_field=name_list[0],
            value_field=name_list[1],
        )
        class_definition_ic += SOURCE_VALIDATOR.format(i=i)

    # Generating the ec class as a string
    class_definition_ec = class_definition
    for i, chunk in enumerate(dict_chunk(class_fields_ec, size=chunk_size)):
        class_definition_ec += f"class Entity{i}(BaseModel):\n"
        class_definition_ec += docstring[i]
        name_list = []
        for field_name, field_definition in chunk:
            class_definition_ec += f"    {field_name}: {field_definition}\n"
            name_list.append(field_name)
        class_definition_ec += f"    answer_facts: List[Fact] = Field(..., description=\"Exact fact quotes from the note supporting the answer.\")\n"
        class_definition_ec += CONDITION_VALIDATOR.format(
            i=i,
            exist_field=name_list[0],
            value_field=name_list[1],
        )        
        class_definition_ec += SOURCE_VALIDATOR.format(i=i)
        
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
