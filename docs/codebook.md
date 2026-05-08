# CyberSecEval Codebook

## Dataset units

- `trainees_anonymised.csv`: one row per trainee evaluation response.
- `trainers_anonymised.csv`: one row per trainer evaluation response.

## Core entity columns

| Column | Description | Release note |
| --- | --- | --- |
| `SurveyID` | Survey identifier | retain if non-personal |
| `SurveyTitle` | Survey title | retain if non-personal |
| `ResponseID` | Response identifier | replace with random non-reversible ID |
| `DateTime` | Response timestamp | convert to month or remove if re-identification risk |
| `Module Type` | Training module code/category | retain |
| `Sector` | Sector context such as maritime, health, energy | retain unless sparse combination risks identity |
| `Training Level` | Training level | retain |
| `Module Title` | Module title | retain |
| `Tools Used` | Tools used during training | retain if no personal or institutional identifiers |
| `Certificate Of Attendance` | Certificate field | retain if categorical only |

## Trainee KPI columns

| Column | Meaning | Scale |
| --- | --- | --- |
| `Q15_Value` | Overall satisfaction | 1--7 |
| `Q18_Value` | Practical relevance / applied practice | 1--7 |
| `Q33_Value` | Relevance to current or desired job role | 1--7 |
| `Q34_Value` | Knowledge and skills enhancement | 1--7 |
| `Q36_Value` | Recommendation item | 0--10 |

## Text columns

Before public release, inspect and clean all free-text fields. Remove names, emails, organisations where not essential, URLs, phone numbers, exact locations, and any information that could identify a trainee, trainer, or institution.

Recommended release options:

1. release cleaned thematic labels only;
2. release paraphrased/anonymised comments;
3. release original comments only after manual review and institutional approval.

## Missing values

Blank, `NA`, `N/A`, and non-numeric entries in numeric KPI columns are treated as missing.

## Exclusion rule

Rows labelled `CSP000` represent cross-module summer-school entries and are excluded from module-specific analysis. They may be analysed separately as cross-module programme-level feedback.
