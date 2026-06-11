# Notebook 16B Report — GENIE BPC NSCLC Outcome Dataset Access Plan

Generated: 2026-06-07T23:48:00.578058

## Why this notebook exists

Notebook 16A showed that the current project does not contain enough real outcome labels to train a hospital-grade predictive model.
The next step is to build a real patient-treatment-outcome dataset.

## Main target dataset

AACR GENIE BPC NSCLC v2.0-public.

Why:
- It is a real-world clinicogenomic NSCLC dataset.
- It contains treatment exposure and outcome-oriented clinical data.
- It is more suitable for hospital-grade model development than simulation/proxy labels.

## Generated files

- /content/drive/MyDrive/desktop_app/data/training/16B_genie_bpc_nsclc_access_checklist.csv
- /content/drive/MyDrive/desktop_app/data/training/16B_hospital_training_schema.csv
- /content/drive/MyDrive/desktop_app/data/training/16B_training_target_definitions.csv
- /content/drive/MyDrive/desktop_app/data/training/16B_patient_treatment_outcome_training_template.csv
- /content/drive/MyDrive/desktop_app/data/training/16B_outcome_dataset_acquisition_tasks.csv

## Next step

Get Synapse access to GENIE BPC NSCLC v2.0-public.
After access is ready, create Notebook 16C to pull and transform the actual tables into the training schema.