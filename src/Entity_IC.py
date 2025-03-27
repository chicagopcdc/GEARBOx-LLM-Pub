from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List

class Sex(Enum):
    MALE = "Male"
    FEMALE = "Female"
    NONE = "None"

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

class Yes_no(Enum):
    YES = "Yes"
    NO = "No"

class Entity(BaseModel):
    age_min_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the minimum age of eligibility?")
    age_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum age of eligibility (in years) considered to be included")
    age_max_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the maximum age of eligibility?")
    age_max: Optional[int] = Field(
        None, 
        description="If so, what is the maximum age of eligibility (in years) considered to be included")
    weight_min_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the minimum weight a patient may have?")
    weight_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum weight (in kilograms) of a patient considered to be included")
    weight_max_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the maximum weight a patient may have?")
    weight_max: Optional[int] = Field(
        None, 
        description="If so, what is the maximum weight (in kilograms) of a patient considered to be included")
    sex_exist: Yes_no = Field(..., description="Does the eligibility criteria mention sexes of a patient?")
    sex: Optional[List[Sex]] = Field(
        None, 
        description="If so, which sexes are considered to be included")
    diagnosis_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a patient's current diagnoses?")
    diagnosis: Optional[List[Diagnosis]] = Field(
        None, 
        description="If so, which diagnoses are considered to be included")
    ever_refractory_exist: Yes_no = Field(..., description="Does the eligibility criteria mention refractory disease?")
    ever_refractory: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with refractory disease considered to be included")
    count_refractory_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the occurrence of refractory disease?")
    count_refractory: Optional[int] = Field(
        None, 
        description="If so, how many occurrences of refractory disease are required to be included")
    current_refractory_num_cycles_exist: Yes_no = Field(..., description="Does the eligibility criteria mention number of cycles of therapy required for refractory disease?")
    current_refractory_num_cycles: Optional[int] = Field(
        None, 
        description="If so, what is the minimum number of cycles of therapy required for refractory disease considered to be included")
    ever_relapse_exist: Yes_no = Field(..., description="Does the eligibility criteria mention confirmed or suspected relapse disease?")
    ever_relapse: Optional[Yes_no] = Field(
        None, 
        description="If so, is confirmed or suspected relapse disease considered to be included")
    count_relapse_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the number of relapses of the patient?")
    count_relapse: Optional[str] = Field(
        None, 
        description="If so, what is the minimum number of relapses required to be included")
    bm_recent_blast_pct_meas_exist: Yes_no = Field(..., description="Does the eligibility criteria mention bone marrow blast percentage?")
    bm_recent_blast_pct_meas: Optional[int] = Field(
        None, 
        description="If so, what is the minimum bone marrow blast percentage considered to be included")
    bm_recent_blast_method_exist: Yes_no = Field(..., description="Does the eligibility criteria mention methods for bone marrow blast percentage assessment?")
    bm_recent_blast_method: Optional[List[Bm_recent_blast_method]] = Field(
        None, 
        description="If so, what are the required methods for bone marrow blast percentage assessment considered to be included")
    periph_blood_blast_abs_meas_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the absolute blast count in peripheral blood?")
    periph_blood_blast_abs_meas: Optional[int] = Field(
        None, 
        description="If so, what is the absolute blast count in peripheral blood measurement (in cells/microliter) considered to be included")
    periph_blood_blast_pct_meas_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the peripheral blood blast percentage?")
    periph_blood_blast_pct_meas: Optional[int] = Field(
        None, 
        description="If so, what is the minimum peripheral blood blast percentage considered to be included")
    corneal_epitheliopathy_exist: Yes_no = Field(..., description="Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy?")
    corneal_epitheliopathy: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with such diagnosis considered to be included")
    cns_status_exist: Yes_no = Field(..., description="Does the eligibility criteria mention CNS status?")
    cns_status: Optional[List[Cns_status]] = Field(
        None, 
        description="If so, what CNS status is considered to be included")
    lanksy_min_exist: Yes_no = Field(..., description="Does the eligibility criteria mention Lansky score?")
    lanksy_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum Lansky score for a patient considered to be included")
    karnofksy_min_exist: Yes_no = Field(..., description="Does the eligibility criteria mention Karnofsky score?")
    karnofksy_min: Optional[int] = Field(
        None, 
        description="If so, what is the minimum Karnofsky score for a patient considered to be included")
    diag_down_syndrome_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of Down syndrome?")
    diag_down_syndrome: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Down syndrome considered to be included")
    diag_iso_emd_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of isolated extramedullary disease (i.e. the absence of bone marrow involvement)?")
    diag_iso_emd: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of isolated extramedullary disease considered to be included")
    diag_iso_testes_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of isolated testicular relapse?")
    diag_iso_testes: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of isolated testicular relapse considered to be included")
    diag_ataxia_telang_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of ataxia-telangiectasia?")
    diag_ataxia_telang: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of ataxia-telangiectasia considered to be included")
    diag_bloom_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of Bloom syndrome?")
    diag_bloom: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Bloom syndrome considered to be included")
    diag_fanconi_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of Fanconi anemia?")
    diag_fanconi: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Fanconi anemia considered to be included")
    diag_kostmann_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of Kostmann syndrome?")
    diag_kostmann: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Kostmann syndrome considered to be included")
    diag_shwachman_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of Shwachman syndrome?")
    diag_shwachman: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Shwachman syndrome considered to be included")
    diag_cong_bmf_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)?")
    diag_cong_bmf: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with such diagnosis considered to be included")
    diag_malabsoption_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of malabsorption syndrome?")
    diag_malabsoption: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of malabsorption syndrome considered to be included")
    diag_chf_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of congestive heart failure (CHF)?")
    diag_chf: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of congestive heart failure considered to be included")
    diag_hiv_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of human immunodeficiency virus (HIV) infection?")
    diag_hiv: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of human immunodeficiency virus infection considered be included")
    diag_uncontr_cns_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis)?")
    diag_uncontr_cns: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis) considered to be included")
    diag_hep_b_c_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of hepatitis B or hepatitis C infection?")
    diag_hep_b_c: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of hepatitis B or hepatitis C infection considered to be included")
    diag_liver_cirr_serious_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of liver cirrhosis or other serious liver disease?")
    diag_liver_cirr_serious: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of liver cirrhosis or other serious liver disease considered to be included")
    active_infection_exist: Yes_no = Field(..., description="Does the eligibility criteria mention an active, uncontrolled infection?")
    active_infection: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with an active, uncontrolled infection considered to be included")
    refractory_transfusion_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a patient known to be refractory to red blood cells or platelet transfusions?")
    refractory_transfusion: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient known to be refractory to red blood cells or platelet transfusions considered to be included")
    cerebellar_toxicity_exist: Yes_no = Field(..., description="Does the eligibility criteria mention an history of cerebellar toxicity or cerebellar neurological findings on exam?")
    cerebellar_toxicity: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a history of cerebellar toxicity or cerebellar neurological findings on exam considered to be included")
    exp_cytotoxic_chemo_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)?")
    exp_cytotoxic_chemo_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids) considered to be included")
    exp_corticosteroids_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy)?")
    exp_corticosteroids_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy) considered to be included")
    exp_anticancer_nonmyelosupp_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to non-myelosuppressive anti-cancer agents?")
    exp_anticancer_nonmyelosupp_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to non-myelosuppressive anti-cancer agents considered to be included")
    exp_anticancer_myelosupp_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to myelosuppressive anti-cancer agents?")
    exp_anticancer_myelosupp_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to myelosuppressive anti-cancer agents considered to be included")
    exp_antibody_drug_conj_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to antibody-drug conjugate?")
    exp_antibody_drug_conj_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to antibody-drug conjugate considered to be included")
    exp_interleukins_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Interleukins, Interferons and Cytokines (not including Hematopoietic Growth Factors)?")
    exp_interleukins_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Interleukins, Interferons and Cytokines considered to be included")
    exp_long_acting_gf_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Long-acting growth factor (eg, pegfilgrastim)?")
    exp_long_acting_gf_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Long-acting growth factor considered to be included")
    exp_short_acting_gf_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Short-acting growth factor?")
    exp_short_acting_gf_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Short-acting growth factor considered to be included")
    exp_rt_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Radiotherapy (RT)?")
    exp_rt_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Radiotherapy considered to be included")
    exp_craniospatial_rt_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Craniospinal radiotherapy (RT)?")
    exp_craniospatial_rt_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Craniospinal radiotherapy considered to be included")
    exp_tbi_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Total Body Irradiation (TBI)?")
    exp_tbi_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Total Body Irradiation considered to be included")
    exp_radiopharma_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Radiopharmaceutical therapy (e.g., radiolabeled antibody, 131I-MIBG)?")
    exp_radiopharma_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Radiopharmaceutical therapy considered to be included")
    exp_hct_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Hematopoietic cell transplantation (HCT)?")
    exp_hct: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Hematopoietic cell transplantation (HCT) considered to be included")
    type_transplant_exist: Yes_no = Field(..., description="Does the eligibility criteria mention type(s) of transplant?")
    type_transplant: Optional[str] = Field(
        None, 
        description="If so, what type(s) of transplant are considered to be included")
    exp_dli_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to DLI (donor lymphocyte infusion) or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.)?")
    exp_dli_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to DLI or any type of cellular therapy considered to be included")
    exp_cyp2d6_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP2D6?")
    exp_cyp2d6_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP2D6 considered to be included")
    exp_cyp3a4_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A4?")
    exp_cyp3a4_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP3A4 considered to be included")
    exp_cyp3a_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A?")
    exp_cyp3a_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Strong inhibitors of CYP3A considered to be included")
    exp_calcineurin_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to calcineurin inhibitors?")
    exp_calcineurin_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to calcineurin inhibitors considered to be included")
    exp_monocl_antib_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to monoclonal antibodies?")
    exp_monocl_antib_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to monoclonal antibodies considered to be included")
    exp_immunotherapy_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to immunotherapy?")
    exp_immunotherapy_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to immunotherapy considered to be included")
    exp_gpc3_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to GPC3-directed immunotherapy?")
    exp_gpc3_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to GPC3-directed immunotherapy considered to be included")
    exp_demeth_hdac_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Demethylating and/or HDAC Inhibitor Therapy?")
    exp_demeth_hdac_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to Demethylating and/or HDAC Inhibitor Therapy considered to be included")
    exp_cd123_cart_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells?")
    exp_cd123_cart: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells considered to be included")
    exp_anthracycline_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to anthracycline or equivalent?")
    exp_anthracycline_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to anthracycline or equivalent considered to be included")
    cumul_anthracycline_exist: Yes_no = Field(..., description="Does eligibility criteria mention cumulative anthracycline or equivalent?")
    cumul_anthracycline: Optional[str] = Field(
        None, 
        description="If so, how much cumulative anthracycline or equivalent (in mg/m^2) is considered to be included")
    gvhd_exist: Yes_no = Field(..., description="Does the eligibility criteria mention presence of graft versus host disease, or GVHD?")
    gvhd: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with presence of graft versus host disease, or GVHD considered to be included")
    vpa_meds_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to receiving valproic acid (VPA) therapy?")
    vpa_meds: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to receiving valproic acid therapy considered to be included")
    prior_solid_organ_transpl_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a prior solid organ transplantation?")
    prior_solid_organ_transpl: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a prior solid organ transplantation considered to be included")
    exp_uproleselan_exist: Yes_no = Field(..., description="Does the eligibility criteria mention prior exposure to uproleselan?")
    exp_uproleselan: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with prior exposure to uproleselan considered to be included")
    exp_flotetuzumab_exist: Yes_no = Field(..., description="Does the eligibility criteria mention prior exposure to flotetuzumab?")
    exp_flotetuzumab: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with prior exposure to flotetuzumab considered to be included")
    exp_venetoclax_exist: Yes_no = Field(..., description="Does the eligibility criteria mention prior exposure to venetoclax?")
    exp_venetoclax: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with prior exposure to venetoclax considered to be included")
    exp_venetoclax_sensitive_exist: Yes_no = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to venetoclax?")
    exp_venetoclax_sensitive: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to venetoclax considered to be included")
    donor_available_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a suitable stem cell donor available?")
    donor_available: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a suitable stem cell donor available considered to be included")
    dyspnea_present_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of dyspnea?")
    dyspnea_present: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of dyspnea considered to be included")
    hypoxia_present_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of hypoxia?")
    hypoxia_present: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of hypoxia considered to be included")
    expression_msln_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of MSLN expression?")
    expression_msln: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of MSLN expression considered to be included")
    expression_cd123_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of CD123 expression?")
    expression_cd123: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of CD123 expression considered to be included")
    expression_eselectin_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of E-selectin expression?")
    expression_eselectin: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of E-selectin expression considered to be included")
    expression_kmt2ar_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of KMT2A rearrangement (KMT2Ar)?")
    expression_kmt2ar: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of KMT2Ar considered to be included")
    expression_t1517_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of t(15;17) translocation?")
    expression_t1517: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of t(15;17) translocation considered to be included")
    expression_som_JAK2_V617F_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of somatic JAK2 V617F mutation?")
    expression_som_JAK2_V617F: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of somatic JAK2 V617F mutation considered to be included")
    expression_flt3_itd_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of FLT3 / internal tandem duplication (ITD) mutation?")
    expression_flt3_itd: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of FLT3 / internal tandem duplication mutation considered to be included")
    diag_cong_blood_disorder_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any congenital bleeding disorders, including but not limited to hemophilia?")
    diag_cong_blood_disorder: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any congenital bleeding disorders, including but not limited to hemophilia considered to be included")
    diag_intercurrent_illness_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of any significant intercurrent disease?")
    diag_intercurrent_illness: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of any significant intercurrent disease considered to be included")
    diag_mets_cns_exist: Yes_no = Field(..., description="Does the eligibility criteria mention metastatic CNS involvement?")
    diag_mets_cns: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with metastatic CNS involvement considered to be included")
    diag_hemolytic_anemia_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of hemolytic anemia?")
    diag_hemolytic_anemia: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of hemolytic anemia considered to be included")
    diag_evans_syndrome_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of Evans syndrome?")
    diag_evans_syndrome: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of Evans syndrome considered to be included")
    diag_uncontrolled_cardiac_rhythm_exist: Yes_no = Field(..., description="Does the eligibility criteria mention uncontrolled cardiac rhythm disturbance?")
    diag_uncontrolled_cardiac_rhythm: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with uncontrolled cardiac rhythm disturbance considered to be included")
    diag_severe_psychiatric_disorder_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of acute or chronic severe psychiatric disorders?")
    diag_severe_psychiatric_disorder: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of acute or chronic severe psychiatric disorders considered to be included")
    diag_other_malignancies_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of other malignancies?")
    diag_other_malignancies: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of other malignancies considered to be included")
    diag_pneumonitis_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of pneumonitis?")
    diag_pneumonitis: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of pneumonitis considered to be included")
    diag_mibg_avidity_exist: Yes_no = Field(..., description="Does the eligibility criteria mention indications of tumor(s) / lesion(s) with known MIBG avidity?")
    diag_mibg_avidity: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with indications of tumor(s) / lesion(s) with known MIBG avidity considered to be included")
    diag_fdg_avidity_exist: Yes_no = Field(..., description="Does the eligibility criteria mention tumor(s) / lesion(s) with known FDG avidity?")
    diag_fdg_avidity: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with tumor(s) / lesion(s) with known FDG avidity considered to be included")
    diag_signif_pleural_effusion_exist: Yes_no = Field(..., description="Does the eligibility criteria mention clinically significant, symptomatic, pleural effusions?")
    diag_signif_pleural_effusion: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with clinically significant, symptomatic, pleural effusions considered to be included")
    diag_signif_pericardial_effusion_exist: Yes_no = Field(..., description="Does the eligibility criteria mention physiologically significant pericardial effusion?")
    diag_signif_pericardial_effusion: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with physiologically significant pericardial effusion considered to be included")
    diag_measureable_disease_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the patient having measurable disease?")
    diag_measureable_disease: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with measurable disease considered to be included")
    diag_measureable_tumor_exist: Yes_no = Field(..., description="Does the eligibility criteria mention the patient having one or more tumor / lesion sites with measurable dimensions?")
    diag_measureable_tumor: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with one or more tumor / lesion sites with measurable dimensions considered to be included")
    diag_primary_immunodeficiency_exist: Yes_no = Field(..., description="Does the eligibility criteria mention a diagnosis of primary immunodeficiency?")
    diag_primary_immunodeficiency: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with a diagnosis of primary immunodeficiency considered to be included")
    exp_cellular_therapy_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell])?")
    exp_cellular_therapy: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell]) considered to be included")
    exp_ch14_18_sensitive_exist: Yes_no = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0)?")
    exp_ch14_18_sensitive: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0) considered to be included")
    exp_anti_gd2_sensitive_exist: Yes_no = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab)?")
    exp_anti_gd2_sensitive: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab) considered to be included")
    exp_hu5f9g4_sensitive_exist: Yes_no = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody?")
    exp_hu5f9g4_sensitive: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody considered to be included")
    exp_gm_csf_sensitive_exist: Yes_no = Field(..., description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO)?")
    exp_gm_csf_sensitive: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO) considered to be included")
    exp_pd1_pdl_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies (e.g. Nivolumab)?")
    exp_pd1_pdl_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies considered to be included")
    exp_anti_ctla4_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to any anti-CTLA4 agent?")
    exp_anti_ctla4_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to any anti-CTLA4 agent considered to be included")
    exp_lorlatinib_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to lorlatinib?")
    exp_lorlatinib_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to lorlatinib considered to be included")
    exp_cd47_sirpalpha_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to any CD47–SIRPα-targeted therapeutics?")
    exp_cd47_sirpalpha_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to any CD47–SIRPα-targeted therapeutics considered to be included")
    exp_ivig_ever_exist: Yes_no = Field(..., description="Does the eligibility criteria mention any prior exposure to Intravenous Immunoglobulin (IVIg) therapy?")
    exp_ivig_ever: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with any prior exposure to  Intravenous Immunoglobulin (IVIg) therapy considered to be included")
    cumul_131l_mibg_exist: Yes_no = Field(..., description="Does the eligibility criteria mention cumulative 131I-MIBG dosing?")
    cumul_131l_mibg: Optional[str] = Field(
        None, 
        description="If so, how much cumulative 131I-MIBG dosing (in mCi/kg) is considered to be included")
    expression_alk_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of ALK mutation?")
    expression_alk: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of ALK mutation considered to be included")
    expression_alk_type_exist: Yes_no = Field(..., description="Does the eligibility criteria mention types of ALK mutations?")
    expression_alk_type: Optional[str] = Field(
        None, 
        description="If so, what types of ALK mutations are considered to be included")
    bclc_stage_exist: Yes_no = Field(..., description="Does the eligibility criteria mention BCLC stage?")
    bclc_stage: Optional[str] = Field(
        None, 
        description="If so, what BCLC stages are considered to be included")
    ctp_score_exist: Yes_no = Field(..., description="Does the eligibility criteria mention Child-Pugh-Turcotte score?")
    ctp_score: Optional[int] = Field(
        None, 
        description="If so, what Child-Pugh-Turcotte score is considered to be included")
    expression_gpc3_exist: Yes_no = Field(..., description="Does the eligibility criteria mention evidence of GPC3 expression?")
    expression_gpc3: Optional[Yes_no] = Field(
        None, 
        description="If so, is a patient with evidence of GPC3 expression considered to be included")
