import instructor
from enum import Enum
from openai import AzureOpenAI
from functools import partial
from Entity_test import Entity
import pandas as pd
from datetime import datetime

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

def ask_ai(IC:str) -> Entity:
    return in_client(
        response_model=Entity,
        messages=[
            {
                "role": "system",
                "content": "You will help extract entities from clinical protocol documents",
            },
            {
                "role": "user",
                "content": "Extract information from the clinical trial eligibility document.",
            },
            {
                "role": "user",
                "content": f"Here is the Inclusion Criteria section {IC}",
            },
        ],
        validation_context={"text_chunk": IC},
    ) 

IC = """
Inclusion Criteria:\n\n* Participants must have a diagnosis of AML or ALAL and meet the criteria below:\n\n  * Refractory leukemia, defined as persistent leukemia after at least two courses of induction chemotherapy, OR\n  * Early relapsed leukemia, defined as the re-appearance of leukemia after the achievement of remission and within one year of diagnosis, OR\n  * Relapsed leukemia that is refractory to at least one course of salvage therapy (i.e., therapy given after the relapse has occurred), OR\n  * Relapsed leukemia following HCT, OR\n  * Second or greater relapse\n  * Patients with late first relapses, defined as the re-appearance of leukemia after the achievement of remission and greater than one year of diagnosis, may be enrolled in the dose expansion portion of the study after safety data from the dose escalation portion is available.\n\nPatients must have ≥ 5% blasts in the bone marrow as assessed by morphology or flow cytometry. However, if flow cytometry cannot be performed or if an adequate bone marrow sample cannot be obtained (e.g., in a patient with acute megakaryoblastic leukemia with marrow fibrosis), patients may be enrolled if there is unequivocal evidence of leukemia with ≥ 5% blasts in the blood.\n\nIn addition, patients in all categories must not be eligible to undergo curative therapy, such as immediate HCT, because of disease burden, time to identify a stem cell donor, or other reasons.\n\n* Adequate organ function defined as the following:\n\n  * Direct bilirubin ≤ 1.5 x institutional upper limit of normal (ULN)\n  * Normal creatinine for age or a calculated creatinine clearance ≥ 30 mL/min/1.73m\\^2\n  * Left ventricular ejection fraction ≥ 40% or shortening fraction ≥ 25%\n* Patients must be ≥ 2 years of age and ≤ 30 years old. The upper age limit may be defined by each institution, but may not exceed 30 years. Patients treated at St. Jude Children's Research Hospital must be ≤ 24 years old.\n* Performance status: Lansky ≥ 50 for patients who are ≤ 16 years old and Karnofsky ≥ 50% for patients who are \\> 16 years old.\n* At least 14 days must have elapsed since the completion of myelosuppressive therapy or hypomethylating agents and the first doses of venetoclax and selinexor.\n* At least 24 hours must have elapsed since the completion of low-dose or non- myelosuppressive therapy, such as hydroxyurea or low-dose cytarabine (up to 100 mg/m\\^2/day), or leukapheresis, and the first doses of venetoclax and selinexor.\n* For patients who have received prior HCT, there can be no evidence of GVHD and greater than 60 days must have elapsed since the HCT.\n* At least 14 days must have elapsed since the completion of any calcineurin inhibitors (e.g. tacrolimus, cyclosporine).\n* Patients may not receive strong or moderate CYP3A inducers, such as rifampin, within 3 days of the first dose of venetoclax or during the administration of venetoclax. During the dose-escalation portion of the trial, we discourage the use of strong CYP3A inhibitors (e.g., ketoconazole, itraconazole, voriconazole, posaconazole) within 3 days of the first dose of venetoclax or during the administration of venetoclax. However, if an azole is required for the treatment or prevention of fungal infection during any phase of the trial, venetoclax dosing will be reduced to 60 mg/m\\^2 (100 mg max) in patients who require treatment with voriconazole and reduced to 40 mg/m\\^2 (70 mg max) in patients who require posaconazole.
"""  
response_IC = ask_ai(IC)

# Convert the Pydantic object to a dictionary
entity_dict = response_IC.dict()

# Transform the Enum fields to their string values for both dictionaries
for key, value in entity_dict.items():
    if isinstance(value, list) and isinstance(value[0], Enum):
        entity_dict[key] = [v.value for v in value]  # Extract the string representation
    elif isinstance(value, Enum):
        entity_dict[key] = value.value  # For single Enum fields

entity_value_data = {
    "Entity": list(entity_dict.keys()),
    "Value_IC": list(entity_dict.values())
}

df_entity_value = pd.DataFrame(entity_value_data)

output_excel_path = f'../results/output_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
df_entity_value.to_excel(output_excel_path, index=False)