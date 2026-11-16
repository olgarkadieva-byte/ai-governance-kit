# AI Governance & Measurement Kit

Practical, framework-aligned tools for governing AI systems **and proving they deliver value**.

This repository is the machine-readable companion to the free
[AI Governance Starter Kit for Notion](https://smartailayer.notion.site/AI-Governance-Starter-Kit-3f0e47a9275080e480efd72a57a9442d).
The Notion template is for teams who want to start using it in an hour. This repo is for people who want
the same content as data, specs, and tested code they can plug into their own tools.

[![tests](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/actions/workflows/tests.yml/badge.svg)](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/actions/workflows/tests.yml)
![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)

## What's inside

| Folder | What it is |
| --- | --- |
| [`controls/`](controls/) | **34 AI controls** as CSV and JSON, including 8 for AI agents. Each is mapped to the **NIST AI RMF**, **ISO/IEC 42001** Annex A, and the **EU AI Act**, with implementation and verification guidance. Plus a generated [framework coverage report](controls/framework-coverage.md). |
| [`risk/`](risk/) | A five-dimension [risk scoring rubric](risk/scoring-rubric.md) (data sensitivity, business impact, autonomy, user exposure, human oversight) and an [EU AI Act tier screening guide](risk/eu-ai-act-tiers.md). |
| [`measurement/`](measurement/) | A platform-neutral [AI tool telemetry spec](measurement/telemetry-spec.md): event model, [JSON Schema](measurement/event-schema.json), [data dictionary](measurement/data-dictionary.csv), and metric definitions for adoption, time saved, and development payback. |
| [`aigov/`](aigov/) | A small Python package that implements the risk scoring and measurement formulas, with [tests](tests/). |
| [`examples/`](examples/) | Three worked AI systems (Low, Moderate, and Critical risk) with value metrics, risk scores, and EU AI Act tiers. |

## Why measurement and governance belong together

Most AI governance stops at "is it safe to launch?". The harder question is "is it worth running?".
This kit treats both as one workflow:

1. **Inventory** each AI system, including what it can do on its own (agent capabilities).
2. **Assess risk** on five dimensions, so one severe risk is never averaged away.
3. **Apply controls** matched to the risks, each mapped to recognized frameworks.
4. **Define value up front**: KPI, baseline, target, measurement method, and a guardrail metric that must not get worse.
5. **Monitor and review** on a schedule set by risk level, tracking KPI actuals against the baseline.

## Quick start

Requires Python 3.10 or later. No dependencies beyond the standard library (tests use `pytest`).

```bash
git clone https://github.com/olgarkadieva-byte/ai-governance-measurement-kit.git
cd ai-governance-measurement-kit

# Score one AI system
python -m aigov score --data 4 --impact 3 --autonomy 2 --exposure 4 --oversight 2
# AI system: Moderate (average 3.00, review every 6 months)

# Score the worked examples
python -m aigov score-file examples/ai-systems.json
# Meeting Notes Summarizer: Low (average 1.40, review every 12 months)
# Customer Support AI Assistant: Moderate (average 3.00, review every 6 months)
# AI Resume Screening Assistant: Critical — Review Required (average 4.20, review every 3 months)

# Run the tests
pip install pytest && python -m pytest
```

Use it as a library:

```python
from aigov import RiskScores, classify, adoption_rate, time_saved_hours, tasks_to_break_even

classify(RiskScores(data_sensitivity=5, business_impact=2, autonomy=1, user_exposure=1, human_oversight=1))
# RiskLevel.HIGH  (a single 5 is never averaged away)

adoption_rate(active_users=30, eligible_users=40)   # 75.0
time_saved_hours(25, 8, 100)                         # 28.3 hours
tasks_to_break_even(development_hours=120, minutes_saved_per_task=15)  # 480 tasks
```

## Using the control library

Load [`controls/ai-control-library.csv`](controls/ai-control-library.csv) into a spreadsheet, GRC tool, or
ticketing system. Fields:

| Field | Meaning |
| --- | --- |
| `id`, `name`, `category` | Control identifier, name, and one of six categories |
| `description` | What the control requires |
| `applicable_risk` | Which of the five risk dimensions it addresses |
| `implementation_guidance`, `verification_guidance` | How to put it in place and how to prove it works |
| `nist_ai_rmf` | Govern, Map, Measure, and/or Manage |
| `iso_iec_42001` | Related Annex A control area(s) |
| `eu_ai_act` | Related article(s) |

Edit [`controls/ai-control-library.json`](controls/ai-control-library.json) and run
`python tools/build_controls.py` to regenerate the CSV and the coverage report.

**Known gaps.** ISO/IEC 42001 A.2 (AI policy) is covered by the AI Policy Template in the Notion kit rather
than a control here, and A.4 (resources for AI systems) is not yet covered. Contributions welcome.

## Important

The framework mapping is indicative: it shows where a control helps, not that implementing it makes an
organization compliant or certifiable. Risk scores are decision-support indicators, not legal
classifications. Adapt everything to your own operations, laws, and policies. This is not legal advice.

## Related reading

- [How to Measure AI Tool Adoption, Productivity, and ROI](https://olgasoffice.substack.com/p/were-building-ai-faster-than-ever)
- [AI Agent Authorization: Why Consent Isn't Enough](https://olgasoffice.substack.com/p/consent-isnt-authorization-the-next)
- [AI Governance in 2026: Why Measurement Is the Hard Part](https://olgasoffice.substack.com/p/ai-governance-in-2026-the-hardest)
- More templates and articles at [smartailayer.com](https://smartailayer.com)

## License

[CC BY-NC 4.0](LICENSE): free to use, share, and adapt with attribution, not for commercial resale.

Created by [Olga A.](https://www.linkedin.com/in/olga-arkadieva-aigp-989677112/) · [Smart AI Layer](https://smartailayer.com)
