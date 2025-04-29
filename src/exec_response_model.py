import pandas as pd

import os
from llm import GearboxLLM
from itertools import islice
from pydantic import BaseModel, Field
from enum import Enum
from typing import TypeVar, Type, Optional, List
from collections import Counter, defaultdict


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

    response_model_output_path = os.environ.get('RESPONSE_MODEL_OUTPUT_PATH')
    output_ic_path = os.environ.get('OUTPUT_IC_PATH')
    output_ec_path = os.environ.get('OUTPUT_EC_PATH')
    
    if criteria_type == 'Inclusion':
        model_file_path =  os.path.join(response_model_output_path, output_ic_path)
    else:
        model_file_path = os.path.join(response_model_output_path, output_ec_path)
   
    EntityModel = import_all_response_models(model_file_path)
    
    responses = []

    for i, Model in enumerate(EntityModel):

        try:
            classifier = GearboxLLM(response_model=Model, client=in_client)
            output = classifier.output(criteria=criteria_text, type=criteria_type)
            responses.append(output)
        except Exception as e:
            print(f"[Error] Failed to process Entity{i} : {e}")
            responses.append(Model())

    return responses
