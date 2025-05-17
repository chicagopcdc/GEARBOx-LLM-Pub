from typing import TypeVar, Type, Optional, List
from pydantic import BaseModel, Field
from enum import Enum
import pandas as pd
import re

T = TypeVar("T", bound=BaseModel)

class  GearboxLLM:
    def __init__(self, response_model: Type[T], client):
        self.response_model = response_model
        self.client = client

    def ask_ai(self, criteria:str, type:str) -> T:
        return self.client(
            response_model=self.response_model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You will help extract entities from clinical protocol documents",
                },
                {
                    "role": "user",
                    "content": f"Extract information from the clinical trial eligibility document ({type} criteria). Extract only explicitly mentioned entities. Do not infer or assume any information beyond what is explicitly stated in the document. ",
                },
                {
                    "role": "user",
                    "content": f"Here is the {type} Criteria section {criteria}",
                },
                # {
                #     "role": "user",
                #     "content": f'''Please follow the following guidelines to answer the questions:
                #                 * Ensure you distinguish between 'CYP3A4' and 'CYP3A'. They are distinct, and an instance of 'CYP3A' should not be interpreted as 'CYP3A4'.
                #                 * Given content 'Refractory leukemia, defined as persistent leukemia after at least two courses of induction chemotherapy', 
                #                 it does not indicate occurrences of refractory disease but indicates the number of cycles of therapy required for refractory disease.
                #                 * Given content 'evidence of leukemia with ≥ 5% blasts in the blood', it dose not indicate blood absolute blast count but indicates blood blast percentage.
                #                 * Given content 'At least 24 hours must have elapsed since the completion of low-dose or non- myelosuppressive therapy', 
                #                 it indicates prior exposure to non-myelosuppressive anti-cancer agents.
                #                 * Given content 'At least 14 days must have elapsed since the completion of myelosuppressive therapy', it indicates prior exposure to myelosuppressive anti-cancer agents.
                #                 ''',
                # },
            ],
            validation_context={"text_chunk": criteria},
        ) 

    def output(self, criteria: str, type: str):
        try:
            response = self.ask_ai(criteria, type)
            entity_dict = response.dict()

            for key, value in entity_dict.items():
                if isinstance(value, list):
                    if value and isinstance(value[0], Enum):
                        entity_dict[key] = [v.value for v in value]  # Extract the string representation
                    # else: keep the list as is
                elif isinstance(value, Enum):
                    entity_dict[key] = value.value  # For single Enum fields

            entity_value_data = {
                "Entity": list(entity_dict.keys()),
                "Value": list(entity_dict.values()),
            }
            df = pd.DataFrame(entity_value_data)
            return df
        
        except Exception as e:
            print(f"Error in output method: {str(e)}")
            # Return an empty DataFrame if an error occurs
            return pd.DataFrame(columns=["Entity", "Value"])

