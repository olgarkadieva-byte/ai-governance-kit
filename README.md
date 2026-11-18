# AI Governance Kit

Practical, framework-aligned tools to **govern AI systems**: know what you run, how risky it is, and which safeguards protect it.

**Website:** [olgarkadieva-byte.github.io/ai-governance-kit](https://olgarkadieva-byte.github.io/ai-governance-kit/)

This repository is the machine-readable companion to the free
[AI Governance Starter Kit for Notion](https://smartailayer.notion.site/AI-Governance-Starter-Kit-3f0e47a9275080e480efd72a57a9442d).
The Notion template is for teams who want to start using it in an hour. This repo is for people who want
the same content as data and tested code they can plug into their own tools.

[![tests](https://github.com/olgarkadieva-byte/ai-governance-kit/actions/workflows/tests.yml/badge.svg)](https://github.com/olgarkadieva-byte/ai-governance-kit/actions/workflows/tests.yml)
![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)

## What's inside

| Folder | What it is |
| --- | --- |
| [`controls/`](controls/) | **34 AI controls** as CSV and JSON, including 8 for AI agents. Each is mapped to the **NIST AI RMF**, **ISO/IEC 42001** Annex A, and the **EU AI Act**, with implementation and verification guidance. Plus a generated [framework coverage report](controls/framework-coverage.md). |
| [`risk/`](risk/) | A five-dimension [risk scoring rubric](risk/scoring-rubric.md) (data sensitivity, business impact, autonomy, user exposure, human oversight) and an [EU AI Act tier screening guide](risk/eu-ai-act-tiers.md). |
| [`aigov/`](aigov/) | A small Python package that implements the risk scoring, with [tests](tests/). |
| [`examples/`](examples/) | Three worked AI system inventory records (Low, Moderate, and Critical risk) with risk scores and EU AI Act tiers. |

## The governance workflow

1. **Inventory** each AI system, including what it can do on its own (agent capabilities) and the outcome it is meant to deliver.
2. **Assess risk** on five dimensions, so one severe risk is never averaged away.
3. **Apply controls** matched to the risks, each mapped to recognized frameworks.
4. **Assign accountability**: an owner, an approval record, and a policy.
5. **Review** on a schedule set by risk level.

## Governance, then measurement

This kit answers "is this AI system safe, accountable and under control?". To answer "what did it actually change, and
is it worth what it costs?", use the companion tool **[AI Impact Measurement](https://github.com/olgarkadieva-byte/ai-impact-measurement)**
([live demo](https://olgarkadieva-byte.github.io/ai-impact-measurement/)): adoption, time saved, cost and ROI measured against a
control group, with a keep / fix / retire verdict for every AI tool.

## Quick start

Requires Python 3.10 or later. No dependencies beyond the standard library (tests use `pytest`).

```bash
git clone https://github.com/olgarkadieva-byte/ai-governance-kit.git
cd ai-governance-kit

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
from aigov import RiskScores, classify, review_interval_months

level = classify(RiskScores(data_sensitivity=5, business_impact=2, autonomy=1, user_exposure=1, human_oversight=1))
# RiskLevel.HIGH  (a single 5 is never averaged away)
review_interval_months(level)  # 3 (months)
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

- [AI Agent Authorization: Why Consent Isn't Enough](https://olgasoffice.substack.com/p/consent-isnt-authorization-the-next)
- [AI Governance in 2026: Why Measurement Is the Hard Part](https://olgasoffice.substack.com/p/ai-governance-in-2026-the-hardest)
- More templates and articles at [smartailayer.com](https://smartailayer.com)

## License

[CC BY-NC 4.0](LICENSE): free to use, share, and adapt with attribution, not for commercial resale.

Created by [Olga Arkadieva](https://www.linkedin.com/in/olga-arkadieva-aigp-989677112/) · [Smart AI Layer](https://smartailayer.com)
