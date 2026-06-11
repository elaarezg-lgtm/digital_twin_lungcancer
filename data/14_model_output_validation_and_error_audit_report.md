
# Notebook 14 Report — Model Output Validation and Error Audit

Generated: 2026-06-06T14:04:53.244923

## Purpose

This notebook validates the current EGFR lung cancer digital twin dashboard outputs before adding more data or increasing model complexity.

The objective is to make the project more scientifically trusted and precise by identifying:
- impossible numeric values,
- treatment logic inconsistencies,
- resistance/bypass logic issues,
- missing evidence labels,
- missing patient fields,
- pathway proxy range issues.

## Dataset audited

JSON file:
/content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified.json

Patients audited:
75

## Treatment distribution

                  best_drug  patient_count  percent
                Osimertinib             48    64.00
Platinum-based Chemotherapy             14    18.67
                   Afatinib              7     9.33
                Amivantamab              6     8.00

## Audit summary

| audit                            |   rows |   pass_count |   warn_or_review_count |   fail_count | status   |
|:---------------------------------|-------:|-------------:|-----------------------:|-------------:|:---------|
| basic_output_completeness        |     75 |           75 |                      0 |            0 | PASS     |
| alteration_treatment_consistency |     75 |           61 |                     14 |            0 | REVIEW   |
| resistance_logic                 |     75 |           69 |                      6 |            0 | REVIEW   |
| timeline_values                  |    975 |          975 |                      0 |            0 | PASS     |
| pathway_values                   |     75 |           75 |                      0 |            0 | PASS     |
| evidence_labels                  |     75 |           75 |                      0 |            0 | PASS     |
| patient_level_error_report       |     75 |           60 |                     15 |            0 | REVIEW   |

## Key review counts

- Alteration-treatment cases needing review: 14
- Resistance logic cases needing review: 6
- Timeline failing frames: 0
- Pathway cases needing review: 0
- Patients with at least one review/error flag: 15

## Interpretation

PASS means the current output is structurally and logically acceptable for the research prototype.
REVIEW means the output is not necessarily wrong, but requires expert or rule-level inspection.
FAIL means the output must be corrected before being presented as reliable.

## Scientific status

The system is a research prototype under development with the goal of becoming a reliable oncology decision-support tool after rigorous validation.

Current limitations:
- treatment evidence still requires citation enrichment,
- pathway values are still mutation-derived proxies unless true proteomics/phosphoproteomics are integrated,
- country-level studies are context only unless patient-level data is legally available,
- outputs are not standalone medical decisions.

## Output files

- /content/drive/MyDrive/desktop_app/data/validation/14_basic_output_completeness_audit.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_treatment_distribution_audit.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_alteration_treatment_consistency_audit.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_resistance_logic_audit.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_timeline_value_audit.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_pathway_value_audit.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_evidence_label_audit.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_patient_level_error_report.csv
- /content/drive/MyDrive/desktop_app/data/validation/14_model_output_validation_summary.csv

## Next step

If the validation summary has FAIL rows, fix them first.

If only REVIEW rows remain, continue to:

15_EVIDENCE_CITATION_ENRICHMENT.ipynb

That notebook will replace manual verification placeholders with cited, traceable oncology evidence.
