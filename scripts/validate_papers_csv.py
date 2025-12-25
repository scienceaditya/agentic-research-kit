#!/usr/bin/env python3
"""
Validate data/papers.csv for required columns and missing fields.

Usage:
  python3 scripts/validate_papers_csv.py data/papers.csv

Exit codes:
  0 = OK
  1 = Validation errors
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = [
    "paper_id",
    "year",
    "citation",
    "doi_or_url",
    "system",
    "topic_tags",
    "assumption_targeted",
    "key_findings_1",
    "key_findings_2",
    "methods",
    "model_system",
    "data_type",
    "notes",
    "confidence",
    "added_by",
    "date_added",
]

# Fields that should usually be present for a useful entry.
# You can relax or expand this list later.
REQUIRED_NONEMPTY_FIELDS = [
    "paper_id",
    "year",
    "citation",
    "topic_tags",
    "assumption_targeted",
    "date_added",
]

ALLOWED_ASSUMPTIONS = {
    "pathway_independence",
    "static_complexes",
    "single_defect_disease",
    "general",
}

ALLOWED_CONFIDENCE = {"low", "medium", "high", ""}


def error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"[WARN] {msg}", file=sys.stderr)


def validate_header(header: list[str]) -> list[str]:
    missing = [c for c in REQUIRED_COLUMNS if c not in header]
    extra = [c for c in header if c not in REQUIRED_COLUMNS]

    if missing:
        error(f"Missing required columns: {missing}")
    if extra:
        warn(f"Unexpected columns present (allowed, but check typos): {extra}")

    return missing


def validate_row(row_num: int, row: dict[str, str]) -> int:
    errs = 0

    # Required non-empty fields
    for field in REQUIRED_NONEMPTY_FIELDS:
        val = (row.get(field) or "").strip()
        if not val:
            error(f"Row {row_num}: missing value for '{field}'")
            errs += 1

    # Year should be an integer if present
    year = (row.get("year") or "").strip()
    if year:
        try:
            y = int(year)
            if y < 1900 or y > 2100:
                warn(f"Row {row_num}: year '{year}' looks unusual")
        except ValueError:
            error(f"Row {row_num}: year '{year}' is not an integer")
            errs += 1

    # assumption_targeted should be from allowed set (if present)
    assumption = (row.get("assumption_targeted") or "").strip()
    if assumption and assumption not in ALLOWED_ASSUMPTIONS:
        error(
            f"Row {row_num}: assumption_targeted '{assumption}' not in {sorted(ALLOWED_ASSUMPTIONS)}"
        )
        errs += 1

    # confidence should be low/medium/high (or blank)
    confidence = (row.get("confidence") or "").strip().lower()
    if confidence not in ALLOWED_CONFIDENCE:
        error(
            f"Row {row_num}: confidence '{confidence}' not in {sorted(ALLOWED_CONFIDENCE - {''})}"
        )
        errs += 1

    # topic_tags should be semicolon-separated (soft check)
    tags = (row.get("topic_tags") or "").strip()
    if tags and "," in tags:
        warn(f"Row {row_num}: topic_tags contains commas. Prefer semicolons.")

    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "csv_path",
        nargs="?",
        default="data/papers.csv",
        help="Path to papers.csv (default: data/papers.csv)",
    )
    args = ap.parse_args()

    path = Path(args.csv_path)
    if not path.exists():
        error(f"File not found: {path}")
        return 1

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            error("CSV has no header row.")
            return 1

        header = [h.strip() for h in reader.fieldnames]
        missing_cols = validate_header(header)
        if missing_cols:
            return 1

        total_errs = 0
        row_count = 0
        for i, row in enumerate(reader, start=2):  # header is line 1
            row_count += 1

            # Skip completely empty rows
            if all(((v or "").strip() == "") for v in row.values()):
                continue

            total_errs += validate_row(i, row)

        if row_count == 0:
            warn("No rows found (header only). That is fine for now.")

        if total_errs:
            error(f"Validation failed with {total_errs} error(s).")
            return 1

    print("OK: papers.csv looks valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
