---
layout: default
title: "AI Governance & Measurement Kit"
description: "Free, framework-aligned AI governance toolkit: 34 controls mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act, a risk scoring model, and an AI tool telemetry spec to measure adoption, time saved and ROI."
permalink: /
---

# AI Governance & Measurement Kit

Practical, framework-aligned tools for governing AI systems **and proving they deliver value**. Free to use.

| | |
| --- | --- |
| [**AI Control Library**](controls.html) | 34 controls, including 8 for AI agents, mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act. Download as CSV or JSON. |
| [**AI Risk Scoring Rubric**](risk-scoring.html) | Score any AI system on five dimensions. One severe risk is never averaged away. |
| [**EU AI Act Tier Screening**](eu-ai-act-tiers.html) | Is your AI system prohibited, high-risk, subject to transparency rules, or minimal risk? |
| [**AI Tool Telemetry Spec**](telemetry-spec.html) | Measure AI adoption, task success, time saved, and development payback, without collecting prompts. |

## Two ways to use it

- **No-code:** duplicate the free [AI Governance Starter Kit for Notion](https://smartailayer.notion.site/AI-Governance-Starter-Kit-3f0e47a9275080e480efd72a57a9442d). Set up in about an hour.
- **Data and code:** use the [GitHub repository](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit) for CSV and JSON files, a JSON Schema, and a tested Python package.

```bash
pip install pytest
git clone https://github.com/olgarkadieva-byte/ai-governance-measurement-kit.git && cd ai-governance-measurement-kit
python -m aigov score --data 4 --impact 3 --autonomy 2 --exposure 4 --oversight 2
# AI system: Moderate (average 3.00, review every 6 months)
```

## Why measurement and governance belong together

Most AI governance stops at "is it safe to launch?". The harder question is "is it worth running?". This kit treats both as one workflow:
inventory each AI system, assess its risk, apply controls mapped to recognized frameworks, define its value up front with a baseline,
target and guardrail metric, then review it on a schedule set by its risk level.

## Related reading

- [How to Measure AI Tool Adoption, Productivity, and ROI](https://olgasoffice.substack.com/p/were-building-ai-faster-than-ever)
- [AI Agent Authorization: Why Consent Isn't Enough](https://olgasoffice.substack.com/p/consent-isnt-authorization-the-next)
- [AI Governance in 2026: Why Measurement Is the Hard Part](https://olgasoffice.substack.com/p/ai-governance-in-2026-the-hardest)
- [When Identity Is No Longer Human](https://olgasoffice.substack.com/p/when-identity-is-no-longer-human)

Created by [Olga Arkadieva](https://www.linkedin.com/in/olga-arkadieva-aigp-989677112/), AIGP · [Smart AI Layer](https://smartailayer.com) ·
Licensed [CC BY-NC 4.0](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/blob/main/LICENSE). Not legal advice.
