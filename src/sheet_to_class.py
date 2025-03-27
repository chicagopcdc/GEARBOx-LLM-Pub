import os
import pandas as pd
from response_model import generate_class_fields_and_enums
from text_util import export_class_to_file

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
CREDENTIAL_PATH = "../credentials.json"

creds = None
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


# generate_entity_class("Entity_IC.py", class_definition_ic)
# generate_entity_class("Entity_EC.py", class_definition_ec)
def generate_entity_class(gearbox_df:pd.DataFrame):
# Generate class fields from the DataFrame
    class_fields_ic, enum_classes = generate_class_fields_and_enums(gearbox_df, "included")
    class_fields_ec, _ = generate_class_fields_and_enums(gearbox_df, "excluded")

    class_definition = "from enum import Enum\nfrom pydantic import BaseModel, Field\nfrom typing import Optional, List\n\n"
    for enum_name, enum_definition in enum_classes.items():
        class_definition += f"{enum_definition}\n"

    # Generating the ic class as a string
    class_definition_ic = class_definition + "class Entity(BaseModel):\n"
    for field_name, field_definition in class_fields_ic.items():
        class_definition_ic += f"    {field_name}: {field_definition}\n"

    # Generating the ec class as a string
    class_definition_ec = class_definition + "class Entity(BaseModel):\n"
    for field_name, field_definition in class_fields_ec.items():
        class_definition_ec += f"    {field_name}: {field_definition}\n"

    return class_definition_ic, class_definition_ec

def main():
    google_spreadsheet_id = os.environ.get('GOOGLE_SPREADSHEET_ID')
    google_range_name = os.environ.get('GOOGLE_RANGE_NAME')
    class_output_path = os.environ.get('CLASS_OUTPUT_PATH')
    output_ic_path = os.environ.get('OUTPUT_IC_PATH')
    output_ec_path = os.environ.get('OUTPUT_EC_PATH')

    print("Generating entity classes from Google Sheet")
    print("Google spreadsheet ID:", google_spreadsheet_id)
    print("Google sheet range:", google_range_name)
    print("Entity classes:", output_ic_path, output_ec_path)

    gearbox_df = read_google_sheet(google_spreadsheet_id, google_range_name)
    class_definition_ic, class_definition_ec = generate_entity_class(gearbox_df)

    # Save the class definition to a file
    export_class_to_file(class_output_path+output_ic_path, class_definition_ic)
    export_class_to_file(class_output_path+output_ec_path, class_definition_ec)

    print("Entity classes saved to file")

if __name__ == "__main__":
    main()
