# CyberSecEval Codebook

## Dataset units

- `trainees_anonymised.csv`: one row per trainee evaluation response.
- `trainers_anonymised.csv`: one row per trainer evaluation response.

## Core entity columns

| Column | Description | Release note |
| --- | --- | --- |
| `SurveyID` | Survey identifier | retained if non-personal |
| `SurveyTitle` | Survey title | retained if non-personal |
| `ResponseID` | Response identifier | replaced with random non-reversible ID |
| `DateTime` | Response timestamp | kept as it is |
| `Module Type` | Training module code/category | retained |
| `Sector` | Sector context such as maritime, health, energy | retained unless sparse combination risks identity |
| `Training Level` | Training level | retained |
| `Module Title` | Module title | retained |
| `Tools Used` | Tools used during training | retained if no personal or institutional identifiers |
| `Certificate Of Attendance` | Certificate field | retained if categorical only |

## Trainee KPI columns

| Column | Meaning | Scale |
| --- | --- | --- |
| `Q15_Value` | Overall satisfaction | 1--7 |
| `Q18_Value` | Practical relevance / applied practice | 1--7 |
| `Q33_Value` | Relevance to current or desired job role | 1--7 |
| `Q34_Value` | Knowledge and skills enhancement | 1--7 |
| `Q36_Value` | Recommendation item | 0--10 |

## Text columns

Before public release, inspect and clean all free-text fields. Remove names, emails, organisations where not essential, URLs, 
1. cleaned thematic labels only;
2. paraphrased/anonymised comments;

