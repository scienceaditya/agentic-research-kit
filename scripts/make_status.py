#!/usr/bin/env python3
"""
Generate a simple STATUS.md from a papers CSV.

Usage:
  python3 scripts/make_status.py --papers data/papers.csv --out STATUS.md
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

REQUIRED_COLUMNS = [
    "citation_key",
    "title",
    "authors",
    "year",
    "venue",
    "doi",
    "url",
    "tags",
    "why_included",
    "evidence_level",
    "status",
    "notes",
    "full_citation",
]

ALLOW_EMPTY = {"doi", "url", "notes", "tags"}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no header.")
        missing = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(missing)}")
        return list(reader)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--papers", required=True, help="Path to papers.csv")
    p.add_argument("--out", required=True, help="Output markdown path, e.g. STATUS.md")
    args = p.parse_args()

    papers_path = Path(args.papers)
    out_path = Path(args.out)

    rows = load_rows(papers_path)
    total = len(rows)

    missing_counter: Counter[str] = Counter()
    empty_rows = 0

    for r in rows:
        row_missing = 0
        for col in REQUIRED_COLUMNS:
            v = (r.get(col) or "").strip()
            if (not v) and (col not in ALLOW_EMPTY):
                missing_counter[col] += 1
                row_missing += 1
        if row_missing:
            empty_rows += 1

    evidence_counts = Counter((r.get("evidence_level") or "").strip() for r in rows if (r.get("evidence_level") or "").strip())
    status_counts = Counter((r.get("status") or "").strip() for r in rows if (r.get("status") or "").strip())

    now = datetime.now().strftime("%Y-%m-%d %H:%M %Z").strip()
    lines = []
    lines.append("# Repo status")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append("")
    lines.append("## Papers index")
    lines.append(f"- Total entries: {total}")
    lines.append(f"- Entries with missing required fields: {empty_rows}")
    lines.append("")

    if missing_counter:
        lines.append("## Missing fields summary")
        for col, n in missing_counter.most_common():
            lines.append(f"- {col}: {n}")
        lines.append("")

    if evidence_counts:
        lines.append("## Evidence level")
        for k, n in evidence_counts.most_common():
            lines.append(f"- {k}: {n}")
        lines.append("")

    if status_counts:
        lines.append("## Status")
        for k, n in status_counts.most_common():
            lines.append(f"- {k}: {n}")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
