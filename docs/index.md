---
layout: default
title: "AI Governance Kit"
description: "Free, framework-aligned AI governance toolkit: 34 AI controls (8 for AI agents) mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act, a five-dimension AI risk scoring model, and an EU AI Act tier screening guide."
permalink: /
---

# AI Governance Kit

Practical, framework-aligned tools to govern AI systems: know what you run, how risky it is, and which safeguards protect it. Free to use.

| | |
| --- | --- |
| [**AI Control Library**](controls.html) | 34 controls, including 8 for AI agents, mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act. Download as CSV or JSON. |
| [**AI Risk Scoring Rubric**](risk-scoring.html) | Score any AI system on five dimensions. One severe risk is never averaged away. |
| [**EU AI Act Tier Screening**](eu-ai-act-tiers.html) | Is your AI system prohibited, high-risk, subject to transparency rules, or minimal risk? |

## Two ways to use it

- **No-code:** duplicate the free [AI Governance Starter Kit for Notion](https://smartailayer.notion.site/AI-Governance-Starter-Kit-3f0e47a9275080e480efd72a57a9442d). Set up in about an hour.
- **Data and code:** use the [GitHub repository](https://github.com/olgarkadieva-byte/ai-governance-kit) for CSV and JSON files and a tested Python package.

```bash
git clone https://github.com/olgarkadieva-byte/ai-governance-kit.git && cd ai-governance-kit
python -m aigov score --data 4 --impact 3 --autonomy 2 --exposure 4 --oversight 2
# AI system: Moderate (average 3.00, review every 6 months)
```

## Governance, then measurement

This kit answers "is this AI system safe, accountable and under control?". To answer "what did it actually change, and is it worth
what it costs?", use the companion tool [AI Impact Measurement](https://olgarkadieva-byte.github.io/ai-impact-measurement/): adoption, time saved, cost and ROI against a control
group, with a keep / fix / retire verdict for every AI tool. For AI agents, [AgentMeter](https://olgarkadieva-byte.github.io/agentmeter/) tests each agent
version before release (task success, reliability, tool use, permission-policy violations, cost and latency) with a
Ship / Hold / Block release gate for CI.

## Related reading

- [AI Agent Authorization: Why Consent Isn't Enough](https://olgasoffice.substack.com/p/consent-isnt-authorization-the-next)
- [AI Governance in 2026: Why Measurement Is the Hard Part](https://olgasoffice.substack.com/p/ai-governance-in-2026-the-hardest)
- [When Identity Is No Longer Human](https://olgasoffice.substack.com/p/when-identity-is-no-longer-human)

Created by [Olga Arkadieva](https://www.linkedin.com/in/olga-arkadieva-aigp-989677112/), AIGP · [Smart AI Layer](https://smartailayer.com) ·
Licensed [CC BY-NC 4.0](https://github.com/olgarkadieva-byte/ai-governance-kit/blob/main/LICENSE). Not legal advice.
