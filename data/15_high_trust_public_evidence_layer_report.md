# Notebook 15 Report — High-Trust Public Evidence Layer

Generated: 2026-06-07T13:38:04.623601

## Purpose

This notebook adds a high-trust public evidence validation layer while waiting for official OncoKB production API access.

Only high-trust public sources were used:
- CIViC
- openFDA drug labels
- cBioPortal API
- ClinicalTrials.gov API v2

DGIdb was excluded from scoring because it is drug-gene interaction support only.
OncoKB therapeutic validation is marked as pending official production token.

## Inputs

- Dashboard patients: /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified.json
- Patients loaded: 75
- Local evidence KB: /content/drive/MyDrive/desktop_app/data/knowledge/12_egfr_precision_oncology_evidence_kb.csv

## API evidence summaries

### openFDA

evidence_status
FDA_LABEL_NSCLC_EGFR_SUPPORT                   32
FDA_LABEL_FOUND_BUT_NOT_EGFR_NSCLC_SPECIFIC    10

### ClinicalTrials.gov

evidence_status
TRIAL_CONTEXT_SUPPORT            166
TRIAL_CONTEXT_WEAK_OR_GENERAL    114

### CIViC

No CIViC rows or API query unavailable.

### cBioPortal

cBioPortal lung/NSCLC candidate studies found: 36

## Drug-level public evidence support

| drug                        |   openfda_label_score | openfda_status               |   openfda_records |   civic_score | civic_status                                   |   civic_records |   clinical_trials_score | clinical_trials_status               |   clinical_trials_count |   cbioportal_genomic_context_score | cbioportal_genomic_context_status    |   internal_audit_pass_score | oncokb_status                                          | dgidb_status                                    |   public_high_trust_support_score | public_high_trust_status                      |
|:----------------------------|----------------------:|:-----------------------------|------------------:|--------------:|:-----------------------------------------------|----------------:|------------------------:|:-------------------------------------|------------------------:|-----------------------------------:|:-------------------------------------|----------------------------:|:-------------------------------------------------------|:------------------------------------------------|----------------------------------:|:----------------------------------------------|
| Osimertinib                 |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                 2 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       1 | TRIAL_CONTEXT_SUPPORT                |                      30 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.65 | MODERATE_HIGH_TRUST_PUBLIC_EVIDENCE_SUPPORTED |
| Afatinib                    |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                 2 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       1 | TRIAL_CONTEXT_SUPPORT                |                      30 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.65 | MODERATE_HIGH_TRUST_PUBLIC_EVIDENCE_SUPPORTED |
| Erlotinib                   |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                 5 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       1 | TRIAL_CONTEXT_SUPPORT                |                      24 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.65 | MODERATE_HIGH_TRUST_PUBLIC_EVIDENCE_SUPPORTED |
| Gefitinib                   |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                 6 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       1 | TRIAL_CONTEXT_SUPPORT                |                      32 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.65 | MODERATE_HIGH_TRUST_PUBLIC_EVIDENCE_SUPPORTED |
| Dacomitinib                 |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                 2 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       1 | TRIAL_CONTEXT_SUPPORT                |                      24 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.65 | MODERATE_HIGH_TRUST_PUBLIC_EVIDENCE_SUPPORTED |
| Amivantamab                 |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                 4 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       1 | TRIAL_CONTEXT_SUPPORT                |                      19 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.65 | MODERATE_HIGH_TRUST_PUBLIC_EVIDENCE_SUPPORTED |
| Amivantamab + Lazertinib    |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                 6 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       1 | TRIAL_CONTEXT_SUPPORT                |                       7 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.65 | MODERATE_HIGH_TRUST_PUBLIC_EVIDENCE_SUPPORTED |
| Platinum-based Chemotherapy |                     1 | FDA_LABEL_NSCLC_EGFR_SUPPORT |                15 |             0 | NO_CIVIC_API_EVIDENCE_FOUND_OR_API_UNAVAILABLE |               0 |                       0 | NO_RELEVANT_EGFR_NSCLC_TRIAL_CONTEXT |                       0 |                                  1 | PUBLIC_CBIOPORTAL_LUNG_COHORTS_FOUND |                           1 | PENDING_OFFICIAL_PRODUCTION_TOKEN_FOR_THERAPEUTIC_DATA | EXCLUDED_FROM_HIGH_TRUST_SCORE_INTERACTION_ONLY |                              0.5  | PARTIALLY_SUPPORTED_BY_PUBLIC_EVIDENCE        |

## Patient-level public validation status

patient_public_validation_status
HIGH_TRUST_PUBLIC_VALIDATION_SUPPORTED    62
PARTIAL_PUBLIC_VALIDATION_SUPPORTED       13

## Model trust score after high-trust public validation

```json
{
  "created_at": "2026-06-07T13:38:04.551491",
  "model_version": "EGFR_Global_TrustedEvidenceFusion_v1_15_high_trust_public_validation",
  "patients": 75,
  "technical_functionality_score_0_10": 8.5,
  "internal_consistency_score_0_10": 9.0,
  "scientific_traceability_score_0_10": 7.85,
  "clinical_readiness_score_0_10": 5.0,
  "global_prototype_score_0_10": 7.73,
  "average_patient_public_trust_score_0_1": 0.7834,
  "high_trust_apis_used": [
    "CIViC",
    "openFDA drug labels",
    "cBioPortal",
    "ClinicalTrials.gov API v2"
  ],
  "excluded_from_high_trust_scoring": {
    "DGIdb": "Excluded because drug-gene interaction support is not standalone clinical actionability.",
    "OncoKB": "Full therapeutic validation pending approved production API token."
  },
  "interpretation": "This public evidence layer improves traceability and moves the prototype closer to a defensible 8/10 research-grade system. It does not yet establish clinical prediction accuracy because true treatment response/outcome validation is still required."
}
```

## Scientific interpretation

The model is now more traceable and scientifically defensible because each drug ranking can be connected to public evidence layers:

- public FDA label evidence where available
- CIViC variant evidence where retrievable
- ClinicalTrials.gov trial context
- cBioPortal external genomic context
- internal audit pass status

However, this does not yet prove clinical prediction accuracy.
True clinical accuracy still requires treatment-response labels, retrospective/external validation, and expert review.

## Updated outputs

- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_openfda_drug_label_evidence.csv
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_clinicaltrials_context.csv
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_cbioportal_external_genomic_validation.csv
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_civic_variant_evidence.csv
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_drug_public_high_trust_support.csv
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_patient_high_trust_public_validation.csv
- /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified_hightrust.json
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_public_evidence_consensus_table.csv
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence/15_model_trust_score_after_high_trust_validation.json
- /content/drive/MyDrive/desktop_app/data/audit/15_high_trust_api_status_audit.csv

## Recommended next step

Review the outputs first.

If acceptable, copy:

dashboard_simulation_patients_verified_hightrust.json

to the dashboard as:

dashboard_simulation_patients_verified.json

Then continue to true clinical evidence citation enrichment and external validation.