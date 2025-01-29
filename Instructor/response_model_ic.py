from typing import TypeVar, Type, Optional, List

from pydantic import BaseModel, Field

class DynamicEntity(BaseModel):
    age_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the minimum age of eligibility? If so, what is the minimum age of eligibility (in years) considered to be included?")
class DynamicEntity(BaseModel):
    age_max: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the maximum age of eligibility? If so, what is the maximum age of eligibility (in years) considered to be included?")
class DynamicEntity(BaseModel):
    weight_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the minimum weight a patient may have? If so, what is the minimum weight (in kilograms) of a patient considered to be included?")
class DynamicEntity(BaseModel):
    weight_max: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the maximum weight a patient may have? If so, what is the maximum weight (in kilograms) of a patient considered to be included?")
class DynamicEntity(BaseModel):
    sex: Optional[List[Sex]] = Field(
        None, 
        description="Does the eligibility criteria mention sexes of a patient? If so, which sexes are considered to be included?")
class DynamicEntity(BaseModel):
    diagnosis: Optional[List[Diagnosis]] = Field(
        None, 
        description="Does the eligibility criteria mention a patient's current diagnoses? If so, which diagnoses are considered to be included?")
class DynamicEntity(BaseModel):
    ever_refractory: Optional[List[Ever_refractory]] = Field(
        None, 
        description="Does the eligibility criteria mention refractory disease? If so, is a patient with refractory disease considered to be included? Example: refractory disease are diseases such as \"Refractory leukemia\"")
class DynamicEntity(BaseModel):
    count_refractory: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the occurrences of refractory disease? If so, how many occurrences of refractory disease are required to be included?")
class DynamicEntity(BaseModel):
    current_refractory_num_cycles: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention number of cycles of therapy required for refractory disease? If so, what is the minimum number of cycles of therapy required for refractory disease considered to be included? Example: the answer is 1 if \"refractory to at least one course of salvage therapy\", the answer is 2 if \"persistent after at least two courses of induction \"chemotherapy\", the answer is 2 if \"refractory disease after >= 2 cycles of chemotherapy\"")
class DynamicEntity(BaseModel):
    ever_relapse: Optional[List[Ever_relapse]] = Field(
        None, 
        description="Does the eligibility criteria mention confirmed or suspected relapse disease? If so, is confirmed or suspected relapse disease considered to be included? Example: relapse disease such as \"relapsed leukemia\"")
class DynamicEntity(BaseModel):
    count_relapse: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention the number of relapses required? If so, what is the minimum number of relapses required to be included? Example: the answer is 2 if \"Second or greater relapse\", the answer is 1 if \"first relapses\"")
class DynamicEntity(BaseModel):
    bm_recent_blast_pct_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention bone marrow blast percentage? If so, what is the minimum bone marrow blast percentage considered to be included? Example: the answer is 5 if \">= 5% blasts in the bone marrow\", the answer is 5 if \"> 5% blasts in the BM\" is mentioned")
class DynamicEntity(BaseModel):
    bm_recent_blast_method: Optional[List[Bm_recent_blast_method]] = Field(
        None, 
        description="Does the eligibility criteria mention methods for bone marrow blast percentage assessment? If so, what are the required methods for bone marrow blast percentage assessment considered to be included? Example: \"Morphology\", \"Flow cytometry\"")
class DynamicEntity(BaseModel):
    periph_blood_blast_abs_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the peripheral blood absolute blast count measurement? If so, what is the peripheral blood absolute blast count measurement (in cells/microliter) considered to be included?")
class DynamicEntity(BaseModel):
    periph_blood_blast_pct_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the defined peripheral blood blast percentage? If so, what is the minimum defined peripheral blood blast percentage considered to be included? Example: the answer is 5 if \">= 5% blasts in the peripheral blood\" is mentioned, the answer is 5 if \">=5% blasts in the blood\" is mentioned")
class DynamicEntity(BaseModel):
    corneal_epitheliopathy: Optional[List[Corneal_epitheliopathy]] = Field(
        None, 
        description="Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy? If so, is a patient with such diagnosis considered to be included?")
class DynamicEntity(BaseModel):
    cns_status: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention CNS status? If so, what CNS status is considered to be included? Example: \"CNS 1\", \"CNS 2\", \"CNS 3\"")
class DynamicEntity(BaseModel):
    lanksy_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Lansky score? If so, what is the minimum Lansky score for a patient considered to be included? Example: the answer is 70 if \"Lansky score>=70\" is mentioned")
class DynamicEntity(BaseModel):
    karnofksy_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Karnofsky score? If so, what is the minimum Karnofsky score for a patient considered to be included? Example: the answer is 50 if \"Karnofsky score >= 50\" is mentioned")
class DynamicEntity(BaseModel):
    diag_down_syndrome: Optional[List[Diag_down_syndrome]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Down syndrome? If so, is a patient with a diagnosis of Down syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_iso_emd: Optional[List[Diag_iso_emd]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of isolated extramedullary disease (i.e. the absence of bone marrow involvement)? If so, is a patient with a diagnosis of isolated extramedullary disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_iso_testes: Optional[List[Diag_iso_testes]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of isolated testicular relapse? If so, is a patient with a diagnosis of isolated testicular relapse considered to be included?")
class DynamicEntity(BaseModel):
    diag_ataxia_telang: Optional[List[Diag_ataxia_telang]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of ataxia-telangiectasia? If so, is a patient with a diagnosis of ataxia-telangiectasia considered to be included?")
class DynamicEntity(BaseModel):
    diag_bloom: Optional[List[Diag_bloom]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Bloom syndrome? If so, is a patient with a diagnosis of Bloom syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_fanconi: Optional[List[Diag_fanconi]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Fanconi anemia? If so, is a patient with a diagnosis of Fanconi anemia considered to be included?")
class DynamicEntity(BaseModel):
    diag_kostmann: Optional[List[Diag_kostmann]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Kostmann syndrome? If so, is a patient with a diagnosis of Kostmann syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_shwachman: Optional[List[Diag_shwachman]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Shwachman syndrome? If so, is a patient with a diagnosis of Shwachman syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_cong_bmf: Optional[List[Diag_cong_bmf]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)? If so, is a patient with such diagnosis considered to be included?")
class DynamicEntity(BaseModel):
    diag_malabsoption: Optional[List[Diag_malabsoption]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of malabsorption syndrome? If so, is a patient with a diagnosis of malabsorption syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_chf: Optional[List[Diag_chf]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of congestive heart failure (CHF)? If so, is a patient with a diagnosis of congestive heart failure considered to be included?")
class DynamicEntity(BaseModel):
    diag_hiv: Optional[List[Diag_hiv]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of human immunodeficiency virus (HIV) infection? If so, is a patient with a diagnosis of human immunodeficiency virus infection considered be included?")
class DynamicEntity(BaseModel):
    diag_uncontr_cns: Optional[List[Diag_uncontr_cns]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis)? If so, is a patient with a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology considered to be included?")
class DynamicEntity(BaseModel):
    diag_hep_b_c: Optional[List[Diag_hep_b_c]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of hepatitis B or C infection? If so, is a patient with a diagnosis of hepatitis B or C infection considered to be included?")
class DynamicEntity(BaseModel):
    diag_liver_cirr_serious: Optional[List[Diag_liver_cirr_serious]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of liver cirrhosis or other serious liver disease? If so, is a patient with a diagnosis of liver cirrhosis or other serious liver disease considered to be included?")
class DynamicEntity(BaseModel):
    active_infection: Optional[List[Active_infection]] = Field(
        None, 
        description="Does the eligibility criteria mention a documented active, uncontrolled infection? If so, is a patient with a documented active, uncontrolled infection considered to be included?")
class DynamicEntity(BaseModel):
    refractory_transfusion: Optional[List[Refractory_transfusion]] = Field(
        None, 
        description="Does the eligibility criteria mention a patient known to be refractory to red blood cells or platelet transfusions? If so, is a patient known to be refractory to red blood cells or platelet transfusions considered to be included?")
class DynamicEntity(BaseModel):
    cerebellar_toxicity: Optional[List[Cerebellar_toxicity]] = Field(
        None, 
        description="Does the eligibility criteria mention an history of cerebellar toxicity or cerebellar neurological findings on exam? If so, is a patient with a history of cerebellar toxicity or cerebellar neurological findings on exam considered to be included?")
class DynamicEntity(BaseModel):
    exp_cytotoxic_chemo_ever: Optional[List[Exp_cytotoxic_chemo_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)? If so, is a patient with any prior exposure to cytotoxic chemotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_corticosteroids_ever: Optional[List[Exp_corticosteroids_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy)? If so, is a patient with any prior exposure to corticosteroids considered to be included?")
class DynamicEntity(BaseModel):
    exp_anticancer_nonmyelosupp_ever: Optional[List[Exp_anticancer_nonmyelosupp_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to non-myelosuppressive anti-cancer agents? If so, is a patient with any prior exposure to non-myelosuppressive anti-cancer agents considered to be included?")
class DynamicEntity(BaseModel):
    exp_anticancer_myelosupp_ever: Optional[List[Exp_anticancer_myelosupp_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to myelosuppressive anti-cancer agents? If so, is a patient with any prior exposure to myelosuppressive anti-cancer agents considered to be included?")
class DynamicEntity(BaseModel):
    exp_antibody_drug_conj_ever: Optional[List[Exp_antibody_drug_conj_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to antibody-drug conjugate? If so, is a patient with any prior exposure to antibody-drug conjugate considered to be included?")
class DynamicEntity(BaseModel):
    exp_interleukins_ever: Optional[List[Exp_interleukins_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Interleukins, Interferons and Cytokines (not including Hematopoietic Growth Factors)? If so, is a patient with any prior exposure to Interleukins, Interferons and Cytokines considered to be included?")
class DynamicEntity(BaseModel):
    exp_long_acting_gf_ever: Optional[List[Exp_long_acting_gf_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Long-acting growth factor (eg, pegfilgrastim)? If so, is a patient with any prior exposure to Long-acting growth factor considered to be included?")
class DynamicEntity(BaseModel):
    exp_short_acting_gf_ever: Optional[List[Exp_short_acting_gf_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Short-acting growth factor? If so, is a patient with any prior exposure to Short-acting growth factor considered to be included?")
class DynamicEntity(BaseModel):
    exp_rt_ever: Optional[List[Exp_rt_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Radiotherapy (RT)? If so, is a patient with any prior exposure to Radiotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_craniospatial_rt_ever: Optional[List[Exp_craniospatial_rt_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Craniospinal radiotherapy (RT)? If so, is a patient with any prior exposure to Craniospinal radiotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_tbi_ever: Optional[List[Exp_tbi_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Total Body Irradiation (TBI)? If so, is a patient with any prior exposure to Total Body Irradiation considered to be included?")
class DynamicEntity(BaseModel):
    exp_radiopharma_ever: Optional[List[Exp_radiopharma_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Radiopharmaceutical therapy (e.g., radiolabeled antibody, 131I-MIBG)? If so, is a patient with any prior exposure to Radiopharmaceutical therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_hct: Optional[List[Exp_hct]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Hematopoietic cell transplantation (HCT)? If so, is a patient with any prior exposure to Hematopoietic cell transplantation (HCT) considered to be included?")
class DynamicEntity(BaseModel):
    type_transplant: Optional[List[Type_transplant]] = Field(
        None, 
        description="Does the eligibility criteria mention type(s) of transplant? If so, what type(s) of transplant are considered to be included?")
class DynamicEntity(BaseModel):
    exp_dli_ever: Optional[List[Exp_dli_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to DLI (donor lymphocyte infusion) or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.)? If so, is a patient with any prior exposure to DLI or any type of cellular therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_cyp2d6_ever: Optional[List[Exp_cyp2d6_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP2D6? If so, is a patient with any prior exposure to Strong inhibitors of CYP2D6 considered to be included?")
class DynamicEntity(BaseModel):
    exp_cyp3a4_ever: Optional[List[Exp_cyp3a4_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A4? If so, is a patient with any prior exposure to Strong inhibitors of CYP3A4 considered to be included? Example: Consider CYP3A4 and CYP3A as distinct instances.")
class DynamicEntity(BaseModel):
    exp_cyp3a_ever: Optional[List[Exp_cyp3a_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A? If so, is a patient with any prior exposure to Strong inhibitors of CYP3A considered to be included? Example: Consider CYP3A4 and CYP3A as distinct instances.")
class DynamicEntity(BaseModel):
    exp_calcineurin_ever: Optional[List[Exp_calcineurin_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to calcineurin inhibitors? If so, is a patient with any prior exposure to calcineurin inhibitors considered to be included?")
class DynamicEntity(BaseModel):
    exp_monocl_antib_ever: Optional[List[Exp_monocl_antib_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to monoclonal antibodies? If so, is a patient with any prior exposure to monoclonal antibodies considered to be included?")
class DynamicEntity(BaseModel):
    exp_immunotherapy_ever: Optional[List[Exp_immunotherapy_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to immunotherapy? If so, is a patient with any prior exposure to immunotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_gpc3_ever: Optional[List[Exp_gpc3_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to GPC3-directed immunotherapy? If so, is a patient with any prior exposure to GPC3-directed immunotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_demeth_hdac_ever: Optional[List[Exp_demeth_hdac_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Demethylating and/or HDAC Inhibitor Therapy? If so, is a patient with any prior exposure to Demethylating and/or HDAC Inhibitor Therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_cd123_cart: Optional[List[Exp_cd123_cart]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells? If so, is a patient with any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells considered to be included?")
class DynamicEntity(BaseModel):
    exp_anthracycline_ever: Optional[List[Exp_anthracycline_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to anthracycline or equivalent? If so, is a patient with any prior exposure to anthracycline or equivalent considered to be included?")
class DynamicEntity(BaseModel):
    cumul_anthracycline: Optional[str] = Field(
        None, 
        description="Does eligibility criteria mention cumulative anthracycline or equivalent? If so, how much cumulative anthracycline or equivalent (in mg/m^2) is considered to be included? Example: the answer is 450 mg/m^2, if \"total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2\"")
class DynamicEntity(BaseModel):
    gvhd: Optional[List[Gvhd]] = Field(
        None, 
        description="Does the eligibility criteria mention presence of graft versus host disease, or GVHD? If so, is a patient with presence of GVHD considered to be included? Example: \"active uncontrolled graft versus host disease (GvHD)\"")
class DynamicEntity(BaseModel):
    vpa_meds: Optional[List[Vpa_meds]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to receiving valproic acid (VPA) therapy? If so, is a patient with any prior exposure to receiving valproic acid therapy considered to be included?")
class DynamicEntity(BaseModel):
    prior_solid_organ_transpl: Optional[List[Prior_solid_organ_transpl]] = Field(
        None, 
        description="Does the eligibility criteria mention a prior solid organ transplantation? If so, is a patient with a prior solid organ transplantation considered to be included?")
class DynamicEntity(BaseModel):
    exp_uproleselan: Optional[List[Exp_uproleselan]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to uproleselan? If so, is a patient with prior exposure to uproleselan considered to be included?")
class DynamicEntity(BaseModel):
    exp_flotetuzumab: Optional[List[Exp_flotetuzumab]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to flotetuzumab? If so, is a patient with prior exposure to flotetuzumab considered to be included?")
class DynamicEntity(BaseModel):
    exp_venetoclax: Optional[List[Exp_venetoclax]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to venetoclax? If so, is a patient with prior exposure to venetoclax considered to be included?")
class DynamicEntity(BaseModel):
    exp_venetoclax_sensitive: Optional[List[Exp_venetoclax_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to venetoclax? If so, is a patient with previous toxicity or hypersensitivity directly attributed to venetoclax considered to be included?")
class DynamicEntity(BaseModel):
    donor_available: Optional[List[Donor_available]] = Field(
        None, 
        description="Does the eligibility criteria mention a suitable stem cell donor available? If so, is a patient with a suitable stem cell donor available considered to be included?")
class DynamicEntity(BaseModel):
    dyspnea_present: Optional[List[Dyspnea_present]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of dyspnea? If so, is a patient with evidence of dyspnea considered to be included?")
class DynamicEntity(BaseModel):
    hypoxia_present: Optional[List[Hypoxia_present]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of hypoxia? If so, is a patient with evidence of hypoxia considered to be included?")
class DynamicEntity(BaseModel):
    expression_msln: Optional[List[Expression_msln]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of MSLN expression? If so, is a patient with evidence of MSLN expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_cd123: Optional[List[Expression_cd123]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of CD123 expression? If so, is a patient with evidence of CD123 expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_eselectin: Optional[List[Expression_eselectin]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of E-selectin expression? If so, is a patient with evidence of E-selectin expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_kmt2ar: Optional[List[Expression_kmt2ar]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of KMT2A rearrangement (KMT2Ar)? If so, is a patient with evidence of KMT2Ar considered to be included?")
class DynamicEntity(BaseModel):
    expression_t1517: Optional[List[Expression_t1517]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of t(15;17) translocation? If so, is a patient with evidence of t(15;17) translocation considered to be included?")
class DynamicEntity(BaseModel):
    expression_som_JAK2_V617F: Optional[List[Expression_som_jak2_v617f]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of somatic JAK2 V617F mutation? If so, is a patient with evidence of somatic JAK2 V617F mutation considered to be included?")
class DynamicEntity(BaseModel):
    expression_flt3_itd: Optional[List[Expression_flt3_itd]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of FLT3 / internal tandem duplication (ITD) mutation? If so, is a patient with evidence of FLT3 / internal tandem duplication mutation considered to be included?")
class DynamicEntity(BaseModel):
    diag_cong_blood_disorder: Optional[List[Diag_cong_blood_disorder]] = Field(
        None, 
        description="Does the eligibility criteria mention any congenital bleeding disorders, including but not limited to hemophilia? If so, is a patient with any congenital bleeding disorders, including but not limited to hemophilia considered to be included?")
class DynamicEntity(BaseModel):
    diag_intercurrent_illness: Optional[List[Diag_intercurrent_illness]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of any significant intercurrent disease? If so, is a patient with a diagnosis of any significant intercurrent disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_mets_cns: Optional[List[Diag_mets_cns]] = Field(
        None, 
        description="Does the eligibility criteria mention metastatic CNS involvement? If so, is a patient with metastatic CNS involvement considered to be included?")
class DynamicEntity(BaseModel):
    diag_hemolytic_anemia: Optional[List[Diag_hemolytic_anemia]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of hemolytic anemia? If so, is a patient with a diagnosis of hemolytic anemia considered to be included?")
class DynamicEntity(BaseModel):
    diag_evans_syndrome: Optional[List[Diag_evans_syndrome]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Evans syndrome? If so, is a patient with a diagnosis of Evans syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_uncontrolled_cardiac_rhythm: Optional[List[Diag_uncontrolled_cardiac_rhythm]] = Field(
        None, 
        description="Does the eligibility criteria mention uncontrolled cardiac rhythm disturbance? If so, is a patient with uncontrolled cardiac rhythm disturbance considered to be included?")
class DynamicEntity(BaseModel):
    diag_severe_psychiatric_disorder: Optional[List[Diag_severe_psychiatric_disorder]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of acute or chronic severe psychiatric disorders? If so, is a patient with a diagnosis of acute or chronic severe psychiatric disorders considered to be included?")
class DynamicEntity(BaseModel):
    diag_other_malignancies: Optional[List[Diag_other_malignancies]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of other malignancies? If so, is a patient with a diagnosis of other malignancies considered to be included?")
class DynamicEntity(BaseModel):
    diag_pneumonitis: Optional[List[Diag_pneumonitis]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of pneumonitis? If so, is a patient with a diagnosis of pneumonitis considered to be included?")
class DynamicEntity(BaseModel):
    diag_mibg_avidity: Optional[List[Diag_mibg_avidity]] = Field(
        None, 
        description="Does the eligibility criteria mention indications of tumor(s) / lesion(s) with known MIBG avidity? If so, is a patient with indications of tumor(s) / lesion(s) with known MIBG avidity considered to be included?")
class DynamicEntity(BaseModel):
    diag_fdg_avidity: Optional[List[Diag_fdg_avidity]] = Field(
        None, 
        description="Does the eligibility criteria mention tumor(s) / lesion(s) with known FDG avidity? If so, is a patient with tumor(s) / lesion(s) with known FDG avidity considered to be included?")
class DynamicEntity(BaseModel):
    diag_signif_pleural_effusion: Optional[List[Diag_signif_pleural_effusion]] = Field(
        None, 
        description="Does the eligibility criteria mention clinically significant, symptomatic, pleural effusions? If so, is a patient with clinically significant, symptomatic, pleural effusions considered to be included?")
class DynamicEntity(BaseModel):
    diag_signif_pericardial_effusion: Optional[List[Diag_signif_pericardial_effusion]] = Field(
        None, 
        description="Does the eligibility criteria mention physiologically significant pericardial effusion? If so, is a patient with physiologically significant pericardial effusion considered to be included?")
class DynamicEntity(BaseModel):
    diag_measureable_disease: Optional[List[Diag_measureable_disease]] = Field(
        None, 
        description="Does the eligibility criteria mention the patient having measurable disease? If so, is a patient with measurable disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_measureable_tumor: Optional[List[Diag_measureable_tumor]] = Field(
        None, 
        description="Does the eligibility criteria mention the patient having one or more tumor / lesion sites with measurable dimensions? If so, is a patient with one or more tumor / lesion sites with measurable dimensions considered to be included?")
class DynamicEntity(BaseModel):
    diag_primary_immunodeficiency: Optional[List[Diag_primary_immunodeficiency]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of primary immunodeficiency? If so, is a patient with a diagnosis of primary immunodeficiency considered to be included?")
class DynamicEntity(BaseModel):
    exp_cellular_therapy: Optional[List[Exp_cellular_therapy]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to  live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell])? If so, is a patient with any prior exposure to live cellular therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_ch14_18_sensitive: Optional[List[Exp_ch14_18_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to ch14.18 considered to be included?")
class DynamicEntity(BaseModel):
    exp_anti_gd2_sensitive: Optional[List[Exp_anti_gd2_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody considered to be included?")
class DynamicEntity(BaseModel):
    exp_hu5f9g4_sensitive: Optional[List[Exp_hu5f9g4_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody? If so, is a patient with previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 monoclonal antibody considered to be included?")
class DynamicEntity(BaseModel):
    exp_gm_csf_sensitive: Optional[List[Exp_gm_csf_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide considered to be included?")
class DynamicEntity(BaseModel):
    exp_pd1_pdl_ever: Optional[List[Exp_pd1_pdl_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies (e.g. Nivolumab)? If so, is a patient with any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies considered to be included?")
class DynamicEntity(BaseModel):
    exp_anti_ctla4_ever: Optional[List[Exp_anti_ctla4_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any anti-CTLA4 agent? If so, is a patient with any prior exposure to any anti-CTLA4 agent considered to be included?")
class DynamicEntity(BaseModel):
    exp_lorlatinib_ever: Optional[List[Exp_lorlatinib_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to lorlatinib? If so, is a patient with any prior exposure to lorlatinib considered to be included?")
class DynamicEntity(BaseModel):
    exp_cd47_sirpalpha_ever: Optional[List[Exp_cd47_sirpalpha_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any CD47–SIRPα-targeted therapeutics? If so, is a patient with any prior exposure to any CD47–SIRPα-targeted therapeutics considered to be included?")
class DynamicEntity(BaseModel):
    exp_ivig_ever: Optional[List[Exp_ivig_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Intravenous Immunoglobulin (IVIg) therapy? If so, is a patient with any prior exposure to  Intravenous Immunoglobulin therapy considered to be included?")
class DynamicEntity(BaseModel):
    cumul_131l_mibg: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention cumulative 131I-MIBG dosing? If so, how much cumulative 131I-MIBG dosing (in mCi/kg) is considered to be included? Example: the answer is > 54 mCi/kg, if \"treated with iodine-131 (131I)-MIBG who have already received a cumulative I-131 dose > 54 mCi/kg or who would exceed 54 mCi/kg by participating\"")
class DynamicEntity(BaseModel):
    expression_alk: Optional[List[Expression_alk]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of ALK mutation? If so, is a patient with evidence of ALK mutation considered to be included?")
class DynamicEntity(BaseModel):
    expression_alk_type: Optional[List[Expression_alk_type]] = Field(
        None, 
        description="Does the eligibility criteria mention ALK mutations? If so, what types of ALK mutations are considered to be included?")
class DynamicEntity(BaseModel):
    bclc_stage: Optional[List[Bclc_stage]] = Field(
        None, 
        description="Does the eligibility criteria mention BCLC stage? If so, what BCLC stages are considered to be included?")
class DynamicEntity(BaseModel):
    ctp_score: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Child-Pugh-Turcotte score? If so, what Child-Pugh-Turcotte score is considered to be included?")
class DynamicEntity(BaseModel):
    expression_gpc3: Optional[List[Expression_gpc3]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?")
class DynamicEntity(BaseModel):
    age_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the minimum age of eligibility? If so, what is the minimum age of eligibility (in years) considered to be included?")
class DynamicEntity(BaseModel):
    age_max: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the maximum age of eligibility? If so, what is the maximum age of eligibility (in years) considered to be included?")
class DynamicEntity(BaseModel):
    weight_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the minimum weight a patient may have? If so, what is the minimum weight (in kilograms) of a patient considered to be included?")
class DynamicEntity(BaseModel):
    weight_max: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the maximum weight a patient may have? If so, what is the maximum weight (in kilograms) of a patient considered to be included?")
class DynamicEntity(BaseModel):
    sex: Optional[List[Sex]] = Field(
        None, 
        description="Does the eligibility criteria mention sexes of a patient? If so, which sexes are considered to be included?")
class DynamicEntity(BaseModel):
    diagnosis: Optional[List[Diagnosis]] = Field(
        None, 
        description="Does the eligibility criteria mention a patient's current diagnoses? If so, which diagnoses are considered to be included?")
class DynamicEntity(BaseModel):
    ever_refractory: Optional[List[Ever_refractory]] = Field(
        None, 
        description="Does the eligibility criteria mention refractory disease? If so, is a patient with refractory disease considered to be included? Example: refractory disease are diseases such as \"Refractory leukemia\"")
class DynamicEntity(BaseModel):
    count_refractory: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the occurrences of refractory disease? If so, how many occurrences of refractory disease are required to be included?")
class DynamicEntity(BaseModel):
    current_refractory_num_cycles: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention number of cycles of therapy required for refractory disease? If so, what is the minimum number of cycles of therapy required for refractory disease considered to be included? Example: the answer is 1 if \"refractory to at least one course of salvage therapy\", the answer is 2 if \"persistent after at least two courses of induction \"chemotherapy\", the answer is 2 if \"refractory disease after >= 2 cycles of chemotherapy\"")
class DynamicEntity(BaseModel):
    ever_relapse: Optional[List[Ever_relapse]] = Field(
        None, 
        description="Does the eligibility criteria mention confirmed or suspected relapse disease? If so, is confirmed or suspected relapse disease considered to be included? Example: relapse disease such as \"relapsed leukemia\"")
class DynamicEntity(BaseModel):
    count_relapse: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention the number of relapses required? If so, what is the minimum number of relapses required to be included? Example: the answer is 2 if \"Second or greater relapse\", the answer is 1 if \"first relapses\"")
class DynamicEntity(BaseModel):
    bm_recent_blast_pct_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention bone marrow blast percentage? If so, what is the minimum bone marrow blast percentage considered to be included? Example: the answer is 5 if \">= 5% blasts in the bone marrow\", the answer is 5 if \"> 5% blasts in the BM\" is mentioned")
class DynamicEntity(BaseModel):
    bm_recent_blast_method: Optional[List[Bm_recent_blast_method]] = Field(
        None, 
        description="Does the eligibility criteria mention methods for bone marrow blast percentage assessment? If so, what are the required methods for bone marrow blast percentage assessment considered to be included? Example: \"Morphology\", \"Flow cytometry\"")
class DynamicEntity(BaseModel):
    periph_blood_blast_abs_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the peripheral blood absolute blast count measurement? If so, what is the peripheral blood absolute blast count measurement (in cells/microliter) considered to be included?")
class DynamicEntity(BaseModel):
    periph_blood_blast_pct_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the defined peripheral blood blast percentage? If so, what is the minimum defined peripheral blood blast percentage considered to be included? Example: the answer is 5 if \">= 5% blasts in the peripheral blood\" is mentioned, the answer is 5 if \">=5% blasts in the blood\" is mentioned")
class DynamicEntity(BaseModel):
    corneal_epitheliopathy: Optional[List[Corneal_epitheliopathy]] = Field(
        None, 
        description="Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy? If so, is a patient with such diagnosis considered to be included?")
class DynamicEntity(BaseModel):
    cns_status: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention CNS status? If so, what CNS status is considered to be included? Example: \"CNS 1\", \"CNS 2\", \"CNS 3\"")
class DynamicEntity(BaseModel):
    lanksy_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Lansky score? If so, what is the minimum Lansky score for a patient considered to be included? Example: the answer is 70 if \"Lansky score>=70\" is mentioned")
class DynamicEntity(BaseModel):
    karnofksy_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Karnofsky score? If so, what is the minimum Karnofsky score for a patient considered to be included? Example: the answer is 50 if \"Karnofsky score >= 50\" is mentioned")
class DynamicEntity(BaseModel):
    diag_down_syndrome: Optional[List[Diag_down_syndrome]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Down syndrome? If so, is a patient with a diagnosis of Down syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_iso_emd: Optional[List[Diag_iso_emd]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of isolated extramedullary disease (i.e. the absence of bone marrow involvement)? If so, is a patient with a diagnosis of isolated extramedullary disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_iso_testes: Optional[List[Diag_iso_testes]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of isolated testicular relapse? If so, is a patient with a diagnosis of isolated testicular relapse considered to be included?")
class DynamicEntity(BaseModel):
    diag_ataxia_telang: Optional[List[Diag_ataxia_telang]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of ataxia-telangiectasia? If so, is a patient with a diagnosis of ataxia-telangiectasia considered to be included?")
class DynamicEntity(BaseModel):
    diag_bloom: Optional[List[Diag_bloom]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Bloom syndrome? If so, is a patient with a diagnosis of Bloom syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_fanconi: Optional[List[Diag_fanconi]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Fanconi anemia? If so, is a patient with a diagnosis of Fanconi anemia considered to be included?")
class DynamicEntity(BaseModel):
    diag_kostmann: Optional[List[Diag_kostmann]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Kostmann syndrome? If so, is a patient with a diagnosis of Kostmann syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_shwachman: Optional[List[Diag_shwachman]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Shwachman syndrome? If so, is a patient with a diagnosis of Shwachman syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_cong_bmf: Optional[List[Diag_cong_bmf]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)? If so, is a patient with such diagnosis considered to be included?")
class DynamicEntity(BaseModel):
    diag_malabsoption: Optional[List[Diag_malabsoption]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of malabsorption syndrome? If so, is a patient with a diagnosis of malabsorption syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_chf: Optional[List[Diag_chf]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of congestive heart failure (CHF)? If so, is a patient with a diagnosis of congestive heart failure considered to be included?")
class DynamicEntity(BaseModel):
    diag_hiv: Optional[List[Diag_hiv]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of human immunodeficiency virus (HIV) infection? If so, is a patient with a diagnosis of human immunodeficiency virus infection considered be included?")
class DynamicEntity(BaseModel):
    diag_uncontr_cns: Optional[List[Diag_uncontr_cns]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis)? If so, is a patient with a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology considered to be included?")
class DynamicEntity(BaseModel):
    diag_hep_b_c: Optional[List[Diag_hep_b_c]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of hepatitis B or C infection? If so, is a patient with a diagnosis of hepatitis B or C infection considered to be included?")
class DynamicEntity(BaseModel):
    diag_liver_cirr_serious: Optional[List[Diag_liver_cirr_serious]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of liver cirrhosis or other serious liver disease? If so, is a patient with a diagnosis of liver cirrhosis or other serious liver disease considered to be included?")
class DynamicEntity(BaseModel):
    active_infection: Optional[List[Active_infection]] = Field(
        None, 
        description="Does the eligibility criteria mention a documented active, uncontrolled infection? If so, is a patient with a documented active, uncontrolled infection considered to be included?")
class DynamicEntity(BaseModel):
    refractory_transfusion: Optional[List[Refractory_transfusion]] = Field(
        None, 
        description="Does the eligibility criteria mention a patient known to be refractory to red blood cells or platelet transfusions? If so, is a patient known to be refractory to red blood cells or platelet transfusions considered to be included?")
class DynamicEntity(BaseModel):
    cerebellar_toxicity: Optional[List[Cerebellar_toxicity]] = Field(
        None, 
        description="Does the eligibility criteria mention an history of cerebellar toxicity or cerebellar neurological findings on exam? If so, is a patient with a history of cerebellar toxicity or cerebellar neurological findings on exam considered to be included?")
class DynamicEntity(BaseModel):
    exp_cytotoxic_chemo_ever: Optional[List[Exp_cytotoxic_chemo_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)? If so, is a patient with any prior exposure to cytotoxic chemotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_corticosteroids_ever: Optional[List[Exp_corticosteroids_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy)? If so, is a patient with any prior exposure to corticosteroids considered to be included?")
class DynamicEntity(BaseModel):
    exp_anticancer_nonmyelosupp_ever: Optional[List[Exp_anticancer_nonmyelosupp_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to non-myelosuppressive anti-cancer agents? If so, is a patient with any prior exposure to non-myelosuppressive anti-cancer agents considered to be included?")
class DynamicEntity(BaseModel):
    exp_anticancer_myelosupp_ever: Optional[List[Exp_anticancer_myelosupp_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to myelosuppressive anti-cancer agents? If so, is a patient with any prior exposure to myelosuppressive anti-cancer agents considered to be included?")
class DynamicEntity(BaseModel):
    exp_antibody_drug_conj_ever: Optional[List[Exp_antibody_drug_conj_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to antibody-drug conjugate? If so, is a patient with any prior exposure to antibody-drug conjugate considered to be included?")
class DynamicEntity(BaseModel):
    exp_interleukins_ever: Optional[List[Exp_interleukins_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Interleukins, Interferons and Cytokines (not including Hematopoietic Growth Factors)? If so, is a patient with any prior exposure to Interleukins, Interferons and Cytokines considered to be included?")
class DynamicEntity(BaseModel):
    exp_long_acting_gf_ever: Optional[List[Exp_long_acting_gf_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Long-acting growth factor (eg, pegfilgrastim)? If so, is a patient with any prior exposure to Long-acting growth factor considered to be included?")
class DynamicEntity(BaseModel):
    exp_short_acting_gf_ever: Optional[List[Exp_short_acting_gf_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Short-acting growth factor? If so, is a patient with any prior exposure to Short-acting growth factor considered to be included?")
class DynamicEntity(BaseModel):
    exp_rt_ever: Optional[List[Exp_rt_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Radiotherapy (RT)? If so, is a patient with any prior exposure to Radiotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_craniospatial_rt_ever: Optional[List[Exp_craniospatial_rt_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Craniospinal radiotherapy (RT)? If so, is a patient with any prior exposure to Craniospinal radiotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_tbi_ever: Optional[List[Exp_tbi_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Total Body Irradiation (TBI)? If so, is a patient with any prior exposure to Total Body Irradiation considered to be included?")
class DynamicEntity(BaseModel):
    exp_radiopharma_ever: Optional[List[Exp_radiopharma_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Radiopharmaceutical therapy (e.g., radiolabeled antibody, 131I-MIBG)? If so, is a patient with any prior exposure to Radiopharmaceutical therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_hct: Optional[List[Exp_hct]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Hematopoietic cell transplantation (HCT)? If so, is a patient with any prior exposure to Hematopoietic cell transplantation (HCT) considered to be included?")
class DynamicEntity(BaseModel):
    type_transplant: Optional[List[Type_transplant]] = Field(
        None, 
        description="Does the eligibility criteria mention type(s) of transplant? If so, what type(s) of transplant are considered to be included?")
class DynamicEntity(BaseModel):
    exp_dli_ever: Optional[List[Exp_dli_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to DLI (donor lymphocyte infusion) or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.)? If so, is a patient with any prior exposure to DLI or any type of cellular therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_cyp2d6_ever: Optional[List[Exp_cyp2d6_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP2D6? If so, is a patient with any prior exposure to Strong inhibitors of CYP2D6 considered to be included?")
class DynamicEntity(BaseModel):
    exp_cyp3a4_ever: Optional[List[Exp_cyp3a4_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A4? If so, is a patient with any prior exposure to Strong inhibitors of CYP3A4 considered to be included? Example: Consider CYP3A4 and CYP3A as distinct instances.")
class DynamicEntity(BaseModel):
    exp_cyp3a_ever: Optional[List[Exp_cyp3a_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A? If so, is a patient with any prior exposure to Strong inhibitors of CYP3A considered to be included? Example: Consider CYP3A4 and CYP3A as distinct instances.")
class DynamicEntity(BaseModel):
    exp_calcineurin_ever: Optional[List[Exp_calcineurin_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to calcineurin inhibitors? If so, is a patient with any prior exposure to calcineurin inhibitors considered to be included?")
class DynamicEntity(BaseModel):
    exp_monocl_antib_ever: Optional[List[Exp_monocl_antib_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to monoclonal antibodies? If so, is a patient with any prior exposure to monoclonal antibodies considered to be included?")
class DynamicEntity(BaseModel):
    exp_immunotherapy_ever: Optional[List[Exp_immunotherapy_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to immunotherapy? If so, is a patient with any prior exposure to immunotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_gpc3_ever: Optional[List[Exp_gpc3_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to GPC3-directed immunotherapy? If so, is a patient with any prior exposure to GPC3-directed immunotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_demeth_hdac_ever: Optional[List[Exp_demeth_hdac_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Demethylating and/or HDAC Inhibitor Therapy? If so, is a patient with any prior exposure to Demethylating and/or HDAC Inhibitor Therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_cd123_cart: Optional[List[Exp_cd123_cart]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells? If so, is a patient with any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells considered to be included?")
class DynamicEntity(BaseModel):
    exp_anthracycline_ever: Optional[List[Exp_anthracycline_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to anthracycline or equivalent? If so, is a patient with any prior exposure to anthracycline or equivalent considered to be included?")
class DynamicEntity(BaseModel):
    cumul_anthracycline: Optional[str] = Field(
        None, 
        description="Does eligibility criteria mention cumulative anthracycline or equivalent? If so, how much cumulative anthracycline or equivalent (in mg/m^2) is considered to be included? Example: the answer is 450 mg/m^2, if \"total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2\"")
class DynamicEntity(BaseModel):
    gvhd: Optional[List[Gvhd]] = Field(
        None, 
        description="Does the eligibility criteria mention presence of graft versus host disease, or GVHD? If so, is a patient with presence of GVHD considered to be included? Example: \"active uncontrolled graft versus host disease (GvHD)\"")
class DynamicEntity(BaseModel):
    vpa_meds: Optional[List[Vpa_meds]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to receiving valproic acid (VPA) therapy? If so, is a patient with any prior exposure to receiving valproic acid therapy considered to be included?")
class DynamicEntity(BaseModel):
    prior_solid_organ_transpl: Optional[List[Prior_solid_organ_transpl]] = Field(
        None, 
        description="Does the eligibility criteria mention a prior solid organ transplantation? If so, is a patient with a prior solid organ transplantation considered to be included?")
class DynamicEntity(BaseModel):
    exp_uproleselan: Optional[List[Exp_uproleselan]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to uproleselan? If so, is a patient with prior exposure to uproleselan considered to be included?")
class DynamicEntity(BaseModel):
    exp_flotetuzumab: Optional[List[Exp_flotetuzumab]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to flotetuzumab? If so, is a patient with prior exposure to flotetuzumab considered to be included?")
class DynamicEntity(BaseModel):
    exp_venetoclax: Optional[List[Exp_venetoclax]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to venetoclax? If so, is a patient with prior exposure to venetoclax considered to be included?")
class DynamicEntity(BaseModel):
    exp_venetoclax_sensitive: Optional[List[Exp_venetoclax_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to venetoclax? If so, is a patient with previous toxicity or hypersensitivity directly attributed to venetoclax considered to be included?")
class DynamicEntity(BaseModel):
    donor_available: Optional[List[Donor_available]] = Field(
        None, 
        description="Does the eligibility criteria mention a suitable stem cell donor available? If so, is a patient with a suitable stem cell donor available considered to be included?")
class DynamicEntity(BaseModel):
    dyspnea_present: Optional[List[Dyspnea_present]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of dyspnea? If so, is a patient with evidence of dyspnea considered to be included?")
class DynamicEntity(BaseModel):
    hypoxia_present: Optional[List[Hypoxia_present]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of hypoxia? If so, is a patient with evidence of hypoxia considered to be included?")
class DynamicEntity(BaseModel):
    expression_msln: Optional[List[Expression_msln]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of MSLN expression? If so, is a patient with evidence of MSLN expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_cd123: Optional[List[Expression_cd123]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of CD123 expression? If so, is a patient with evidence of CD123 expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_eselectin: Optional[List[Expression_eselectin]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of E-selectin expression? If so, is a patient with evidence of E-selectin expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_kmt2ar: Optional[List[Expression_kmt2ar]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of KMT2A rearrangement (KMT2Ar)? If so, is a patient with evidence of KMT2Ar considered to be included?")
class DynamicEntity(BaseModel):
    expression_t1517: Optional[List[Expression_t1517]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of t(15;17) translocation? If so, is a patient with evidence of t(15;17) translocation considered to be included?")
class DynamicEntity(BaseModel):
    expression_som_JAK2_V617F: Optional[List[Expression_som_jak2_v617f]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of somatic JAK2 V617F mutation? If so, is a patient with evidence of somatic JAK2 V617F mutation considered to be included?")
class DynamicEntity(BaseModel):
    expression_flt3_itd: Optional[List[Expression_flt3_itd]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of FLT3 / internal tandem duplication (ITD) mutation? If so, is a patient with evidence of FLT3 / internal tandem duplication mutation considered to be included?")
class DynamicEntity(BaseModel):
    diag_cong_blood_disorder: Optional[List[Diag_cong_blood_disorder]] = Field(
        None, 
        description="Does the eligibility criteria mention any congenital bleeding disorders, including but not limited to hemophilia? If so, is a patient with any congenital bleeding disorders, including but not limited to hemophilia considered to be included?")
class DynamicEntity(BaseModel):
    diag_intercurrent_illness: Optional[List[Diag_intercurrent_illness]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of any significant intercurrent disease? If so, is a patient with a diagnosis of any significant intercurrent disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_mets_cns: Optional[List[Diag_mets_cns]] = Field(
        None, 
        description="Does the eligibility criteria mention metastatic CNS involvement? If so, is a patient with metastatic CNS involvement considered to be included?")
class DynamicEntity(BaseModel):
    diag_hemolytic_anemia: Optional[List[Diag_hemolytic_anemia]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of hemolytic anemia? If so, is a patient with a diagnosis of hemolytic anemia considered to be included?")
class DynamicEntity(BaseModel):
    diag_evans_syndrome: Optional[List[Diag_evans_syndrome]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Evans syndrome? If so, is a patient with a diagnosis of Evans syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_uncontrolled_cardiac_rhythm: Optional[List[Diag_uncontrolled_cardiac_rhythm]] = Field(
        None, 
        description="Does the eligibility criteria mention uncontrolled cardiac rhythm disturbance? If so, is a patient with uncontrolled cardiac rhythm disturbance considered to be included?")
class DynamicEntity(BaseModel):
    diag_severe_psychiatric_disorder: Optional[List[Diag_severe_psychiatric_disorder]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of acute or chronic severe psychiatric disorders? If so, is a patient with a diagnosis of acute or chronic severe psychiatric disorders considered to be included?")
class DynamicEntity(BaseModel):
    diag_other_malignancies: Optional[List[Diag_other_malignancies]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of other malignancies? If so, is a patient with a diagnosis of other malignancies considered to be included?")
class DynamicEntity(BaseModel):
    diag_pneumonitis: Optional[List[Diag_pneumonitis]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of pneumonitis? If so, is a patient with a diagnosis of pneumonitis considered to be included?")
class DynamicEntity(BaseModel):
    diag_mibg_avidity: Optional[List[Diag_mibg_avidity]] = Field(
        None, 
        description="Does the eligibility criteria mention indications of tumor(s) / lesion(s) with known MIBG avidity? If so, is a patient with indications of tumor(s) / lesion(s) with known MIBG avidity considered to be included?")
class DynamicEntity(BaseModel):
    diag_fdg_avidity: Optional[List[Diag_fdg_avidity]] = Field(
        None, 
        description="Does the eligibility criteria mention tumor(s) / lesion(s) with known FDG avidity? If so, is a patient with tumor(s) / lesion(s) with known FDG avidity considered to be included?")
class DynamicEntity(BaseModel):
    diag_signif_pleural_effusion: Optional[List[Diag_signif_pleural_effusion]] = Field(
        None, 
        description="Does the eligibility criteria mention clinically significant, symptomatic, pleural effusions? If so, is a patient with clinically significant, symptomatic, pleural effusions considered to be included?")
class DynamicEntity(BaseModel):
    diag_signif_pericardial_effusion: Optional[List[Diag_signif_pericardial_effusion]] = Field(
        None, 
        description="Does the eligibility criteria mention physiologically significant pericardial effusion? If so, is a patient with physiologically significant pericardial effusion considered to be included?")
class DynamicEntity(BaseModel):
    diag_measureable_disease: Optional[List[Diag_measureable_disease]] = Field(
        None, 
        description="Does the eligibility criteria mention the patient having measurable disease? If so, is a patient with measurable disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_measureable_tumor: Optional[List[Diag_measureable_tumor]] = Field(
        None, 
        description="Does the eligibility criteria mention the patient having one or more tumor / lesion sites with measurable dimensions? If so, is a patient with one or more tumor / lesion sites with measurable dimensions considered to be included?")
class DynamicEntity(BaseModel):
    diag_primary_immunodeficiency: Optional[List[Diag_primary_immunodeficiency]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of primary immunodeficiency? If so, is a patient with a diagnosis of primary immunodeficiency considered to be included?")
class DynamicEntity(BaseModel):
    exp_cellular_therapy: Optional[List[Exp_cellular_therapy]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to  live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell])? If so, is a patient with any prior exposure to live cellular therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_ch14_18_sensitive: Optional[List[Exp_ch14_18_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to ch14.18 considered to be included?")
class DynamicEntity(BaseModel):
    exp_anti_gd2_sensitive: Optional[List[Exp_anti_gd2_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody considered to be included?")
class DynamicEntity(BaseModel):
    exp_hu5f9g4_sensitive: Optional[List[Exp_hu5f9g4_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody? If so, is a patient with previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 monoclonal antibody considered to be included?")
class DynamicEntity(BaseModel):
    exp_gm_csf_sensitive: Optional[List[Exp_gm_csf_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide considered to be included?")
class DynamicEntity(BaseModel):
    exp_pd1_pdl_ever: Optional[List[Exp_pd1_pdl_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies (e.g. Nivolumab)? If so, is a patient with any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies considered to be included?")
class DynamicEntity(BaseModel):
    exp_anti_ctla4_ever: Optional[List[Exp_anti_ctla4_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any anti-CTLA4 agent? If so, is a patient with any prior exposure to any anti-CTLA4 agent considered to be included?")
class DynamicEntity(BaseModel):
    exp_lorlatinib_ever: Optional[List[Exp_lorlatinib_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to lorlatinib? If so, is a patient with any prior exposure to lorlatinib considered to be included?")
class DynamicEntity(BaseModel):
    exp_cd47_sirpalpha_ever: Optional[List[Exp_cd47_sirpalpha_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any CD47–SIRPα-targeted therapeutics? If so, is a patient with any prior exposure to any CD47–SIRPα-targeted therapeutics considered to be included?")
class DynamicEntity(BaseModel):
    exp_ivig_ever: Optional[List[Exp_ivig_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Intravenous Immunoglobulin (IVIg) therapy? If so, is a patient with any prior exposure to  Intravenous Immunoglobulin therapy considered to be included?")
class DynamicEntity(BaseModel):
    cumul_131l_mibg: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention cumulative 131I-MIBG dosing? If so, how much cumulative 131I-MIBG dosing (in mCi/kg) is considered to be included? Example: the answer is > 54 mCi/kg, if \"treated with iodine-131 (131I)-MIBG who have already received a cumulative I-131 dose > 54 mCi/kg or who would exceed 54 mCi/kg by participating\"")
class DynamicEntity(BaseModel):
    expression_alk: Optional[List[Expression_alk]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of ALK mutation? If so, is a patient with evidence of ALK mutation considered to be included?")
class DynamicEntity(BaseModel):
    expression_alk_type: Optional[List[Expression_alk_type]] = Field(
        None, 
        description="Does the eligibility criteria mention ALK mutations? If so, what types of ALK mutations are considered to be included?")
class DynamicEntity(BaseModel):
    bclc_stage: Optional[List[Bclc_stage]] = Field(
        None, 
        description="Does the eligibility criteria mention BCLC stage? If so, what BCLC stages are considered to be included?")
class DynamicEntity(BaseModel):
    ctp_score: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Child-Pugh-Turcotte score? If so, what Child-Pugh-Turcotte score is considered to be included?")
class DynamicEntity(BaseModel):
    expression_gpc3: Optional[List[Expression_gpc3]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?")
class DynamicEntity(BaseModel):
    age_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the minimum age of eligibility? If so, what is the minimum age of eligibility (in years) considered to be included?")
class DynamicEntity(BaseModel):
    age_max: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the maximum age of eligibility? If so, what is the maximum age of eligibility (in years) considered to be included?")
class DynamicEntity(BaseModel):
    weight_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the minimum weight a patient may have? If so, what is the minimum weight (in kilograms) of a patient considered to be included?")
class DynamicEntity(BaseModel):
    weight_max: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the maximum weight a patient may have? If so, what is the maximum weight (in kilograms) of a patient considered to be included?")
class DynamicEntity(BaseModel):
    sex: Optional[List[Sex]] = Field(
        None, 
        description="Does the eligibility criteria mention sexes of a patient? If so, which sexes are considered to be included?")
class DynamicEntity(BaseModel):
    diagnosis: Optional[List[Diagnosis]] = Field(
        None, 
        description="Does the eligibility criteria mention a patient's current diagnoses? If so, which diagnoses are considered to be included?")
class DynamicEntity(BaseModel):
    ever_refractory: Optional[List[Ever_refractory]] = Field(
        None, 
        description="Does the eligibility criteria mention refractory disease? If so, is a patient with refractory disease considered to be included? Example: refractory disease are diseases such as \"Refractory leukemia\"")
class DynamicEntity(BaseModel):
    count_refractory: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the occurrences of refractory disease? If so, how many occurrences of refractory disease are required to be included?")
class DynamicEntity(BaseModel):
    current_refractory_num_cycles: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention number of cycles of therapy required for refractory disease? If so, what is the minimum number of cycles of therapy required for refractory disease considered to be included? Example: the answer is 1 if \"refractory to at least one course of salvage therapy\", the answer is 2 if \"persistent after at least two courses of induction \"chemotherapy\", the answer is 2 if \"refractory disease after >= 2 cycles of chemotherapy\"")
class DynamicEntity(BaseModel):
    ever_relapse: Optional[List[Ever_relapse]] = Field(
        None, 
        description="Does the eligibility criteria mention confirmed or suspected relapse disease? If so, is confirmed or suspected relapse disease considered to be included? Example: relapse disease such as \"relapsed leukemia\"")
class DynamicEntity(BaseModel):
    count_relapse: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention the number of relapses required? If so, what is the minimum number of relapses required to be included? Example: the answer is 2 if \"Second or greater relapse\", the answer is 1 if \"first relapses\"")
class DynamicEntity(BaseModel):
    bm_recent_blast_pct_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention bone marrow blast percentage? If so, what is the minimum bone marrow blast percentage considered to be included? Example: the answer is 5 if \">= 5% blasts in the bone marrow\", the answer is 5 if \"> 5% blasts in the BM\" is mentioned")
class DynamicEntity(BaseModel):
    bm_recent_blast_method: Optional[List[Bm_recent_blast_method]] = Field(
        None, 
        description="Does the eligibility criteria mention methods for bone marrow blast percentage assessment? If so, what are the required methods for bone marrow blast percentage assessment considered to be included? Example: \"Morphology\", \"Flow cytometry\"")
class DynamicEntity(BaseModel):
    periph_blood_blast_abs_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the peripheral blood absolute blast count measurement? If so, what is the peripheral blood absolute blast count measurement (in cells/microliter) considered to be included?")
class DynamicEntity(BaseModel):
    periph_blood_blast_pct_meas: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention the defined peripheral blood blast percentage? If so, what is the minimum defined peripheral blood blast percentage considered to be included? Example: the answer is 5 if \">= 5% blasts in the peripheral blood\" is mentioned, the answer is 5 if \">=5% blasts in the blood\" is mentioned")
class DynamicEntity(BaseModel):
    corneal_epitheliopathy: Optional[List[Corneal_epitheliopathy]] = Field(
        None, 
        description="Does the eligibility criteria mention diagnosis of corneal epitheliopathy or any eye disorder that may predispose the patient to corneal epitheliopathy? If so, is a patient with such diagnosis considered to be included?")
class DynamicEntity(BaseModel):
    cns_status: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention CNS status? If so, what CNS status is considered to be included? Example: \"CNS 1\", \"CNS 2\", \"CNS 3\"")
class DynamicEntity(BaseModel):
    lanksy_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Lansky score? If so, what is the minimum Lansky score for a patient considered to be included? Example: the answer is 70 if \"Lansky score>=70\" is mentioned")
class DynamicEntity(BaseModel):
    karnofksy_min: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Karnofsky score? If so, what is the minimum Karnofsky score for a patient considered to be included? Example: the answer is 50 if \"Karnofsky score >= 50\" is mentioned")
class DynamicEntity(BaseModel):
    diag_down_syndrome: Optional[List[Diag_down_syndrome]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Down syndrome? If so, is a patient with a diagnosis of Down syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_iso_emd: Optional[List[Diag_iso_emd]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of isolated extramedullary disease (i.e. the absence of bone marrow involvement)? If so, is a patient with a diagnosis of isolated extramedullary disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_iso_testes: Optional[List[Diag_iso_testes]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of isolated testicular relapse? If so, is a patient with a diagnosis of isolated testicular relapse considered to be included?")
class DynamicEntity(BaseModel):
    diag_ataxia_telang: Optional[List[Diag_ataxia_telang]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of ataxia-telangiectasia? If so, is a patient with a diagnosis of ataxia-telangiectasia considered to be included?")
class DynamicEntity(BaseModel):
    diag_bloom: Optional[List[Diag_bloom]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Bloom syndrome? If so, is a patient with a diagnosis of Bloom syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_fanconi: Optional[List[Diag_fanconi]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Fanconi anemia? If so, is a patient with a diagnosis of Fanconi anemia considered to be included?")
class DynamicEntity(BaseModel):
    diag_kostmann: Optional[List[Diag_kostmann]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Kostmann syndrome? If so, is a patient with a diagnosis of Kostmann syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_shwachman: Optional[List[Diag_shwachman]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Shwachman syndrome? If so, is a patient with a diagnosis of Shwachman syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_cong_bmf: Optional[List[Diag_cong_bmf]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of any known congenital bone marrow failure syndrome (e.g. Fanconi anemia, Kostmann syndrome, Shwachman syndrome)? If so, is a patient with such diagnosis considered to be included?")
class DynamicEntity(BaseModel):
    diag_malabsoption: Optional[List[Diag_malabsoption]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of malabsorption syndrome? If so, is a patient with a diagnosis of malabsorption syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_chf: Optional[List[Diag_chf]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of congestive heart failure (CHF)? If so, is a patient with a diagnosis of congestive heart failure considered to be included?")
class DynamicEntity(BaseModel):
    diag_hiv: Optional[List[Diag_hiv]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of human immunodeficiency virus (HIV) infection? If so, is a patient with a diagnosis of human immunodeficiency virus infection considered be included?")
class DynamicEntity(BaseModel):
    diag_uncontr_cns: Optional[List[Diag_uncontr_cns]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology (e.g. epilepsy, childhood seizure, paresis, aphasia, stroke, severe brain injuries, organic brain syndrome, or psychosis)? If so, is a patient with a diagnosis of clinically significant uncontrolled central nervous system (CNS) pathology considered to be included?")
class DynamicEntity(BaseModel):
    diag_hep_b_c: Optional[List[Diag_hep_b_c]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of hepatitis B or C infection? If so, is a patient with a diagnosis of hepatitis B or C infection considered to be included?")
class DynamicEntity(BaseModel):
    diag_liver_cirr_serious: Optional[List[Diag_liver_cirr_serious]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of liver cirrhosis or other serious liver disease? If so, is a patient with a diagnosis of liver cirrhosis or other serious liver disease considered to be included?")
class DynamicEntity(BaseModel):
    active_infection: Optional[List[Active_infection]] = Field(
        None, 
        description="Does the eligibility criteria mention a documented active, uncontrolled infection? If so, is a patient with a documented active, uncontrolled infection considered to be included?")
class DynamicEntity(BaseModel):
    refractory_transfusion: Optional[List[Refractory_transfusion]] = Field(
        None, 
        description="Does the eligibility criteria mention a patient known to be refractory to red blood cells or platelet transfusions? If so, is a patient known to be refractory to red blood cells or platelet transfusions considered to be included?")
class DynamicEntity(BaseModel):
    cerebellar_toxicity: Optional[List[Cerebellar_toxicity]] = Field(
        None, 
        description="Does the eligibility criteria mention an history of cerebellar toxicity or cerebellar neurological findings on exam? If so, is a patient with a history of cerebellar toxicity or cerebellar neurological findings on exam considered to be included?")
class DynamicEntity(BaseModel):
    exp_cytotoxic_chemo_ever: Optional[List[Exp_cytotoxic_chemo_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to cytotoxic chemotherapy (not including intrathecal cytotoxic chemotherapy, hydroxyurea, or corticosteroids)? If so, is a patient with any prior exposure to cytotoxic chemotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_corticosteroids_ever: Optional[List[Exp_corticosteroids_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to corticosteroids (if used to modify immune adverse events related to prior therapy)? If so, is a patient with any prior exposure to corticosteroids considered to be included?")
class DynamicEntity(BaseModel):
    exp_anticancer_nonmyelosupp_ever: Optional[List[Exp_anticancer_nonmyelosupp_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to non-myelosuppressive anti-cancer agents? If so, is a patient with any prior exposure to non-myelosuppressive anti-cancer agents considered to be included?")
class DynamicEntity(BaseModel):
    exp_anticancer_myelosupp_ever: Optional[List[Exp_anticancer_myelosupp_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to myelosuppressive anti-cancer agents? If so, is a patient with any prior exposure to myelosuppressive anti-cancer agents considered to be included?")
class DynamicEntity(BaseModel):
    exp_antibody_drug_conj_ever: Optional[List[Exp_antibody_drug_conj_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to antibody-drug conjugate? If so, is a patient with any prior exposure to antibody-drug conjugate considered to be included?")
class DynamicEntity(BaseModel):
    exp_interleukins_ever: Optional[List[Exp_interleukins_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Interleukins, Interferons and Cytokines (not including Hematopoietic Growth Factors)? If so, is a patient with any prior exposure to Interleukins, Interferons and Cytokines considered to be included?")
class DynamicEntity(BaseModel):
    exp_long_acting_gf_ever: Optional[List[Exp_long_acting_gf_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Long-acting growth factor (eg, pegfilgrastim)? If so, is a patient with any prior exposure to Long-acting growth factor considered to be included?")
class DynamicEntity(BaseModel):
    exp_short_acting_gf_ever: Optional[List[Exp_short_acting_gf_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Short-acting growth factor? If so, is a patient with any prior exposure to Short-acting growth factor considered to be included?")
class DynamicEntity(BaseModel):
    exp_rt_ever: Optional[List[Exp_rt_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Radiotherapy (RT)? If so, is a patient with any prior exposure to Radiotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_craniospatial_rt_ever: Optional[List[Exp_craniospatial_rt_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Craniospinal radiotherapy (RT)? If so, is a patient with any prior exposure to Craniospinal radiotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_tbi_ever: Optional[List[Exp_tbi_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Total Body Irradiation (TBI)? If so, is a patient with any prior exposure to Total Body Irradiation considered to be included?")
class DynamicEntity(BaseModel):
    exp_radiopharma_ever: Optional[List[Exp_radiopharma_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Radiopharmaceutical therapy (e.g., radiolabeled antibody, 131I-MIBG)? If so, is a patient with any prior exposure to Radiopharmaceutical therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_hct: Optional[List[Exp_hct]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Hematopoietic cell transplantation (HCT)? If so, is a patient with any prior exposure to Hematopoietic cell transplantation (HCT) considered to be included?")
class DynamicEntity(BaseModel):
    type_transplant: Optional[List[Type_transplant]] = Field(
        None, 
        description="Does the eligibility criteria mention type(s) of transplant? If so, what type(s) of transplant are considered to be included?")
class DynamicEntity(BaseModel):
    exp_dli_ever: Optional[List[Exp_dli_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to DLI (donor lymphocyte infusion) or any type of cellular therapy (eg, modified T cells, NK cells, dendritic cells, etc.)? If so, is a patient with any prior exposure to DLI or any type of cellular therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_cyp2d6_ever: Optional[List[Exp_cyp2d6_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP2D6? If so, is a patient with any prior exposure to Strong inhibitors of CYP2D6 considered to be included?")
class DynamicEntity(BaseModel):
    exp_cyp3a4_ever: Optional[List[Exp_cyp3a4_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A4? If so, is a patient with any prior exposure to Strong inhibitors of CYP3A4 considered to be included? Example: Consider CYP3A4 and CYP3A as distinct instances.")
class DynamicEntity(BaseModel):
    exp_cyp3a_ever: Optional[List[Exp_cyp3a_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Strong inhibitors of CYP3A? If so, is a patient with any prior exposure to Strong inhibitors of CYP3A considered to be included? Example: Consider CYP3A4 and CYP3A as distinct instances.")
class DynamicEntity(BaseModel):
    exp_calcineurin_ever: Optional[List[Exp_calcineurin_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to calcineurin inhibitors? If so, is a patient with any prior exposure to calcineurin inhibitors considered to be included?")
class DynamicEntity(BaseModel):
    exp_monocl_antib_ever: Optional[List[Exp_monocl_antib_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to monoclonal antibodies? If so, is a patient with any prior exposure to monoclonal antibodies considered to be included?")
class DynamicEntity(BaseModel):
    exp_immunotherapy_ever: Optional[List[Exp_immunotherapy_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to immunotherapy? If so, is a patient with any prior exposure to immunotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_gpc3_ever: Optional[List[Exp_gpc3_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to GPC3-directed immunotherapy? If so, is a patient with any prior exposure to GPC3-directed immunotherapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_demeth_hdac_ever: Optional[List[Exp_demeth_hdac_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Demethylating and/or HDAC Inhibitor Therapy? If so, is a patient with any prior exposure to Demethylating and/or HDAC Inhibitor Therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_cd123_cart: Optional[List[Exp_cd123_cart]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells? If so, is a patient with any prior exposure to CD123 directed antibody or CD123 directed chimeric antigen receptor (CAR) T cells considered to be included?")
class DynamicEntity(BaseModel):
    exp_anthracycline_ever: Optional[List[Exp_anthracycline_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to anthracycline or equivalent? If so, is a patient with any prior exposure to anthracycline or equivalent considered to be included?")
class DynamicEntity(BaseModel):
    cumul_anthracycline: Optional[str] = Field(
        None, 
        description="Does eligibility criteria mention cumulative anthracycline or equivalent? If so, how much cumulative anthracycline or equivalent (in mg/m^2) is considered to be included? Example: the answer is 450 mg/m^2, if \"total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2\"")
class DynamicEntity(BaseModel):
    gvhd: Optional[List[Gvhd]] = Field(
        None, 
        description="Does the eligibility criteria mention presence of graft versus host disease, or GVHD? If so, is a patient with presence of GVHD considered to be included? Example: \"active uncontrolled graft versus host disease (GvHD)\"")
class DynamicEntity(BaseModel):
    vpa_meds: Optional[List[Vpa_meds]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to receiving valproic acid (VPA) therapy? If so, is a patient with any prior exposure to receiving valproic acid therapy considered to be included?")
class DynamicEntity(BaseModel):
    prior_solid_organ_transpl: Optional[List[Prior_solid_organ_transpl]] = Field(
        None, 
        description="Does the eligibility criteria mention a prior solid organ transplantation? If so, is a patient with a prior solid organ transplantation considered to be included?")
class DynamicEntity(BaseModel):
    exp_uproleselan: Optional[List[Exp_uproleselan]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to uproleselan? If so, is a patient with prior exposure to uproleselan considered to be included?")
class DynamicEntity(BaseModel):
    exp_flotetuzumab: Optional[List[Exp_flotetuzumab]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to flotetuzumab? If so, is a patient with prior exposure to flotetuzumab considered to be included?")
class DynamicEntity(BaseModel):
    exp_venetoclax: Optional[List[Exp_venetoclax]] = Field(
        None, 
        description="Does the eligibility criteria mention prior exposure to venetoclax? If so, is a patient with prior exposure to venetoclax considered to be included?")
class DynamicEntity(BaseModel):
    exp_venetoclax_sensitive: Optional[List[Exp_venetoclax_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to venetoclax? If so, is a patient with previous toxicity or hypersensitivity directly attributed to venetoclax considered to be included?")
class DynamicEntity(BaseModel):
    donor_available: Optional[List[Donor_available]] = Field(
        None, 
        description="Does the eligibility criteria mention a suitable stem cell donor available? If so, is a patient with a suitable stem cell donor available considered to be included?")
class DynamicEntity(BaseModel):
    dyspnea_present: Optional[List[Dyspnea_present]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of dyspnea? If so, is a patient with evidence of dyspnea considered to be included?")
class DynamicEntity(BaseModel):
    hypoxia_present: Optional[List[Hypoxia_present]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of hypoxia? If so, is a patient with evidence of hypoxia considered to be included?")
class DynamicEntity(BaseModel):
    expression_msln: Optional[List[Expression_msln]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of MSLN expression? If so, is a patient with evidence of MSLN expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_cd123: Optional[List[Expression_cd123]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of CD123 expression? If so, is a patient with evidence of CD123 expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_eselectin: Optional[List[Expression_eselectin]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of E-selectin expression? If so, is a patient with evidence of E-selectin expression considered to be included?")
class DynamicEntity(BaseModel):
    expression_kmt2ar: Optional[List[Expression_kmt2ar]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of KMT2A rearrangement (KMT2Ar)? If so, is a patient with evidence of KMT2Ar considered to be included?")
class DynamicEntity(BaseModel):
    expression_t1517: Optional[List[Expression_t1517]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of t(15;17) translocation? If so, is a patient with evidence of t(15;17) translocation considered to be included?")
class DynamicEntity(BaseModel):
    expression_som_JAK2_V617F: Optional[List[Expression_som_jak2_v617f]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of somatic JAK2 V617F mutation? If so, is a patient with evidence of somatic JAK2 V617F mutation considered to be included?")
class DynamicEntity(BaseModel):
    expression_flt3_itd: Optional[List[Expression_flt3_itd]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of FLT3 / internal tandem duplication (ITD) mutation? If so, is a patient with evidence of FLT3 / internal tandem duplication mutation considered to be included?")
class DynamicEntity(BaseModel):
    diag_cong_blood_disorder: Optional[List[Diag_cong_blood_disorder]] = Field(
        None, 
        description="Does the eligibility criteria mention any congenital bleeding disorders, including but not limited to hemophilia? If so, is a patient with any congenital bleeding disorders, including but not limited to hemophilia considered to be included?")
class DynamicEntity(BaseModel):
    diag_intercurrent_illness: Optional[List[Diag_intercurrent_illness]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of any significant intercurrent disease? If so, is a patient with a diagnosis of any significant intercurrent disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_mets_cns: Optional[List[Diag_mets_cns]] = Field(
        None, 
        description="Does the eligibility criteria mention metastatic CNS involvement? If so, is a patient with metastatic CNS involvement considered to be included?")
class DynamicEntity(BaseModel):
    diag_hemolytic_anemia: Optional[List[Diag_hemolytic_anemia]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of hemolytic anemia? If so, is a patient with a diagnosis of hemolytic anemia considered to be included?")
class DynamicEntity(BaseModel):
    diag_evans_syndrome: Optional[List[Diag_evans_syndrome]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of Evans syndrome? If so, is a patient with a diagnosis of Evans syndrome considered to be included?")
class DynamicEntity(BaseModel):
    diag_uncontrolled_cardiac_rhythm: Optional[List[Diag_uncontrolled_cardiac_rhythm]] = Field(
        None, 
        description="Does the eligibility criteria mention uncontrolled cardiac rhythm disturbance? If so, is a patient with uncontrolled cardiac rhythm disturbance considered to be included?")
class DynamicEntity(BaseModel):
    diag_severe_psychiatric_disorder: Optional[List[Diag_severe_psychiatric_disorder]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of acute or chronic severe psychiatric disorders? If so, is a patient with a diagnosis of acute or chronic severe psychiatric disorders considered to be included?")
class DynamicEntity(BaseModel):
    diag_other_malignancies: Optional[List[Diag_other_malignancies]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of other malignancies? If so, is a patient with a diagnosis of other malignancies considered to be included?")
class DynamicEntity(BaseModel):
    diag_pneumonitis: Optional[List[Diag_pneumonitis]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of pneumonitis? If so, is a patient with a diagnosis of pneumonitis considered to be included?")
class DynamicEntity(BaseModel):
    diag_mibg_avidity: Optional[List[Diag_mibg_avidity]] = Field(
        None, 
        description="Does the eligibility criteria mention indications of tumor(s) / lesion(s) with known MIBG avidity? If so, is a patient with indications of tumor(s) / lesion(s) with known MIBG avidity considered to be included?")
class DynamicEntity(BaseModel):
    diag_fdg_avidity: Optional[List[Diag_fdg_avidity]] = Field(
        None, 
        description="Does the eligibility criteria mention tumor(s) / lesion(s) with known FDG avidity? If so, is a patient with tumor(s) / lesion(s) with known FDG avidity considered to be included?")
class DynamicEntity(BaseModel):
    diag_signif_pleural_effusion: Optional[List[Diag_signif_pleural_effusion]] = Field(
        None, 
        description="Does the eligibility criteria mention clinically significant, symptomatic, pleural effusions? If so, is a patient with clinically significant, symptomatic, pleural effusions considered to be included?")
class DynamicEntity(BaseModel):
    diag_signif_pericardial_effusion: Optional[List[Diag_signif_pericardial_effusion]] = Field(
        None, 
        description="Does the eligibility criteria mention physiologically significant pericardial effusion? If so, is a patient with physiologically significant pericardial effusion considered to be included?")
class DynamicEntity(BaseModel):
    diag_measureable_disease: Optional[List[Diag_measureable_disease]] = Field(
        None, 
        description="Does the eligibility criteria mention the patient having measurable disease? If so, is a patient with measurable disease considered to be included?")
class DynamicEntity(BaseModel):
    diag_measureable_tumor: Optional[List[Diag_measureable_tumor]] = Field(
        None, 
        description="Does the eligibility criteria mention the patient having one or more tumor / lesion sites with measurable dimensions? If so, is a patient with one or more tumor / lesion sites with measurable dimensions considered to be included?")
class DynamicEntity(BaseModel):
    diag_primary_immunodeficiency: Optional[List[Diag_primary_immunodeficiency]] = Field(
        None, 
        description="Does the eligibility criteria mention a diagnosis of primary immunodeficiency? If so, is a patient with a diagnosis of primary immunodeficiency considered to be included?")
class DynamicEntity(BaseModel):
    exp_cellular_therapy: Optional[List[Exp_cellular_therapy]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to  live cellular therapy (natural killer [NK] cell, chimeric antigen receptor T-cell [CAR-T cell])? If so, is a patient with any prior exposure to live cellular therapy considered to be included?")
class DynamicEntity(BaseModel):
    exp_ch14_18_sensitive: Optional[List[Exp_ch14_18_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to ch14.18 monoclonal antibody (e.g., CHO or SP2/0)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to ch14.18 considered to be included?")
class DynamicEntity(BaseModel):
    exp_anti_gd2_sensitive: Optional[List[Exp_anti_gd2_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody (dinutuximab)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to anti-GD2 monoclonal antibody considered to be included?")
class DynamicEntity(BaseModel):
    exp_hu5f9g4_sensitive: Optional[List[Exp_hu5f9g4_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 (magrolimab) monoclonal antibody? If so, is a patient with previous toxicity or hypersensitivity directly attributed to Hu5F9-G4 monoclonal antibody considered to be included?")
class DynamicEntity(BaseModel):
    exp_gm_csf_sensitive: Optional[List[Exp_gm_csf_sensitive]] = Field(
        None, 
        description="Does the eligibility criteria mention previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide (DMSO)? If so, is a patient with previous toxicity or hypersensitivity directly attributed to GM-CSF or dimethyl sulfoxide considered to be included?")
class DynamicEntity(BaseModel):
    exp_pd1_pdl_ever: Optional[List[Exp_pd1_pdl_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies (e.g. Nivolumab)? If so, is a patient with any prior exposure to any PD-1, PD-L1, or PD-L2 targeting antibodies considered to be included?")
class DynamicEntity(BaseModel):
    exp_anti_ctla4_ever: Optional[List[Exp_anti_ctla4_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any anti-CTLA4 agent? If so, is a patient with any prior exposure to any anti-CTLA4 agent considered to be included?")
class DynamicEntity(BaseModel):
    exp_lorlatinib_ever: Optional[List[Exp_lorlatinib_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to lorlatinib? If so, is a patient with any prior exposure to lorlatinib considered to be included?")
class DynamicEntity(BaseModel):
    exp_cd47_sirpalpha_ever: Optional[List[Exp_cd47_sirpalpha_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to any CD47–SIRPα-targeted therapeutics? If so, is a patient with any prior exposure to any CD47–SIRPα-targeted therapeutics considered to be included?")
class DynamicEntity(BaseModel):
    exp_ivig_ever: Optional[List[Exp_ivig_ever]] = Field(
        None, 
        description="Does the eligibility criteria mention any prior exposure to Intravenous Immunoglobulin (IVIg) therapy? If so, is a patient with any prior exposure to  Intravenous Immunoglobulin therapy considered to be included?")
class DynamicEntity(BaseModel):
    cumul_131l_mibg: Optional[str] = Field(
        None, 
        description="Does the eligibility criteria mention cumulative 131I-MIBG dosing? If so, how much cumulative 131I-MIBG dosing (in mCi/kg) is considered to be included? Example: the answer is > 54 mCi/kg, if \"treated with iodine-131 (131I)-MIBG who have already received a cumulative I-131 dose > 54 mCi/kg or who would exceed 54 mCi/kg by participating\"")
class DynamicEntity(BaseModel):
    expression_alk: Optional[List[Expression_alk]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of ALK mutation? If so, is a patient with evidence of ALK mutation considered to be included?")
class DynamicEntity(BaseModel):
    expression_alk_type: Optional[List[Expression_alk_type]] = Field(
        None, 
        description="Does the eligibility criteria mention ALK mutations? If so, what types of ALK mutations are considered to be included?")
class DynamicEntity(BaseModel):
    bclc_stage: Optional[List[Bclc_stage]] = Field(
        None, 
        description="Does the eligibility criteria mention BCLC stage? If so, what BCLC stages are considered to be included?")
class DynamicEntity(BaseModel):
    ctp_score: Optional[int] = Field(
        None, 
        description="Does the eligibility criteria mention Child-Pugh-Turcotte score? If so, what Child-Pugh-Turcotte score is considered to be included?")
class DynamicEntity(BaseModel):
    expression_gpc3: Optional[List[Expression_gpc3]] = Field(
        None, 
        description="Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?")
