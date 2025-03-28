import os
import instructor
import pandas as pd
from text_util import read_abstracts, clean_text
from response_model import generate_class_fields_and_enums, process_chunk_with_dynamic_model
from sheet_to_class import read_google_sheet
from openai import AzureOpenAI
from functools import partial
from datetime import datetime
from enum import Enum

# from Entity_IC import Entity as Entity_IC
# from Entity_EC import Entity as Entity_EC

def initiate_llm():
    api_version = os.environ.get('AZURE_OPENAI_API_VERSION')
    api_key = os.environ.get('AZURE_OPENAI_API_KEY')
    endpoint = os.environ.get('AZURE_OPENAI_API_BASE')
    engine = os.environ.get('AZURE_OPENAI_API_DEPLOYMENT')
    model = os.environ.get('AZURE_OPENAI_API_MODEL')

    if api_key is None:
        raise ValueError("AZURE_OPENAI_API_KEY environment variable is not set.")

    # Create the Azure OpenAI client
    client = AzureOpenAI(
        api_version=api_version,
        api_key=api_key,
        azure_endpoint=endpoint,
        azure_deployment=engine
    )

    # Patch the client with instructor
    client = instructor.patch(client)

    # Optionally, create a partial function with default parameters
    in_client = partial(
        client.chat.completions.create,
        model=model,
        temperature=0,
        max_retries=2  # Retries in case of API issues
    )

    # print(in_client)
    return in_client

def process_criteria(item, class_fields_ic, class_fields_ec, in_client, chunk_size=1):
    file_name, inclusion_criteria, exclusion_criteria = item

    clean_text_ic = clean_text(inclusion_criteria)
    clean_text_ec = clean_text(exclusion_criteria)

    df_IC = process_chunk_with_dynamic_model(clean_text_ic, 'Inclusion', class_fields_ic, in_client, chunk_size)
    df_EC = process_chunk_with_dynamic_model(clean_text_ec, 'Exclusion', class_fields_ec, in_client, chunk_size)

    # Merge the two DataFrames on the 'Entity' column
    df_final = pd.merge(df_IC, df_EC, on='Entity', how='outer', suffixes=('_IC', '_EC'))

    return df_final

def filename_wo_extension(file_path):
    """Prints the filename without the directory and extension."""
    file_name_with_extension = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(file_name_with_extension)
    return file_name

def export_results(df, file_name, output_dir):
    output_dir = output_dir.rstrip(os.path.sep)
    os.makedirs(os.path.basename(output_dir), exist_ok=True)

    output_excel_path = f'{output_dir}{os.path.sep}{file_name}_output_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    df.to_excel(output_excel_path, index=False)

def main():
    # Read GEARBOx knowledge base
    GOOGLE_SPREADSHEET_ID = os.environ.get('GOOGLE_SPREADSHEET_ID')
    GOOGLE_RANGE_NAME = os.environ.get('GOOGLE_RANGE_NAME')
    gearbox_df = read_google_sheet(GOOGLE_SPREADSHEET_ID, GOOGLE_RANGE_NAME)
    CHUNK_SIZE = int(os.environ.get('CHUNK_SIZE', 2))  # Default chunk size is 2 if not set

    # # Generate class fields and enums
    class_fields_ic, enum_classes = generate_class_fields_and_enums(gearbox_df, "included")
    class_fields_ec, _ = generate_class_fields_and_enums(gearbox_df, "excluded")    

    class_enum = ""
    for enum_name, enum_definition in enum_classes.items():
        class_enum += f"{enum_definition}\n"

    exec(class_enum)

    in_client = initiate_llm()

    # Set input/output directories
    INPUT_DIR_NAME = os.environ.get('INPUT_DATA_PATH')
    OUTPUT_DIR_NAME = os.environ.get('OUTPUT_DATA_PATH')

    abstract_list = read_abstracts(INPUT_DIR_NAME)

    for item in abstract_list:
        starttime = datetime.now()

        print("----------------------------------------")
        print("Processing file:", filename_wo_extension(item[0]))
        print("Process started:", starttime.strftime("%Y-%m-%d %H:%M:%S"))

        df_final = process_criteria(item, class_fields_ic, class_fields_ec, in_client, CHUNK_SIZE)

        export_results(df_final, filename_wo_extension(item[0]), OUTPUT_DIR_NAME)

        endtime = datetime.now()
        print("Processing time for file:", filename_wo_extension(item[0]), f"{(endtime - starttime).strftime("%Y-%m-%d %H:%M:%S")}")

if __name__ == "__main__":
    main()
