
from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationInfo, field_validator
from typing import Optional, List, Tuple, Literal
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

class Type_transplant(Enum):
    ALLOGENEIC = "Allogeneic"
    AUTOLOGOUS = "Autologous"

class YesNo(Enum):
    YES = "Yes"
    NO = "No"

class Entity0(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: if "Age =< 21", minimum age of eligibility is 0
    '''
    age_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention the minimum age of eligibility?")
    age_min: int = Field(
        ..., 
        description="If so, what is the minimum age of eligibility (in years) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity0":
        if getattr(self, "age_min_exist") == YesNo.NO:
            setattr(self, "age_min", None)
        return self

class Entity1(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    age_max_exist: YesNo = Field(..., description="Does the eligibility criteria mention the maximum age of eligibility?")
    age_max: int = Field(
        ..., 
        description="If so, what is the maximum age of eligibility (in years) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity1":
        if getattr(self, "age_max_exist") == YesNo.NO:
            setattr(self, "age_max", None)
        return self

class Entity2(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    weight_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention the minimum weight a patient may have?")
    weight_min: int = Field(
        ..., 
        description="If so, what is the minimum weight (in kilograms) of a patient considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity2":
        if getattr(self, "weight_min_exist") == YesNo.NO:
            setattr(self, "weight_min", None)
        return self

class Entity3(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    weight_max_exist: YesNo = Field(..., description="Does the eligibility criteria mention the maximum weight a patient may have?")
    weight_max: int = Field(
        ..., 
        description="If so, what is the maximum weight (in kilograms) of a patient considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity3":
        if getattr(self, "weight_max_exist") == YesNo.NO:
            setattr(self, "weight_max", None)
        return self

class Entity4(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    sex_exist: YesNo = Field(..., description="Does the eligibility criteria mention sexes of a patient?")
    sex: List[str] = Field(
        ..., 
        description="If so, which sexes with condition are considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity4":
        if getattr(self, "sex_exist") == YesNo.NO:
            setattr(self, "sex", None)
        return self

class Entity5(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diagnosis_exist: YesNo = Field(..., description="Does the eligibility criteria mention a patient's current diagnoses?")
    diagnosis: List[Diagnosis] = Field(
        ..., 
        description="If so, which diagnoses are considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity5":
        if getattr(self, "diagnosis_exist") == YesNo.NO:
            setattr(self, "diagnosis", None)
        return self

class Entity6(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: refractory disease are diseases such as "Refractory leukemia"
    '''
    ever_refractory_exist: YesNo = Field(..., description="Does the eligibility criteria mention refractory disease?")
    ever_refractory: YesNo = Field(
        ..., 
        description="If so, is a patient with refractory disease considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity6":
        if getattr(self, "ever_refractory_exist") == YesNo.NO:
            setattr(self, "ever_refractory", None)
        return self

class Entity7(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: If the text mentions **refractory disease** without a clear count (e.g., "1 episode", "2 relapses"), return `count_refractory = ">=1"`.
	    - DO NOT infer the count of refractory disease based on:
	      - Number of chemotherapy cycles
	      - Number of salvage or induction therapy courses
	      - Phrases like “refractory to at least one course of therapy”
	
	    Example:
	    - "Refractory to 2 prior regimens" → return ">=1"
	    - "Had 2 relapses after being refractory" → return "2"
    '''
    count_refractory_exist: YesNo = Field(..., description="Does the eligibility criteria mention the occurrence of refractory disease?")
    count_refractory: str = Field(
        ..., 
        description="If so, how many occurrences of refractory disease are required to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity7":
        if getattr(self, "count_refractory_exist") == YesNo.NO:
            setattr(self, "count_refractory", None)
        return self

class Entity8(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is "1" if "refractory to at least one course of salvage therapy";
	the answer is "2" if "persistent after at least two courses of induction "chemotherapy"; 
	the answer is "2" if "refractory disease after >= 2 cycles of chemotherapy"
    '''
    current_refractory_num_cycles_exist: YesNo = Field(..., description="Does the eligibility criteria mention number of cycles of therapy required for refractory disease?")
    current_refractory_num_cycles: int = Field(
        ..., 
        description="If so, what is the minimum number of cycles of therapy required for refractory disease considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity8":
        if getattr(self, "current_refractory_num_cycles_exist") == YesNo.NO:
            setattr(self, "current_refractory_num_cycles", None)
        return self

class Entity9(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: relapse disease such as "relapsed leukemia"
    '''
    ever_relapse_exist: YesNo = Field(..., description="Does the eligibility criteria mention confirmed or suspected relapse disease?")
    ever_relapse: YesNo = Field(
        ..., 
        description="If so, is confirmed or suspected relapse disease considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity9":
        if getattr(self, "ever_relapse_exist") == YesNo.NO:
            setattr(self, "ever_relapse", None)
        return self

class Entity10(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is ">=2" if "Second or greater relapse"; 
	the answer is ">=1" if only mention the presence of "Relapsed" disease; 
	the answer is "1" if "first relapses";
	"≥ 2 cycles of chemotherapy" or "at least two courses of induction chemotherapy" is not related to count of relapse;
    '''
    count_relapse_exist: YesNo = Field(..., description="Does the eligibility criteria mention the number of relapses of the patient?")
    count_relapse: str = Field(
        ..., 
        description="If so, what is the minimum number of relapses required to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity10":
        if getattr(self, "count_relapse_exist") == YesNo.NO:
            setattr(self, "count_relapse", None)
        return self

class Entity11(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is 5 if ">= 5% blasts in the bone marrow", the answer is 5 if "> 5% blasts in the BM" is mentioned
    '''
    bm_recent_blast_pct_meas_exist: YesNo = Field(..., description="Does the eligibility criteria mention bone marrow blast percentage?")
    bm_recent_blast_pct_meas: int = Field(
        ..., 
        description="If so, what is the minimum bone marrow blast percentage considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity11":
        if getattr(self, "bm_recent_blast_pct_meas_exist") == YesNo.NO:
            setattr(self, "bm_recent_blast_pct_meas", None)
        return self

class Entity12(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "Morphology", "Flow cytometry"; None, if no specific method is mentioned.
    '''
    bm_recent_blast_method_exist: YesNo = Field(..., description="Does the eligibility criteria mention methods for bone marrow blast percentage assessment?")
    bm_recent_blast_method: List[Bm_recent_blast_method] = Field(
        ..., 
        description="If so, what are the required methods for bone marrow blast percentage assessment considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity12":
        if getattr(self, "bm_recent_blast_method_exist") == YesNo.NO:
            setattr(self, "bm_recent_blast_method", None)
        return self

class Entity13(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "leukemia with >= 5% blasts in the peripheral blood": No mention of the absolute blast count in peripheral blood.
    '''
    periph_blood_blast_abs_meas_exist: YesNo = Field(..., description="Does the eligibility criteria mention the absolute blast count in peripheral blood?")
    periph_blood_blast_abs_meas: int = Field(
        ..., 
        description="If so, what is the absolute blast count in peripheral blood measurement (in cells/microliter) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity13":
        if getattr(self, "periph_blood_blast_abs_meas_exist") == YesNo.NO:
            setattr(self, "periph_blood_blast_abs_meas", None)
        return self

class Entity14(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is 5 if ">= 5% blasts in the peripheral blood" is mentioned, the answer is 5 if ">=5% blasts in the blood" is mentioned
    '''
    periph_blood_blast_pct_meas_exist: YesNo = Field(..., description="Does the eligibility criteria mention the peripheral blood blast percentage?")
    periph_blood_blast_pct_meas: int = Field(
        ..., 
        description="If so, what is the minimum peripheral blood blast percentage considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity14":
        if getattr(self, "periph_blood_blast_pct_meas_exist") == YesNo.NO:
            setattr(self, "periph_blood_blast_pct_meas", None)
        return self

class Entity15(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    corneal_epitheliopathy_exist: YesNo = Field(..., description="Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy?")
    corneal_epitheliopathy: YesNo = Field(
        ..., 
        description="If so, is a patient with such diagnosis considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity15":
        if getattr(self, "corneal_epitheliopathy_exist") == YesNo.NO:
            setattr(self, "corneal_epitheliopathy", None)
        return self

class Entity16(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: CNS-1 was defined as the absence of blasts on cytospin preparation, regardless of the number of white blood cells (WBCs). 
	For CNS-2 it was the presence of <5/μL WBCs and cytospin positive for blasts or ≥5/μL WBCs with negative Steinherz-Bleyer algorithm. 
	For CNS-3, the presence of ≥5/μL WBCs and cytospin positive for blasts and/or clinical signs of CNS leukemia (such as facial nerve palsy, brain/eye involvement, or hypothalamic syndrome) were considered.
	CNS 1: WBCs/μL ≤5, RBCs/μL <10, Leukemic blasts: Absent
	CNS 2: WBCs/μL ≤5, RBCs/μL <10, Leukemic blasts: Present
	CNS 3: WBCs/μL >5, RBCs/μL <10, Leukemic blasts: Present
	If no indication of the CNS status, return No even though CNS is mentioned.
    '''
    cns_status_exist: YesNo = Field(..., description="Does the eligibility criteria mention CNS status?")
    cns_status: List[Cns_status] = Field(
        ..., 
        description="If so, what CNS status is considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity16":
        if getattr(self, "cns_status_exist") == YesNo.NO:
            setattr(self, "cns_status", None)
        return self

class Entity17(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is 70 if "Lansky score>=70" is mentioned
    '''
    lansky_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention Lansky score?")
    lansky_min: int = Field(
        ..., 
        description="If so, what is the minimum Lansky score for a patient considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity17":
        if getattr(self, "lansky_min_exist") == YesNo.NO:
            setattr(self, "lansky_min", None)
        return self

class Entity18(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is 50 if "Karnofsky score >= 50" is mentioned
    '''
    karnofsky_min_exist: YesNo = Field(..., description="Does the eligibility criteria mention Karnofsky score?")
    karnofsky_min: int = Field(
        ..., 
        description="If so, what is the minimum Karnofsky score for a patient considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity18":
        if getattr(self, "karnofsky_min_exist") == YesNo.NO:
            setattr(self, "karnofsky_min", None)
        return self

class Entity19(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_down_syndrome_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Down syndrome?")
    diag_down_syndrome: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of Down syndrome considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity19":
        if getattr(self, "diag_down_syndrome_exist") == YesNo.NO:
            setattr(self, "diag_down_syndrome", None)
        return self

class Entity20(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Treat "active cerebral/meningeal disease" and "isolated extramedullary disease" as distinct conditions. Do not infer the existence of "diag_iso_emd_exist" solely based on mention of cerebral or meningeal disease.
    '''
    diag_iso_emd_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of isolated extramedullary disease (i.e. the absence of bone marrow involvement)?")
    diag_iso_emd: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of isolated extramedullary disease considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity20":
        if getattr(self, "diag_iso_emd_exist") == YesNo.NO:
            setattr(self, "diag_iso_emd", None)
        return self

class Entity21(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_iso_testes_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of isolated testicular relapse?")
    diag_iso_testes: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of isolated testicular relapse considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity21":
        if getattr(self, "diag_iso_testes_exist") == YesNo.NO:
            setattr(self, "diag_iso_testes", None)
        return self

class Entity22(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_ataxia_telang_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of ataxia-telangiectasia?")
    diag_ataxia_telang: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of ataxia-telangiectasia considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity22":
        if getattr(self, "diag_ataxia_telang_exist") == YesNo.NO:
            setattr(self, "diag_ataxia_telang", None)
        return self

class Entity23(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_bloom_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Bloom syndrome?")
    diag_bloom: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of Bloom syndrome considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity23":
        if getattr(self, "diag_bloom_exist") == YesNo.NO:
            setattr(self, "diag_bloom", None)
        return self

class Entity24(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: 1. Do **NOT** infer or assume Fanconi anemia based on general terms like "bone marrow failure syndromes" or "inherited bone marrow disorders".
	2. ONLY return `diag_fanconi_exist = "Yes"` if **"Fanconi anemia"** is **explicitly and unambiguously** mentioned in the eligibility text.
    '''
    diag_fanconi_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Fanconi anemia?")
    diag_fanconi: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of Fanconi anemia considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity24":
        if getattr(self, "diag_fanconi_exist") == YesNo.NO:
            setattr(self, "diag_fanconi", None)
        return self

class Entity25(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_kostmann_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Kostmann syndrome?")
    diag_kostmann: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of Kostmann syndrome considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity25":
        if getattr(self, "diag_kostmann_exist") == YesNo.NO:
            setattr(self, "diag_kostmann", None)
        return self

class Entity26(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_shwachman_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Shwachman syndrome?")
    diag_shwachman: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of Shwachman syndrome considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity26":
        if getattr(self, "diag_shwachman_exist") == YesNo.NO:
            setattr(self, "diag_shwachman", None)
        return self

class Entity27(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_cong_bmf_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)?")
    diag_cong_bmf: YesNo = Field(
        ..., 
        description="If so, is a patient with such diagnosis considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity27":
        if getattr(self, "diag_cong_bmf_exist") == YesNo.NO:
            setattr(self, "diag_cong_bmf", None)
        return self

class Entity28(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "Impairment of GI function or GI disease" does not infer malabsorption syndrome.
    '''
    diag_malabsoption_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of malabsorption syndrome?")
    diag_malabsoption: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of malabsorption syndrome considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity28":
        if getattr(self, "diag_malabsoption_exist") == YesNo.NO:
            setattr(self, "diag_malabsoption", None)
        return self

class Entity29(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_chf_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of congestive heart failure (CHF)?")
    diag_chf: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of congestive heart failure considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity29":
        if getattr(self, "diag_chf_exist") == YesNo.NO:
            setattr(self, "diag_chf", None)
        return self

class Entity30(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_hiv_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of human immunodeficiency virus (HIV) infection?")
    diag_hiv: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of human immunodeficiency virus infection considered be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity30":
        if getattr(self, "diag_hiv_exist") == YesNo.NO:
            setattr(self, "diag_hiv", None)
        return self

class Entity31(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_uncontr_cns_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis)?")
    diag_uncontr_cns: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity31":
        if getattr(self, "diag_uncontr_cns_exist") == YesNo.NO:
            setattr(self, "diag_uncontr_cns", None)
        return self

class Entity32(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_hep_b_c_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of hepatitis B or hepatitis C infection?")
    diag_hep_b_c: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of hepatitis B or hepatitis C infection considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity32":
        if getattr(self, "diag_hep_b_c_exist") == YesNo.NO:
            setattr(self, "diag_hep_b_c", None)
        return self

class Entity33(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_liver_cirr_serious_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of liver cirrhosis or other serious liver disease?")
    diag_liver_cirr_serious: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of liver cirrhosis or other serious liver disease considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity33":
        if getattr(self, "diag_liver_cirr_serious_exist") == YesNo.NO:
            setattr(self, "diag_liver_cirr_serious", None)
        return self

class Entity34(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "Uncontrolled infection" is an active infection.
    '''
    active_infection_exist: YesNo = Field(..., description="Does the eligibility criteria mention an active, uncontrolled infection?")
    active_infection: YesNo = Field(
        ..., 
        description="If so, is a patient with an active, uncontrolled infection considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity34":
        if getattr(self, "active_infection_exist") == YesNo.NO:
            setattr(self, "active_infection", None)
        return self

class Entity35(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    refractory_transfusion_exist: YesNo = Field(..., description="Does the eligibility criteria mention a patient known to be refractory to red blood cells or platelet transfusions?")
    refractory_transfusion: YesNo = Field(
        ..., 
        description="If so, is a patient known to be refractory to red blood cells or platelet transfusions considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity35":
        if getattr(self, "refractory_transfusion_exist") == YesNo.NO:
            setattr(self, "refractory_transfusion", None)
        return self

class Entity36(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    cerebellar_toxicity_exist: YesNo = Field(..., description="Does the eligibility criteria mention an history of cerebellar toxicity or cerebellar neurological findings on exam?")
    cerebellar_toxicity: str = Field(
        ..., 
        description="If so, is a patient with a history of cerebellar toxicity or cerebellar neurological findings on exam considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity36":
        if getattr(self, "cerebellar_toxicity_exist") == YesNo.NO:
            setattr(self, "cerebellar_toxicity", None)
        return self

class Entity37(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: You must NOT infer "cytotoxic chemotherapy" from the presence of terms like:
	    - "Chemotherapy"
	    - "Radiotherapy"
	    - "Investigational therapy"
	    - "Induction chemotherapy"
	    - "Salvage therapy"
	
	    Only return `exp_cytotoxic_chemo_ever_exist = Yes` if the text **explicitly uses** the term "cytotoxic chemotherapy".
	
	    If only generic or ambiguous therapy terms are used (e.g., "chemotherapy" or "salvage therapy"), return `No`.
	
	    This overrides any clinical assumptions.
    '''
    exp_cytotoxic_chemo_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)?")
    exp_cytotoxic_chemo_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity37":
        if getattr(self, "exp_cytotoxic_chemo_ever_exist") == YesNo.NO:
            setattr(self, "exp_cytotoxic_chemo_ever", None)
        return self

class Entity38(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_corticosteroids_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy)?")
    exp_corticosteroids_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity38":
        if getattr(self, "exp_corticosteroids_ever_exist") == YesNo.NO:
            setattr(self, "exp_corticosteroids_ever", None)
        return self

class Entity39(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: 1. non-myelosuppressive therapy can indicate subject's the exposure to non-myelosuppressive anti-cancer agents.
	2. Cytarabine and hydroxyurea are not non-myelosuppressive agents.
    '''
    exp_anticancer_nonmyelosupp_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to non-myelosuppressive anti-cancer agents?")
    exp_anticancer_nonmyelosupp_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to non-myelosuppressive anti-cancer agents considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity39":
        if getattr(self, "exp_anticancer_nonmyelosupp_ever_exist") == YesNo.NO:
            setattr(self, "exp_anticancer_nonmyelosupp_ever", None)
        return self

class Entity40(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: myelosuppressive therapy can indicate subject's the exposure to myelosuppressive anti-cancer agents.
    '''
    exp_anticancer_myelosupp_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to myelosuppressive anti-cancer agents?")
    exp_anticancer_myelosupp_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to myelosuppressive anti-cancer agents considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity40":
        if getattr(self, "exp_anticancer_myelosupp_ever_exist") == YesNo.NO:
            setattr(self, "exp_anticancer_myelosupp_ever", None)
        return self

class Entity41(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_antibody_drug_conj_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to antibody-drug conjugate?")
    exp_antibody_drug_conj_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to antibody-drug conjugate considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity41":
        if getattr(self, "exp_antibody_drug_conj_ever_exist") == YesNo.NO:
            setattr(self, "exp_antibody_drug_conj_ever", None)
        return self

class Entity42(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_interleukins_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Interleukins, Interferons and Cytokines (not including Hematopoietic Growth Factors)?")
    exp_interleukins_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Interleukins, Interferons and Cytokines considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity42":
        if getattr(self, "exp_interleukins_ever_exist") == YesNo.NO:
            setattr(self, "exp_interleukins_ever", None)
        return self

class Entity43(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_long_acting_gf_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Long-acting growth factor (eg, pegfilgrastim)?")
    exp_long_acting_gf_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Long-acting growth factor considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity43":
        if getattr(self, "exp_long_acting_gf_ever_exist") == YesNo.NO:
            setattr(self, "exp_long_acting_gf_ever", None)
        return self

class Entity44(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_short_acting_gf_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Short-acting growth factor?")
    exp_short_acting_gf_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Short-acting growth factor considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity44":
        if getattr(self, "exp_short_acting_gf_ever_exist") == YesNo.NO:
            setattr(self, "exp_short_acting_gf_ever", None)
        return self

class Entity45(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Patients "Received anticancer therapy (chemotherapy, immunotherapy, radiotherapy, or investigational therapy) within 2 weeks prior to starting study treatment." should be excluded.
    '''
    exp_rt_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Radiotherapy (RT)?")
    exp_rt_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Radiotherapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity45":
        if getattr(self, "exp_rt_ever_exist") == YesNo.NO:
            setattr(self, "exp_rt_ever", None)
        return self

class Entity46(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_craniospatial_rt_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Craniospinal radiotherapy (RT)?")
    exp_craniospatial_rt_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Craniospinal radiotherapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity46":
        if getattr(self, "exp_craniospatial_rt_ever_exist") == YesNo.NO:
            setattr(self, "exp_craniospatial_rt_ever", None)
        return self

class Entity47(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: 1. Do **NOT** infer or assume Total Body Irradiation (TBI) based on general terms like "severe brain injuries".
	2. ONLY return `exp_tbi_ever = "Yes"` if **"Total Body Irradiation"** or **"TBI"**is **explicitly and unambiguously** mentioned in the eligibility text.
    '''
    exp_tbi_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Total Body Irradiation (TBI)?")
    exp_tbi_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Total Body Irradiation considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity47":
        if getattr(self, "exp_tbi_ever_exist") == YesNo.NO:
            setattr(self, "exp_tbi_ever", None)
        return self

class Entity48(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_radiopharma_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Radiopharmaceutical therapy (e.g., radiolabeled antibody, 131I-MIBG)?")
    exp_radiopharma_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Radiopharmaceutical therapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity48":
        if getattr(self, "exp_radiopharma_ever_exist") == YesNo.NO:
            setattr(self, "exp_radiopharma_ever", None)
        return self

class Entity49(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Return Yes if "HCT" or "Hematopoietic cell transplantation" is explicitly mentioned in the criteria text. Otherwise, return No.
    '''
    exp_hct_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Hematopoietic cell transplantation (HCT)?")
    exp_hct: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Hematopoietic cell transplantation (HCT) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity49":
        if getattr(self, "exp_hct_exist") == YesNo.NO:
            setattr(self, "exp_hct", None)
        return self

class Entity50(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Return Yes for `type_transplant_exist` only if the eligibility criteria explicitly mention the type of transplant as "Allogeneic" or "Autologous".
	If only generic terms like "Hematopoietic Cell Transplantation" (HCT)" are mentioned without specifying the type, return No for `type_transplant_exist`.
    '''
    type_transplant_exist: YesNo = Field(..., description="Does the eligibility criteria mention type(s) of HCT transplant?")
    type_transplant: List[Type_transplant] = Field(
        ..., 
        description="If so, what type(s) of transplant are considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity50":
        if getattr(self, "type_transplant_exist") == YesNo.NO:
            setattr(self, "type_transplant", None)
        return self

class Entity51(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_dli_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to DLI (donor lymphocyte infusion) or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.)?")
    exp_dli_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to DLI or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity51":
        if getattr(self, "exp_dli_ever_exist") == YesNo.NO:
            setattr(self, "exp_dli_ever", None)
        return self

class Entity52(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_cyp2d6_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP2D6?")
    exp_cyp2d6_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP2D6 considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity52":
        if getattr(self, "exp_cyp2d6_ever_exist") == YesNo.NO:
            setattr(self, "exp_cyp2d6_ever", None)
        return self

class Entity53(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Treat "CYP3A4" and "CYP3A" as distinct entities. Do not conflate them — CYP3A4 refers to a specific isoenzyme, whereas CYP3A refers to a broader enzyme family;
	- Mark "Yes" for CYP3A4 only if it is explicitly mentioned.
	- Do not infer CYP3A4 based on CYP3A mention.
    '''
    exp_cyp3a4_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A4?")
    exp_cyp3a4_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP3A4 considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity53":
        if getattr(self, "exp_cyp3a4_ever_exist") == YesNo.NO:
            setattr(self, "exp_cyp3a4_ever", None)
        return self

class Entity54(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Consider CYP3A4 and CYP3A as distinct instances.
    '''
    exp_cyp3a_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A?")
    exp_cyp3a_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP3A considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity54":
        if getattr(self, "exp_cyp3a_ever_exist") == YesNo.NO:
            setattr(self, "exp_cyp3a_ever", None)
        return self

class Entity55(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_calcineurin_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to calcineurin inhibitors?")
    exp_calcineurin_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to calcineurin inhibitors considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity55":
        if getattr(self, "exp_calcineurin_ever_exist") == YesNo.NO:
            setattr(self, "exp_calcineurin_ever", None)
        return self

class Entity56(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_monocl_antib_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to monoclonal antibodies?")
    exp_monocl_antib_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to monoclonal antibodies considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity56":
        if getattr(self, "exp_monocl_antib_ever_exist") == YesNo.NO:
            setattr(self, "exp_monocl_antib_ever", None)
        return self

class Entity57(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_immunotherapy_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to immunotherapy?")
    exp_immunotherapy_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to immunotherapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity57":
        if getattr(self, "exp_immunotherapy_ever_exist") == YesNo.NO:
            setattr(self, "exp_immunotherapy_ever", None)
        return self

class Entity58(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_gpc3_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to GPC3-directed immunotherapy?")
    exp_gpc3_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to GPC3-directed immunotherapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity58":
        if getattr(self, "exp_gpc3_ever_exist") == YesNo.NO:
            setattr(self, "exp_gpc3_ever", None)
        return self

class Entity59(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_demeth_hdac_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Demethylating and/or HDAC Inhibitor Therapy?")
    exp_demeth_hdac_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to Demethylating and/or HDAC Inhibitor Therapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity59":
        if getattr(self, "exp_demeth_hdac_ever_exist") == YesNo.NO:
            setattr(self, "exp_demeth_hdac_ever", None)
        return self

class Entity60(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_cd123_cart_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells?")
    exp_cd123_cart: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity60":
        if getattr(self, "exp_cd123_cart_exist") == YesNo.NO:
            setattr(self, "exp_cd123_cart", None)
        return self

class Entity61(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_anthracycline_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to anthracycline or equivalent?")
    exp_anthracycline_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to anthracycline or equivalent considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity61":
        if getattr(self, "exp_anthracycline_ever_exist") == YesNo.NO:
            setattr(self, "exp_anthracycline_ever", None)
        return self

class Entity62(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is 450 mg/m^2, if "total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2"
    '''
    cumul_anthracycline_exist: YesNo = Field(..., description="Does eligibility criteria mention cumulative anthracycline or equivalent?")
    cumul_anthracycline: str = Field(
        ..., 
        description="If so, how much cumulative anthracycline or equivalent (in mg/m^2) is considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity62":
        if getattr(self, "cumul_anthracycline_exist") == YesNo.NO:
            setattr(self, "cumul_anthracycline", None)
        return self

class Entity63(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    gvhd_exist: YesNo = Field(..., description="Does the eligibility criteria mention presence of graft versus host disease, or GVHD?")
    gvhd: YesNo = Field(
        ..., 
        description="If so, is a patient with presence of graft versus host disease, or GVHD considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity63":
        if getattr(self, "gvhd_exist") == YesNo.NO:
            setattr(self, "gvhd", None)
        return self

class Entity64(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    vpa_meds_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to receiving valproic acid (VPA) therapy?")
    vpa_meds: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to receiving valproic acid therapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity64":
        if getattr(self, "vpa_meds_exist") == YesNo.NO:
            setattr(self, "vpa_meds", None)
        return self

class Entity65(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    prior_solid_organ_transpl_exist: YesNo = Field(..., description="Does the eligibility criteria mention a prior solid organ transplantation?")
    prior_solid_organ_transpl: YesNo = Field(
        ..., 
        description="If so, is a patient with a prior solid organ transplantation considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity65":
        if getattr(self, "prior_solid_organ_transpl_exist") == YesNo.NO:
            setattr(self, "prior_solid_organ_transpl", None)
        return self

class Entity66(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_uproleselan_exist: YesNo = Field(..., description="Does the eligibility criteria mention prior exposure to uproleselan?")
    exp_uproleselan: YesNo = Field(
        ..., 
        description="If so, is a patient with prior exposure to uproleselan considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity66":
        if getattr(self, "exp_uproleselan_exist") == YesNo.NO:
            setattr(self, "exp_uproleselan", None)
        return self

class Entity67(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_flotetuzumab_exist: YesNo = Field(..., description="Does the eligibility criteria mention prior exposure to flotetuzumab?")
    exp_flotetuzumab: YesNo = Field(
        ..., 
        description="If so, is a patient with prior exposure to flotetuzumab considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity67":
        if getattr(self, "exp_flotetuzumab_exist") == YesNo.NO:
            setattr(self, "exp_flotetuzumab", None)
        return self

class Entity68(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_venetoclax_exist: YesNo = Field(..., description="Does the eligibility criteria mention prior exposure to venetoclax?")
    exp_venetoclax: YesNo = Field(
        ..., 
        description="If so, is a patient with prior exposure to venetoclax considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity68":
        if getattr(self, "exp_venetoclax_exist") == YesNo.NO:
            setattr(self, "exp_venetoclax", None)
        return self

class Entity69(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_venetoclax_sensitive_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to venetoclax?")
    exp_venetoclax_sensitive: YesNo = Field(
        ..., 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to venetoclax considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity69":
        if getattr(self, "exp_venetoclax_sensitive_exist") == YesNo.NO:
            setattr(self, "exp_venetoclax_sensitive", None)
        return self

class Entity70(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    donor_available_exist: YesNo = Field(..., description="Does the eligibility criteria mention a suitable stem cell donor available?")
    donor_available: YesNo = Field(
        ..., 
        description="If so, is a patient with a suitable stem cell donor available considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity70":
        if getattr(self, "donor_available_exist") == YesNo.NO:
            setattr(self, "donor_available", None)
        return self

class Entity71(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    dyspnea_present_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of dyspnea?")
    dyspnea_present: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of dyspnea considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity71":
        if getattr(self, "dyspnea_present_exist") == YesNo.NO:
            setattr(self, "dyspnea_present", None)
        return self

class Entity72(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    hypoxia_present_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of hypoxia?")
    hypoxia_present: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of hypoxia considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity72":
        if getattr(self, "hypoxia_present_exist") == YesNo.NO:
            setattr(self, "hypoxia_present", None)
        return self

class Entity73(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_msln_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of MSLN expression?")
    expression_msln: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of MSLN expression considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity73":
        if getattr(self, "expression_msln_exist") == YesNo.NO:
            setattr(self, "expression_msln", None)
        return self

class Entity74(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_cd123_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of CD123 expression?")
    expression_cd123: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of CD123 expression considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity74":
        if getattr(self, "expression_cd123_exist") == YesNo.NO:
            setattr(self, "expression_cd123", None)
        return self

class Entity75(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_eselectin_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of E-selectin expression?")
    expression_eselectin: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of E-selectin expression considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity75":
        if getattr(self, "expression_eselectin_exist") == YesNo.NO:
            setattr(self, "expression_eselectin", None)
        return self

class Entity76(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_kmt2ar_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of KMT2A rearrangement (KMT2Ar)?")
    expression_kmt2ar: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of KMT2Ar considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity76":
        if getattr(self, "expression_kmt2ar_exist") == YesNo.NO:
            setattr(self, "expression_kmt2ar", None)
        return self

class Entity77(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: 1. t(15;17) is chromosomal translocation
	2. Do **NOT** infer or assume t(15;17) translocation based on general terms like "acute promyelocytic leukemia".
	3. ONLY return `expression_t1517 = ""Yes""` if **"t(15;17) translocation"** is **explicitly and unambiguously** mentioned in the eligibility text.
    '''
    expression_t1517_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of t(15;17) translocation?")
    expression_t1517: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of t(15;17) translocation considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity77":
        if getattr(self, "expression_t1517_exist") == YesNo.NO:
            setattr(self, "expression_t1517", None)
        return self

class Entity78(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_som_JAK2_V617F_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of somatic JAK2 V617F mutation?")
    expression_som_JAK2_V617F: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of somatic JAK2 V617F mutation considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity78":
        if getattr(self, "expression_som_JAK2_V617F_exist") == YesNo.NO:
            setattr(self, "expression_som_JAK2_V617F", None)
        return self

class Entity79(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_flt3_itd_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of FLT3 / internal tandem duplication (ITD) mutation?")
    expression_flt3_itd: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of FLT3 / internal tandem duplication mutation considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity79":
        if getattr(self, "expression_flt3_itd_exist") == YesNo.NO:
            setattr(self, "expression_flt3_itd", None)
        return self

class Entity80(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Congenital bleeding disorders including "hemophilia" and "von Willebrand disease"
    '''
    diag_cong_blood_disorder_exist: YesNo = Field(..., description="Does the eligibility criteria mention any congenital bleeding disorders, including but not limited to hemophilia?")
    diag_cong_blood_disorder: YesNo = Field(
        ..., 
        description="If so, is a patient with any congenital bleeding disorders, including but not limited to hemophilia considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity80":
        if getattr(self, "diag_cong_blood_disorder_exist") == YesNo.NO:
            setattr(self, "diag_cong_blood_disorder", None)
        return self

class Entity81(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: 1. Do NOT infer intercurrent illness from related clinical conditions (e.g., 'uncontrolled infection', 'sepsis', 'hepatic disease'). 
	2. Only return `diag_intercurrent_illness_exist = "Yes"` if "intercurrent" is **explicitly** mentioned in the text.
	3. The presence of 'uncontrolled infection' does NOT qualify as an intercurrent illness. This overrides any clinical assumptions.
    '''
    diag_intercurrent_illness_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of any significant intercurrent disease?")
    diag_intercurrent_illness: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of any significant intercurrent disease considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity81":
        if getattr(self, "diag_intercurrent_illness_exist") == YesNo.NO:
            setattr(self, "diag_intercurrent_illness", None)
        return self

class Entity82(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: By definition, metastasis to the CNS connotes stage IV cancer and carries a poor prognosis.
    '''
    diag_mets_cns_exist: YesNo = Field(..., description="Does the eligibility criteria mention metastatic CNS involvement?")
    diag_mets_cns: YesNo = Field(
        ..., 
        description="If so, is a patient with metastatic CNS involvement considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity82":
        if getattr(self, "diag_mets_cns_exist") == YesNo.NO:
            setattr(self, "diag_mets_cns", None)
        return self

class Entity83(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_hemolytic_anemia_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of hemolytic anemia?")
    diag_hemolytic_anemia: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of hemolytic anemia considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity83":
        if getattr(self, "diag_hemolytic_anemia_exist") == YesNo.NO:
            setattr(self, "diag_hemolytic_anemia", None)
        return self

class Entity84(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_evans_syndrome_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of Evans syndrome?")
    diag_evans_syndrome: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of Evans syndrome considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity84":
        if getattr(self, "diag_evans_syndrome_exist") == YesNo.NO:
            setattr(self, "diag_evans_syndrome", None)
        return self

class Entity85(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_uncontrolled_cardiac_rhythm_exist: YesNo = Field(..., description="Does the eligibility criteria mention uncontrolled cardiac rhythm disturbance?")
    diag_uncontrolled_cardiac_rhythm: YesNo = Field(
        ..., 
        description="If so, is a patient with uncontrolled cardiac rhythm disturbance considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity85":
        if getattr(self, "diag_uncontrolled_cardiac_rhythm_exist") == YesNo.NO:
            setattr(self, "diag_uncontrolled_cardiac_rhythm", None)
        return self

class Entity86(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: severe mental illness includes schizophrenia, schizoaffective disorder, schizophreniform disorder, bipolar I disorder, and major depression with psychotic features. These disorders often include psychosis as a component.
    '''
    diag_severe_psychiatric_disorder_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of acute or chronic severe psychiatric disorders?")
    diag_severe_psychiatric_disorder: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of acute or chronic severe psychiatric disorders considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity86":
        if getattr(self, "diag_severe_psychiatric_disorder_exist") == YesNo.NO:
            setattr(self, "diag_severe_psychiatric_disorder", None)
        return self

class Entity87(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_other_malignancies_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of other malignancies?")
    diag_other_malignancies: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of other malignancies considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity87":
        if getattr(self, "diag_other_malignancies_exist") == YesNo.NO:
            setattr(self, "diag_other_malignancies", None)
        return self

class Entity88(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_pneumonitis_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of pneumonitis?")
    diag_pneumonitis: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of pneumonitis considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity88":
        if getattr(self, "diag_pneumonitis_exist") == YesNo.NO:
            setattr(self, "diag_pneumonitis", None)
        return self

class Entity89(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_mibg_avidity_exist: YesNo = Field(..., description="Does the eligibility criteria mention indications of tumor(s) / lesion(s) with known MIBG avidity?")
    diag_mibg_avidity: YesNo = Field(
        ..., 
        description="If so, is a patient with indications of tumor(s) / lesion(s) with known MIBG avidity considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity89":
        if getattr(self, "diag_mibg_avidity_exist") == YesNo.NO:
            setattr(self, "diag_mibg_avidity", None)
        return self

class Entity90(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: FDG avidity refers to the ability of cells or tissues to accumulate fluorodeoxyglucose (FDG), a radioactive sugar analog, when imaged with a Positron Emission Tomography (PET) scan.
    '''
    diag_fdg_avidity_exist: YesNo = Field(..., description="Does the eligibility criteria mention tumor(s) / lesion(s) with known FDG avidity?")
    diag_fdg_avidity: YesNo = Field(
        ..., 
        description="If so, is a patient with tumor(s) / lesion(s) with known FDG avidity considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity90":
        if getattr(self, "diag_fdg_avidity_exist") == YesNo.NO:
            setattr(self, "diag_fdg_avidity", None)
        return self

class Entity91(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_signif_pleural_effusion_exist: YesNo = Field(..., description="Does the eligibility criteria mention clinically significant, symptomatic, pleural effusions?")
    diag_signif_pleural_effusion: YesNo = Field(
        ..., 
        description="If so, is a patient with clinically significant, symptomatic, pleural effusions considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity91":
        if getattr(self, "diag_signif_pleural_effusion_exist") == YesNo.NO:
            setattr(self, "diag_signif_pleural_effusion", None)
        return self

class Entity92(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_signif_pericardial_effusion_exist: YesNo = Field(..., description="Does the eligibility criteria mention physiologically significant pericardial effusion?")
    diag_signif_pericardial_effusion: YesNo = Field(
        ..., 
        description="If so, is a patient with physiologically significant pericardial effusion considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity92":
        if getattr(self, "diag_signif_pericardial_effusion_exist") == YesNo.NO:
            setattr(self, "diag_signif_pericardial_effusion", None)
        return self

class Entity93(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Only return "Yes" if a tumor lesion that can be measured in physical dimensions is mentioned. Quantification of cell percentage alone (e.g., leukemia blasts) is not sufficient.
    '''
    diag_measureable_disease_exist: YesNo = Field(..., description="Does the eligibility criteria mention the patient having measurable disease?")
    diag_measureable_disease: YesNo = Field(
        ..., 
        description="If so, is a patient with measurable disease considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity93":
        if getattr(self, "diag_measureable_disease_exist") == YesNo.NO:
            setattr(self, "diag_measureable_disease", None)
        return self

class Entity94(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Only return "Yes" if a disease with a tumor that can be accurately measured in size mentioned. Otherwise, return "No"
    '''
    diag_measureable_tumor_exist: YesNo = Field(..., description="Does the eligibility criteria mention the patient having one or more tumor / lesion sites with measurable dimensions?")
    diag_measureable_tumor: YesNo = Field(
        ..., 
        description="If so, is a patient with one or more tumor / lesion sites with measurable dimensions considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity94":
        if getattr(self, "diag_measureable_tumor_exist") == YesNo.NO:
            setattr(self, "diag_measureable_tumor", None)
        return self

class Entity95(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    diag_primary_immunodeficiency_exist: YesNo = Field(..., description="Does the eligibility criteria mention a diagnosis of primary immunodeficiency?")
    diag_primary_immunodeficiency: YesNo = Field(
        ..., 
        description="If so, is a patient with a diagnosis of primary immunodeficiency considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity95":
        if getattr(self, "diag_primary_immunodeficiency_exist") == YesNo.NO:
            setattr(self, "diag_primary_immunodeficiency", None)
        return self

class Entity96(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Only return "Yes" if prior exposure to live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell]) is explicitly mentioned. Otherwise, return "No".
    '''
    exp_cellular_therapy_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell])?")
    exp_cellular_therapy: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell]) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity96":
        if getattr(self, "exp_cellular_therapy_exist") == YesNo.NO:
            setattr(self, "exp_cellular_therapy", None)
        return self

class Entity97(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Only return "Yes" if ch14.18 (e.g., CHO or SP2/0) monoclonal antibody is explicitly mentioned. Otherwise, return "No".
    '''
    exp_ch14_18_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0)?")
    exp_ch14_18: YesNo = Field(
        ..., 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity97":
        if getattr(self, "exp_ch14_18_exist") == YesNo.NO:
            setattr(self, "exp_ch14_18", None)
        return self

class Entity98(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_anti_gd2_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab)?")
    exp_anti_gd2: YesNo = Field(
        ..., 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity98":
        if getattr(self, "exp_anti_gd2_exist") == YesNo.NO:
            setattr(self, "exp_anti_gd2", None)
        return self

class Entity99(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: Only return "Yes" if previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody is explicitly mentioned. Otherwise, return "No".
    '''
    exp_hu5f9g4_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody?")
    exp_hu5f9g4: YesNo = Field(
        ..., 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity99":
        if getattr(self, "exp_hu5f9g4_exist") == YesNo.NO:
            setattr(self, "exp_hu5f9g4", None)
        return self

class Entity100(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_gm_csf_exist: YesNo = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO)?")
    exp_gm_csf: YesNo = Field(
        ..., 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO) considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity100":
        if getattr(self, "exp_gm_csf_exist") == YesNo.NO:
            setattr(self, "exp_gm_csf", None)
        return self

class Entity101(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "Nivolumab"
    '''
    exp_pd1_pdl_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies (e.g. Nivolumab)?")
    exp_pd1_pdl_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity101":
        if getattr(self, "exp_pd1_pdl_ever_exist") == YesNo.NO:
            setattr(self, "exp_pd1_pdl_ever", None)
        return self

class Entity102(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "anti-CTLA-4", "Ipilimumab (Yervoy)", "tremelimumab (Imjuno)"
    '''
    exp_anti_ctla4_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to any anti-CTLA4 agent?")
    exp_anti_ctla4_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to any anti-CTLA4 agent considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity102":
        if getattr(self, "exp_anti_ctla4_ever_exist") == YesNo.NO:
            setattr(self, "exp_anti_ctla4_ever", None)
        return self

class Entity103(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_lorlatinib_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to lorlatinib?")
    exp_lorlatinib_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to lorlatinib considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity103":
        if getattr(self, "exp_lorlatinib_ever_exist") == YesNo.NO:
            setattr(self, "exp_lorlatinib_ever", None)
        return self

class Entity104(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_cd47_sirpalpha_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to any CD47–SIRPα-targeted therapeutics?")
    exp_cd47_sirpalpha_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to any CD47–SIRPα-targeted therapeutics considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity104":
        if getattr(self, "exp_cd47_sirpalpha_ever_exist") == YesNo.NO:
            setattr(self, "exp_cd47_sirpalpha_ever", None)
        return self

class Entity105(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    exp_ivig_ever_exist: YesNo = Field(..., description="Does the eligibility criteria mention any prior exposure to Intravenous Immunoglobulin (IVIg) therapy?")
    exp_ivig_ever: YesNo = Field(
        ..., 
        description="If so, is a patient with any prior exposure to  Intravenous Immunoglobulin (IVIg) therapy considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity105":
        if getattr(self, "exp_ivig_ever_exist") == YesNo.NO:
            setattr(self, "exp_ivig_ever", None)
        return self

class Entity106(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: the answer is > 54 mCi/kg, if "treated with iodine-131 (131I)-MIBG who have already received a cumulative I-131 dose > 54 mCi/kg or who would exceed 54 mCi/kg by participating"
    '''
    cumul_131l_mibg_exist: YesNo = Field(..., description="Does the eligibility criteria mention cumulative 131I-MIBG dosing?")
    cumul_131l_mibg: str = Field(
        ..., 
        description="If so, how much cumulative 131I-MIBG dosing (in mCi/kg) is considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity106":
        if getattr(self, "cumul_131l_mibg_exist") == YesNo.NO:
            setattr(self, "cumul_131l_mibg", None)
        return self

class Entity107(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_alk_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of ALK mutation?")
    expression_alk: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of ALK mutation considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity107":
        if getattr(self, "expression_alk_exist") == YesNo.NO:
            setattr(self, "expression_alk", None)
        return self

class Entity108(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "Rearrangement (ALK-R)", "Amplification (ALK-A)", "Point mutation"
    '''
    expression_alk_type_exist: YesNo = Field(..., description="Does the eligibility criteria mention types of ALK mutations?")
    expression_alk_type: str = Field(
        ..., 
        description="If so, what types of ALK mutations are considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity108":
        if getattr(self, "expression_alk_type_exist") == YesNo.NO:
            setattr(self, "expression_alk_type", None)
        return self

class Entity109(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "Stage 0", "Stage A", "Stage B", "Stage C", "Stage D"
    '''
    bclc_stage_exist: YesNo = Field(..., description="Does the eligibility criteria mention BCLC stage?")
    bclc_stage: str = Field(
        ..., 
        description="If so, what BCLC stages are considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity109":
        if getattr(self, "bclc_stage_exist") == YesNo.NO:
            setattr(self, "bclc_stage", None)
        return self

class Entity110(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
	CRITICAL EXTRACTION RULES: "Child-Pugh A": 5 to 6 points; "Child-Pugh B": 7 to 9 points; "Child-Pugh C": 10 to 15 points
    '''
    ctp_score_exist: YesNo = Field(..., description="Does the eligibility criteria mention Child-Pugh-Turcotte score?")
    ctp_score: int = Field(
        ..., 
        description="If so, what Child-Pugh-Turcotte score is considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity110":
        if getattr(self, "ctp_score_exist") == YesNo.NO:
            setattr(self, "ctp_score", None)
        return self

class Entity111(BaseModel):
    '''
    Extracted from the clinical trial eligibility document. Think step-by-step.
    '''
    expression_gpc3_exist: YesNo = Field(..., description="Does the eligibility criteria mention evidence of GPC3 expression?")
    expression_gpc3: YesNo = Field(
        ..., 
        description="If so, is a patient with evidence of GPC3 expression considered to be included? ")

    @model_validator(mode="after")
    def skip_if_not_exist(self, info: ValidationInfo) -> "Entity111":
        if getattr(self, "expression_gpc3_exist") == YesNo.NO:
            setattr(self, "expression_gpc3", None)
        return self

