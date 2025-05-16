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
from collections import defaultdict, Counter

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

def filename_wo_extension(file_path):
    """Prints the filename without the directory and extension."""
    file_name_with_extension = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(file_name_with_extension)
    return file_name

N_REPEATS = int(os.environ.get('N_REPEATS', 1))

def multi_run(item, in_client):
    file_name, inclusion_criteria, exclusion_criteria = item
    file_name = filename_wo_extension(file_name)

    clean_text_ic = clean_text(inclusion_criteria)
    clean_text_ec = clean_text(exclusion_criteria)

    for run in range(int(N_REPEATS)):
        print(f"Process run {run+1}: Inclusion Criteria")
        output_IC = exec(clean_text_ic, 'Inclusion', in_client)
        # Save output_IC_list to JSON
        json_file_path = f"{file_name}_IC_run_{run+1}.json"
        with open(json_file_path, "w") as json_file:
            json.dump(output_IC, json_file, indent=4)
        
        print(f"Process run {run+1}: Exclusion Criteria")
        output_EC = exec(clean_text_ec, 'Exclusion', in_client)
        # Save output_EC_list to JSON
        json_file_path = f"{file_name}_EC_run_{run+1}.json"
        with open(json_file_path, "w") as json_file:
            json.dump(output_EC, json_file, indent=4)

def summarize_runs(file_name, mode="IC"):
    all_runs = []

    # Load each run's JSON result
    for run in range(1, N_REPEATS + 1):
        path = f"{file_name}_{mode}_run_{run}.json"
        with open(path, "r") as f:
            data = json.load(f)
            all_runs.append(data)
    print(all_runs)

    # Organize data by entity
    entity_runs = defaultdict(list)  # Entity -> list of values
    for run_data in all_runs:
        for entry in run_data:  # entry is a dict like {"a_exist": "Yes", "a": "1", ...}
            for entity, value in entry.items():
                entity_runs[entity].append(value)
    print(entity_runs)
    # Step 1: Determine most common value for *_exist keys
    exist_keys = [k for k in entity_runs if k.endswith("_exist")]
    most_common_exist = {}
    for k in exist_keys:
        val_count = Counter(map(str, entity_runs[k]))
        most_common_exist[k] = val_count.most_common(1)[0][0]

    # Step 2: For each non-exist key, find most common value conditioned on the *_exist value
    conditional_most_common = {}
    for k in entity_runs:
        if k in exist_keys or k == "answer_facts":
            continue

        # Figure out corresponding *_exist key
        exist_key = f"{k}_exist"
        if exist_key not in most_common_exist:
            continue  # skip unmatched keys

    # Get values only where exist_key matched the most common exist value
    filtered_values = []
    for i in range(N_REPEATS):
        entry = all_runs[i][0]  # each run is a list with a single dict

        current_exist_val = str(entry.get(exist_key))
        current_val = str(entry.get(k))

        if current_exist_val == most_common_exist[exist_key] and current_val is not None:
            filtered_values.append(current_val)

    if filtered_values:
        conditional_most_common[k] = Counter(filtered_values).most_common(1)[0][0]

    # Step 3: Build summary and find matching run
    summary_rows = []
    for entity, common_val in most_common_exist.items():
        count = sum(1 for v in entity_runs[entity] if str(v) == common_val)
        consistency = round(count / N_REPEATS, 2)
        summary_rows.append({
            "Entity": entity,
            "Most_Common_Value": common_val,
            "Consistency_Rate": consistency
        })

    for entity, common_val in conditional_most_common.items():
        count = sum(
            1 for i in range(N_REPEATS)
            if str(common_val) == str(entity_runs[entity][i])
            and str(most_common_exist.get(f"{entity}_exist")) == str(entity_runs.get(f"{entity}_exist", [None]*N_REPEATS)[i])
        )
        consistency = round(count / N_REPEATS, 3)
        summary_rows.append({
            "Entity": entity,
            "Most_Common_Value": common_val,
            "Consistency_Rate": consistency
        })

    summary_df = pd.DataFrame(summary_rows)

    # Step 4: Find first run matching all expected values
    target_values = {**most_common_exist, **conditional_most_common}
    for i, run in enumerate(all_runs):
        if not run or not isinstance(run[0], dict):
            continue  # Skip if run is empty or not structured as expected
        flat_dict = {k: str(v) for k, v in run[0].items() if k != "answer_facts"}
        if all(flat_dict.get(k) == v for k, v in target_values.items()):
            return summary_df, i + 1, run

def output_to_df(output):
        # Convert to DataFrame
    rows = []
    for entry in output:
        for key, value in entry.items():
            if key.endswith("_exist"):
                entity = key.replace("_exist", "")
                exist = value
                value_key = entity
                facts = entry.get("answer_facts", [])
                rows.append({
                    "Entity": entity,
                    "Exist": exist,
                    "Value": entry.get(value_key, None),
                    "Facts": facts
                })

    df = pd.DataFrame(rows)
    return df

def export_results(summary_ic, summary_ec, best_run_idx_ic, best_run_idx_ec, final_output_ic, final_output_ec, file_name, output_dir):

    output_dir = output_dir.rstrip(os.path.sep)
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_excel_path = os.path.join(output_dir, f"{file_name}_summary_output_{timestamp}.xlsx")

    summary = pd.merge(summary_ic, summary_ec, on="Entity", suffixes=("_IC", "_EC"))
    final_output_ic = output_to_df(final_output_ic)
    final_output_ec = output_to_df(final_output_ec)

    # Write summary and final output as separate sheets
    with pd.ExcelWriter(output_excel_path) as writer:
        summary.to_excel(writer, sheet_name="Summary", index=False)
        final_output_ic.to_excel(writer, sheet_name=f"Final_Output_Run{best_run_idx_ic}", index=False)
        final_output_ec.to_excel(writer, sheet_name=f"Final_Output_Run{best_run_idx_ec}", index=False)

def main():
    in_client = initiate_llm()

    # Set input/output directories
    INPUT_DIR_NAME = os.environ.get('INPUT_DATA_PATH')
    OUTPUT_DIR_NAME = os.environ.get('OUTPUT_DATA_PATH')

    abstract_list = read_abstracts(INPUT_DIR_NAME)

    for item in tqdm(abstract_list, desc="Processing abstracts"):
        starttime = datetime.now()
        file_name = filename_wo_extension(item[0])

        print("\n----------------------------------------")
        print("Processing file:", file_name)
        print("Process started:", starttime.strftime("%Y-%m-%d %H:%M:%S"))

        # Run entity extraction multiple times
        _ = multi_run(item, in_client)  # JSONs are already saved here

        # Summarize runs and get final output
        summary_IC, best_run_idx_IC, best_output_IC = summarize_runs(file_name, mode="IC")
        summary_EC, best_run_idx_EC, best_output_EC = summarize_runs(file_name, mode="EC")
        print(f"Best run for Inclusion Criteria: {best_run_idx_IC}")
        print(f"Best output: {best_output_IC}")

        # Export results
        export_results(summary_IC, summary_EC, best_run_idx_IC, best_run_idx_EC, best_output_IC, best_output_EC, file_name, OUTPUT_DIR_NAME)

        endtime = datetime.now()
        time_elapsed = endtime - starttime
        print(f'Processing time for file: {file_name} - {str(time_elapsed)}')

if __name__ == "__main__":
    main()
