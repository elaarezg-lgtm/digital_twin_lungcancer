# Notebook 15B Report — CIViC and Label Citation Repair

Generated: 2026-06-07T14:01:16.554570

## Purpose

Notebook 15 improved public evidence traceability but CIViC returned no usable evidence rows.
This notebook repairs the evidence layer using CIViC releases/API attempts, openFDA exact label matching, and PubMed citation context.

## Inputs

- Patients loaded: 75
- Input JSON: /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified_hightrust.json
- Previous global score: 7.73

## CIViC repair

- CIViC normalized rows: 266
- CIViC exact rule matches: 8
- CIViC raw file: /content/drive/MyDrive/desktop_app/data/high_trust_evidence_repair/15B_civic_raw_evidence_attempt.csv
- CIViC normalized file: /content/drive/MyDrive/desktop_app/data/high_trust_evidence_repair/15B_civic_egfr_lung_evidence_normalized.csv

## Rule evidence repair

- openFDA exact rule matches: 10
- PubMed citation context matches: 10

## Patient validation distribution

repaired_patient_public_validation_status
HIGH_TRUST_PUBLIC_VALIDATION_SUPPORTED_AFTER_15B    62
PARTIAL_PUBLIC_VALIDATION_SUPPORTED_AFTER_15B       13

## Repaired model trust score

```json
{
  "created_at": "2026-06-07T14:01:16.494298",
  "model_version": "EGFR_Global_TrustedEvidenceFusion_v1_15B_civic_label_citation_repair",
  "patients": 75,
  "previous_global_prototype_score_0_10": 7.73,
  "technical_functionality_score_0_10": 8.5,
  "internal_consistency_score_0_10": 9.0,
  "scientific_traceability_score_0_10": 8.63,
  "clinical_readiness_score_0_10": 5.2,
  "global_prototype_score_0_10": 8.0,
  "average_patient_public_trust_score_0_1": 0.9329,
  "patient_status_distribution": {
    "HIGH_TRUST_PUBLIC_VALIDATION_SUPPORTED_AFTER_15B": 62,
    "PARTIAL_PUBLIC_VALIDATION_SUPPORTED_AFTER_15B": 13
  },
  "civic_rows_retrieved": 266,
  "civic_rule_exact_matches": 8,
  "openfda_rule_exact_matches": 10,
  "pubmed_rule_context_matches": 10,
  "high_trust_sources_used": [
    "CIViC accepted evidence release/API when available",
    "openFDA drug labels",
    "PubMed E-utilities citation context",
    "ClinicalTrials.gov trial context",
    "cBioPortal public genomic cohort context"
  ],
  "excluded_or_pending": {
    "OncoKB": "Full therapeutic validation pending approved production API token.",
    "DGIdb": "Excluded from high-trust scoring because interaction support is not clinical actionability."
  },
  "interpretation": "15B improves rule-level traceability using public high-trust evidence. It still does not establish clinical outcome prediction accuracy. Final clinical validation requires real response/PFS/OS labels, external cohorts, and expert review."
}
```

## Scientific interpretation

This repair improves rule-level traceability. It does not prove clinical outcome prediction accuracy.
The model still requires OncoKB production validation when the token is approved, real outcome labels, external validation, and expert oncologist review.

## Recommended dashboard use

Do not overwrite the main dashboard JSON automatically.
First review the repaired score and audit table.

If acceptable, copy:

/content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified_15B_repaired.json

to:

/content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified.json

## Outputs

- /content/drive/MyDrive/desktop_app/data/high_trust_evidence_repair/15B_repaired_rule_evidence_consensus.csv
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence_repair/15B_patient_repaired_public_validation.csv
- /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified_15B_repaired.json
- /content/drive/MyDrive/desktop_app/data/high_trust_evidence_repair/15B_model_trust_score_after_civic_label_citation_repair.json
- /content/drive/MyDrive/desktop_app/data/audit/15B_civic_label_citation_repair_audit.csv