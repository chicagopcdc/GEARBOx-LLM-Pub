import pandas as pd
import re
import os
from llm import GearboxLLM
from itertools import islice
from pydantic import BaseModel, Field
from enum import Enum
from typing import TypeVar, Type, Optional, List
from collections import Counter, defaultdict

# Function to generate class fields and enums
def generate_class_fields_and_enums(df, verb):
    fields = {}
    enum_classes = {}  # Dictionary to store generated enum classes as strings

    for _, row in df.iterrows():
        param_name = row['Parameter Name']
        param_name_exist = f"{param_name}_exist"

        # Determine the field type based on 'Type' and 'Enum' columns
        if row['Type'] in ['integer', 'number']:
            field_type = 'Optional[int]'
        elif pd.notna(row['Enum']) and 'Yes' in row['Enum']:
            field_type = 'Optional[Yes_no]'  # Assuming YesOrNo is a defined type elsewhere
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

        # Combine description and examples if available
        description = row['Description']
        example = row['Examples']
        if pd.notna(example) and example.strip():
            description += f" Example: {example}"
        parts = description.split('?')
        first_yesno = parts[0] + '?'
        second_criteria = parts[1].strip().replace("{verb}", verb) + '? '
        if len(parts) > 2:
            second_criteria = second_criteria + parts[2].replace('"', '\\"')
        
        fields[param_name_exist] = f"Yes_no = Field(..., description=\"{first_yesno}\")"
        fields[param_name] = f"{field_type} = Field(\n        None, \n        description=\"{second_criteria}\")"
    
    enum_items = ["Yes","No"]
    enum_class_str = f"class Yes_no(Enum):\n"
    for item in enum_items:
        enum_name = item.upper()
        enum_class_str += f"    {enum_name} = \"{item}\"\n"
    enum_classes["Yes_no"] = enum_class_str

    return fields, enum_classes

def import_all_response_models(module_path: str, prefix="Entity") -> list:
    import importlib.util
    import os
    import sys

    module_name = os.path.splitext(os.path.basename(module_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    entity_models = []
    i = 0
    while True:
        class_name = f"{prefix}{i}"
        if hasattr(module, class_name):
            entity_models.append(getattr(module, class_name))
            i += 1
        else:
            break
    return entity_models

def exec(criteria_text: str, 
         criteria_type: str, 
         in_client) -> pd.DataFrame:
        #  n_repeats: int = 1) -> pd.DataFrame:

    response_model_output_path = os.environ.get('RESPONSE_MODEL_OUTPUT_PATH')
    output_ic_path = os.environ.get('OUTPUT_IC_PATH')
    output_ec_path = os.environ.get('OUTPUT_EC_PATH')
    
    if criteria_type == 'Inclusion':
        model_file_path =  os.path.join(response_model_output_path, output_ic_path)
    else:
        model_file_path = os.path.join(response_model_output_path, output_ec_path)
   
    EntityModel = import_all_response_models(model_file_path)
    
    responses = []
    # n_repeats = int(n_repeats)

    for i, Model in enumerate(EntityModel):
        # for run in range(n_repeats):
        try:
            classifier = GearboxLLM(response_model=Model, client=in_client)
            output = classifier.output(criteria=criteria_text, type=criteria_type)
            # output['criteria_type'] = criteria_type
            responses.append(output)
        except Exception as e:
            print(f"[Error] Failed to process Entity{i} : {e}")
            responses.append(Model())

    return responses
