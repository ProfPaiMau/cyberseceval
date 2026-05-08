# Anonymisation Protocol

The following protocol instructions were applied before public release on GitHub or Zenodo.

## Remove or transform direct identifiers

- Remove names, emails, phone numbers, addresses, and personal URLs.
- Replace `ResponseID` with a new random non-reversible identifier.
- Remove metadata that can identify individuals or small training events.

## Generalise quasi-identifiers

- Convert exact timestamps to month or quarter.
- Avoid combinations of sector, country, institution, and small module groups that uniquely identify a person.
- For small cells (e.g., fewer than five responses), consider aggregation or suppression.

## Free-text review

Manually inspect all text fields, especially:

- recommendations;
- general feedback;
- open-ended improvement fields;
- training-location descriptions;
- tool and platform descriptions.

Remove or paraphrase any personally identifying details.

## Recommended final public files

- `trainees_anonymised.csv`
- `trainers_anonymised.csv`
- `kpi_mapping.csv`
- `codebook.md`
- `analyze_training_evaluations.py`

## Validation checklist

Before release, confirm:

- no emails remain;
- no names remain;
- no exact personal locations remain;
- no direct identifiers remain;
- small-cell disclosure risk has been considered;
- license and citation metadata are correct.
