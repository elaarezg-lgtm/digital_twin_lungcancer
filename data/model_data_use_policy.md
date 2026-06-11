
# EGFR Lung Cancer Digital Twin — Scientific Data Use Policy

Generated: 2026-06-04T11:48:26.929313

## Core principle

No treatment recommendation, pathway score, population claim, or model training input may be used unless its origin is traceable and its use category is explicit.

## Allowed source categories

### 1. TRAINABLE_PATIENT_LEVEL
Patient/sample-level data with legal access and usable clinical/molecular fields.
Examples:
- TCGA-LUAD
- CPTAC-LUAD
- cBioPortal downloadable public studies
- GENIE only after official access/terms are completed

Allowed:
- feature matrix construction
- mutation/co-mutation analysis
- external validation if outcomes exist

Not automatically allowed:
- treatment response prediction unless real treatment-response labels exist

### 2. KNOWLEDGE_EVIDENCE
Curated variant/drug evidence and interpretation sources.
Examples:
- CIViC
- Cancer Genome Interpreter
- DGIdb
- peer-reviewed trials
- regulatory labels/guidelines when manually curated

Allowed:
- treatment logic explanation
- evidence audit
- sensitivity/resistance support

Not allowed:
- generating fake patient outcomes
- training as patient-level cohort

### 3. REGIONAL_PREVALENCE_CONTEXT
Country or region-level studies with EGFR mutation frequencies or summary statistics.

Allowed:
- dashboard context after manual verification
- report discussion
- regional prevalence comparison

Not allowed:
- training as individual patients
- creating synthetic patients without labeling them as simulation only

### 4. CONTROLLED_ACCESS_REQUIRED
Potentially valuable but blocked until official access/terms are completed.

Allowed:
- keep in registry
- plan future integration

Not allowed:
- model training
- dashboard claims
- scraping or bypassing access controls

### 5. PROXY_PENDING_VALIDATION
Derived internal features such as mutation-derived pathway scores.

Allowed:
- dashboard explanation if clearly labeled as proxy
- exploratory analysis

Not allowed:
- claiming true phosphoproteomics or clinical validation

### 6. DO_NOT_USE
Any untraceable, restricted, fabricated, or unsupported data.

Never allowed.

## Current trusted base from Notebook 10

- Clinical patients: 1198
- Clinical samples: 1262
- Curated mutations: 104504
- EGFR mutation rows: 99
- Feature matrix patients: 1198
- EGFR-mutant patient table: 75
- Pathway proxy rows: 8386

## Important limitation

The current pathway file is a mutation-derived pathway proxy.
It is not true CPTAC phosphoproteomics yet.
It must be labeled as:

"Mutation-derived pathway activity proxy, pending true CPTAC proteomics/phosphoproteomics integration."

## Country expansion rule

For Tunisia, Morocco, Egypt, Spain, Italy, Japan, China, India and other countries:

1. Search literature and repositories.
2. Classify each source.
3. Use summary papers only as regional context.
4. Use patient-level tables only if downloadable/authorized and de-identified.
5. Keep citation and access terms for every source.
6. Never fabricate country patients.

## Dashboard labeling requirement

Every output must show one of:

- Patient-level dataset evidence
- Knowledgebase evidence
- Regional prevalence context
- Model-derived proxy
- Pending validation
- Not available

## Next phase

Notebook 12 should build the evidence knowledge base and global fusion:
- CIViC-style evidence table
- CGI-style actionability support
- DGIdb drug-gene support
- EGFR alteration treatment logic
- global dashboard JSON
