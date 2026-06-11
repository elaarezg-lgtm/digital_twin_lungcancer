
# 14B Final Bypass Resistance Patch Report

Generated: 2026-06-07T11:50:41.923896

## Why this patch was added

The 14B correction solved alteration-treatment consistency, timeline values, and pathway values, but 10 patients still had:

bypass_present_but_resistance_risk_low

This final cell applies a resistance-risk floor whenever MET/KRAS/PIK3CA/BRAF bypass is detected.

## Resistance floors

- One bypass alteration: minimum resistance risk 0.35
- Two bypass alterations: minimum resistance risk 0.45
- Three or more bypass alterations: minimum resistance risk 0.55

## Treatment distribution after final patch

| best_drug                   |   patient_count |   percent |
|:----------------------------|----------------:|----------:|
| Osimertinib                 |              48 |     64    |
| Platinum-based Chemotherapy |              13 |     17.33 |
| Afatinib                    |               8 |     10.67 |
| Amivantamab                 |               6 |      8    |

## Final validation summary

| audit                            |   rows |   PASS |   REVIEW |   FAIL | status   |
|:---------------------------------|-------:|-------:|---------:|-------:|:---------|
| final_patch_alteration_treatment |     75 |     75 |        0 |      0 | PASS     |
| final_patch_resistance           |     75 |     75 |        0 |      0 | PASS     |
| final_patch_timeline             |    975 |    975 |        0 |      0 | PASS     |
| final_patch_pathway              |     75 |     75 |        0 |      0 | PASS     |
| final_patch_patient_error_report |     75 |     75 |        0 |      0 | PASS     |

## Remaining review cases

| patient_id   | egfr   | best_drug   | error_count   | errors   | status   |
|--------------|--------|-------------|---------------|----------|----------|

## Updated files

- /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_global.json
- /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified.json
- /content/drive/MyDrive/desktop_app/data/corrections/14B_final_bypass_resistance_patch_log.csv
- /content/drive/MyDrive/desktop_app/data/corrections/14B_final_patch_validation_summary.csv
- /content/drive/MyDrive/desktop_app/data/corrections/14B_final_patch_patient_error_report.csv

## Scientific note

This patch corrects internal consistency. It does not replace clinical validation.
The model remains a research prototype moving toward reliable oncology decision support after rigorous validation.
