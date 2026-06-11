
# Notebook 12 Report — Knowledge Evidence and Global Fusion

Generated: 2026-06-04T13:04:52.135338

## Purpose

This notebook fused the validated TCGA/CPTAC EGFR-mutant patient table with a conservative,
traceable precision-oncology evidence layer.

## Inputs

- EGFR patient table: /content/drive/MyDrive/desktop_app/data/fused/10_global_egfr_mutant_patient_table_seed.csv
- EGFR mutation table: /content/drive/MyDrive/desktop_app/data/curated/10_egfr_mutations_curated.csv
- Feature matrix: /content/drive/MyDrive/desktop_app/data/fused/10_global_egfr_nsclc_feature_matrix_seed.csv
- Trusted source filter: /content/drive/MyDrive/desktop_app/data/registry/trusted_source_filter.csv

## Input counts

- Clinical patients: 1198
- Curated mutations: 104504
- EGFR mutation rows: 99
- EGFR-mutant patients: 75
- Feature matrix rows: 1198
- Pathway proxy rows: 8386

## Evidence layer

Evidence KB rows: 19

The evidence table is conservative and source-labeled.
It is not presented as official OncoKB validation.
Rows requiring manual verification are labeled:

MANUAL_VERIFICATION_REQUIRED

DGIdb was queried only as drug-gene interaction support.
DGIdb alone is not clinical actionability.

DGIdb API status:
{
  "ok": true,
  "error": null,
  "queried_genes": [
    "EGFR",
    "MET",
    "KRAS",
    "PIK3CA",
    "BRAF",
    "ERBB2",
    "ALK",
    "RET",
    "ROS1"
  ],
  "timestamp": "2026-06-04T12:28:54.031373"
}

## Outputs

- Evidence KB: /content/drive/MyDrive/desktop_app/data/knowledge/12_egfr_precision_oncology_evidence_kb.csv
- DGIdb support: /content/drive/MyDrive/desktop_app/data/knowledge/12_dgidb_drug_gene_interaction_support.csv
- Patient evidence matches: /content/drive/MyDrive/desktop_app/data/fused/12_patient_evidence_matches.csv
- Ranking summary: /content/drive/MyDrive/desktop_app/data/fused/12_patient_treatment_ranking_summary.csv
- Dashboard global JSON: /content/drive/MyDrive/desktop_app/data/dashboard_simulation_patients_global.json
- Global fusion table: /content/drive/MyDrive/desktop_app/data/fused/12_global_patient_evidence_fusion_table.csv
- Quality audit: /content/drive/MyDrive/desktop_app/data/audit/12_knowledge_fusion_quality_audit.csv

## Dashboard output

Generated patients:
75

Best treatment distribution:
best_drug
Osimertinib                    48
Platinum-based Chemotherapy    14
Afatinib                        7
Amivantamab                     6

## Mandatory scientific limitations

1. This is a research prototype, not a clinical decision tool.
2. Treatment ranking is evidence-grounded but not a prescription.
3. Current pathway states are mutation-derived proxies.
4. Regional/country literature is not training data unless patient-level access is verified.
5. Manual evidence verification and citation enrichment remain required before any clinical use.

## Next notebook

13_DASHBOARD_GLOBAL_INTEGRATION_AND_VALIDATION.ipynb

Purpose:
- copy dashboard_simulation_patients_global.json into local/dashboard API path,
- update API to serve global JSON,
- add evidence badges to dashboard,
- validate patient selection and global source labels.
