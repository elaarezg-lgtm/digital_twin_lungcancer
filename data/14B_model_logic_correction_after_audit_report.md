
# Notebook 14B Report — Model Logic Correction After Audit

Generated: 2026-06-06T14:43:19.476970

## Why this notebook was created

Notebook 14 showed:
- no FAIL rows,
- valid timeline values,
- valid pathway values,
- valid evidence labels,
- but REVIEW cases in alteration-treatment consistency and resistance/bypass logic.

This notebook applied targeted corrections instead of blindly changing the model.

## Corrections applied

1. Other EGFR alteration handling
   - Unknown/other EGFR alterations are handled as cautious fallback cases.
   - Platinum-based chemotherapy is allowed as cautious fallback, not as a precision matched targeted recommendation.

2. Uncommon EGFR sensitizing alterations
   - G719X, S768I and L861Q are prioritized toward Afatinib/Osimertinib before non-targeted fallback.
   - This remains manual-verification-required until citation enrichment is completed.

3. EGFR exon 20 insertion
   - Amivantamab / Amivantamab + Lazertinib ranking strengthened.
   - Erlotinib/Gefitinib penalized as default choices.

4. T790M
   - Osimertinib ranking strengthened.
   - Erlotinib/Gefitinib resistance penalty applied.

5. Bypass resistance calibration
   - MET/KRAS/PIK3CA/BRAF bypass now increases bypass penalty and resistance risk for EGFR TKI monotherapy.
   - Pathway proxy state is updated accordingly.

## Patients

Patients corrected:
75

Patients with at least one correction log:
75

## Treatment distribution after correction

| best_drug                   |   patient_count |   percent |
|:----------------------------|----------------:|----------:|
| Osimertinib                 |              48 |     64    |
| Platinum-based Chemotherapy |              13 |     17.33 |
| Afatinib                    |               8 |     10.67 |
| Amivantamab                 |               6 |      8    |

## Post-correction validation summary

| audit                                |   rows |   PASS |   REVIEW |   FAIL | status   |
|:-------------------------------------|-------:|-------:|---------:|-------:|:---------|
| post_correction_alteration_treatment |     75 |     75 |        0 |      0 | PASS     |
| post_correction_resistance           |     75 |     65 |       10 |      0 | REVIEW   |
| post_correction_timeline             |    975 |    975 |        0 |      0 | PASS     |
| post_correction_pathway              |     75 |     75 |        0 |      0 | PASS     |
| post_correction_patient_error_report |     75 |     65 |       10 |      0 | REVIEW   |

## Remaining review cases

| patient_id                        | egfr                                                                            | best_drug                   |   error_count | errors                                            | status   |
|:----------------------------------|:--------------------------------------------------------------------------------|:----------------------------|--------------:|:--------------------------------------------------|:---------|
| CPTAC__luad_cptac_2020__C3L-00604 | EGFR exon 19 deletion EGFR exon 19 deletion p.E746_A750del p.E746_A750del       | Osimertinib                 |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| CPTAC__luad_cptac_2020__C3L-00913 | Other EGFR alteration Other EGFR alteration p.L777L p.L777L                     | Platinum-based Chemotherapy |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| CPTAC__luad_cptac_2020__C3N-02582 | EGFR exon 19 deletion EGFR exon 19 deletion p.E746_A750del p.E746_A750del       | Osimertinib                 |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| CPTAC__luad_cptac_2020__X11LU016  | EGFR G719X; EGFR S768I EGFR G719X; EGFR S768I p.G719C; p.S768I p.G719C; p.S768I | Afatinib                    |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| TCGA__luad_tcga__TCGA-05-4382     | Other EGFR alteration Other EGFR alteration p.E545Q; p.R222L p.E545Q; p.R222L   | Platinum-based Chemotherapy |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| TCGA__luad_tcga__TCGA-05-4410     | Other EGFR alteration Other EGFR alteration p.R377S p.R377S                     | Platinum-based Chemotherapy |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| TCGA__luad_tcga__TCGA-50-5933     | Other EGFR alteration Other EGFR alteration p.P753= p.P753=                     | Platinum-based Chemotherapy |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| TCGA__luad_tcga__TCGA-69-7765     | Other EGFR alteration Other EGFR alteration p.Q486* p.Q486*                     | Platinum-based Chemotherapy |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| TCGA__luad_tcga__TCGA-95-7039     | Other EGFR alteration Other EGFR alteration p.S921R p.S921R                     | Platinum-based Chemotherapy |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |
| TCGA__luad_tcga__TCGA-95-7947     | Other EGFR alteration Other EGFR alteration p.I91V; p.R1052I p.I91V; p.R1052I   | Platinum-based Chemotherapy |             1 | resistance:bypass_present_but_resistance_risk_low | REVIEW   |

## Scientific caution

This correction improves internal logic but does not replace formal clinical validation.

Evidence rows still require citation enrichment from trusted sources such as:
- CIViC
- regulatory labels
- guidelines
- peer-reviewed clinical studies
- expert oncology review

Current status:
Research prototype under development, with the objective of becoming reliable oncology decision support after rigorous validation.

## Updated files

- /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_global.json
- /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_verified.json
- /content/drive/MyDrive/desktop_app/data/corrections/14B_dashboard_simulation_patients_audit_corrected.json
- /content/drive/MyDrive/desktop_app/data/corrections/14B_logic_correction_log.csv
- /content/drive/MyDrive/desktop_app/data/corrections/14B_post_correction_validation_summary.csv
- /content/drive/MyDrive/desktop_app/data/corrections/14B_post_correction_patient_error_report.csv
