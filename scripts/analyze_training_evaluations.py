#!/usr/bin/env python3
"""Compute CyberSecEval KPI summaries from anonymised trainee CSV exports."""

from __future__ import annotations

import argparse
import os
import re
from typing import Optional

import pandas as pd

CORE_ITEMS = {
    "Overall Satisfaction (Q15)": "Q15_Value",
    "Applied Practice (Q18)": "Q18_Value",
    "Knowledge Transfer (Q34)": "Q34_Value",
    "Job-role Relevance (Q33)": "Q33_Value",
    "Recommendation (Q36)": "Q36_Value",
}

MODULE_COL_CANDIDATES = ["Module Type", "Module", "ModuleCode", "Module Title"]


def find_module_col(df: pd.DataFrame) -> str:
    for col in MODULE_COL_CANDIDATES:
        if col in df.columns:
            return col
    # fallback: choose first column containing CSP-like values
    for col in df.columns:
        values = df[col].astype(str).head(50)
        if values.str.contains(r"CSP\d{3}", regex=True, na=False).any():
            return col
    raise ValueError("Could not identify module column. Expected one of: " + ", ".join(MODULE_COL_CANDIDATES))


def extract_module_code(value: object) -> Optional[str]:
    if pd.isna(value):
        return None
    match = re.search(r"CSP\d{3}", str(value))
    return match.group(0) if match else None


def to_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def summarise_item(series: pd.Series) -> dict:
    x = to_numeric(series).dropna()
    return {
        "Valid_N": int(x.shape[0]),
        "Mean": round(float(x.mean()), 4) if not x.empty else None,
        "SD": round(float(x.std(ddof=1)), 4) if x.shape[0] > 1 else None,
        "Median": round(float(x.median()), 4) if not x.empty else None,
    }


def nps(series: pd.Series) -> dict:
    x = to_numeric(series).dropna()
    if x.empty:
        return {"Valid_N": 0, "NPS": None, "Promoters_pct": None, "Detractors_pct": None}
    promoters = (x >= 9).mean() * 100
    detractors = (x <= 6).mean() * 100
    return {
        "Valid_N": int(x.shape[0]),
        "NPS": round(float(promoters - detractors), 4),
        "Promoters_pct": round(float(promoters), 4),
        "Detractors_pct": round(float(detractors), 4),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to anonymised trainee CSV")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--include-csp000", action="store_true", help="Include cross-module CSP000 rows")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    df = pd.read_csv(args.input)
    module_col = find_module_col(df)
    df["ModuleCode"] = df[module_col].apply(extract_module_code)

    if not args.include_csp000:
        df = df[df["ModuleCode"] != "CSP000"].copy()

    # Overall KPI summary
    overall_rows = []
    for metric, col in CORE_ITEMS.items():
        if col in df.columns:
            row = {"Metric": metric, **summarise_item(df[col])}
            overall_rows.append(row)
    if "Q36_Value" in df.columns:
        overall_rows.append({"Metric": "NPS (Q36)", **nps(df["Q36_Value"])})
    overall = pd.DataFrame(overall_rows)
    overall.to_csv(os.path.join(args.output, "overall_kpi_summary.csv"), index=False)

    # Module-level summary
    module_rows = []
    for module, group in sorted(df.groupby("ModuleCode", dropna=True), key=lambda kv: str(kv[0])):
        row = {"Module": module, "Responses_N": int(group.shape[0])}
        for metric, col in CORE_ITEMS.items():
            if col in group.columns:
                stats = summarise_item(group[col])
                short = col.replace("_Value", "")
                row[f"{short}_Valid_N"] = stats["Valid_N"]
                row[f"{short}_Mean"] = stats["Mean"]
                row[f"{short}_SD"] = stats["SD"]
        if "Q36_Value" in group.columns:
            row.update({f"Q36_{k}": v for k, v in nps(group["Q36_Value"]).items()})
        module_rows.append(row)
    module_summary = pd.DataFrame(module_rows)
    module_summary.to_csv(os.path.join(args.output, "module_kpi_summary.csv"), index=False)

    # Compact LaTeX table for paper
    table_cols = ["Module", "Responses_N", "Q15_Mean", "Q18_Mean", "Q34_Mean"]
    available = [c for c in table_cols if c in module_summary.columns]
    latex = module_summary[available].to_latex(index=False, escape=True, float_format="%.2f")
    with open(os.path.join(args.output, "module_kpi_summary_latex.tex"), "w", encoding="utf-8") as f:
        f.write(latex)

    print(f"Wrote outputs to {args.output}")


if __name__ == "__main__":
    main()
