from typing import TypeVar, Type, Optional, List

from pydantic import BaseModel, Field

class Age_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    age_min_mention: YesNo
    age_min_output: Optional[int]


class Age_MaxEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    age_max_mention: YesNo
    age_max_output: Optional[int]


class Weight_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    weight_min_mention: YesNo
    weight_min_output: Optional[int]


class Weight_MaxEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    weight_max_mention: YesNo
    weight_max_output: Optional[int]


class SexEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    sex_mention: YesNo
    sex_output: Optional[List[Sex]]


class DiagnosisEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diagnosis_mention: YesNo
    diagnosis_output: Optional[List[Diagnosis]] = Field(
        None, 
        description='Diagnoses include "Acute promyelocytic leukemia (APL)", "Acute myeloid leukemia (AML)", "Down syndrome acute myeloid leukemia (DS AML)", "B-cell acute lymphoblastic leukemia (B-ALL)", "Juvenile myelomonocytic leukemia (JMML)", "Mixed-phenotype acute leukemia (MPAL)", "Myelodysplastic syndromes (MDS)", "Myelodysplastic syndrome who have progressed to AML (MDS-AML)", "Treatment-related acute myeloid leukemia (tAML)", "T-cell acute lymphoblastic leukemia (T-ALL)", "Acute lymphoblastic leukemia (ALL)", "KMT2A acute lymphoblastic leukemia", "Early T-cell precursor acute lymphoblastic leukemia (ETP-ALL)", "Ambiguous lineage acute leukemia (ALAL)" ')


class Ever_RefractoryEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    ever_refractory_mention: YesNo
    ever_refractory_output: Optional[List[Ever_refractory]] = Field(
        None, 
        description='refractory disease are diseases such as "Refractory leukemia"')


class Count_RefractoryEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    count_refractory_mention: YesNo
    count_refractory_output: Optional[int]


class Current_Refractory_Num_CyclesEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    current_refractory_num_cycles_mention: YesNo
    current_refractory_num_cycles_output: Optional[int] = Field(
        None, 
        description='the answer is 1 if "refractory to at least one course of salvage therapy", the answer is 2 if "persistent after at least two courses of induction "chemotherapy", the answer is 2 if "refractory disease after >= 2 cycles of chemotherapy"')


class Ever_RelapseEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    ever_relapse_mention: YesNo
    ever_relapse_output: Optional[List[Ever_relapse]] = Field(
        None, 
        description='relapse disease such as "relapsed leukemia"')


class Count_RelapseEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    count_relapse_mention: YesNo
    count_relapse_output: Optional[str] = Field(
        None, 
        description='the answer is 2 if "Second or greater relapse"; the answer is 1 if "first relapses"')


class Bm_Recent_Blast_Pct_MeasEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    bm_recent_blast_pct_meas_mention: YesNo
    bm_recent_blast_pct_meas_output: Optional[int] = Field(
        None, 
        description='the answer is 5 if ">= 5% blasts in the bone marrow", the answer is 5 if "> 5% blasts in the BM" is mentioned')


class Bm_Recent_Blast_MethodEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    bm_recent_blast_method_mention: YesNo
    bm_recent_blast_method_output: Optional[List[Bm_recent_blast_method]] = Field(
        None, 
        description='"Morphology", "Flow cytometry"')


class Periph_Blood_Blast_Abs_MeasEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    periph_blood_blast_abs_meas_mention: YesNo
    periph_blood_blast_abs_meas_output: Optional[int]


class Periph_Blood_Blast_Pct_MeasEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    periph_blood_blast_pct_meas_mention: YesNo
    periph_blood_blast_pct_meas_output: Optional[int] = Field(
        None, 
        description='the answer is 5 if ">= 5% blasts in the peripheral blood" is mentioned, the answer is 5 if ">=5% blasts in the blood" is mentioned')


class Corneal_EpitheliopathyEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    corneal_epitheliopathy_mention: YesNo
    corneal_epitheliopathy_output: Optional[List[Corneal_epitheliopathy]]


class Cns_StatusEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    cns_status_mention: YesNo
    cns_status_output: Optional[str] = Field(
        None, 
        description='CNS status have CNS 1, CNS 2, and CNS 3')


class Lanksy_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    lanksy_min_mention: YesNo
    lanksy_min_output: Optional[int] = Field(
        None, 
        description='the answer is 70 if "Lansky score>=70" is mentioned')


class Karnofksy_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    karnofksy_min_mention: YesNo
    karnofksy_min_output: Optional[int] = Field(
        None, 
        description='the answer is 50 if "Karnofsky score >= 50" is mentioned')


class Diag_Down_SyndromeEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_down_syndrome_mention: YesNo
    diag_down_syndrome_output: Optional[List[Diag_down_syndrome]]


class Diag_Iso_EmdEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_iso_emd_mention: YesNo
    diag_iso_emd_output: Optional[List[Diag_iso_emd]]


class Diag_Iso_TestesEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_iso_testes_mention: YesNo
    diag_iso_testes_output: Optional[List[Diag_iso_testes]]


class Diag_Ataxia_TelangEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_ataxia_telang_mention: YesNo
    diag_ataxia_telang_output: Optional[List[Diag_ataxia_telang]]


class Diag_BloomEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_bloom_mention: YesNo
    diag_bloom_output: Optional[List[Diag_bloom]]


class Diag_FanconiEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_fanconi_mention: YesNo
    diag_fanconi_output: Optional[List[Diag_fanconi]]


class Diag_KostmannEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_kostmann_mention: YesNo
    diag_kostmann_output: Optional[List[Diag_kostmann]]


class Diag_ShwachmanEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_shwachman_mention: YesNo
    diag_shwachman_output: Optional[List[Diag_shwachman]]


class Diag_Cong_BmfEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_cong_bmf_mention: YesNo
    diag_cong_bmf_output: Optional[List[Diag_cong_bmf]]


class Diag_MalabsoptionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_malabsoption_mention: YesNo
    diag_malabsoption_output: Optional[List[Diag_malabsoption]]


class Diag_ChfEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_chf_mention: YesNo
    diag_chf_output: Optional[List[Diag_chf]]


class Diag_HivEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_hiv_mention: YesNo
    diag_hiv_output: Optional[List[Diag_hiv]]


class Diag_Uncontr_CnsEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_uncontr_cns_mention: YesNo
    diag_uncontr_cns_output: Optional[List[Diag_uncontr_cns]]


class Diag_Hep_B_CEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_hep_b_c_mention: YesNo
    diag_hep_b_c_output: Optional[List[Diag_hep_b_c]]


class Diag_Liver_Cirr_SeriousEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_liver_cirr_serious_mention: YesNo
    diag_liver_cirr_serious_output: Optional[List[Diag_liver_cirr_serious]]


class Active_InfectionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    active_infection_mention: YesNo
    active_infection_output: Optional[List[Active_infection]]


class Refractory_TransfusionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    refractory_transfusion_mention: YesNo
    refractory_transfusion_output: Optional[List[Refractory_transfusion]]


class Cerebellar_ToxicityEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    cerebellar_toxicity_mention: YesNo
    cerebellar_toxicity_output: Optional[List[Cerebellar_toxicity]]


class Exp_Cytotoxic_Chemo_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cytotoxic_chemo_ever_mention: YesNo
    exp_cytotoxic_chemo_ever_output: Optional[List[Exp_cytotoxic_chemo_ever]]


class Exp_Corticosteroids_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_corticosteroids_ever_mention: YesNo
    exp_corticosteroids_ever_output: Optional[List[Exp_corticosteroids_ever]]


class Exp_Anticancer_Nonmyelosupp_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anticancer_nonmyelosupp_ever_mention: YesNo
    exp_anticancer_nonmyelosupp_ever_output: Optional[List[Exp_anticancer_nonmyelosupp_ever]]


class Exp_Anticancer_Myelosupp_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anticancer_myelosupp_ever_mention: YesNo
    exp_anticancer_myelosupp_ever_output: Optional[List[Exp_anticancer_myelosupp_ever]]


class Exp_Antibody_Drug_Conj_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_antibody_drug_conj_ever_mention: YesNo
    exp_antibody_drug_conj_ever_output: Optional[List[Exp_antibody_drug_conj_ever]]


class Exp_Interleukins_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_interleukins_ever_mention: YesNo
    exp_interleukins_ever_output: Optional[List[Exp_interleukins_ever]]


class Exp_Long_Acting_Gf_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_long_acting_gf_ever_mention: YesNo
    exp_long_acting_gf_ever_output: Optional[List[Exp_long_acting_gf_ever]]


class Exp_Short_Acting_Gf_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_short_acting_gf_ever_mention: YesNo
    exp_short_acting_gf_ever_output: Optional[List[Exp_short_acting_gf_ever]]


class Exp_Rt_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_rt_ever_mention: YesNo
    exp_rt_ever_output: Optional[List[Exp_rt_ever]]


class Exp_Craniospatial_Rt_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_craniospatial_rt_ever_mention: YesNo
    exp_craniospatial_rt_ever_output: Optional[List[Exp_craniospatial_rt_ever]]


class Exp_Tbi_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_tbi_ever_mention: YesNo
    exp_tbi_ever_output: Optional[List[Exp_tbi_ever]]


class Exp_Radiopharma_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_radiopharma_ever_mention: YesNo
    exp_radiopharma_ever_output: Optional[List[Exp_radiopharma_ever]]


class Exp_HctEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_hct_mention: YesNo
    exp_hct_output: Optional[List[Exp_hct]]


class Type_TransplantEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    type_transplant_mention: YesNo
    type_transplant_output: Optional[List[Type_transplant]] = Field(
        None, 
        description='The transplant type can be "Allogeneic", "Autologous", or both of them')


class Exp_Dli_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_dli_ever_mention: YesNo
    exp_dli_ever_output: Optional[List[Exp_dli_ever]]


class Exp_Cyp2D6_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cyp2d6_ever_mention: YesNo
    exp_cyp2d6_ever_output: Optional[List[Exp_cyp2d6_ever]]


class Exp_Cyp3A4_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cyp3a4_ever_mention: YesNo
    exp_cyp3a4_ever_output: Optional[List[Exp_cyp3a4_ever]] = Field(
        None, 
        description='Consider CYP3A4 and CYP3A as distinct instances.')


class Exp_Cyp3A_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cyp3a_ever_mention: YesNo
    exp_cyp3a_ever_output: Optional[List[Exp_cyp3a_ever]] = Field(
        None, 
        description='Consider CYP3A4 and CYP3A as distinct instances.')


class Exp_Calcineurin_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_calcineurin_ever_mention: YesNo
    exp_calcineurin_ever_output: Optional[List[Exp_calcineurin_ever]]


class Exp_Monocl_Antib_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_monocl_antib_ever_mention: YesNo
    exp_monocl_antib_ever_output: Optional[List[Exp_monocl_antib_ever]]


class Exp_Immunotherapy_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_immunotherapy_ever_mention: YesNo
    exp_immunotherapy_ever_output: Optional[List[Exp_immunotherapy_ever]]


class Exp_Gpc3_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_gpc3_ever_mention: YesNo
    exp_gpc3_ever_output: Optional[List[Exp_gpc3_ever]]


class Exp_Demeth_Hdac_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_demeth_hdac_ever_mention: YesNo
    exp_demeth_hdac_ever_output: Optional[List[Exp_demeth_hdac_ever]]


class Exp_Cd123_CartEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cd123_cart_mention: YesNo
    exp_cd123_cart_output: Optional[List[Exp_cd123_cart]]


class Exp_Anthracycline_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anthracycline_ever_mention: YesNo
    exp_anthracycline_ever_output: Optional[List[Exp_anthracycline_ever]]


class Cumul_AnthracyclineEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    cumul_anthracycline_mention: YesNo
    cumul_anthracycline_output: Optional[str] = Field(
        None, 
        description='the answer is 450 mg/m^2, if "total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2"')


class GvhdEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    gvhd_mention: YesNo
    gvhd_output: Optional[List[Gvhd]] = Field(
        None, 
        description='active uncontrolled graft versus host disease (GvHD)')


class Vpa_MedsEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    vpa_meds_mention: YesNo
    vpa_meds_output: Optional[List[Vpa_meds]]


class Prior_Solid_Organ_TransplEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    prior_solid_organ_transpl_mention: YesNo
    prior_solid_organ_transpl_output: Optional[List[Prior_solid_organ_transpl]]


class Exp_UproleselanEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_uproleselan_mention: YesNo
    exp_uproleselan_output: Optional[List[Exp_uproleselan]]


class Exp_FlotetuzumabEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_flotetuzumab_mention: YesNo
    exp_flotetuzumab_output: Optional[List[Exp_flotetuzumab]]


class Exp_VenetoclaxEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_venetoclax_mention: YesNo
    exp_venetoclax_output: Optional[List[Exp_venetoclax]]


class Exp_Venetoclax_SensitiveEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_venetoclax_sensitive_mention: YesNo
    exp_venetoclax_sensitive_output: Optional[List[Exp_venetoclax_sensitive]]


class Donor_AvailableEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    donor_available_mention: YesNo
    donor_available_output: Optional[List[Donor_available]]


class Dyspnea_PresentEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    dyspnea_present_mention: YesNo
    dyspnea_present_output: Optional[List[Dyspnea_present]]


class Hypoxia_PresentEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    hypoxia_present_mention: YesNo
    hypoxia_present_output: Optional[List[Hypoxia_present]]


class Expression_MslnEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_msln_mention: YesNo
    expression_msln_output: Optional[List[Expression_msln]]


class Expression_Cd123Entity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_cd123_mention: YesNo
    expression_cd123_output: Optional[List[Expression_cd123]]


class Expression_EselectinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_eselectin_mention: YesNo
    expression_eselectin_output: Optional[List[Expression_eselectin]]


class Expression_Kmt2ArEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_kmt2ar_mention: YesNo
    expression_kmt2ar_output: Optional[List[Expression_kmt2ar]]


class Expression_T1517Entity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_t1517_mention: YesNo
    expression_t1517_output: Optional[List[Expression_t1517]]


class Expression_Som_Jak2_V617FEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_som_JAK2_V617F_mention: YesNo
    expression_som_JAK2_V617F_output: Optional[List[Expression_som_jak2_v617f]]


class Expression_Flt3_ItdEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_flt3_itd_mention: YesNo
    expression_flt3_itd_output: Optional[List[Expression_flt3_itd]]


class Diag_Cong_Blood_DisorderEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_cong_blood_disorder_mention: YesNo
    diag_cong_blood_disorder_output: Optional[List[Diag_cong_blood_disorder]]


class Diag_Intercurrent_IllnessEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_intercurrent_illness_mention: YesNo
    diag_intercurrent_illness_output: Optional[List[Diag_intercurrent_illness]]


class Diag_Mets_CnsEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_mets_cns_mention: YesNo
    diag_mets_cns_output: Optional[List[Diag_mets_cns]]


class Diag_Hemolytic_AnemiaEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_hemolytic_anemia_mention: YesNo
    diag_hemolytic_anemia_output: Optional[List[Diag_hemolytic_anemia]]


class Diag_Evans_SyndromeEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_evans_syndrome_mention: YesNo
    diag_evans_syndrome_output: Optional[List[Diag_evans_syndrome]]


class Diag_Uncontrolled_Cardiac_RhythmEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_uncontrolled_cardiac_rhythm_mention: YesNo
    diag_uncontrolled_cardiac_rhythm_output: Optional[List[Diag_uncontrolled_cardiac_rhythm]]


class Diag_Severe_Psychiatric_DisorderEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_severe_psychiatric_disorder_mention: YesNo
    diag_severe_psychiatric_disorder_output: Optional[List[Diag_severe_psychiatric_disorder]]


class Diag_Other_MalignanciesEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_other_malignancies_mention: YesNo
    diag_other_malignancies_output: Optional[List[Diag_other_malignancies]]


class Diag_PneumonitisEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_pneumonitis_mention: YesNo
    diag_pneumonitis_output: Optional[List[Diag_pneumonitis]]


class Diag_Mibg_AvidityEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_mibg_avidity_mention: YesNo
    diag_mibg_avidity_output: Optional[List[Diag_mibg_avidity]]


class Diag_Fdg_AvidityEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_fdg_avidity_mention: YesNo
    diag_fdg_avidity_output: Optional[List[Diag_fdg_avidity]]


class Diag_Signif_Pleural_EffusionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_signif_pleural_effusion_mention: YesNo
    diag_signif_pleural_effusion_output: Optional[List[Diag_signif_pleural_effusion]]


class Diag_Signif_Pericardial_EffusionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_signif_pericardial_effusion_mention: YesNo
    diag_signif_pericardial_effusion_output: Optional[List[Diag_signif_pericardial_effusion]]


class Diag_Measureable_DiseaseEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_measureable_disease_mention: YesNo
    diag_measureable_disease_output: Optional[List[Diag_measureable_disease]]


class Diag_Measureable_TumorEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_measureable_tumor_mention: YesNo
    diag_measureable_tumor_output: Optional[List[Diag_measureable_tumor]]


class Diag_Primary_ImmunodeficiencyEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_primary_immunodeficiency_mention: YesNo
    diag_primary_immunodeficiency_output: Optional[List[Diag_primary_immunodeficiency]]


class Exp_Cellular_TherapyEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cellular_therapy_mention: YesNo
    exp_cellular_therapy_output: Optional[List[Exp_cellular_therapy]]


class Exp_Ch14_18_SensitiveEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_ch14_18_sensitive_mention: YesNo
    exp_ch14_18_sensitive_output: Optional[List[Exp_ch14_18_sensitive]]


class Exp_Anti_Gd2_SensitiveEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anti_gd2_sensitive_mention: YesNo
    exp_anti_gd2_sensitive_output: Optional[List[Exp_anti_gd2_sensitive]]


class Exp_Hu5F9G4_SensitiveEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_hu5f9g4_sensitive_mention: YesNo
    exp_hu5f9g4_sensitive_output: Optional[List[Exp_hu5f9g4_sensitive]]


class Exp_Gm_Csf_SensitiveEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_gm_csf_sensitive_mention: YesNo
    exp_gm_csf_sensitive_output: Optional[List[Exp_gm_csf_sensitive]]


class Exp_Pd1_Pdl_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_pd1_pdl_ever_mention: YesNo
    exp_pd1_pdl_ever_output: Optional[List[Exp_pd1_pdl_ever]]


class Exp_Anti_Ctla4_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anti_ctla4_ever_mention: YesNo
    exp_anti_ctla4_ever_output: Optional[List[Exp_anti_ctla4_ever]]


class Exp_Lorlatinib_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_lorlatinib_ever_mention: YesNo
    exp_lorlatinib_ever_output: Optional[List[Exp_lorlatinib_ever]]


class Exp_Cd47_Sirpalpha_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cd47_sirpalpha_ever_mention: YesNo
    exp_cd47_sirpalpha_ever_output: Optional[List[Exp_cd47_sirpalpha_ever]]


class Exp_Ivig_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_ivig_ever_mention: YesNo
    exp_ivig_ever_output: Optional[List[Exp_ivig_ever]]


class Cumul_131L_MibgEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    cumul_131l_mibg_mention: YesNo
    cumul_131l_mibg_output: Optional[str] = Field(
        None, 
        description='the answer is > 54 mCi/kg, if "treated with iodine-131 (131I)-MIBG who have already received a cumulative I-131 dose > 54 mCi/kg or who would exceed 54 mCi/kg by participating"')


class Expression_AlkEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_alk_mention: YesNo
    expression_alk_output: Optional[List[Expression_alk]]


class Expression_Alk_TypeEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_alk_type_mention: YesNo
    expression_alk_type_output: Optional[List[Expression_alk_type]] = Field(
        None, 
        description='ALK mutation types include "Rearrangement (ALK-R)", "Amplification (ALK-A)", amd "Point mutation"')


class Bclc_StageEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    bclc_stage_mention: YesNo
    bclc_stage_output: Optional[List[Bclc_stage]] = Field(
        None, 
        description='The BCLC stages include "Stage 0", "Stage A", "Stage B", "Stage C", and "Stage D".')


class Ctp_ScoreEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    ctp_score_mention: YesNo
    ctp_score_output: Optional[int]


class Expression_Gpc3Entity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_gpc3_mention: YesNo
    expression_gpc3_output: Optional[List[Expression_gpc3]]


class Age_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    age_min_mention: YesNo
    age_min_output: Optional[int]


class Age_MaxEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    age_max_mention: YesNo
    age_max_output: Optional[int]


class Weight_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    weight_min_mention: YesNo
    weight_min_output: Optional[int]


class Weight_MaxEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    weight_max_mention: YesNo
    weight_max_output: Optional[int]


class SexEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    sex_mention: YesNo
    sex_output: Optional[List[Sex]]


class DiagnosisEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diagnosis_mention: YesNo
    diagnosis_output: Optional[List[Diagnosis]] = Field(
        None, 
        description='Diagnoses include "Acute promyelocytic leukemia (APL)", "Acute myeloid leukemia (AML)", "Down syndrome acute myeloid leukemia (DS AML)", "B-cell acute lymphoblastic leukemia (B-ALL)", "Juvenile myelomonocytic leukemia (JMML)", "Mixed-phenotype acute leukemia (MPAL)", "Myelodysplastic syndromes (MDS)", "Myelodysplastic syndrome who have progressed to AML (MDS-AML)", "Treatment-related acute myeloid leukemia (tAML)", "T-cell acute lymphoblastic leukemia (T-ALL)", "Acute lymphoblastic leukemia (ALL)", "KMT2A acute lymphoblastic leukemia", "Early T-cell precursor acute lymphoblastic leukemia (ETP-ALL)", "Ambiguous lineage acute leukemia (ALAL)" ')


class Ever_RefractoryEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    ever_refractory_mention: YesNo
    ever_refractory_output: Optional[List[Ever_refractory]] = Field(
        None, 
        description='refractory disease are diseases such as "Refractory leukemia"')


class Count_RefractoryEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    count_refractory_mention: YesNo
    count_refractory_output: Optional[int]


class Current_Refractory_Num_CyclesEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    current_refractory_num_cycles_mention: YesNo
    current_refractory_num_cycles_output: Optional[int] = Field(
        None, 
        description='the answer is 1 if "refractory to at least one course of salvage therapy", the answer is 2 if "persistent after at least two courses of induction "chemotherapy", the answer is 2 if "refractory disease after >= 2 cycles of chemotherapy"')


class Ever_RelapseEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    ever_relapse_mention: YesNo
    ever_relapse_output: Optional[List[Ever_relapse]] = Field(
        None, 
        description='relapse disease such as "relapsed leukemia"')


class Count_RelapseEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    count_relapse_mention: YesNo
    count_relapse_output: Optional[str] = Field(
        None, 
        description='the answer is 2 if "Second or greater relapse"; the answer is 1 if "first relapses"')


class Bm_Recent_Blast_Pct_MeasEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    bm_recent_blast_pct_meas_mention: YesNo
    bm_recent_blast_pct_meas_output: Optional[int] = Field(
        None, 
        description='the answer is 5 if ">= 5% blasts in the bone marrow", the answer is 5 if "> 5% blasts in the BM" is mentioned')


class Bm_Recent_Blast_MethodEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    bm_recent_blast_method_mention: YesNo
    bm_recent_blast_method_output: Optional[List[Bm_recent_blast_method]] = Field(
        None, 
        description='"Morphology", "Flow cytometry"')


class Periph_Blood_Blast_Abs_MeasEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    periph_blood_blast_abs_meas_mention: YesNo
    periph_blood_blast_abs_meas_output: Optional[int]


class Periph_Blood_Blast_Pct_MeasEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    periph_blood_blast_pct_meas_mention: YesNo
    periph_blood_blast_pct_meas_output: Optional[int] = Field(
        None, 
        description='the answer is 5 if ">= 5% blasts in the peripheral blood" is mentioned, the answer is 5 if ">=5% blasts in the blood" is mentioned')


class Corneal_EpitheliopathyEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    corneal_epitheliopathy_mention: YesNo
    corneal_epitheliopathy_output: Optional[List[Corneal_epitheliopathy]]


class Cns_StatusEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    cns_status_mention: YesNo
    cns_status_output: Optional[str] = Field(
        None, 
        description='CNS status have CNS 1, CNS 2, and CNS 3')


class Lanksy_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    lanksy_min_mention: YesNo
    lanksy_min_output: Optional[int] = Field(
        None, 
        description='the answer is 70 if "Lansky score>=70" is mentioned')


class Karnofksy_MinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    karnofksy_min_mention: YesNo
    karnofksy_min_output: Optional[int] = Field(
        None, 
        description='the answer is 50 if "Karnofsky score >= 50" is mentioned')


class Diag_Down_SyndromeEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_down_syndrome_mention: YesNo
    diag_down_syndrome_output: Optional[List[Diag_down_syndrome]]


class Diag_Iso_EmdEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_iso_emd_mention: YesNo
    diag_iso_emd_output: Optional[List[Diag_iso_emd]]


class Diag_Iso_TestesEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_iso_testes_mention: YesNo
    diag_iso_testes_output: Optional[List[Diag_iso_testes]]


class Diag_Ataxia_TelangEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_ataxia_telang_mention: YesNo
    diag_ataxia_telang_output: Optional[List[Diag_ataxia_telang]]


class Diag_BloomEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_bloom_mention: YesNo
    diag_bloom_output: Optional[List[Diag_bloom]]


class Diag_FanconiEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_fanconi_mention: YesNo
    diag_fanconi_output: Optional[List[Diag_fanconi]]


class Diag_KostmannEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_kostmann_mention: YesNo
    diag_kostmann_output: Optional[List[Diag_kostmann]]


class Diag_ShwachmanEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_shwachman_mention: YesNo
    diag_shwachman_output: Optional[List[Diag_shwachman]]


class Diag_Cong_BmfEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_cong_bmf_mention: YesNo
    diag_cong_bmf_output: Optional[List[Diag_cong_bmf]]


class Diag_MalabsoptionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_malabsoption_mention: YesNo
    diag_malabsoption_output: Optional[List[Diag_malabsoption]]


class Diag_ChfEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_chf_mention: YesNo
    diag_chf_output: Optional[List[Diag_chf]]


class Diag_HivEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_hiv_mention: YesNo
    diag_hiv_output: Optional[List[Diag_hiv]]


class Diag_Uncontr_CnsEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_uncontr_cns_mention: YesNo
    diag_uncontr_cns_output: Optional[List[Diag_uncontr_cns]]


class Diag_Hep_B_CEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_hep_b_c_mention: YesNo
    diag_hep_b_c_output: Optional[List[Diag_hep_b_c]]


class Diag_Liver_Cirr_SeriousEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    diag_liver_cirr_serious_mention: YesNo
    diag_liver_cirr_serious_output: Optional[List[Diag_liver_cirr_serious]]


class Active_InfectionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    active_infection_mention: YesNo
    active_infection_output: Optional[List[Active_infection]]


class Refractory_TransfusionEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    refractory_transfusion_mention: YesNo
    refractory_transfusion_output: Optional[List[Refractory_transfusion]]


class Cerebellar_ToxicityEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    cerebellar_toxicity_mention: YesNo
    cerebellar_toxicity_output: Optional[List[Cerebellar_toxicity]]


class Exp_Cytotoxic_Chemo_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cytotoxic_chemo_ever_mention: YesNo
    exp_cytotoxic_chemo_ever_output: Optional[List[Exp_cytotoxic_chemo_ever]]


class Exp_Corticosteroids_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_corticosteroids_ever_mention: YesNo
    exp_corticosteroids_ever_output: Optional[List[Exp_corticosteroids_ever]]


class Exp_Anticancer_Nonmyelosupp_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anticancer_nonmyelosupp_ever_mention: YesNo
    exp_anticancer_nonmyelosupp_ever_output: Optional[List[Exp_anticancer_nonmyelosupp_ever]]


class Exp_Anticancer_Myelosupp_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anticancer_myelosupp_ever_mention: YesNo
    exp_anticancer_myelosupp_ever_output: Optional[List[Exp_anticancer_myelosupp_ever]]


class Exp_Antibody_Drug_Conj_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_antibody_drug_conj_ever_mention: YesNo
    exp_antibody_drug_conj_ever_output: Optional[List[Exp_antibody_drug_conj_ever]]


class Exp_Interleukins_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_interleukins_ever_mention: YesNo
    exp_interleukins_ever_output: Optional[List[Exp_interleukins_ever]]


class Exp_Long_Acting_Gf_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_long_acting_gf_ever_mention: YesNo
    exp_long_acting_gf_ever_output: Optional[List[Exp_long_acting_gf_ever]]


class Exp_Short_Acting_Gf_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_short_acting_gf_ever_mention: YesNo
    exp_short_acting_gf_ever_output: Optional[List[Exp_short_acting_gf_ever]]


class Exp_Rt_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_rt_ever_mention: YesNo
    exp_rt_ever_output: Optional[List[Exp_rt_ever]]


class Exp_Craniospatial_Rt_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_craniospatial_rt_ever_mention: YesNo
    exp_craniospatial_rt_ever_output: Optional[List[Exp_craniospatial_rt_ever]]


class Exp_Tbi_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_tbi_ever_mention: YesNo
    exp_tbi_ever_output: Optional[List[Exp_tbi_ever]]


class Exp_Radiopharma_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_radiopharma_ever_mention: YesNo
    exp_radiopharma_ever_output: Optional[List[Exp_radiopharma_ever]]


class Exp_HctEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_hct_mention: YesNo
    exp_hct_output: Optional[List[Exp_hct]]


class Type_TransplantEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    type_transplant_mention: YesNo
    type_transplant_output: Optional[List[Type_transplant]] = Field(
        None, 
        description='The transplant type can be "Allogeneic", "Autologous", or both of them')


class Exp_Dli_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_dli_ever_mention: YesNo
    exp_dli_ever_output: Optional[List[Exp_dli_ever]]


class Exp_Cyp2D6_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cyp2d6_ever_mention: YesNo
    exp_cyp2d6_ever_output: Optional[List[Exp_cyp2d6_ever]]


class Exp_Cyp3A4_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cyp3a4_ever_mention: YesNo
    exp_cyp3a4_ever_output: Optional[List[Exp_cyp3a4_ever]] = Field(
        None, 
        description='Consider CYP3A4 and CYP3A as distinct instances.')


class Exp_Cyp3A_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cyp3a_ever_mention: YesNo
    exp_cyp3a_ever_output: Optional[List[Exp_cyp3a_ever]] = Field(
        None, 
        description='Consider CYP3A4 and CYP3A as distinct instances.')


class Exp_Calcineurin_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_calcineurin_ever_mention: YesNo
    exp_calcineurin_ever_output: Optional[List[Exp_calcineurin_ever]]


class Exp_Monocl_Antib_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_monocl_antib_ever_mention: YesNo
    exp_monocl_antib_ever_output: Optional[List[Exp_monocl_antib_ever]]


class Exp_Immunotherapy_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_immunotherapy_ever_mention: YesNo
    exp_immunotherapy_ever_output: Optional[List[Exp_immunotherapy_ever]]


class Exp_Gpc3_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_gpc3_ever_mention: YesNo
    exp_gpc3_ever_output: Optional[List[Exp_gpc3_ever]]


class Exp_Demeth_Hdac_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_demeth_hdac_ever_mention: YesNo
    exp_demeth_hdac_ever_output: Optional[List[Exp_demeth_hdac_ever]]


class Exp_Cd123_CartEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_cd123_cart_mention: YesNo
    exp_cd123_cart_output: Optional[List[Exp_cd123_cart]]


class Exp_Anthracycline_EverEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_anthracycline_ever_mention: YesNo
    exp_anthracycline_ever_output: Optional[List[Exp_anthracycline_ever]]


class Cumul_AnthracyclineEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    cumul_anthracycline_mention: YesNo
    cumul_anthracycline_output: Optional[str] = Field(
        None, 
        description='the answer is 450 mg/m^2, if "total cumulative doses of non-liposomal daunorubicin, or other anthracycline equivalent, greater than 450 mg/m^2"')


class GvhdEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    gvhd_mention: YesNo
    gvhd_output: Optional[List[Gvhd]] = Field(
        None, 
        description='active uncontrolled graft versus host disease (GvHD)')


class Vpa_MedsEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    vpa_meds_mention: YesNo
    vpa_meds_output: Optional[List[Vpa_meds]]


class Prior_Solid_Organ_TransplEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    prior_solid_organ_transpl_mention: YesNo
    prior_solid_organ_transpl_output: Optional[List[Prior_solid_organ_transpl]]


class Exp_UproleselanEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_uproleselan_mention: YesNo
    exp_uproleselan_output: Optional[List[Exp_uproleselan]]


class Exp_FlotetuzumabEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_flotetuzumab_mention: YesNo
    exp_flotetuzumab_output: Optional[List[Exp_flotetuzumab]]


class Exp_VenetoclaxEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_venetoclax_mention: YesNo
    exp_venetoclax_output: Optional[List[Exp_venetoclax]]


class Exp_Venetoclax_SensitiveEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    exp_venetoclax_sensitive_mention: YesNo
    exp_venetoclax_sensitive_output: Optional[List[Exp_venetoclax_sensitive]]


class Donor_AvailableEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    donor_available_mention: YesNo
    donor_available_output: Optional[List[Donor_available]]


class Dyspnea_PresentEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    dyspnea_present_mention: YesNo
    dyspnea_present_output: Optional[List[Dyspnea_present]]


class Hypoxia_PresentEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    hypoxia_present_mention: YesNo
    hypoxia_present_output: Optional[List[Hypoxia_present]]


class Expression_MslnEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_msln_mention: YesNo
    expression_msln_output: Optional[List[Expression_msln]]


class Expression_Cd123Entity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_cd123_mention: YesNo
    expression_cd123_output: Optional[List[Expression_cd123]]


class Expression_EselectinEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_eselectin_mention: YesNo
    expression_eselectin_output: Optional[List[Expression_eselectin]]


class Expression_Kmt2ArEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_kmt2ar_mention: YesNo
    expression_kmt2ar_output: Optional[List[Expression_kmt2ar]]


class Expression_T1517Entity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_t1517_mention: YesNo
    expression_t1517_output: Optional[List[Expression_t1517]]


class Expression_Som_Jak2_V617FEntity(BaseModel):
    """
    Questions:Does the eligibility criteria mention evidence of GPC3 expression? If so, is a patient with evidence of GPC3 expression considered to be included?
    """

    expression_som_JAK2_V617F_mention: YesNo
    expression_som_JAK2_V617F_output: Optional[List[Expression_som_jak2_v617f]]


