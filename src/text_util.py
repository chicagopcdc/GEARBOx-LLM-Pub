import re
import os
import pandas as pd

## Adopted codes from CFG parser.
reMatchInclusions = "(?is)inclusions?(?: *:| criteria(?:[^:\n]*?:| *\n))(.*?)(?:[^\n]*exclusions?(?: *:| criteria(?:[^:\n]*?:| *\n))|$)"
reMatchExclusions = "(?is)exclusions?(?: *:| criteria(?:[^:\n]*?:| *\n))(.*?)(?:[^\n]*inclusions?(?: *:| criteria(?:[^:\n]*?:| *\n))|$)"

def extract_criteria(s: str, pattern: str) -> list:
    values = re.split(pattern, s)

    if len(values) == 0:
        return list()

    if len(values) > 2:
        c = list()
        for i in range(int((len(values) - 1) / 2)):
            c.append(values[(i * 2) + 1].strip())
    return c

def extract_inclusion_criteria(s: str) -> list:
    """extract_inclusion_criteria extracts a block of inclusion criteria from the string."""
    return extract_criteria(s, reMatchInclusions)

def extract_exclusion_criteria(s: str) -> list:
    """extract_exclusion_criteria extracts a block of exclusion criteria from the string."""
    return extract_criteria(s, reMatchExclusions)

def list_source_files(input: str) -> list:
    file_list = []

    if os.path.isdir(input):
        file_list = [os.path.join(input, file_name) for file_name in os.listdir(input) if file_name.endswith('.txt')]
    else:
        if os.sep in input:
            file_list = [input]
        else:
            file_list = [os.path.join(os.getcwd(), input)]

    return file_list

def clean_text(text: str) -> str:
    return text.replace("  ", " ").replace("\n", "; ").replace(';', ' ')

def read_abstracts(input: str) -> list:
    """
    read_abstracts reads all abstracts from the specified input directory or file,
    extracts inclusion and exclusion criteria, and returns a list of abstracts.
    :param input: str - The directory or file path containing the abstracts.
    :return: list - A list of abstracts with inclusion and exclusion criteria.
    """
    df = pd.DataFrame(columns=['File Name', 'Inclusion Criteria', 'Exclusion Criteria'])
    abstract_list = []

    file_list = list_source_files(input)

    for file_name in file_list:
        print(f"Reading file: {file_name}")
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            inclusion_criteria = extract_inclusion_criteria(content)
            exclusion_criteria = extract_exclusion_criteria(content)

            one_row = pd.DataFrame({'File Name': [file_name], 
                                    'Inclusion Criteria': inclusion_criteria, 
                                    'Exclusion Criteria': exclusion_criteria})
            df = pd.concat([df, one_row], ignore_index=True)

    abstract_list = df[['File Name', 'Inclusion Criteria', 'Exclusion Criteria']].values.tolist()
    return abstract_list

def export_class_to_file(output_path: str, class_definition:str):
    with open(output_path, 'w') as file:
        file.write(class_definition)
