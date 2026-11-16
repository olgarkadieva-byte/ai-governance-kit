"""Build the CSV and coverage tables from controls/ai-control-library.json.

Run from the repository root:
    python tools/build_controls.py
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "controls" / "ai-control-library.json"
CSV_OUT = ROOT / "controls" / "ai-control-library.csv"
COVERAGE_OUT = ROOT / "controls" / "framework-coverage.md"

LIST_FIELDS = ["applicable_risk", "nist_ai_rmf", "iso_iec_42001", "eu_ai_act"]
COLUMNS = [
    "id",
    "name",
    "category",
    "description",
    "applicable_risk",
    "implementation_guidance",
    "verification_guidance",
    "nist_ai_rmf",
    "iso_iec_42001",
    "eu_ai_act",
]


def _sort_key(label: str) -> tuple:
    """Sort 'A.10 ...' after 'A.9 ...' and 'Art. 50' after 'Art. 9'."""
    head = label.split(" ")[0] if not label.startswith("Art.") else label.split(" ")[1]
    number = "".join(ch for ch in head if ch.isdigit() or ch == ".").strip(".")
    parts = [int(p) for p in number.split(".") if p.isdigit()]
    return (parts, label)


def main() -> None:
    controls = json.loads(SOURCE.read_text(encoding="utf-8"))
    controls.sort(key=lambda c: c["id"])

    with CSV_OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        for c in controls:
            row = {k: c[k] for k in COLUMNS}
            for k in LIST_FIELDS:
                row[k] = "; ".join(c[k])
            writer.writerow(row)

    lines = [
        "# Framework coverage",
        "",
        f"Generated from `ai-control-library.json` ({len(controls)} controls) by `tools/build_controls.py`.",
        "The mapping is indicative: it shows where a control helps, not that implementing it makes an",
        "organization compliant or certifiable.",
        "",
    ]
    for field, title in [
        ("nist_ai_rmf", "NIST AI RMF functions"),
        ("iso_iec_42001", "ISO/IEC 42001 Annex A areas"),
        ("eu_ai_act", "EU AI Act articles"),
    ]:
        counts = Counter(label for c in controls for label in c[field])
        if field == "nist_ai_rmf":
            order = [x for x in ["Govern", "Map", "Measure", "Manage"] if x in counts]
        else:
            order = sorted(counts, key=_sort_key)
        lines += [f"## {title}", "", "| Item | Controls | IDs |", "| --- | ---: | --- |"]
        for label in order:
            ids = ", ".join(c["id"] for c in controls if label in c[field])
            lines.append(f"| {label} | {counts[label]} | {ids} |")
        lines.append("")

    by_category = Counter(c["category"] for c in controls)
    lines += ["## Controls by category", "", "| Category | Controls |", "| --- | ---: |"]
    for cat, n in sorted(by_category.items()):
        lines.append(f"| {cat} | {n} |")
    lines.append("")

    COVERAGE_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {CSV_OUT.relative_to(ROOT)} and {COVERAGE_OUT.relative_to(ROOT)} for {len(controls)} controls")


if __name__ == "__main__":
    main()
