from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError, ConfigDict
from typing import List
import os
import instructor
from enum import Enum
import re
import json
from openai import AzureOpenAI
from functools import partial

# Define your Azure OpenAI configuration
model = "gpt4o_cursor"
engine = "gpt4o_cursor"
endpoint = "https://gpt4o-xj.openai.azure.com/"

api_version = "2024-02-15-preview"
api_type = "azure"

# key_name = "AZURE_KEY"
api_key = 'YOUR-API-KEY'

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

app = FastAPI()

# Define the NER labels as an Enum
class EntityLabel(str, Enum):
    NAME = "name"
    DOB = "date_of_birth"
    ADDRESS = "address"
    PHONE_NUMBER = "phone_number"
    PROVIDER = "provider"
    EQUIPMENT = "equipment"
    FAX_NUMBER = "fax_number"
    RECEIVING_DATE = "receiving_date"
    APPROVAL_STATUS = "approval_status"
    IMPORTANT_INFO = "important_info"
    DOCUMENT_TYPE = "document_type"

# Define the list of document types
DOCUMENT_TYPES = [
    "invoice",
    "receipt",
    "medical report",
    "legal document",
    "email",
    "vendor approval",
    "information needed",
    # Add more document types as needed
]

# Define the Pydantic model for an entity
class Entity(BaseModel):
    text: str = Field(..., description="The extracted entity text")
    label: EntityLabel = Field(..., description="The label of the entity")
    start_char: int = Field(None, description="The starting character index of the entity in the text")
    end_char: int = Field(None, description="The ending character index of the entity in the text")
    validated: bool = Field(False, description="Indicates if the entity was validated in the text")
    infer: bool = Field(False, description="Indicates if the entity was inferred")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "text": "John Doe",
                    "label": "name",
                    "start_char": 0,
                    "end_char": 8,
                    "validated": True,
                    "infer": False
                },
                {
                    "text": "information needed",
                    "label": "document_type",
                    "validated": False,
                    "infer": True
                },
            ]
        }
    )

# Define the response model
class NERResponse(BaseModel):
    entities: List[Entity] = Field(..., description="List of extracted entities")

# Define the request body
class TextInput(BaseModel):
    text: str = Field(..., description="The input text to analyze")

# Define the labels to validate
VALIDATED_LABELS = {
    EntityLabel.NAME,
    EntityLabel.DOB,
    EntityLabel.ADDRESS,
    EntityLabel.PHONE_NUMBER,
    EntityLabel.PROVIDER,
    EntityLabel.FAX_NUMBER,
    EntityLabel.RECEIVING_DATE,
    EntityLabel.APPROVAL_STATUS,
    EntityLabel.EQUIPMENT,
}

# Custom validation function to ensure entities are correctly extracted
def validate_entities(entities: List[Entity], text: str) -> List[Entity]:
    valid_entities = []
    for entity in entities:
        if entity.label in VALIDATED_LABELS:
            # Use regex to find the entity text in the input text
            matches = list(re.finditer(re.escape(entity.text), text, re.IGNORECASE))
            if matches:
                # Assign positions from the first match
                match = matches[0]
                entity.start_char = match.start()
                entity.end_char = match.end()
                entity.validated = True
                entity.infer = False
                valid_entities.append(entity)
            else:
                # Entity not found; mark as inferred
                entity.validated = False
                entity.infer = True
                entity.start_char = None
                entity.end_char = None
                print(f"Entity '{entity.text}' with label '{entity.label}' not found in input text. Marked as inferred.")
                valid_entities.append(entity)
        elif entity.label == EntityLabel.DOCUMENT_TYPE:
            # Check if the entity.text matches one of the predefined document types
            if entity.text.lower() in [doc_type.lower() for doc_type in DOCUMENT_TYPES]:
                entity.validated = False
                entity.infer = True
                valid_entities.append(entity)
            else:
                print(f"Invalid document type: {entity.text}")
        elif entity.label == EntityLabel.IMPORTANT_INFO:
            # Accept the summary as is
            entity.validated = False
            entity.infer = True
            valid_entities.append(entity)
        else:
            # Handle other labels if necessary
            pass
    return valid_entities

# Define the API endpoint
@app.post("/ner", response_model=NERResponse)
def extract_entities(input: TextInput):
    try:
        # Modify the prompt to include specific instructions
        prompt = f"""
Perform named entity recognition, summarization, and classification on the following text. Extract entities for the specified labels.

**Validated Labels (attempt to find exact text in the input):**
- Name
- Date of Birth (DOB)
- Address
- Phone Number
- Provider
- Fax Number
- Receiving Date
- Approval Status
- Equipment: Extract any specific devices or equipment mentioned.

For these, provide 'text', 'label', 'start_char', and 'end_char'. Mark them with "validated": true if found in the text; otherwise, "validated": false. Set "infer": false.

**Inferred Contents (do not require exact text in input):**
- Important Information Summary: Provide a concise summary of the most important information from the text.
- Document Type: Classify the text into one of the following types: {', '.join(DOCUMENT_TYPES)}.

For these, provide 'text' and 'label'. Mark them with "validated": false, "infer": true. Do not include 'start_char' and 'end_char'.

Return the entities as a JSON list with the fields specified. Ensure that the 'label' is one of the specified labels.

**Examples:**
- {{ "text": "John Doe", "label": "name", "start_char": 5, "end_char": 13, "validated": true, "infer": false }}
- {{ "text": "Vendor approval", "label": "document_type", "validated": false, "infer": true }}
- {{ "text": "CPAP machine", "label": "equipment", "start_char": 100, "end_char": 112, "validated": true, "infer": false }}
- {{ "text": "The patient requires a CPAP machine.", "label": "important_info", "validated": false, "infer": true }}

**Text:**
\"\"\"
{input.text}
\"\"\"
"""

        # Use the Azure OpenAI client to generate the response
        response = in_client(
            response_model=NERResponse,
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that extracts named entities from text, classifies and summarizes text.",
                },
                {"role": "user", "content": prompt},
            ],
        )

        # Perform additional validation
        response.entities = validate_entities(response.entities, input.text)

        # Print the response beautifully
        print("Named Entity Recognition Results:")
        for entity in response.entities:
            extracted_text = input.text[entity.start_char:entity.end_char] if entity.start_char is not None else None
            print(json.dumps({
                "text": entity.text,
                "label": entity.label,
                "start_char": entity.start_char,
                "end_char": entity.end_char,
                "validated": entity.validated,
                "infer": entity.infer,
                "text_from_file": extracted_text
            }, indent=4))

        return response

    except ValidationError as ve:
        error_details = ve.errors()
        print(f"Validation error occurred: {error_details}")
        raise HTTPException(status_code=400, detail=error_details)
    except Exception as e:
        error_message = str(e)
        print(f"An error occurred: {error_message}")
        raise HTTPException(status_code=500, detail=error_message)
