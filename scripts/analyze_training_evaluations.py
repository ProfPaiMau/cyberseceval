from pathlib import Path
import pandas as pd
import re

ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = ROOT / "data" / "raw" / "trainees_anonymised.csv"
OUTPUT_DIR = ROOT / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODULE_OUTPUT = OUTPUT_DIR / "module_kpi_summary_current.csv"
OVERALL_OUTPUT = OUTPUT_DIR / "overall_kpi_summary_current.csv"

CORE_KPIS = {
    "OS_Q15": "Q15_Value",
    "AP_Q18": "Q18_Value",
    "KT_Q34": "Q34_Value",
    "JR_Q33": "Q33_Value",
    "REC_Q36": "Q36_Value",
}


def extract_csp_code(value):
    if pd.isna(value):
        return None

    value = str(value)
    match = re.search(r"CSP\d{3}", value)
    if match:
        return match.group(0)

    return None


def nps_score(series):
    values = pd.to_numeric(series, errors="coerce").dropna()

    if len(values) == 0:
        return None

    promoters = (values >= 9).sum()
    detractors = (values <= 6).sum()

    return round(((promoters / len(values)) - (detractors / len(values))) * 100, 2)


def summarise_group(df, group_col=None):
    rows = []

    if group_col:
        grouped = df.groupby(group_col, dropna=False)
    else:
        grouped = [("Overall", df)]

    for group_name, group in grouped:
        row = {
            "Module": group_name,
            "N_total": len(group),
        }

        for label, col in CORE_KPIS.items():
            if col not in group.columns:
                row[f"N_{label}"] = 0
                row[f"mean_{label}"] = None
                row[f"sd_{label}"] = None
                continue

            values = pd.to_numeric(group[col], errors="coerce")
            valid = values.dropna()

            row[f"N_{label}"] = len(valid)
            row[f"mean_{label}"] = round(valid.mean(), 2) if len(valid) else None
            row[f"sd_{label}"] = round(valid.std(ddof=1), 2) if len(valid) > 1 else None

        if "Q36_Value" in group.columns:
            row["NPS_Q36"] = nps_score(group["Q36_Value"])
        else:
            row["NPS_Q36"] = None

        rows.append(row)

    return pd.DataFrame(rows)


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Could not find input file: {INPUT_FILE}\n"
            "Place the anonymised trainee CSV at data/raw/trainees_anonymised.csv"
        )

    df = pd.read_csv(INPUT_FILE)

    if "Module Title" not in df.columns:
        raise ValueError(
            "Expected column 'Module Title' was not found. "
            "Please check the trainee CSV header."
        )

    df["Module"] = df["Module Title"].apply(extract_csp_code)

    # Exclude cross-module or non-module rows if present.
    df = df[df["Module"].notna()]
    df = df[df["Module"] != "CSP000"]

    module_summary = summarise_group(df, "Module")
    module_summary = module_summary.sort_values("Module")
    module_summary.to_csv(MODULE_OUTPUT, index=False)

    overall_summary = summarise_group(df)
    overall_summary.to_csv(OVERALL_OUTPUT, index=False)

    print(f"Wrote module summary to: {MODULE_OUTPUT}")
    print(f"Wrote overall summary to: {OVERALL_OUTPUT}")
    print()
    print(module_summary)


if __name__ == "__main__":
    main()