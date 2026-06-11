# Notebook 16A Report — Outcome Dataset Audit and Training Table Seed

Generated: 2026-06-07T22:51:10.776055

## Purpose

This notebook checks whether the current project contains real hospital-training labels.
The goal is to separate real clinical labels from model-derived proxy outputs.

## Input data scanned

- Data directory: /content/drive/MyDrive/desktop_app/data
- Files scanned: 178
- Dashboard JSON used: /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified_15B_repaired.json
- Patients loaded into training seed: 75

## Source distribution

source_group
CPTAC    40
TCGA     35

## Current recommended-treatment distribution

recommended_treatment
Osimertinib                    48
Platinum-based Chemotherapy    13
Afatinib                        8
Amivantamab                     6

## Candidate label columns found across files

label_type
response      355
treatment     272
resistance    144
survival      100

## Label quality audit

| label                        |   available_patients |   total_patients |   availability_pct | hospital_training_ready   | minimum_research_training_ready   | notes                                                                      |
|:-----------------------------|---------------------:|-----------------:|-------------------:|:--------------------------|:----------------------------------|:---------------------------------------------------------------------------|
| real_treatment_received      |                    0 |               75 |               0    | False                     | False                             | Current dashboard recommendation is not the same as real received therapy. |
| real_response_label          |                    0 |               75 |               0    | False                     | False                             | Need CR/PR/SD/PD or RECIST response from real treatment records.           |
| real_pfs_label               |                    0 |               75 |               0    | False                     | False                             | Need progression-free survival months/time-to-event.                       |
| real_overall_survival_months |                   34 |               75 |              45.33 | False                     | False                             | Can support survival modeling only if enough real OS values exist.         |
| real_survival_status         |                   35 |               75 |              46.67 | False                     | False                             | Vital status alone is weak without follow-up time.                         |
| any_real_outcome_label       |                   35 |               75 |              46.67 | False                     | False                             | Any real outcome label available from source data.                         |

## Training readiness decision

```json
{
  "created_at": "2026-06-07T22:51:10.758505",
  "patients_in_seed_table": 75,
  "real_treatment_received_count": 0,
  "real_response_label_count": 0,
  "real_pfs_label_count": 0,
  "real_os_label_count": 34,
  "can_train_response_model_now": false,
  "can_train_survival_model_now": false,
  "recommended_next_action": "Do not train a clinical prediction model yet. Build outcome-labeled dataset first from GENIE/BPC, cBioPortal studies with treatment/outcomes, institutional retrospective data, or curated literature tables.",
  "scientific_decision": "Current data supports evidence-ranked research prototype, not trained hospital-grade outcome prediction."
}
```

## Scientific interpretation

The current dashboard contains strong evidence-ranked recommendations and simulation proxies.
However, simulation/proxy outputs must not be treated as real treatment-response labels.
A hospital-grade trained model requires real received therapy plus real outcome labels such as RECIST response, PFS, OS, progression, or resistance emergence.

## Next step

If real outcome labels are not sufficient, create Notebook 16B to collect outcome-labeled cohorts and construct a patient-treatment-outcome dataset.

## Outputs

- /content/drive/MyDrive/desktop_app/data/training/16A_data_file_inventory.csv
- /content/drive/MyDrive/desktop_app/data/training/16A_column_inventory.csv
- /content/drive/MyDrive/desktop_app/data/training/16A_candidate_outcome_and_treatment_labels.csv
- /content/drive/MyDrive/desktop_app/data/training/16A_missingness_preview_report.csv
- /content/drive/MyDrive/desktop_app/data/training/16A_patient_treatment_outcome_training_seed.csv
- /content/drive/MyDrive/desktop_app/data/training/16A_label_quality_audit.csv
- /content/drive/MyDrive/desktop_app/data/training/16A_feature_dictionary.csv
- /content/drive/MyDrive/desktop_app/data/training/16A_training_readiness_decision.json