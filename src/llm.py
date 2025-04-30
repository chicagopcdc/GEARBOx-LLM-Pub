from typing import TypeVar, Type, Optional, List
from pydantic import BaseModel, Field
from enum import Enum
import pandas as pd
import re
import os

T = TypeVar("T", bound=BaseModel)

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
            # df = pd.DataFrame(entity_value_data)
            return entity_value_data
        
        except Exception as e:
            print(f"Error in output method: {str(e)}")

