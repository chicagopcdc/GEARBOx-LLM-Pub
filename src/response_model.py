import pandas as pd
import re
from llm import GearboxLLM
from itertools import islice
from pydantic import BaseModel, Field
from enum import Enum
from Entity_IC import *
from Entity_IC import Entity as Entity_IC
from Entity_EC import Entity as Entity_EC
from typing import TypeVar, Type, Optional, List

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
        if pd.notna(example):
            description += f" Example: {example}"
        parts = description.split('?')
        first_yesno = parts[0] + '?'
        second_criteria = parts[1].strip().replace("{verb}", verb)
        
        fields[param_name_exist] = f"Yes_no = Field(..., description=\"{first_yesno}\")"
        fields[param_name] = f"{field_type} = Field(\n        None, \n        description=\"{second_criteria}\")"
    
    enum_items = ["Yes","No"]
    enum_class_str = f"class Yes_no(Enum):\n"
    for item in enum_items:
        enum_name = item.upper()
        enum_class_str += f"    {enum_name} = \"{item}\"\n"
    enum_classes["Yes_no"] = enum_class_str

    return fields, enum_classes

# def process_with_dynamic_model(criteria_text:str, criteria_type:str, class_fields, in_client):
#     # exec(class_enum)

#     entity_value_list = []
#     # Loop through each field and process
#     for field_name, field_definition in class_fields.items():
#         # Dynamically create the response model class
#         class_basemodel = f"""
# class Entity(BaseModel):
#     {field_name}: {field_definition}
# """
#         # Compile the class definition into a Python class
#         exec(class_basemodel)

#         response_model = locals()["Entity"]

#         print(f"Processing field '{field_name}'")
#         # Initialize and use the classifier
#         try:
#             Classifier = GearboxLLM(response_model=response_model, client=in_client)
#             output = Classifier.output(criteria=criteria_text, type=criteria_type)
#         except Exception as e:
#             print(f"Error processing field '{field_name}': {e}")

#         entity_value_list.append(output)
#     df_c = pd.concat(entity_value_list, ignore_index=True)
    
#     return df_c

# Helper function to get dictionary chunks of size 2
def dict_chunk(dictionary:dict, size:int = 2):
    iterator = iter(dictionary.items())
    for chunk in iter(lambda: list(islice(iterator, size)), []):
        yield chunk

def process_chunk_with_dynamic_model(criteria_text:str, criteria_type:str, class_fields, in_client, chunk_size:int = 1):
    entity_value_list = []
    # Loop through each field and process
    for chunk in dict_chunk(class_fields, size = chunk_size):
        class_basemodel = "class Entity(BaseModel):\n"
        for field_name, field_definition in chunk:
            class_basemodel += f"    {field_name}: {field_definition}\n"

        # Remove any unintended leading or trailing whitespace
        class_basemodel = class_basemodel.strip()

        print(f"Processing field '{chunk}'")
        try:
            # Compile the class definition
            exec(class_basemodel)
            response_model = locals()["Entity"]

            # Initialize and use the classifier
            Classifier = GearboxLLM(response_model=response_model, client=in_client)
            output = Classifier.output(criteria=criteria_text, type=criteria_type)
        except Exception as e:
            print(f"Error processing fields {[field_name for field_name, _ in chunk]}: {e}")
        entity_value_list.append(output)
    df_c = pd.concat(entity_value_list, ignore_index=True)

    return df_c
