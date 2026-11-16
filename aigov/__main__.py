"""Command-line entry point.

Score one AI system:
    python -m aigov score --data 4 --impact 3 --autonomy 2 --exposure 4 --oversight 2

Score every system in a JSON file (see examples/ai-systems.json):
    python -m aigov score-file examples/ai-systems.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .risk import RiskScores, classify, review_interval_months


def _print_result(name: str, scores: RiskScores) -> None:
    level = classify(scores)
    avg = scores.average
    avg_text = f"{avg:.2f}" if avg is not None else "n/a"
    print(f"{name}: {level.value} (average {avg_text}, review every {review_interval_months(level)} months)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="aigov", description="Score AI system risk.")
    sub = parser.add_subparsers(dest="command", required=True)

    one = sub.add_parser("score", help="Score a single AI system")
    one.add_argument("--data", type=int, required=True, help="Data Sensitivity, 1-5")
    one.add_argument("--impact", type=int, required=True, help="Business Impact, 1-5")
    one.add_argument("--autonomy", type=int, required=True, help="Autonomy, 1-5")
    one.add_argument("--exposure", type=int, required=True, help="User Exposure, 1-5")
    one.add_argument("--oversight", type=int, required=True, help="Human Oversight, 1-5 (5 = least oversight)")

    many = sub.add_parser("score-file", help="Score every system in a JSON file")
    many.add_argument("path", type=Path)

    args = parser.parse_args(argv)

    if args.command == "score":
        scores = RiskScores(args.data, args.impact, args.autonomy, args.exposure, args.oversight)
        _print_result("AI system", scores)
        return 0

    systems = json.loads(args.path.read_text(encoding="utf-8"))
    for system in systems:
        _print_result(system["name"], RiskScores(**system["risk_scores"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
