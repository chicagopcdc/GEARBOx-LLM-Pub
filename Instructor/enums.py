from enum import Enum

class YesNo(Enum):
    YES = "Yes"
    NO = "No"

class Sex(Enum):
    MALE = "Male"
    FEMALE = "Female"

class Diagnosis(Enum):
    ACUTE_PROMYELOCYTIC_LEUKEMIA_APL_ = "Acute promyelocytic leukemia (APL)"
    ACUTE_MYELOID_LEUKEMIA_AML_ = "Acute myeloid leukemia (AML)"
    DOWN_SYNDROME_ACUTE_MYELOID_LEUKEMIA_DS_AML_ = "Down syndrome acute myeloid leukemia (DS AML)"
    B_CELL_ACUTE_LYMPHOBLASTIC_LEUKEMIA_B_ALL_ = "B-cell acute lymphoblastic leukemia (B-ALL)"
    JUVENILE_MYELOMONOCYTIC_LEUKEMIA_JMML_ = "Juvenile myelomonocytic leukemia (JMML)"
    MIXED_PHENOTYPE_ACUTE_LEUKEMIA_MPAL_ = "Mixed-phenotype acute leukemia (MPAL)"
    MYELODYSPLASTIC_SYNDROMES_MDS_ = "Myelodysplastic syndromes (MDS)"
    MYELODYSPLASTIC_SYNDROME_MDS_WHO_HAVE_PROGRESSED_TO_AML = "Myelodysplastic syndrome (MDS) who have progressed to AML"
    TREATMENT_RELATED_ACUTE_MYELOID_LEUKEMIA_TAML_ = "Treatment-related acute myeloid leukemia (tAML)"
    T_CELL_ACUTE_LYMPHOBLASTIC_LEUKEMIA_T_ALL_ = "T-cell acute lymphoblastic leukemia (T-ALL)"
    ACUTE_LYMPHOBLASTIC_LEUKEMIA_ALL_ = "Acute lymphoblastic leukemia (ALL)"
    KMT2A_ACUTE_LYMPHOBLASTIC_LEUKEMIA = "KMT2A acute lymphoblastic leukemia"
    EARLY_T_CELL_PRECURSOR_ACUTE_LYMPHOBLASTIC_LEUKEMIA_ETP_ALL_ = "Early T-cell precursor acute lymphoblastic leukemia (ETP-ALL)"
    AMBIGUOUS_LINEAGE_ACUTE_LEUKEMIA_ALAL_ = "Ambiguous lineage acute leukemia (ALAL)"

class Ever_refractory(Enum):
    YES = "Yes"
    NO = "No"

class Ever_relapse(Enum):
    YES = "Yes"
    NO = "No"

class Bm_recent_blast_method(Enum):
    MORPHOLOGY = "Morphology"
    FLOW_CYTOMETRY = "Flow cytometry"

class Corneal_epitheliopathy(Enum):
    YES = "Yes"
    NO = "No"

class Diag_down_syndrome(Enum):
    YES = "Yes"
    NO = "No"

class Diag_iso_emd(Enum):
    YES = "Yes"
    NO = "No"

class Diag_iso_testes(Enum):
    YES = "Yes"
    NO = "No"

class Diag_ataxia_telang(Enum):
    YES = "Yes"
    NO = "No"

class Diag_bloom(Enum):
    YES = "Yes"
    NO = "No"

class Diag_fanconi(Enum):
    YES = "Yes"
    NO = "No"

class Diag_kostmann(Enum):
    YES = "Yes"
    NO = "No"

class Diag_shwachman(Enum):
    YES = "Yes"
    NO = "No"

class Diag_cong_bmf(Enum):
    YES = "Yes"
    NO = "No"

class Diag_malabsoption(Enum):
    YES = "Yes"
    NO = "No"

class Diag_chf(Enum):
    YES = "Yes"
    NO = "No"

class Diag_hiv(Enum):
    YES = "Yes"
    NO = "No"

class Diag_uncontr_cns(Enum):
    YES = "Yes"
    NO = "No"

class Diag_hep_b_c(Enum):
    YES = "Yes"
    NO = "No"

class Diag_liver_cirr_serious(Enum):
    YES = "Yes"
    NO = "No"

class Active_infection(Enum):
    YES = "Yes"
    NO = "No"

class Refractory_transfusion(Enum):
    YES = "Yes"
    NO = "No"

class Cerebellar_toxicity(Enum):
    YES = "Yes"
    NO = "No"

class Exp_cytotoxic_chemo_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_corticosteroids_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_anticancer_nonmyelosupp_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_anticancer_myelosupp_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_antibody_drug_conj_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_interleukins_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_long_acting_gf_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_short_acting_gf_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_rt_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_craniospatial_rt_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_tbi_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_radiopharma_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_hct(Enum):
    YES = "Yes"
    NO = "No"

class Type_transplant(Enum):
    ALLOGENEIC = "Allogeneic"
    AUTOLOGOUS = "Autologous"

class Exp_dli_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_cyp2d6_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_cyp3a4_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_cyp3a_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_calcineurin_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_monocl_antib_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_immunotherapy_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_gpc3_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_demeth_hdac_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_cd123_cart(Enum):
    YES = "Yes"
    NO = "No"

class Exp_anthracycline_ever(Enum):
    YES = "Yes"
    NO = "No"

class Gvhd(Enum):
    YES = "Yes"
    NO = "No"

class Vpa_meds(Enum):
    YES = "Yes"
    NO = "No"

class Prior_solid_organ_transpl(Enum):
    YES = "Yes"
    NO = "No"

class Exp_uproleselan(Enum):
    YES = "Yes"
    NO = "No"

class Exp_flotetuzumab(Enum):
    YES = "Yes"
    NO = "No"

class Exp_venetoclax(Enum):
    YES = "Yes"
    NO = "No"

class Exp_venetoclax_sensitive(Enum):
    YES = "Yes"
    NO = "No"

class Donor_available(Enum):
    YES = "Yes"
    NO = "No"

class Dyspnea_present(Enum):
    YES = "Yes"
    NO = "No"

class Hypoxia_present(Enum):
    YES = "Yes"
    NO = "No"

class Expression_msln(Enum):
    YES = "Yes"
    NO = "No"

class Expression_cd123(Enum):
    YES = "Yes"
    NO = "No"

class Expression_eselectin(Enum):
    YES = "Yes"
    NO = "No"

class Expression_kmt2ar(Enum):
    YES = "Yes"
    NO = "No"

class Expression_t1517(Enum):
    YES = "Yes"
    NO = "No"

class Expression_som_jak2_v617f(Enum):
    YES = "Yes"
    NO = "No"

class Expression_flt3_itd(Enum):
    YES = "Yes"
    NO = "No"

class Diag_cong_blood_disorder(Enum):
    YES = "Yes"
    NO = "No"

class Diag_intercurrent_illness(Enum):
    YES = "Yes"
    NO = "No"

class Diag_mets_cns(Enum):
    YES = "Yes"
    NO = "No"

class Diag_hemolytic_anemia(Enum):
    YES = "Yes"
    NO = "No"

class Diag_evans_syndrome(Enum):
    YES = "Yes"
    NO = "No"

class Diag_uncontrolled_cardiac_rhythm(Enum):
    YES = "Yes"
    NO = "No"

class Diag_severe_psychiatric_disorder(Enum):
    YES = "Yes"
    NO = "No"

class Diag_other_malignancies(Enum):
    YES = "Yes"
    NO = "No"

class Diag_pneumonitis(Enum):
    YES = "Yes"
    NO = "No"

class Diag_mibg_avidity(Enum):
    YES = "Yes"
    NO = "No"

class Diag_fdg_avidity(Enum):
    YES = "Yes"
    NO = "No"

class Diag_signif_pleural_effusion(Enum):
    YES = "Yes"
    NO = "No"

class Diag_signif_pericardial_effusion(Enum):
    YES = "Yes"
    NO = "No"

class Diag_measureable_disease(Enum):
    YES = "Yes"
    NO = "No"

class Diag_measureable_tumor(Enum):
    YES = "Yes"
    NO = "No"

class Diag_primary_immunodeficiency(Enum):
    YES = "Yes"
    NO = "No"

class Exp_cellular_therapy(Enum):
    YES = "Yes"
    NO = "No"

class Exp_ch14_18_sensitive(Enum):
    YES = "Yes"
    NO = "No"

class Exp_anti_gd2_sensitive(Enum):
    YES = "Yes"
    NO = "No"

class Exp_hu5f9g4_sensitive(Enum):
    YES = "Yes"
    NO = "No"

class Exp_gm_csf_sensitive(Enum):
    YES = "Yes"
    NO = "No"

class Exp_pd1_pdl_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_anti_ctla4_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_lorlatinib_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_cd47_sirpalpha_ever(Enum):
    YES = "Yes"
    NO = "No"

class Exp_ivig_ever(Enum):
    YES = "Yes"
    NO = "No"

class Expression_alk(Enum):
    YES = "Yes"
    NO = "No"

class Expression_alk_type(Enum):
    REARRANGEMENT_ALK_R_ = "Rearrangement (ALK-R)"
    AMPLIFICATION_ALK_A_ = "Amplification (ALK-A)"
    POINT_MUTATION = "Point mutation"

class Bclc_stage(Enum):
    STAGE_0 = "Stage 0"
    STAGE_A = "Stage A"
    STAGE_B = "Stage B"
    STAGE_C = "Stage C"
    STAGE_D = "Stage D"

class Expression_gpc3(Enum):
    YES = "Yes"
    NO = "No"

