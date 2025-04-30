
from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationInfo, validator
from typing import Optional, List
import re

class Fact(BaseModel):
    fact: str = Field(...)
    substring_quote: List[str] = Field(...)

    @model_validator(mode="after")
    def validate_sources(self, info: ValidationInfo) -> "Fact":
        text_chunks = info.context.get("text_chunk", None)
        spans = list(self.get_spans(text_chunks))
        self.substring_quote = [text_chunks[span[0] : span[1]] for span in spans]
        return self

    def get_spans(self, context):
        for quote in self.substring_quote:
            yield from self._get_span(quote, context)

    def _get_span(self, quote, context):
        for match in re.finditer(re.escape(quote), context):
            yield match.span()

class Bm_recent_blast_method(Enum):
    MORPHOLOGY = "Morphology"
    FLOWCYTOMETRY = "Flow cytometry"

class Cns_status(Enum):
    CNS1 = "CNS 1"
    CNS2 = "CNS 2"
    CNS3 = "CNS 3"

class YesNo(Enum):
    YES = "Yes"
    NO = "No"

class Entity0(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is >=2 if "Second or greater relapse"; the answer is 1 if "first relapses"; 
    '''
    count_relapse_exist: YesNo = Field(..., description="Does the eligibility criteria mention the number of relapses of the patient?")
    count_relapse: Optional[str] = Field(
        None, 
        description="If so, what is the minimum number of relapses required to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity0":
        if getattr(self, "count_relapse_exist") == YesNo.NO:
            if getattr(self, "count_relapse") is not None:
                raise ValueError("count_relapse must be None if count_relapse_exist is 'NO'")
            setattr(self, "count_relapse", None)
            self.answer_facts = []
        return self

  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity0":
        self.answer_fact = [fact for fact in self.answer_fact if len(fact.substring_quote) > 0]
        return self

class Entity1(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is 5 if ">= 5% blasts in the bone marrow", the answer is 5 if "> 5% blasts in the BM" is mentioned
    '''
    bm_recent_blast_pct_meas_exist: YesNo = Field(..., description="Does the eligibility criteria mention bone marrow blast percentage?")
    bm_recent_blast_pct_meas: Optional[int] = Field(
        None, 
        description="If so, what is the minimum bone marrow blast percentage considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity1":
        if getattr(self, "bm_recent_blast_pct_meas_exist") == YesNo.NO:
            if getattr(self, "bm_recent_blast_pct_meas") is not None:
                raise ValueError("bm_recent_blast_pct_meas must be None if bm_recent_blast_pct_meas_exist is 'NO'")
            setattr(self, "bm_recent_blast_pct_meas", None)
            self.answer_facts = []
        return self

  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity1":
        self.answer_fact = [fact for fact in self.answer_fact if len(fact.substring_quote) > 0]
        return self

class Entity2(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "Morphology", "Flow cytometry"; None, if no specific method is mentioned.
    '''
    bm_recent_blast_method_exist: YesNo = Field(..., description="Does the eligibility criteria mention methods for bone marrow blast percentage assessment?")
    bm_recent_blast_method: Optional[List[Bm_recent_blast_method]] = Field(
        None, 
        description="If so, what are the required methods for bone marrow blast percentage assessment considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity2":
        if getattr(self, "bm_recent_blast_method_exist") == YesNo.NO:
            if getattr(self, "bm_recent_blast_method") is not None:
                raise ValueError("bm_recent_blast_method must be None if bm_recent_blast_method_exist is 'NO'")
            setattr(self, "bm_recent_blast_method", None)
            self.answer_facts = []
        return self

  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity2":
        self.answer_fact = [fact for fact in self.answer_fact if len(fact.substring_quote) > 0]
        return self

class Entity3(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: Do not calculate the absolute blast count unless all the necessary measurement are stated.
    '''
    periph_blood_blast_abs_meas_exist: YesNo = Field(..., description="Does the eligibility criteria mention the absolute blast count in peripheral blood?")
    periph_blood_blast_abs_meas: Optional[int] = Field(
        None, 
        description="If so, what is the absolute blast count in peripheral blood measurement (in cells/microliter) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity3":
        if getattr(self, "periph_blood_blast_abs_meas_exist") == YesNo.NO:
            if getattr(self, "periph_blood_blast_abs_meas") is not None:
                raise ValueError("periph_blood_blast_abs_meas must be None if periph_blood_blast_abs_meas_exist is 'NO'")
            setattr(self, "periph_blood_blast_abs_meas", None)
            self.answer_facts = []
        return self

  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity3":
        self.answer_fact = [fact for fact in self.answer_fact if len(fact.substring_quote) > 0]
        return self

class Entity4(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is 5 if ">= 5% blasts in the peripheral blood" is mentioned, the answer is 5 if ">=5% blasts in the blood" is mentioned
    '''
    periph_blood_blast_pct_meas_exist: YesNo = Field(..., description="Does the eligibility criteria mention the peripheral blood blast percentage?")
    periph_blood_blast_pct_meas: Optional[int] = Field(
        None, 
        description="If so, what is the minimum peripheral blood blast percentage considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity4":
        if getattr(self, "periph_blood_blast_pct_meas_exist") == YesNo.NO:
            if getattr(self, "periph_blood_blast_pct_meas") is not None:
                raise ValueError("periph_blood_blast_pct_meas must be None if periph_blood_blast_pct_meas_exist is 'NO'")
            setattr(self, "periph_blood_blast_pct_meas", None)
            self.answer_facts = []
        return self

  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity4":
        self.answer_fact = [fact for fact in self.answer_fact if len(fact.substring_quote) > 0]
        return self

class Entity5(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    corneal_epitheliopathy_exist: YesNo = Field(..., description="Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy?")
    corneal_epitheliopathy: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with such diagnosis considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity5":
        if getattr(self, "corneal_epitheliopathy_exist") == YesNo.NO:
            if getattr(self, "corneal_epitheliopathy") is not None:
                raise ValueError("corneal_epitheliopathy must be None if corneal_epitheliopathy_exist is 'NO'")
            setattr(self, "corneal_epitheliopathy", None)
            self.answer_facts = []
        return self

  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity5":
        self.answer_fact = [fact for fact in self.answer_fact if len(fact.substring_quote) > 0]
        return self

class Entity6(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "CNS 1": < 5 WBC in the cerebrospinal fluid (CSF) without blasts; "CNS 2": (< 5 WBC in the CSF with blasts; "CNS 3":  ≥5 WBC in the CSF with blasts;
CNS-1 was defined as the absence of blasts on cytospin preparation, regardless of the number of white blood cells (WBCs). For CNS-2 it was the presence of <5/μL WBCs and cytospin positive for blasts or ≥5/μL WBCs with negative Steinherz-Bleyer algorithm. For CNS-3, the presence of ≥5/μL WBCs and cytospin positive for blasts and/or clinical signs of CNS leukemia (such as facial nerve palsy, brain/eye involvement, or hypothalamic syndrome) were considered.
CNS 1: WBCs/μL ≤5, RBCs/μL <10, Leukemic blasts: Absent
CNS 2: WBCs/μL ≤5, RBCs/μL <10, Leukemic blasts: Present
CNS 3: WBCs/μL >5, RBCs/μL <10, Leukemic blasts: Present
    '''
    cns_status_exist: YesNo = Field(..., description="Does the eligibility criteria mention CNS status?")
    cns_status: Optional[List[Cns_status]] = Field(
        None, 
        description="If so, what CNS status is considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity6":
        if getattr(self, "cns_status_exist") == YesNo.NO:
            if getattr(self, "cns_status") is not None:
                raise ValueError("cns_status must be None if cns_status_exist is 'NO'")
            setattr(self, "cns_status", None)
            self.answer_facts = []
        return self

  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity6":
        self.answer_fact = [fact for fact in self.answer_fact if len(fact.substring_quote) > 0]
        return self

