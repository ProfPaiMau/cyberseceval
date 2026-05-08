# CyberSecEval

CyberSecEval is a reusable dataset and KPI-mapping framework for evaluating cybersecurity training effectiveness across multi-module professional training programmes.

The artefact supports the ASE 2026 Tools and Datasets submission: **CyberSecEval: A Multi-Module Dataset and KPI Framework for Evaluating Cybersecurity Training Effectiveness**.

## Intended users

CyberSecEval is intended for researchers and practitioners working on:

- cybersecurity education and training evaluation;
- software/security engineering education datasets;
- empirical evaluation of professional training programmes;
- KPI construction and reproducible survey analytics.

## Artefact contents

```text
CyberSecEval/
├── data/
│   ├── raw/                  # anonymised input CSVs to be added before release
│   └── processed/            # derived aggregate outputs safe for release
├── docs/
│   ├── codebook.md           # survey and variable documentation
│   ├── kpi_mapping.csv       # survey-item to KPI operationalisation
│   ├── anonymisation_protocol.md
│   └── zenodo_release_steps.md
├── scripts/
│   └── analyze_training_evaluations.py
├── outputs/                  # generated tables/figures from script
├── CITATION.cff
├── LICENSE
└── README.md
```

## Data overview

The current evaluation dataset contains:

- 835 trainee survey rows in the original export;
- 814 module-specific trainee evaluations after excluding 21 cross-module `CSP000` rows;
- 87 trainer evaluations;
- 12 training modules (`CSP001`--`CSP012`), of which 11 have trainee evaluation data in the analysed period;
- Likert-scale trainee variables for satisfaction, practical relevance, learning gain, job-role relevance, and recommendation intent.

## Core KPI mapping

The primary KPIs are computed from numeric survey columns:

| KPI | Survey item | Scale |
| --- | --- | --- |
| Overall Satisfaction | `Q15_Value` | 1--7 |
| Applied Practice / Practical Relevance | `Q18_Value` | 1--7 |
| Knowledge Transfer / Learning Gain | `Q34_Value` | 1--7 |
| Job-role Relevance | `Q33_Value` | 1--7 |
| Recommendation | `Q36_Value` | 0--10 |

NPS is computed from `Q36_Value` as `%promoters - %detractors`, where promoters are scores 9--10 and detractors are scores 0--6.

## Reproducing the analysis

1. Place the anonymised trainee export at:

```text
data/raw/trainees_anonymised.csv
```

2. Optionally place the anonymised trainer export at:

```text
data/raw/trainers_anonymised.csv
```

3. Run:

```bash
python scripts/analyze_training_evaluations.py --input data/raw/trainees_anonymised.csv --output outputs
```

The script will produce:

- `outputs/module_kpi_summary.csv`
- `outputs/overall_kpi_summary.csv`
- `outputs/module_kpi_summary_latex.tex`

## Current derived results

Using the analysed trainee dataset (`N=814` module-specific evaluations):

- Overall Satisfaction: `M=6.2475`, `SD=1.0644`, valid `N=804`
- Applied Practice: `M=6.2797`, `SD=0.9786`, valid `N=808`
- Knowledge Transfer: `M=5.6481`, `SD=1.4685`, valid `N=807`
- Recommendation: `M=8.5675`, `SD=1.8857`, valid `N=807`
- NPS: `50.1859`

# License

Dataset + documentation → CC BY 4.0
Code/scripts → MIT License