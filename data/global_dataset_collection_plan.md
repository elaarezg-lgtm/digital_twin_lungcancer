
# Global Dataset Collection and Fusion Plan
Generated: 2026-06-04T00:36:20.425373

## Goal
Build a trusted EGFR-mutated NSCLC/LUAD digital twin data foundation by combining:
- public patient cohorts,
- multi-omics datasets,
- proteogenomics/phosphoproteomics,
- real-world genomics,
- open precision-oncology evidence knowledgebases.

## Priority order
1. TCGA-LUAD / GDC
2. cBioPortal TCGA-LUAD PanCancer Atlas
3. CPTAC-LUAD proteogenomics
4. AACR GENIE public + GENIE BPC NSCLC
5. CIViC evidence knowledgebase
6. Cancer Genome Interpreter / CGI
7. DGIdb drug-gene support
8. DepMap/GDSC cell-line drug response later
9. TCIA imaging later

## Key principle
Do not blindly merge datasets. Every source must pass:
- ID harmonization
- tumor type filtering
- gene/protein alteration normalization
- missingness analysis
- duplicate check
- evidence traceability
- terms/access compliance

## Current generated files
- /content/drive/MyDrive/desktop_app/data/audit/dataset_sources.csv
- /content/drive/MyDrive/desktop_app/data/audit/global_dataset_collection_checklist.csv
- /content/drive/MyDrive/desktop_app/data/audit/harmonization_rules.json
- /content/drive/MyDrive/desktop_app/data/audit/missingness_report.csv
- /content/drive/MyDrive/desktop_app/data/audit/duplicate_patient_report.csv
- /content/drive/MyDrive/desktop_app/data/audit/evidence_traceability_report.csv
- /content/drive/MyDrive/desktop_app/data/fused/global_egfr_nsclc_patient_table.csv
- /content/drive/MyDrive/desktop_app/data/fused/global_egfr_nsclc_mutation_table.csv
- /content/drive/MyDrive/desktop_app/data/fused/global_egfr_nsclc_knowledge_table.csv

## Next notebook
10_TCGA_CPTAC_GENIE_DATA_INGESTION.ipynb

This next notebook should ingest TCGA/cBioPortal first, then CPTAC, then GENIE.
