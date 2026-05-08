# Zenodo Release Steps

## Recommended route: GitHub + Zenodo DOI

1. Create a GitHub repository named `cyberseceval`.
2. Upload the repository contents.
3. Add anonymised data files under `data/raw/`.
4. Check that `README.md`, `LICENSE`, `CITATION.cff`, and `docs/` are complete.
5. Log in to Zenodo.
6. Go to **GitHub** integration in Zenodo.
7. Enable Zenodo archiving for the `cyberseceval` repository.
8. In GitHub, create a release, for example `v1.0.0`.
9. Zenodo will automatically archive the release and issue a DOI.
10. Copy the DOI into:
    - `README.md`
    - `CITATION.cff`
    - the ASE paper Data Availability Statement

## Alternative route: Zenodo manual upload

1. Create a ZIP file of the repository.
2. Go to Zenodo and select **New Upload**.
3. Upload the ZIP file.
4. Select upload type: Dataset.
5. Add title, authors, description, keywords, and license.
6. Reserve or publish DOI.
7. Add DOI to paper and metadata.

## Recommended metadata

Title:
CyberSecEval: A Multi-Module Dataset and KPI Framework for Evaluating Cybersecurity Training Effectiveness

Description:
A reusable anonymised dataset and KPI-mapping framework for analysing cybersecurity training effectiveness across multiple professional training modules.

Keywords:
cybersecurity training; software engineering education; empirical software engineering; training evaluation; dataset; KPI framework

License:
CC BY 4.0 for dataset and documentation; MIT for scripts.
