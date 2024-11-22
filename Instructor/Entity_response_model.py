from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationInfo, ConfigDict
from typing import Optional, List, TypeVar
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
  MDSAML = "Myelodysplastic syndrome (MDS) who have progressed to AML"
  TAML = "Treatment-related acute myeloid leukemia (tAML)"
  TALL = "T-cell acute lymphoblastic leukemia (T-ALL)"
  ALL = "Acute lymphoblastic leukemia (ALL)"
  KMT2AALL = "KMT2A acute lymphoblastic leukemia (KMT2A-ALL)"
  ETPALL = "Early T-cell precursor acute lymphoblastic leukemia (ETP-ALL)"
  ALAL = "Ambiguous lineage acute leukemia (ALAL)"

class Bm_recent_blast_method(Enum):
  MORPHOLOGY = "Morphology"
  FLOWCYTOMETRY = "Flow cytometry"

class Type_transplant(Enum):
  ALLOGENEIC = "Allogeneic"
  AUTOLOGOUS = "Autologous"

class Expression_alk_type(Enum):
  ALKR = "Rearrangement (ALK-R)"
  ALKA = "Amplification (ALK-A)"
  POINTMUTATION = "Point mutation"

class Yes_no(Enum):
  YES = "Yes"
  NO = "No"

class test(BaseModel):
  age_min: Optional[Yes_no] = Field(...,description="Do the eligibility criteria mention the minimum age? ")
  
  # diag_cong_bmf_fact: str = Field(..., description="The fact that indicates whether the eligibility criteria mentions a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome). Note: just 'bone marrow' does not count.")
  # diag_cong_bmf: Optional[Yes_no] = Field(
  #   None, 
  #   description='Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)?')
  # diag_malabsoption_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions a diagnosis of malabsorption syndrome')
  # diag_malabsoption: Optional[Yes_no] = Field(
  #   None, 
  #   description='Does the eligibility criteria mention a diagnosis of malabsorption syndrome?')

class Demographic(BaseModel):
  age_min: Optional[int] = Field(
    None, 
    description='What is the minimum age of eligibility (in years)?')
  age_max: Optional[int] = Field(
    None, 
    description='What is the maximum age of eligibility (in years)?')
  weight_min: Optional[int] = Field(
    None, 
    description='What is the minimum weight a patient may have and still be eligibile (in kilograms)?')
  weight_max: Optional[int] = Field(
    None, 
    description='What is the maximum weight a patient may have and still be eligibile (in kilograms)?')
  sex: Optional[List[Sex]] = Field(
    None, 
    description='Which sexes are eligible in the eligibility criteria?')
  diagnosis: Optional[List[Diagnosis]] = Field(
    None, 
    description='Which diagnoses are eligible in this clinical trial?')

class Refractory_Relapse(BaseModel):
  ever_refractory_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions refractory disease')
  ever_refractory: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention refractory disease? Example: refractory disease are diseases such as "refractory leukemia"')
  
  count_refractory_fact: str = Field(..., description='The fact that indicates the number of occurrences of refractory disease required for eligibility')
  count_refractory: Optional[int] = Field(
    None, 
    description='The number of occurrences of refractory disease are required for eligibility?')
  
  current_refractory_num_cycles_fact: str = Field(..., description='The fact that indicates the minimum number of cycles of therapy required for refractory disease mentioned in the eligibility criteria')
  current_refractory_num_cycles: Optional[int] = Field(
    None, 
    description='What is the minimum number of cycles of therapy required for refractory disease mentioned in the eligibility criteria? Example: the answer is 1 if "refractory to at least one course of salvage therapy", the answer is 2 if "persistent after at least two courses of induction "chemotherapy", the answer is 2 if "refractory disease after >= 2 cycles of chemotherapy"')
 
  ever_relapse_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions relapse disease')
  ever_relapse: Optional[Yes_no] = Field(
    None, 
    description='Is confirmed or suspected relapse disease mentioned in the eligibility criteria? Example: relapse diesease are diseases such as "relapsed leukemia"')
  
  count_relapse_fact: str = Field(..., description='The fact that indicates the minimum number of occurrences of relapse disease required for eligibility')
  count_relapse: Optional[int] = Field(
    None, 
    description='What is the minimum number of relapses required for eilgibility? Example: the answer is 2 if "Second or greater relapses", the answer is 1 if "first relapse"')

  model_config = ConfigDict(
      json_schema_extra={
          "examples": [
              {
                  "ever_refractory_fact": "Refractory leukemia, defined as persistent leukemia after at least two courses of induction chemotherapy",
                  "ever_refractory": "Yes",
                  "count_refractory_fact": "Refractory leukemia, defined as persistent leukemia after at least two courses of induction chemotherapy",
                  "count_refractory": None,
                  "current_refractory_num_cycles_fact": "Refractory leukemia, defined as persistent leukemia after at least two courses of induction chemotherapy",
                  "current_refractory_num_cycles": 2,
                  "ever_relapse_fact": "Disease relapse or the presence of refractory disease after ≥ 2 cycles of chemotherapy must be documented",
                  "ever_relapse": "Yes",
                  "count_relapse_fact": "Disease relapse or the presence of refractory disease after ≥ 2 cycles of chemotherapy must be documented",
                  "count_relapse": 2
              },
          ]
      }
  )

class Blast(BaseModel):
  bm_recent_blast_pct_meas_fact: str = Field(..., description='The fact that indicates the bone marrow blast percentage mentioned in the eligibility criteria')
  bm_recent_blast_pct_meas: Optional[int] = Field(
    None, 
    description='What is the minimum bone marrow blast percentage mentioned in the eligibility criteria? Example: the answer is 5 if ">= 5% blasts in the bone marrow", the answer is 5 if "> 5% blasts in the BM" is mentioned')
  
  bm_recent_blast_method_fact: str = Field(..., description='The fact that indicates the method for bone marrow blast percentage assessment mentioned in the eligibility criteria')
  bm_recent_blast_method: Optional[List[Bm_recent_blast_method]] = Field(
    None, 
    description='What are the required methods for bone marrow blast percentage assessment mentioned in the eligibility criteria?')
  
  periph_blood_blast_abs_meas_fact: str = Field(..., description='The fact that indicates the peripheral blood absolute blast count measurement (in cells/microliter) mentioned in the eligibility criteria')
  periph_blood_blast_abs_meas: Optional[int] = Field(
    None, 
    description='What is the peripheral blood absolute blast count measurement (in cells/microliter) mentioned in the eligibility criteria?')
  
  periph_blood_blast_pct_meas_fact: str = Field(..., description='The fact that indicates the peripheral blood blast percentage mentioned in the eligibility criteria')
  periph_blood_blast_pct_meas: Optional[int] = Field(
    None, 
    description='What is the minimum defined peripheral blood blast percentage mentioned in the eligibility criteria? Example: the answer is 5 if ">= 5% blasts in the peripheral blood" is mentioned, the answer is 5 if ">=5% blasts in the blood" is mentioned')  
  
  model_config = ConfigDict(
      json_schema_extra={
          "examples": [
              {
                  "bm_recent_blast_method_fact": "bone marrow (BM) examination",
                  "bm_recent_blast_method": None,
              },
          ]
      }
  )

class Diagnosis(BaseModel):
  corneal_epitheliopathy: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy?')
  cns_status: Optional[str] = Field(
    None, 
    description='What CNS status is mentioned in the eligibility criteria? Example: "CNS 1", "CNS 2", "CNS 3"')
  lanksy_min: Optional[int] = Field(
    None, 
    description='What is the minimum Lansky score a patient must have to be eligible? Example: the answer is 70 if "Lansky score>=70" is mentioned')
  karnofksy_min: Optional[int] = Field(
    None, 
    description='What is the minimum Karnofsky score a patient must have to be eligible? Example: the answer is 50 if "Karnofsky score >= 50" is mentioned')
  diag_down_syndrome: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of Down syndrome?')
  diag_iso_emd: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of isolated extramedullary disease (i.e. the absence of bone marrow involvement)?')
  diag_iso_testes: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of isolated testicular relapse?')
  diag_ataxia_telang: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of ataxia-telangiectasia?')
  diag_bloom: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of Bloom syndrome?')
  diag_fanconi: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of Fanconi anemia?')
  diag_kostmann: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of Kostmann syndrome?')
  diag_shwachman: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of Shwachman syndrome?')
  diag_cong_bmf_fact: str = Field(..., description="The fact that indicates whether the eligibility criteria mentions a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome). Note: just 'bone marrow' does not count.")
  diag_cong_bmf: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)?')
  diag_malabsoption_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions a diagnosis of malabsorption syndrome')
  diag_malabsoption: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of malabsorption syndrome?')
  diag_chf: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of congestive heart failure (CHF)?')
  diag_hiv: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of human immunodeficiency virus (HIV) infection?')
  diag_uncontr_cns: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis)?')
  diag_hep_b_c: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of hepatitis B or C infection?')
  diag_liver_cirr_serious: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of liver cirrhosis or other serious liver disease?')
  active_infection: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a documented active, uncontrolled infection?')
  refractory_transfusion: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention being refractory to red blood cells or platelet transfusions?')
  cerebellar_toxicity: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention an history of cerebellar toxicity or cerebellar neurological findings on exam?')
  exp_cytotoxic_chemo_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)')
  exp_cytotoxic_chemo_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)?')
  exp_corticosteroids_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy)?')
  exp_anticancer_nonmyelosupp_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions any prior exposure to non-myelosuppressive anti-cancer agents')
  exp_anticancer_nonmyelosupp_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to non-myelosuppressive anti-cancer agents?')
  exp_anticancer_myelosupp_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions any prior exposure to myelosuppressive anti-cancer agents')
  exp_anticancer_myelosupp_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to myelosuppressive anti-cancer agents?')
  exp_antibody_drug_conj_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to antibody-drug conjugate?')
  exp_interleukins_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Interleukins, Interferons and Cytokines (not including Hematopoietic Growth Factors)?')
  exp_long_acting_gf_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Long-acting growth factor (eg, pegfilgrastim)?')
  exp_short_acting_gf_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Short-acting growth factor?')
  exp_rt_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Radiotherapy (RT)?')
  exp_craniospatial_rt_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Craniospinal radiotherapy (RT)?')
  exp_tbi_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Total Body Irradiation (TBI)?')
  exp_radiopharma_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Radiopharmaceutical therapy (e.g., radiolabeled antibody, 131I-MIBG)?')
  exp_hct: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Hematopoietic cell transplantation (HCT)?')
  type_transplant: Optional[List[Type_transplant]] = Field(
    None, 
    description='What type(s) of transplant are mentioned in the eligibility criteria?')
  exp_dli_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to DLI (donor lymphocyte infusion) or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.)?')
  exp_cyp2d6_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to strong inhibitors of CYP2D6?')
  exp_cyp3a4_fact: str = Field(..., description="The fact that indicates whether the eligibility criteria mentions any prior exposure to strong inhibitors of CYP3A4. Please match exactly the term 'CYP3A4' in the text. Note: 'CYP3A' does not count.")
  exp_cyp3a4_ever: Optional[Yes_no] = Field(
    None, 
    description="Does the eligibility criteria mention any prior exposure to strong inhibitors of CYP3A4? Only answer 'Yes' if 'CYP3A4' is explicitly mentioned.")
  exp_cyp3a_fact: str = Field(..., description="The fact that indicates whether the eligibility criteria mentions any prior exposure to strong inhibitors of CYP3A. Note: 'CYP3A4' is a different enzyme and should not be counted.")
  exp_cyp3a_ever: Optional[Yes_no] = Field(
    None, 
    description="Does the eligibility criteria mention any prior exposure to strong inhibitors of CYP3A? Please note: 'CYP3A' is distinct from 'CYP3A4'")
  exp_calcineurin_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions any prior exposure to calcineurin inhibitors')
  exp_calcineurin_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to calcineurin inhibitors?')
  exp_monocl_antib_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to monoclonal antibodies?')
  exp_immunotherapy_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to immunotherapy?')
  exp_gpc3_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to GPC3-directed immunotherapy?')
  exp_demeth_hdac_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to Demethylating and/or HDAC Inhibitor Therapy?')
  exp_cd123_cart: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells?')
  exp_anthracycline_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to anthracycline or equivalent?')
  cumul_anthracycline: Optional[str] = Field(
    None, 
    description='How much cumulative anthracycline or equivalent (in mg/m^2) is mentioned in the eligibility criteria? Example: the answer is 450 mg/m^2, if "total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2"')
  gvhd_fact: str = Field(..., description='The fact that indicates whether the presence of graft versus host disease, or GVHD is excluded from this study')
  gvhd: Optional[Yes_no] = Field(
    None, 
    description='Is presence of graft versus host disease, or GVHD, excluded from this study?')
  vpa_meds: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to receiving valproic acid (VPA) therapy?')
  prior_solid_organ_transpl_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions a prior solid organ transplantation')
  prior_solid_organ_transpl: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a prior solid organ transplantation?')
  exp_uproleselan: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention prior exposure to uproleselan?')
  exp_flotetuzumab: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention prior exposure to flotetuzumab?')
  exp_venetoclax_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions venetoclax')
  exp_venetoclax: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention venetoclax?')
  exp_venetoclax_sensitive_fact: str = Field(..., description='The fact that indicates whether the eligibility criteria mentions previous toxicity or hypersensitivity directly attributed to venetoclax')
  exp_venetoclax_sensitive: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to venetoclax?')
  donor_available: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a suitable stem cell donor available?')
  dyspnea_present: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of dyspnea?')
  hypoxia_present: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of hypoxia?')
  expression_msln: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of MSLN expression?')
  expression_cd123: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of CD123 expression?')
  expression_eselectin: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of E-selectin expression?')
  expression_kmt2ar: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of KMT2A rearrangement (KMT2Ar)?')
  expression_t1517: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of t(15;17) translocation?')
  expression_som_JAK2_V617F: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of somatic JAK2 V617F mutation?')
  expression_flt3_itd: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of FLT3 / internal tandem duplication (ITD) mutation?')
  diag_cong_blood_disorder: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any congenital bleeding disorders, including but not limited to hemophilia?')
  diag_intercurrent_illness: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of any significant intercurrent disease?')
  diag_mets_cns: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention Metastatic CNS involvement?')
  diag_hemolytic_anemia: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of hemolytic anemia?')
  diag_evans_syndrome: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of Evans syndrome?')
  diag_uncontrolled_cardiac_rhythm: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention uncontrolled cardiac rhythm disturbance?')
  diag_severe_psychiatric_disorder: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of acute or chronic severe psychiatric disorders?')
  diag_other_malignancies: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of other malignancies?')
  diag_pneumonitis: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of pneumonitis?')
  diag_mibg_avidity: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention indications of tumor(s) / lesion(s) with known MIBG avidity?')
  diag_fdg_avidity: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention tumor(s) / lesion(s) with known FDG avidity?')
  diag_signif_pleural_effusion: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention clinically significant, symptomatic, pleural effusions?')
  diag_signif_pericardial_effusion: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention physiologically significant pericardial effusion?')
  diag_measureable_disease: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention the patient having measurable disease?')
  diag_measureable_tumor: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention the patient having one or more tumor / lesion sites with measurable dimensions?')
  diag_primary_immunodeficiency: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention a diagnosis of primary immunodeficiency?')
  exp_cellular_therapy: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to  live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell])?')
  exp_ch14_18_sensitive: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to ch14.18 (CHO or SP2/0)?')
  exp_anti_gd2_sensitive: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab)?')
  exp_hu5f9g4_sensitive: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody?')
  exp_gm_csf_sensitive: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO)?')
  exp_pd1_pdl_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to  any PD-1, PD-L1, or PD-L2 targeting antibodies (e.g. Nivolumab)?')
  exp_anti_ctla4_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to  any anti-CTLA4 agent?')
  exp_lorlatinib_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to  lorlatinib?')
  exp_cd47_sirpalpha_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to  any CD47–SIRPα-targeted therapeutics?')
  exp_ivig_ever: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention any prior exposure to  Intravenous Immunoglobulin (IVIg) therapy?')
  cumul_131l_mibg: Optional[str] = Field(
    None, 
    description='How much cumulative 131I-MIBG dosing (in mCi/kg) is mentioned in the eligibility criteria? Example: the answer is > 54 mCi/kg, if "treated with iodine-131 (131I)-MIBG who have already received a cumulative I-131 dose > 54 mCi/kg or who would exceed 54 mCi/kg by participating"')
  expression_alk: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of ALK mutation?')
  expression_alk_type: Optional[List[Expression_alk_type]] = Field(
    None, 
    description='What types of ALK mutations are mentioned in the eligibility criteria?')
  bclc_stage: Optional[str] = Field(
    None, 
    description='What BCLC stage is mentioned in the eligibility criteria? Example: "Stage 0", "Stage A", "Stage B", "Stage C", "Stage D"')
  ctp_score: Optional[int] = Field(
    None, 
    description='What Child-Pugh-Turcotte score is mentioned in the eligibility criteria?')
  expression_gpc3: Optional[Yes_no] = Field(
    None, 
    description='Does the eligibility criteria mention evidence of GPC3 expression?')
  
  model_config = ConfigDict(
    json_schema_extra={
        "examples": [
            {
                "exp_anticancer_nonmyelosupp_fact": "At least 24 hours must have elapsed since the completion of low-dose or non- myelosuppressive therapy",
                "exp_anticancer_nonmyelosupp_ever": "Yes",
                "exp_anticancer_myelosupp_fact": "At least 14 days must have elapsed since the completion of myelosuppressive therapy ",
                "exp_anticancer_myelosupp_ever": "Yes",
                "exp_cyp3a4_fact": "During the dose-escalation portion of the trial, we discourage the use of strong CYP3A inhibitors",
                "exp_cyp3a4_ever": "No",
                "exp_cyp3a_fact": "Patients may not receive strong or moderate CYP3A inhibitors",
                "exp_cyp3a_ever": "Yes",
                'gvhd_fact': 'For patients who have received prior HCT, there can be no evidence of GVHD and greater than 60 days must have elapsed since the HCT.',
                'gvhd': 'Yes',
                'exp_venetoclax_fact': 'At least 14 days must have elapsed since the completion of myelosuppressive therapy or hypomethylating agents and the first doses of venetoclax and selinexor',
                'exp_venetoclax': 'Yes',
                'exp_venetoclax_sensitive_fact': 'Previous toxicity or hypersensitivity directly attributed to venetoclax',
                'exp_venetoclax_sensitive': 'Yes',
                "prior_solid_organ_transpl_fact": "Prior bone marrow transplant presenting with active uncontrolled graft versus host disease (GvHD)",
                "prior_solid_organ_transpl": "Yes",
            },
            {
                'exp_venetoclax_fact': 'Previous toxicity or hypersensitivity directly attributed to venetoclax',
                'exp_venetoclax': 'Yes',
            }
        ]
      }
  ) 



  
# class Disease(BaseModel):
#     # list dieases properties
#     name: str
#     defination: str
#     severity: str
#     inclusion: bool
#     ...
#     @gpt_function
#     def from_criteria(criteria) -> "Disease":
#         """Extract disease properties from the criteria."""

# # expected output
# disease = Disease.from_criteria("Refractory leukemia, defined as persistent leukemia after at least two courses of induction chemotherapy")
# # Disease(name='Refractory leukemia', 
# #     defination='persistent leukemia after at least two courses of induction chemotherapy', 
# #     severity=None,
# #     inclusion=Yes)