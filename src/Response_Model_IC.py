
from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationInfo
from typing import Optional, List, Tuple
import re

class Fact(BaseModel):
    fact: str = Field(...)
    substring_quote: List[str] = Field(...)
    substring_indices: List[List[int]] = Field(default_factory=list, description="Indices of substring_quote in the context")

    @model_validator(mode="after")
    def validate_sources(self, info: ValidationInfo) -> "Fact":
        context = info.context.get("text_chunk", None)
        spans = list(self.get_spans(context))

        self.substring_quote = [context[start:end] for start, end in spans]
        self.substring_indices = [list(span) for span in spans]
        return self

    def get_spans(self, context):
        for quote in self.substring_quote:
            yield from self._get_span(quote, context)

    def _get_span(self, quote, context):
        for match in re.finditer(re.escape(quote), context):
            yield match.span()

class Sex(Enum):
    MALE = "Male"
    FEMALE = "Female"

class Diagnosis(Enum):
    APL = "Acute promyelocytic leukemia (APL)"
    AML = "Acute myeloid leukemia (AML)"
    DSAML = "Down syndrome acute myeloid leukemia (DS AML)"
    BALL = "B-cell acute lymphoblastic leukemia (B-ALL)"
    JMML = "Juvenile myelomonocytic leukemia (JMML)"
    MPAL = "Mixed-phenotype acute leukemia (MPAL)"
    MDS = "Myelodysplastic syndromes (MDS)"
    MDSAML = "Myelodysplastic syndrome who have progressed to AML (MDS-AML)"
    TAML = "Treatment-related acute myeloid leukemia (tAML)"
    TALL = "T-cell acute lymphoblastic leukemia (T-ALL)"
    ALL = "Acute lymphoblastic leukemia (ALL)"
    KMT2AACUTELYMPHOBLASTICLEUKEMIA = "KMT2A acute lymphoblastic leukemia"
    ETPALL = "Early T-cell precursor acute lymphoblastic leukemia (ETP-ALL)"
    ALAL = "Ambiguous lineage acute leukemia (ALAL)"

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
    '''
    age_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention the minimum age of eligibility?")
    age_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum age of eligibility (in years) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity0":
        if getattr(self, "age_min_exist") == YesNo.NO:
            if getattr(self, "age_min") is not None:
                raise ValueError("age_min must be None if age_min_exist is 'NO'")
            setattr(self, "age_min", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity0":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity1(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    age_max_exist: YesNo = Field(..., description="Does the eligibility criteria mention the maximum age of eligibility?")
    age_max: Optional[int] = Field(
        None, 
        description="If so, what is the maximum age of eligibility (in years) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity1":
        if getattr(self, "age_max_exist") == YesNo.NO:
            if getattr(self, "age_max") is not None:
                raise ValueError("age_max must be None if age_max_exist is 'NO'")
            setattr(self, "age_max", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity1":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity2(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    weight_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention the minimum weight a patient may have?")
    weight_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum weight (in kilograms) of a patient considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity2":
        if getattr(self, "weight_min_exist") == YesNo.NO:
            if getattr(self, "weight_min") is not None:
                raise ValueError("weight_min must be None if weight_min_exist is 'NO'")
            setattr(self, "weight_min", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity2":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity3(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    weight_max_exist: YesNo = Field(..., description="Does the eligibility criteria mention the maximum weight a patient may have?")
    weight_max: Optional[int] = Field(
        None, 
        description="If so, what is the maximum weight (in kilograms) of a patient considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity3":
        if getattr(self, "weight_max_exist") == YesNo.NO:
            if getattr(self, "weight_max") is not None:
                raise ValueError("weight_max must be None if weight_max_exist is 'NO'")
            setattr(self, "weight_max", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity3":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity4(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    sex_exist: YesNo = Field(..., description="Does the eligibility criteria mention sexes of a patient?")
    sex: Optional[List[Sex]] = Field(
        None, 
        description="If so, which sexes are considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity4":
        if getattr(self, "sex_exist") == YesNo.NO:
            if getattr(self, "sex") is not None:
                raise ValueError("sex must be None if sex_exist is 'NO'")
            setattr(self, "sex", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity4":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity5(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diagnosis_exist: YesNo = Field(..., description="Does the eligibility criteria mention a patient's current diagnoses?")
    diagnosis: Optional[List[Diagnosis]] = Field(
        None, 
        description="If so, which diagnoses are considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity5":
        if getattr(self, "diagnosis_exist") == YesNo.NO:
            if getattr(self, "diagnosis") is not None:
                raise ValueError("diagnosis must be None if diagnosis_exist is 'NO'")
            setattr(self, "diagnosis", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity5":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity6(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: refractory disease are diseases such as "Refractory leukemia"
    '''
    ever_refractory_exist: YesNo = Field(..., description="Does the eligibility criteria mention refractory disease?")
    ever_refractory: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with refractory disease considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity6":
        if getattr(self, "ever_refractory_exist") == YesNo.NO:
            if getattr(self, "ever_refractory") is not None:
                raise ValueError("ever_refractory must be None if ever_refractory_exist is 'NO'")
            setattr(self, "ever_refractory", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity6":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity7(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    count_refractory_exist: YesNo = Field(..., description="Does the eligibility criteria mention the occurrence of refractory disease?")
    count_refractory: Optional[int] = Field(
        None, 
        description="If so, how many occurrences of refractory disease are required to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity7":
        if getattr(self, "count_refractory_exist") == YesNo.NO:
            if getattr(self, "count_refractory") is not None:
                raise ValueError("count_refractory must be None if count_refractory_exist is 'NO'")
            setattr(self, "count_refractory", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity7":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity8(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is 1 if "refractory to at least one course of salvage therapy", the answer is 2 if "persistent after at least two courses of induction "chemotherapy", the answer is 2 if "refractory disease after >= 2 cycles of chemotherapy"
    '''
    current_refractory_num_cycles_exist: YesNo = Field(..., description="Does the eligibility criteria mention number of cycles of therapy required for refractory disease?")
    current_refractory_num_cycles: Optional[int] = Field(
        None, 
        description="If so, what is the minimum number of cycles of therapy required for refractory disease considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity8":
        if getattr(self, "current_refractory_num_cycles_exist") == YesNo.NO:
            if getattr(self, "current_refractory_num_cycles") is not None:
                raise ValueError("current_refractory_num_cycles must be None if current_refractory_num_cycles_exist is 'NO'")
            setattr(self, "current_refractory_num_cycles", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity8":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity9(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: relapse disease such as "relapsed leukemia"
    '''
    ever_relapse_exist: YesNo = Field(..., description="Does the eligibility criteria mention confirmed or suspected relapse disease?")
    ever_relapse: Optional[YesNo] = Field(
        None, 
        description="If so, is confirmed or suspected relapse disease considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity9":
        if getattr(self, "ever_relapse_exist") == YesNo.NO:
            if getattr(self, "ever_relapse") is not None:
                raise ValueError("ever_relapse must be None if ever_relapse_exist is 'NO'")
            setattr(self, "ever_relapse", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity9":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity10(BaseModel):
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
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity10":
        if getattr(self, "count_relapse_exist") == YesNo.NO:
            if getattr(self, "count_relapse") is not None:
                raise ValueError("count_relapse must be None if count_relapse_exist is 'NO'")
            setattr(self, "count_relapse", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity10":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity11(BaseModel):
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
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity11":
        if getattr(self, "bm_recent_blast_pct_meas_exist") == YesNo.NO:
            if getattr(self, "bm_recent_blast_pct_meas") is not None:
                raise ValueError("bm_recent_blast_pct_meas must be None if bm_recent_blast_pct_meas_exist is 'NO'")
            setattr(self, "bm_recent_blast_pct_meas", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity11":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity12(BaseModel):
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
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity12":
        if getattr(self, "bm_recent_blast_method_exist") == YesNo.NO:
            if getattr(self, "bm_recent_blast_method") is not None:
                raise ValueError("bm_recent_blast_method must be None if bm_recent_blast_method_exist is 'NO'")
            setattr(self, "bm_recent_blast_method", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity12":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity13(BaseModel):
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
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity13":
        if getattr(self, "periph_blood_blast_abs_meas_exist") == YesNo.NO:
            if getattr(self, "periph_blood_blast_abs_meas") is not None:
                raise ValueError("periph_blood_blast_abs_meas must be None if periph_blood_blast_abs_meas_exist is 'NO'")
            setattr(self, "periph_blood_blast_abs_meas", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity13":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity14(BaseModel):
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
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity14":
        if getattr(self, "periph_blood_blast_pct_meas_exist") == YesNo.NO:
            if getattr(self, "periph_blood_blast_pct_meas") is not None:
                raise ValueError("periph_blood_blast_pct_meas must be None if periph_blood_blast_pct_meas_exist is 'NO'")
            setattr(self, "periph_blood_blast_pct_meas", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity14":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity15(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    corneal_epitheliopathy_exist: YesNo = Field(..., description="Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy?")
    corneal_epitheliopathy: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with such diagnosis considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity15":
        if getattr(self, "corneal_epitheliopathy_exist") == YesNo.NO:
            if getattr(self, "corneal_epitheliopathy") is not None:
                raise ValueError("corneal_epitheliopathy must be None if corneal_epitheliopathy_exist is 'NO'")
            setattr(self, "corneal_epitheliopathy", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity15":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity16(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: CNS-1 was defined as the absence of blasts on cytospin preparation, regardless of the number of white blood cells (WBCs). 
For CNS-2 it was the presence of <5/μL WBCs and cytospin positive for blasts or ≥5/μL WBCs with negative Steinherz-Bleyer algorithm. 
For CNS-3, the presence of ≥5/μL WBCs and cytospin positive for blasts and/or clinical signs of CNS leukemia (such as facial nerve palsy, brain/eye involvement, or hypothalamic syndrome) were considered.
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
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity16":
        if getattr(self, "cns_status_exist") == YesNo.NO:
            if getattr(self, "cns_status") is not None:
                raise ValueError("cns_status must be None if cns_status_exist is 'NO'")
            setattr(self, "cns_status", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity16":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity17(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is 70 if "Lansky score>=70" is mentioned
    '''
    lansky_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention Lansky score?")
    lansky_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum Lansky score for a patient considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity17":
        if getattr(self, "lansky_min_exist") == YesNo.NO:
            if getattr(self, "lansky_min") is not None:
                raise ValueError("lansky_min must be None if lansky_min_exist is 'NO'")
            setattr(self, "lansky_min", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity17":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity18(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is 50 if "Karnofsky score >= 50" is mentioned
    '''
    karnofsky_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention Karnofsky score?")
    karnofsky_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum Karnofsky score for a patient considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity18":
        if getattr(self, "karnofsky_min_exist") == YesNo.NO:
            if getattr(self, "karnofsky_min") is not None:
                raise ValueError("karnofsky_min must be None if karnofsky_min_exist is 'NO'")
            setattr(self, "karnofsky_min", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity18":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity19(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_down_syndrome_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Down syndrome?")
    diag_down_syndrome: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Down syndrome considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity19":
        if getattr(self, "diag_down_syndrome_exist") == YesNo.NO:
            if getattr(self, "diag_down_syndrome") is not None:
                raise ValueError("diag_down_syndrome must be None if diag_down_syndrome_exist is 'NO'")
            setattr(self, "diag_down_syndrome", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity19":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity20(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_iso_emd_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of isolated extramedullary disease (i.e. the absence of bone marrow involvement)?")
    diag_iso_emd: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of isolated extramedullary disease considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity20":
        if getattr(self, "diag_iso_emd_exist") == YesNo.NO:
            if getattr(self, "diag_iso_emd") is not None:
                raise ValueError("diag_iso_emd must be None if diag_iso_emd_exist is 'NO'")
            setattr(self, "diag_iso_emd", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity20":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity21(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_iso_testes_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of isolated testicular relapse?")
    diag_iso_testes: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of isolated testicular relapse considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity21":
        if getattr(self, "diag_iso_testes_exist") == YesNo.NO:
            if getattr(self, "diag_iso_testes") is not None:
                raise ValueError("diag_iso_testes must be None if diag_iso_testes_exist is 'NO'")
            setattr(self, "diag_iso_testes", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity21":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity22(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_ataxia_telang_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of ataxia-telangiectasia?")
    diag_ataxia_telang: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of ataxia-telangiectasia considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity22":
        if getattr(self, "diag_ataxia_telang_exist") == YesNo.NO:
            if getattr(self, "diag_ataxia_telang") is not None:
                raise ValueError("diag_ataxia_telang must be None if diag_ataxia_telang_exist is 'NO'")
            setattr(self, "diag_ataxia_telang", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity22":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity23(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_bloom_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Bloom syndrome?")
    diag_bloom: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Bloom syndrome considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity23":
        if getattr(self, "diag_bloom_exist") == YesNo.NO:
            if getattr(self, "diag_bloom") is not None:
                raise ValueError("diag_bloom must be None if diag_bloom_exist is 'NO'")
            setattr(self, "diag_bloom", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity23":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity24(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_fanconi_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Fanconi anemia?")
    diag_fanconi: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Fanconi anemia considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity24":
        if getattr(self, "diag_fanconi_exist") == YesNo.NO:
            if getattr(self, "diag_fanconi") is not None:
                raise ValueError("diag_fanconi must be None if diag_fanconi_exist is 'NO'")
            setattr(self, "diag_fanconi", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity24":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity25(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_kostmann_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Kostmann syndrome?")
    diag_kostmann: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Kostmann syndrome considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity25":
        if getattr(self, "diag_kostmann_exist") == YesNo.NO:
            if getattr(self, "diag_kostmann") is not None:
                raise ValueError("diag_kostmann must be None if diag_kostmann_exist is 'NO'")
            setattr(self, "diag_kostmann", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity25":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity26(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_shwachman_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Shwachman syndrome?")
    diag_shwachman: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Shwachman syndrome considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity26":
        if getattr(self, "diag_shwachman_exist") == YesNo.NO:
            if getattr(self, "diag_shwachman") is not None:
                raise ValueError("diag_shwachman must be None if diag_shwachman_exist is 'NO'")
            setattr(self, "diag_shwachman", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity26":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity27(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_cong_bmf_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)?")
    diag_cong_bmf: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with such diagnosis considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity27":
        if getattr(self, "diag_cong_bmf_exist") == YesNo.NO:
            if getattr(self, "diag_cong_bmf") is not None:
                raise ValueError("diag_cong_bmf must be None if diag_cong_bmf_exist is 'NO'")
            setattr(self, "diag_cong_bmf", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity27":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity28(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_malabsoption_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of malabsorption syndrome?")
    diag_malabsoption: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of malabsorption syndrome considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity28":
        if getattr(self, "diag_malabsoption_exist") == YesNo.NO:
            if getattr(self, "diag_malabsoption") is not None:
                raise ValueError("diag_malabsoption must be None if diag_malabsoption_exist is 'NO'")
            setattr(self, "diag_malabsoption", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity28":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity29(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_chf_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of congestive heart failure (CHF)?")
    diag_chf: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of congestive heart failure considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity29":
        if getattr(self, "diag_chf_exist") == YesNo.NO:
            if getattr(self, "diag_chf") is not None:
                raise ValueError("diag_chf must be None if diag_chf_exist is 'NO'")
            setattr(self, "diag_chf", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity29":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity30(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_hiv_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of human immunodeficiency virus (HIV) infection?")
    diag_hiv: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of human immunodeficiency virus infection considered be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity30":
        if getattr(self, "diag_hiv_exist") == YesNo.NO:
            if getattr(self, "diag_hiv") is not None:
                raise ValueError("diag_hiv must be None if diag_hiv_exist is 'NO'")
            setattr(self, "diag_hiv", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity30":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity31(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_uncontr_cns_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis)?")
    diag_uncontr_cns: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity31":
        if getattr(self, "diag_uncontr_cns_exist") == YesNo.NO:
            if getattr(self, "diag_uncontr_cns") is not None:
                raise ValueError("diag_uncontr_cns must be None if diag_uncontr_cns_exist is 'NO'")
            setattr(self, "diag_uncontr_cns", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity31":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity32(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_hep_b_c_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of hepatitis B or hepatitis C infection?")
    diag_hep_b_c: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of hepatitis B or hepatitis C infection considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity32":
        if getattr(self, "diag_hep_b_c_exist") == YesNo.NO:
            if getattr(self, "diag_hep_b_c") is not None:
                raise ValueError("diag_hep_b_c must be None if diag_hep_b_c_exist is 'NO'")
            setattr(self, "diag_hep_b_c", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity32":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity33(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_liver_cirr_serious_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of liver cirrhosis or other serious liver disease?")
    diag_liver_cirr_serious: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of liver cirrhosis or other serious liver disease considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity33":
        if getattr(self, "diag_liver_cirr_serious_exist") == YesNo.NO:
            if getattr(self, "diag_liver_cirr_serious") is not None:
                raise ValueError("diag_liver_cirr_serious must be None if diag_liver_cirr_serious_exist is 'NO'")
            setattr(self, "diag_liver_cirr_serious", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity33":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity34(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    active_infection_exist: YesNo = Field(..., description="Does the eligibility criteria mention an active, uncontrolled infection?")
    active_infection: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with an active, uncontrolled infection considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity34":
        if getattr(self, "active_infection_exist") == YesNo.NO:
            if getattr(self, "active_infection") is not None:
                raise ValueError("active_infection must be None if active_infection_exist is 'NO'")
            setattr(self, "active_infection", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity34":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity35(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    refractory_transfusion_exist: YesNo = Field(..., description="Does the eligibility criteria mention a patient known to be refractory to red blood cells or platelet transfusions?")
    refractory_transfusion: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient known to be refractory to red blood cells or platelet transfusions considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity35":
        if getattr(self, "refractory_transfusion_exist") == YesNo.NO:
            if getattr(self, "refractory_transfusion") is not None:
                raise ValueError("refractory_transfusion must be None if refractory_transfusion_exist is 'NO'")
            setattr(self, "refractory_transfusion", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity35":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity36(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    cerebellar_toxicity_exist: YesNo = Field(..., description="Does the eligibility criteria mention an history of cerebellar toxicity or cerebellar neurological findings on exam?")
    cerebellar_toxicity: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a history of cerebellar toxicity or cerebellar neurological findings on exam considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity36":
        if getattr(self, "cerebellar_toxicity_exist") == YesNo.NO:
            if getattr(self, "cerebellar_toxicity") is not None:
                raise ValueError("cerebellar_toxicity must be None if cerebellar_toxicity_exist is 'NO'")
            setattr(self, "cerebellar_toxicity", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity36":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity37(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_cytotoxic_chemo_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)?")
    exp_cytotoxic_chemo_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity37":
        if getattr(self, "exp_cytotoxic_chemo_ever_exist") == YesNo.NO:
            if getattr(self, "exp_cytotoxic_chemo_ever") is not None:
                raise ValueError("exp_cytotoxic_chemo_ever must be None if exp_cytotoxic_chemo_ever_exist is 'NO'")
            setattr(self, "exp_cytotoxic_chemo_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity37":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity38(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_corticosteroids_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy)?")
    exp_corticosteroids_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity38":
        if getattr(self, "exp_corticosteroids_ever_exist") == YesNo.NO:
            if getattr(self, "exp_corticosteroids_ever") is not None:
                raise ValueError("exp_corticosteroids_ever must be None if exp_corticosteroids_ever_exist is 'NO'")
            setattr(self, "exp_corticosteroids_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity38":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity39(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: non-myelosuppressive therapy can indicate subject's the exposure to non-myelosuppressive anti-cancer agents.
    '''
    exp_anticancer_nonmyelosupp_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to non-myelosuppressive anti-cancer agents?")
    exp_anticancer_nonmyelosupp_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to non-myelosuppressive anti-cancer agents considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity39":
        if getattr(self, "exp_anticancer_nonmyelosupp_ever_exist") == YesNo.NO:
            if getattr(self, "exp_anticancer_nonmyelosupp_ever") is not None:
                raise ValueError("exp_anticancer_nonmyelosupp_ever must be None if exp_anticancer_nonmyelosupp_ever_exist is 'NO'")
            setattr(self, "exp_anticancer_nonmyelosupp_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity39":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity40(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: myelosuppressive therapy can indicate subject's the exposure to myelosuppressive anti-cancer agents.
    '''
    exp_anticancer_myelosupp_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to myelosuppressive anti-cancer agents?")
    exp_anticancer_myelosupp_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to myelosuppressive anti-cancer agents considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity40":
        if getattr(self, "exp_anticancer_myelosupp_ever_exist") == YesNo.NO:
            if getattr(self, "exp_anticancer_myelosupp_ever") is not None:
                raise ValueError("exp_anticancer_myelosupp_ever must be None if exp_anticancer_myelosupp_ever_exist is 'NO'")
            setattr(self, "exp_anticancer_myelosupp_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity40":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity41(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_antibody_drug_conj_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to antibody-drug conjugate?")
    exp_antibody_drug_conj_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to antibody-drug conjugate considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity41":
        if getattr(self, "exp_antibody_drug_conj_ever_exist") == YesNo.NO:
            if getattr(self, "exp_antibody_drug_conj_ever") is not None:
                raise ValueError("exp_antibody_drug_conj_ever must be None if exp_antibody_drug_conj_ever_exist is 'NO'")
            setattr(self, "exp_antibody_drug_conj_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity41":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity42(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_interleukins_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Interleukins, Interferons and Cytokines (not including Hematopoietic Growth Factors)?")
    exp_interleukins_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Interleukins, Interferons and Cytokines considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity42":
        if getattr(self, "exp_interleukins_ever_exist") == YesNo.NO:
            if getattr(self, "exp_interleukins_ever") is not None:
                raise ValueError("exp_interleukins_ever must be None if exp_interleukins_ever_exist is 'NO'")
            setattr(self, "exp_interleukins_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity42":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity43(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_long_acting_gf_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Long-acting growth factor (eg, pegfilgrastim)?")
    exp_long_acting_gf_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Long-acting growth factor considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity43":
        if getattr(self, "exp_long_acting_gf_ever_exist") == YesNo.NO:
            if getattr(self, "exp_long_acting_gf_ever") is not None:
                raise ValueError("exp_long_acting_gf_ever must be None if exp_long_acting_gf_ever_exist is 'NO'")
            setattr(self, "exp_long_acting_gf_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity43":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity44(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_short_acting_gf_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Short-acting growth factor?")
    exp_short_acting_gf_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Short-acting growth factor considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity44":
        if getattr(self, "exp_short_acting_gf_ever_exist") == YesNo.NO:
            if getattr(self, "exp_short_acting_gf_ever") is not None:
                raise ValueError("exp_short_acting_gf_ever must be None if exp_short_acting_gf_ever_exist is 'NO'")
            setattr(self, "exp_short_acting_gf_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity44":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity45(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_rt_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Radiotherapy (RT)?")
    exp_rt_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Radiotherapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity45":
        if getattr(self, "exp_rt_ever_exist") == YesNo.NO:
            if getattr(self, "exp_rt_ever") is not None:
                raise ValueError("exp_rt_ever must be None if exp_rt_ever_exist is 'NO'")
            setattr(self, "exp_rt_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity45":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity46(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_craniospatial_rt_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Craniospinal radiotherapy (RT)?")
    exp_craniospatial_rt_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Craniospinal radiotherapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity46":
        if getattr(self, "exp_craniospatial_rt_ever_exist") == YesNo.NO:
            if getattr(self, "exp_craniospatial_rt_ever") is not None:
                raise ValueError("exp_craniospatial_rt_ever must be None if exp_craniospatial_rt_ever_exist is 'NO'")
            setattr(self, "exp_craniospatial_rt_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity46":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity47(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_tbi_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Total Body Irradiation (TBI)?")
    exp_tbi_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Total Body Irradiation considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity47":
        if getattr(self, "exp_tbi_ever_exist") == YesNo.NO:
            if getattr(self, "exp_tbi_ever") is not None:
                raise ValueError("exp_tbi_ever must be None if exp_tbi_ever_exist is 'NO'")
            setattr(self, "exp_tbi_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity47":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity48(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_radiopharma_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Radiopharmaceutical therapy (e.g., radiolabeled antibody, 131I-MIBG)?")
    exp_radiopharma_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Radiopharmaceutical therapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity48":
        if getattr(self, "exp_radiopharma_ever_exist") == YesNo.NO:
            if getattr(self, "exp_radiopharma_ever") is not None:
                raise ValueError("exp_radiopharma_ever must be None if exp_radiopharma_ever_exist is 'NO'")
            setattr(self, "exp_radiopharma_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity48":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity49(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_hct_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Hematopoietic cell transplantation (HCT)?")
    exp_hct: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Hematopoietic cell transplantation (HCT) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity49":
        if getattr(self, "exp_hct_exist") == YesNo.NO:
            if getattr(self, "exp_hct") is not None:
                raise ValueError("exp_hct must be None if exp_hct_exist is 'NO'")
            setattr(self, "exp_hct", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity49":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity50(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "Allogeneic", "Autologous", "Both"
    '''
    type_transplant_exist: YesNo = Field(..., description="Does the eligibility criteria mention type(s) of transplant?")
    type_transplant: Optional[str] = Field(
        None, 
        description="If so, what type(s) of transplant are considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity50":
        if getattr(self, "type_transplant_exist") == YesNo.NO:
            if getattr(self, "type_transplant") is not None:
                raise ValueError("type_transplant must be None if type_transplant_exist is 'NO'")
            setattr(self, "type_transplant", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity50":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity51(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_dli_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to DLI (donor lymphocyte infusion) or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.)?")
    exp_dli_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to DLI or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity51":
        if getattr(self, "exp_dli_ever_exist") == YesNo.NO:
            if getattr(self, "exp_dli_ever") is not None:
                raise ValueError("exp_dli_ever must be None if exp_dli_ever_exist is 'NO'")
            setattr(self, "exp_dli_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity51":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity52(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_cyp2d6_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP2D6?")
    exp_cyp2d6_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP2D6 considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity52":
        if getattr(self, "exp_cyp2d6_ever_exist") == YesNo.NO:
            if getattr(self, "exp_cyp2d6_ever") is not None:
                raise ValueError("exp_cyp2d6_ever must be None if exp_cyp2d6_ever_exist is 'NO'")
            setattr(self, "exp_cyp2d6_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity52":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity53(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: Consider CYP3A4 and CYP3A as distinct instances.
    '''
    exp_cyp3a4_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A4?")
    exp_cyp3a4_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP3A4 considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity53":
        if getattr(self, "exp_cyp3a4_ever_exist") == YesNo.NO:
            if getattr(self, "exp_cyp3a4_ever") is not None:
                raise ValueError("exp_cyp3a4_ever must be None if exp_cyp3a4_ever_exist is 'NO'")
            setattr(self, "exp_cyp3a4_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity53":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity54(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: Consider CYP3A4 and CYP3A as distinct instances.
    '''
    exp_cyp3a_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A?")
    exp_cyp3a_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP3A considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity54":
        if getattr(self, "exp_cyp3a_ever_exist") == YesNo.NO:
            if getattr(self, "exp_cyp3a_ever") is not None:
                raise ValueError("exp_cyp3a_ever must be None if exp_cyp3a_ever_exist is 'NO'")
            setattr(self, "exp_cyp3a_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity54":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity55(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_calcineurin_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to calcineurin inhibitors?")
    exp_calcineurin_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to calcineurin inhibitors considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity55":
        if getattr(self, "exp_calcineurin_ever_exist") == YesNo.NO:
            if getattr(self, "exp_calcineurin_ever") is not None:
                raise ValueError("exp_calcineurin_ever must be None if exp_calcineurin_ever_exist is 'NO'")
            setattr(self, "exp_calcineurin_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity55":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity56(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_monocl_antib_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to monoclonal antibodies?")
    exp_monocl_antib_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to monoclonal antibodies considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity56":
        if getattr(self, "exp_monocl_antib_ever_exist") == YesNo.NO:
            if getattr(self, "exp_monocl_antib_ever") is not None:
                raise ValueError("exp_monocl_antib_ever must be None if exp_monocl_antib_ever_exist is 'NO'")
            setattr(self, "exp_monocl_antib_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity56":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity57(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_immunotherapy_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to immunotherapy?")
    exp_immunotherapy_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to immunotherapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity57":
        if getattr(self, "exp_immunotherapy_ever_exist") == YesNo.NO:
            if getattr(self, "exp_immunotherapy_ever") is not None:
                raise ValueError("exp_immunotherapy_ever must be None if exp_immunotherapy_ever_exist is 'NO'")
            setattr(self, "exp_immunotherapy_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity57":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity58(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_gpc3_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to GPC3-directed immunotherapy?")
    exp_gpc3_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to GPC3-directed immunotherapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity58":
        if getattr(self, "exp_gpc3_ever_exist") == YesNo.NO:
            if getattr(self, "exp_gpc3_ever") is not None:
                raise ValueError("exp_gpc3_ever must be None if exp_gpc3_ever_exist is 'NO'")
            setattr(self, "exp_gpc3_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity58":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity59(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_demeth_hdac_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Demethylating and/or HDAC Inhibitor Therapy?")
    exp_demeth_hdac_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Demethylating and/or HDAC Inhibitor Therapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity59":
        if getattr(self, "exp_demeth_hdac_ever_exist") == YesNo.NO:
            if getattr(self, "exp_demeth_hdac_ever") is not None:
                raise ValueError("exp_demeth_hdac_ever must be None if exp_demeth_hdac_ever_exist is 'NO'")
            setattr(self, "exp_demeth_hdac_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity59":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity60(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_cd123_cart_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells?")
    exp_cd123_cart: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity60":
        if getattr(self, "exp_cd123_cart_exist") == YesNo.NO:
            if getattr(self, "exp_cd123_cart") is not None:
                raise ValueError("exp_cd123_cart must be None if exp_cd123_cart_exist is 'NO'")
            setattr(self, "exp_cd123_cart", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity60":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity61(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_anthracycline_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to anthracycline or equivalent?")
    exp_anthracycline_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to anthracycline or equivalent considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity61":
        if getattr(self, "exp_anthracycline_ever_exist") == YesNo.NO:
            if getattr(self, "exp_anthracycline_ever") is not None:
                raise ValueError("exp_anthracycline_ever must be None if exp_anthracycline_ever_exist is 'NO'")
            setattr(self, "exp_anthracycline_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity61":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity62(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is 450 mg/m^2, if "total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2"
    '''
    cumul_anthracycline_exist: YesNo = Field(..., description="Does eligibility criteria mention cumulative anthracycline or equivalent?")
    cumul_anthracycline: Optional[str] = Field(
        None, 
        description="If so, how much cumulative anthracycline or equivalent (in mg/m^2) is considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity62":
        if getattr(self, "cumul_anthracycline_exist") == YesNo.NO:
            if getattr(self, "cumul_anthracycline") is not None:
                raise ValueError("cumul_anthracycline must be None if cumul_anthracycline_exist is 'NO'")
            setattr(self, "cumul_anthracycline", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity62":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity63(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    gvhd_exist: YesNo = Field(..., description="Does the eligibility criteria mention presence of graft versus host disease, or GVHD?")
    gvhd: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with presence of graft versus host disease, or GVHD considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity63":
        if getattr(self, "gvhd_exist") == YesNo.NO:
            if getattr(self, "gvhd") is not None:
                raise ValueError("gvhd must be None if gvhd_exist is 'NO'")
            setattr(self, "gvhd", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity63":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity64(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    vpa_meds_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to receiving valproic acid (VPA) therapy?")
    vpa_meds: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to receiving valproic acid therapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity64":
        if getattr(self, "vpa_meds_exist") == YesNo.NO:
            if getattr(self, "vpa_meds") is not None:
                raise ValueError("vpa_meds must be None if vpa_meds_exist is 'NO'")
            setattr(self, "vpa_meds", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity64":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity65(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    prior_solid_organ_transpl_exist: YesNo = Field(..., description="Does the eligibility criteria mention a prior solid organ transplantation?")
    prior_solid_organ_transpl: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a prior solid organ transplantation considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity65":
        if getattr(self, "prior_solid_organ_transpl_exist") == YesNo.NO:
            if getattr(self, "prior_solid_organ_transpl") is not None:
                raise ValueError("prior_solid_organ_transpl must be None if prior_solid_organ_transpl_exist is 'NO'")
            setattr(self, "prior_solid_organ_transpl", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity65":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity66(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_uproleselan_exist: YesNo = Field(..., description="Does the eligibility criteria mention prior exposure to uproleselan?")
    exp_uproleselan: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with prior exposure to uproleselan considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity66":
        if getattr(self, "exp_uproleselan_exist") == YesNo.NO:
            if getattr(self, "exp_uproleselan") is not None:
                raise ValueError("exp_uproleselan must be None if exp_uproleselan_exist is 'NO'")
            setattr(self, "exp_uproleselan", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity66":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity67(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_flotetuzumab_exist: YesNo = Field(..., description="Does the eligibility criteria mention prior exposure to flotetuzumab?")
    exp_flotetuzumab: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with prior exposure to flotetuzumab considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity67":
        if getattr(self, "exp_flotetuzumab_exist") == YesNo.NO:
            if getattr(self, "exp_flotetuzumab") is not None:
                raise ValueError("exp_flotetuzumab must be None if exp_flotetuzumab_exist is 'NO'")
            setattr(self, "exp_flotetuzumab", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity67":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity68(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_venetoclax_exist: YesNo = Field(..., description="Does the eligibility criteria mention prior exposure to venetoclax?")
    exp_venetoclax: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with prior exposure to venetoclax considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity68":
        if getattr(self, "exp_venetoclax_exist") == YesNo.NO:
            if getattr(self, "exp_venetoclax") is not None:
                raise ValueError("exp_venetoclax must be None if exp_venetoclax_exist is 'NO'")
            setattr(self, "exp_venetoclax", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity68":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity69(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_venetoclax_sensitive_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to venetoclax?")
    exp_venetoclax_sensitive: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to venetoclax considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity69":
        if getattr(self, "exp_venetoclax_sensitive_exist") == YesNo.NO:
            if getattr(self, "exp_venetoclax_sensitive") is not None:
                raise ValueError("exp_venetoclax_sensitive must be None if exp_venetoclax_sensitive_exist is 'NO'")
            setattr(self, "exp_venetoclax_sensitive", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity69":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity70(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    donor_available_exist: YesNo = Field(..., description="Does the eligibility criteria mention a suitable stem cell donor available?")
    donor_available: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a suitable stem cell donor available considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity70":
        if getattr(self, "donor_available_exist") == YesNo.NO:
            if getattr(self, "donor_available") is not None:
                raise ValueError("donor_available must be None if donor_available_exist is 'NO'")
            setattr(self, "donor_available", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity70":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity71(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    dyspnea_present_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of dyspnea?")
    dyspnea_present: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of dyspnea considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity71":
        if getattr(self, "dyspnea_present_exist") == YesNo.NO:
            if getattr(self, "dyspnea_present") is not None:
                raise ValueError("dyspnea_present must be None if dyspnea_present_exist is 'NO'")
            setattr(self, "dyspnea_present", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity71":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity72(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    hypoxia_present_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of hypoxia?")
    hypoxia_present: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of hypoxia considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity72":
        if getattr(self, "hypoxia_present_exist") == YesNo.NO:
            if getattr(self, "hypoxia_present") is not None:
                raise ValueError("hypoxia_present must be None if hypoxia_present_exist is 'NO'")
            setattr(self, "hypoxia_present", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity72":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity73(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_msln_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of MSLN expression?")
    expression_msln: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of MSLN expression considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity73":
        if getattr(self, "expression_msln_exist") == YesNo.NO:
            if getattr(self, "expression_msln") is not None:
                raise ValueError("expression_msln must be None if expression_msln_exist is 'NO'")
            setattr(self, "expression_msln", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity73":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity74(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_cd123_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of CD123 expression?")
    expression_cd123: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of CD123 expression considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity74":
        if getattr(self, "expression_cd123_exist") == YesNo.NO:
            if getattr(self, "expression_cd123") is not None:
                raise ValueError("expression_cd123 must be None if expression_cd123_exist is 'NO'")
            setattr(self, "expression_cd123", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity74":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity75(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_eselectin_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of E-selectin expression?")
    expression_eselectin: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of E-selectin expression considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity75":
        if getattr(self, "expression_eselectin_exist") == YesNo.NO:
            if getattr(self, "expression_eselectin") is not None:
                raise ValueError("expression_eselectin must be None if expression_eselectin_exist is 'NO'")
            setattr(self, "expression_eselectin", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity75":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity76(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_kmt2ar_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of KMT2A rearrangement (KMT2Ar)?")
    expression_kmt2ar: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of KMT2Ar considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity76":
        if getattr(self, "expression_kmt2ar_exist") == YesNo.NO:
            if getattr(self, "expression_kmt2ar") is not None:
                raise ValueError("expression_kmt2ar must be None if expression_kmt2ar_exist is 'NO'")
            setattr(self, "expression_kmt2ar", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity76":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity77(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: t(15;17) chromosomal translocation
    '''
    expression_t1517_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of t(15;17) translocation?")
    expression_t1517: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of t(15;17) translocation considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity77":
        if getattr(self, "expression_t1517_exist") == YesNo.NO:
            if getattr(self, "expression_t1517") is not None:
                raise ValueError("expression_t1517 must be None if expression_t1517_exist is 'NO'")
            setattr(self, "expression_t1517", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity77":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity78(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_som_JAK2_V617F_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of somatic JAK2 V617F mutation?")
    expression_som_JAK2_V617F: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of somatic JAK2 V617F mutation considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity78":
        if getattr(self, "expression_som_JAK2_V617F_exist") == YesNo.NO:
            if getattr(self, "expression_som_JAK2_V617F") is not None:
                raise ValueError("expression_som_JAK2_V617F must be None if expression_som_JAK2_V617F_exist is 'NO'")
            setattr(self, "expression_som_JAK2_V617F", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity78":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity79(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_flt3_itd_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of FLT3 / internal tandem duplication (ITD) mutation?")
    expression_flt3_itd: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of FLT3 / internal tandem duplication mutation considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity79":
        if getattr(self, "expression_flt3_itd_exist") == YesNo.NO:
            if getattr(self, "expression_flt3_itd") is not None:
                raise ValueError("expression_flt3_itd must be None if expression_flt3_itd_exist is 'NO'")
            setattr(self, "expression_flt3_itd", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity79":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity80(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "hemophilia", "von Willebrand disease"
    '''
    diag_cong_blood_disorder_exist: YesNo = Field(..., description="Does the eligibility criteria mention any congenital bleeding disorders, including but not limited to hemophilia?")
    diag_cong_blood_disorder: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any congenital bleeding disorders, including but not limited to hemophilia considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity80":
        if getattr(self, "diag_cong_blood_disorder_exist") == YesNo.NO:
            if getattr(self, "diag_cong_blood_disorder") is not None:
                raise ValueError("diag_cong_blood_disorder must be None if diag_cong_blood_disorder_exist is 'NO'")
            setattr(self, "diag_cong_blood_disorder", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity80":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity81(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_intercurrent_illness_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of any significant intercurrent disease?")
    diag_intercurrent_illness: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of any significant intercurrent disease considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity81":
        if getattr(self, "diag_intercurrent_illness_exist") == YesNo.NO:
            if getattr(self, "diag_intercurrent_illness") is not None:
                raise ValueError("diag_intercurrent_illness must be None if diag_intercurrent_illness_exist is 'NO'")
            setattr(self, "diag_intercurrent_illness", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity81":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity82(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: By definition, metastasis to the CNS connotes stage IV cancer and carries a poor prognosis.
    '''
    diag_mets_cns_exist: YesNo = Field(..., description="Does the eligibility criteria mention metastatic CNS involvement?")
    diag_mets_cns: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with metastatic CNS involvement considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity82":
        if getattr(self, "diag_mets_cns_exist") == YesNo.NO:
            if getattr(self, "diag_mets_cns") is not None:
                raise ValueError("diag_mets_cns must be None if diag_mets_cns_exist is 'NO'")
            setattr(self, "diag_mets_cns", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity82":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity83(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_hemolytic_anemia_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of hemolytic anemia?")
    diag_hemolytic_anemia: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of hemolytic anemia considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity83":
        if getattr(self, "diag_hemolytic_anemia_exist") == YesNo.NO:
            if getattr(self, "diag_hemolytic_anemia") is not None:
                raise ValueError("diag_hemolytic_anemia must be None if diag_hemolytic_anemia_exist is 'NO'")
            setattr(self, "diag_hemolytic_anemia", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity83":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity84(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_evans_syndrome_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Evans syndrome?")
    diag_evans_syndrome: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Evans syndrome considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity84":
        if getattr(self, "diag_evans_syndrome_exist") == YesNo.NO:
            if getattr(self, "diag_evans_syndrome") is not None:
                raise ValueError("diag_evans_syndrome must be None if diag_evans_syndrome_exist is 'NO'")
            setattr(self, "diag_evans_syndrome", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity84":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity85(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_uncontrolled_cardiac_rhythm_exist: YesNo = Field(..., description="Does the eligibility criteria mention uncontrolled cardiac rhythm disturbance?")
    diag_uncontrolled_cardiac_rhythm: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with uncontrolled cardiac rhythm disturbance considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity85":
        if getattr(self, "diag_uncontrolled_cardiac_rhythm_exist") == YesNo.NO:
            if getattr(self, "diag_uncontrolled_cardiac_rhythm") is not None:
                raise ValueError("diag_uncontrolled_cardiac_rhythm must be None if diag_uncontrolled_cardiac_rhythm_exist is 'NO'")
            setattr(self, "diag_uncontrolled_cardiac_rhythm", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity85":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity86(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: severe mental illness includes schizophrenia, schizoaffective disorder, schizophreniform disorder, bipolar I disorder, and major depression with psychotic features. These disorders often include psychosis as a component.
    '''
    diag_severe_psychiatric_disorder_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of acute or chronic severe psychiatric disorders?")
    diag_severe_psychiatric_disorder: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of acute or chronic severe psychiatric disorders considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity86":
        if getattr(self, "diag_severe_psychiatric_disorder_exist") == YesNo.NO:
            if getattr(self, "diag_severe_psychiatric_disorder") is not None:
                raise ValueError("diag_severe_psychiatric_disorder must be None if diag_severe_psychiatric_disorder_exist is 'NO'")
            setattr(self, "diag_severe_psychiatric_disorder", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity86":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity87(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_other_malignancies_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of other malignancies?")
    diag_other_malignancies: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of other malignancies considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity87":
        if getattr(self, "diag_other_malignancies_exist") == YesNo.NO:
            if getattr(self, "diag_other_malignancies") is not None:
                raise ValueError("diag_other_malignancies must be None if diag_other_malignancies_exist is 'NO'")
            setattr(self, "diag_other_malignancies", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity87":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity88(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_pneumonitis_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of pneumonitis?")
    diag_pneumonitis: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of pneumonitis considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity88":
        if getattr(self, "diag_pneumonitis_exist") == YesNo.NO:
            if getattr(self, "diag_pneumonitis") is not None:
                raise ValueError("diag_pneumonitis must be None if diag_pneumonitis_exist is 'NO'")
            setattr(self, "diag_pneumonitis", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity88":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity89(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_mibg_avidity_exist: YesNo = Field(..., description="Does the eligibility criteria mention indications of tumor(s) / lesion(s) with known MIBG avidity?")
    diag_mibg_avidity: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with indications of tumor(s) / lesion(s) with known MIBG avidity considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity89":
        if getattr(self, "diag_mibg_avidity_exist") == YesNo.NO:
            if getattr(self, "diag_mibg_avidity") is not None:
                raise ValueError("diag_mibg_avidity must be None if diag_mibg_avidity_exist is 'NO'")
            setattr(self, "diag_mibg_avidity", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity89":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity90(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: FDG avidity refers to the ability of cells or tissues to accumulate fluorodeoxyglucose (FDG), a radioactive sugar analog, when imaged with a Positron Emission Tomography (PET) scan.
    '''
    diag_fdg_avidity_exist: YesNo = Field(..., description="Does the eligibility criteria mention tumor(s) / lesion(s) with known FDG avidity?")
    diag_fdg_avidity: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with tumor(s) / lesion(s) with known FDG avidity considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity90":
        if getattr(self, "diag_fdg_avidity_exist") == YesNo.NO:
            if getattr(self, "diag_fdg_avidity") is not None:
                raise ValueError("diag_fdg_avidity must be None if diag_fdg_avidity_exist is 'NO'")
            setattr(self, "diag_fdg_avidity", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity90":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity91(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_signif_pleural_effusion_exist: YesNo = Field(..., description="Does the eligibility criteria mention clinically significant, symptomatic, pleural effusions?")
    diag_signif_pleural_effusion: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with clinically significant, symptomatic, pleural effusions considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity91":
        if getattr(self, "diag_signif_pleural_effusion_exist") == YesNo.NO:
            if getattr(self, "diag_signif_pleural_effusion") is not None:
                raise ValueError("diag_signif_pleural_effusion must be None if diag_signif_pleural_effusion_exist is 'NO'")
            setattr(self, "diag_signif_pleural_effusion", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity91":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity92(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_signif_pericardial_effusion_exist: YesNo = Field(..., description="Does the eligibility criteria mention physiologically significant pericardial effusion?")
    diag_signif_pericardial_effusion: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with physiologically significant pericardial effusion considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity92":
        if getattr(self, "diag_signif_pericardial_effusion_exist") == YesNo.NO:
            if getattr(self, "diag_signif_pericardial_effusion") is not None:
                raise ValueError("diag_signif_pericardial_effusion must be None if diag_signif_pericardial_effusion_exist is 'NO'")
            setattr(self, "diag_signif_pericardial_effusion", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity92":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity93(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: measurable disease: a tumor that can be accurately measured in size. 
    '''
    diag_measureable_disease_exist: YesNo = Field(..., description="Does the eligibility criteria mention the patient having measurable disease?")
    diag_measureable_disease: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with measurable disease considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity93":
        if getattr(self, "diag_measureable_disease_exist") == YesNo.NO:
            if getattr(self, "diag_measureable_disease") is not None:
                raise ValueError("diag_measureable_disease must be None if diag_measureable_disease_exist is 'NO'")
            setattr(self, "diag_measureable_disease", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity93":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity94(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: measurable disease: a tumor that can be accurately measured in size. 
    '''
    diag_measureable_tumor_exist: YesNo = Field(..., description="Does the eligibility criteria mention the patient having one or more tumor / lesion sites with measurable dimensions?")
    diag_measureable_tumor: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with one or more tumor / lesion sites with measurable dimensions considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity94":
        if getattr(self, "diag_measureable_tumor_exist") == YesNo.NO:
            if getattr(self, "diag_measureable_tumor") is not None:
                raise ValueError("diag_measureable_tumor must be None if diag_measureable_tumor_exist is 'NO'")
            setattr(self, "diag_measureable_tumor", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity94":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity95(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    diag_primary_immunodeficiency_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of primary immunodeficiency?")
    diag_primary_immunodeficiency: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with a diagnosis of primary immunodeficiency considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity95":
        if getattr(self, "diag_primary_immunodeficiency_exist") == YesNo.NO:
            if getattr(self, "diag_primary_immunodeficiency") is not None:
                raise ValueError("diag_primary_immunodeficiency must be None if diag_primary_immunodeficiency_exist is 'NO'")
            setattr(self, "diag_primary_immunodeficiency", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity95":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity96(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_cellular_therapy_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell])?")
    exp_cellular_therapy: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell]) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity96":
        if getattr(self, "exp_cellular_therapy_exist") == YesNo.NO:
            if getattr(self, "exp_cellular_therapy") is not None:
                raise ValueError("exp_cellular_therapy must be None if exp_cellular_therapy_exist is 'NO'")
            setattr(self, "exp_cellular_therapy", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity96":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity97(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_ch14_18_sensitive_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0)?")
    exp_ch14_18_sensitive: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity97":
        if getattr(self, "exp_ch14_18_sensitive_exist") == YesNo.NO:
            if getattr(self, "exp_ch14_18_sensitive") is not None:
                raise ValueError("exp_ch14_18_sensitive must be None if exp_ch14_18_sensitive_exist is 'NO'")
            setattr(self, "exp_ch14_18_sensitive", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity97":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity98(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_anti_gd2_sensitive_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab)?")
    exp_anti_gd2_sensitive: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity98":
        if getattr(self, "exp_anti_gd2_sensitive_exist") == YesNo.NO:
            if getattr(self, "exp_anti_gd2_sensitive") is not None:
                raise ValueError("exp_anti_gd2_sensitive must be None if exp_anti_gd2_sensitive_exist is 'NO'")
            setattr(self, "exp_anti_gd2_sensitive", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity98":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity99(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_hu5f9g4_sensitive_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody?")
    exp_hu5f9g4_sensitive: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity99":
        if getattr(self, "exp_hu5f9g4_sensitive_exist") == YesNo.NO:
            if getattr(self, "exp_hu5f9g4_sensitive") is not None:
                raise ValueError("exp_hu5f9g4_sensitive must be None if exp_hu5f9g4_sensitive_exist is 'NO'")
            setattr(self, "exp_hu5f9g4_sensitive", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity99":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity100(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_gm_csf_sensitive_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO)?")
    exp_gm_csf_sensitive: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO) considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity100":
        if getattr(self, "exp_gm_csf_sensitive_exist") == YesNo.NO:
            if getattr(self, "exp_gm_csf_sensitive") is not None:
                raise ValueError("exp_gm_csf_sensitive must be None if exp_gm_csf_sensitive_exist is 'NO'")
            setattr(self, "exp_gm_csf_sensitive", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity100":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity101(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "Nivolumab"
    '''
    exp_pd1_pdl_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies (e.g. Nivolumab)?")
    exp_pd1_pdl_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity101":
        if getattr(self, "exp_pd1_pdl_ever_exist") == YesNo.NO:
            if getattr(self, "exp_pd1_pdl_ever") is not None:
                raise ValueError("exp_pd1_pdl_ever must be None if exp_pd1_pdl_ever_exist is 'NO'")
            setattr(self, "exp_pd1_pdl_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity101":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity102(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "anti-CTLA-4", "Ipilimumab (Yervoy)", "tremelimumab (Imjuno)"
    '''
    exp_anti_ctla4_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to any anti-CTLA4 agent?")
    exp_anti_ctla4_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to any anti-CTLA4 agent considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity102":
        if getattr(self, "exp_anti_ctla4_ever_exist") == YesNo.NO:
            if getattr(self, "exp_anti_ctla4_ever") is not None:
                raise ValueError("exp_anti_ctla4_ever must be None if exp_anti_ctla4_ever_exist is 'NO'")
            setattr(self, "exp_anti_ctla4_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity102":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity103(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_lorlatinib_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to lorlatinib?")
    exp_lorlatinib_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to lorlatinib considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity103":
        if getattr(self, "exp_lorlatinib_ever_exist") == YesNo.NO:
            if getattr(self, "exp_lorlatinib_ever") is not None:
                raise ValueError("exp_lorlatinib_ever must be None if exp_lorlatinib_ever_exist is 'NO'")
            setattr(self, "exp_lorlatinib_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity103":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity104(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_cd47_sirpalpha_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to any CD47–SIRPα-targeted therapeutics?")
    exp_cd47_sirpalpha_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to any CD47–SIRPα-targeted therapeutics considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity104":
        if getattr(self, "exp_cd47_sirpalpha_ever_exist") == YesNo.NO:
            if getattr(self, "exp_cd47_sirpalpha_ever") is not None:
                raise ValueError("exp_cd47_sirpalpha_ever must be None if exp_cd47_sirpalpha_ever_exist is 'NO'")
            setattr(self, "exp_cd47_sirpalpha_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity104":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity105(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    exp_ivig_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Intravenous Immunoglobulin (IVIg) therapy?")
    exp_ivig_ever: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with any prior exposure to  Intravenous Immunoglobulin (IVIg) therapy considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity105":
        if getattr(self, "exp_ivig_ever_exist") == YesNo.NO:
            if getattr(self, "exp_ivig_ever") is not None:
                raise ValueError("exp_ivig_ever must be None if exp_ivig_ever_exist is 'NO'")
            setattr(self, "exp_ivig_ever", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity105":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity106(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: the answer is > 54 mCi/kg, if "treated with iodine-131 (131I)-MIBG who have already received a cumulative I-131 dose > 54 mCi/kg or who would exceed 54 mCi/kg by participating"
    '''
    cumul_131l_mibg_exist: YesNo = Field(..., description="Does the eligibility criteria mention cumulative 131I-MIBG dosing?")
    cumul_131l_mibg: Optional[str] = Field(
        None, 
        description="If so, how much cumulative 131I-MIBG dosing (in mCi/kg) is considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity106":
        if getattr(self, "cumul_131l_mibg_exist") == YesNo.NO:
            if getattr(self, "cumul_131l_mibg") is not None:
                raise ValueError("cumul_131l_mibg must be None if cumul_131l_mibg_exist is 'NO'")
            setattr(self, "cumul_131l_mibg", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity106":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity107(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_alk_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of ALK mutation?")
    expression_alk: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of ALK mutation considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity107":
        if getattr(self, "expression_alk_exist") == YesNo.NO:
            if getattr(self, "expression_alk") is not None:
                raise ValueError("expression_alk must be None if expression_alk_exist is 'NO'")
            setattr(self, "expression_alk", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity107":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity108(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "Rearrangement (ALK-R)", "Amplification (ALK-A)", "Point mutation"
    '''
    expression_alk_type_exist: YesNo = Field(..., description="Does the eligibility criteria mention types of ALK mutations?")
    expression_alk_type: Optional[str] = Field(
        None, 
        description="If so, what types of ALK mutations are considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity108":
        if getattr(self, "expression_alk_type_exist") == YesNo.NO:
            if getattr(self, "expression_alk_type") is not None:
                raise ValueError("expression_alk_type must be None if expression_alk_type_exist is 'NO'")
            setattr(self, "expression_alk_type", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity108":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity109(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "Stage 0", "Stage A", "Stage B", "Stage C", "Stage D"
    '''
    bclc_stage_exist: YesNo = Field(..., description="Does the eligibility criteria mention BCLC stage?")
    bclc_stage: Optional[str] = Field(
        None, 
        description="If so, what BCLC stages are considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity109":
        if getattr(self, "bclc_stage_exist") == YesNo.NO:
            if getattr(self, "bclc_stage") is not None:
                raise ValueError("bclc_stage must be None if bclc_stage_exist is 'NO'")
            setattr(self, "bclc_stage", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity109":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity110(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
Example: "Child-Pugh A": 5 to 6 points; "Child-Pugh B": 7 to 9 points; "Child-Pugh C": 10 to 15 points
    '''
    ctp_score_exist: YesNo = Field(..., description="Does the eligibility criteria mention Child-Pugh-Turcotte score?")
    ctp_score: Optional[int] = Field(
        None, 
        description="If so, what Child-Pugh-Turcotte score is considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity110":
        if getattr(self, "ctp_score_exist") == YesNo.NO:
            if getattr(self, "ctp_score") is not None:
                raise ValueError("ctp_score must be None if ctp_score_exist is 'NO'")
            setattr(self, "ctp_score", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity110":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

class Entity111(BaseModel):
    '''
    Extracted from the clinical trial eligibility document.
    '''
    expression_gpc3_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of GPC3 expression?")
    expression_gpc3: Optional[YesNo] = Field(
        None, 
        description="If so, is a patient with evidence of GPC3 expression considered to be included? ")
    answer_facts: List[Fact] = Field(..., description="Exact fact quotes from the note supporting the answer.")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity111":
        if getattr(self, "expression_gpc3_exist") == YesNo.NO:
            if getattr(self, "expression_gpc3") is not None:
                raise ValueError("expression_gpc3 must be None if expression_gpc3_exist is 'NO'")
            setattr(self, "expression_gpc3", None)
            self.answer_facts = []
        return self
  
    @model_validator(mode='after')
    def validate_sources(self) -> "Entity111":
        self.answer_facts = [fact for fact in self.answer_facts if len(fact.substring_quote) > 0]
        return self

