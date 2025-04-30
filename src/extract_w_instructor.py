import os
from dotenv import load_dotenv

import instructor
import pandas as pd
from text_util import read_abstracts, clean_text
from exec_response_model import exec
from sheet_to_model import read_google_sheet, read_excel_file
from openai import AzureOpenAI
from functools import partial
from datetime import datetime
from enum import Enum
import json
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

def initiate_llm():
    api_version = os.environ.get('AZURE_OPENAI_API_VERSION')
    api_key = os.environ.get('AZURE_OPENAI_API_KEY')
    endpoint = os.environ.get('AZURE_OPENAI_API_ENDPOINT')
    engine = os.environ.get('AZURE_OPENAI_API_ENGINE')
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

def multi_run(item, in_client, n_repeats):
    file_name, inclusion_criteria, exclusion_criteria = item

    clean_text_ic = clean_text(inclusion_criteria)
    clean_text_ec = clean_text(exclusion_criteria)

    ic_results = []
    ec_results = []

    for run in range(int(n_repeats)):
        print(f"Process run {run+1}")
        output_IC = exec(clean_text_ic, 'Inclusion', in_client)
        output_EC = exec(clean_text_ec, 'Exclusion', in_client)
        output_IC_list = [r.dict() for r in output_IC]
        output_EC_list = [r.dict() for r in output_EC]
        ic_results.extend(output_IC_list)  # Flatten results
        ec_results.extend(output_EC_list)  # Flatten results

        # Save output_IC_list to JSON
        json_file_path = f"{file_name}_IC_run_{run+1}.json"
        with open(json_file_path, "w") as json_file:
            json.dump(output_IC_list, json_file, indent=4)

    return ic_results, ec_results

def filename_wo_extension(file_path):
    """Prints the filename without the directory and extension."""
    file_name_with_extension = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(file_name_with_extension)
    return file_name

def export_results(ic_results, ec_results, file_name, output_dir):
    df = pd.DataFrame(ic_results + ec_results)
    output_dir = output_dir.rstrip(os.path.sep)
    os.makedirs(os.path.basename(output_dir), exist_ok=True)

    output_excel_path = f'{output_dir}{os.path.sep}{file_name}_output_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    df.to_excel(output_excel_path, index=False)

def main():
    in_client = initiate_llm()

    # Set input/output directories
    INPUT_DIR_NAME = os.environ.get('INPUT_DATA_PATH')
    OUTPUT_DIR_NAME = os.environ.get('OUTPUT_DATA_PATH')

    abstract_list = read_abstracts(INPUT_DIR_NAME)

    for item in tqdm(abstract_list, desc="Processing abstracts"):
        starttime = datetime.now()

        print("----------------------------------------")
        print("Processing file:", filename_wo_extension(item[0]))
        print("Process started:", starttime.strftime("%Y-%m-%d %H:%M:%S"))

        df_final = multi_run(item, in_client, n_repeats=1)

        export_results(df_final, filename_wo_extension(item[0]), OUTPUT_DIR_NAME)

        endtime = datetime.now()
        time_elapsed = endtime - starttime
        print(f'Processing time for file: {filename_wo_extension(item[0])} {time_elapsed.strftime("%Y-%m-%d %H:%M:%S")}')

if __name__ == "__main__":
    main()
