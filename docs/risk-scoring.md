---
layout: default
title: "AI Risk Scoring Rubric: score AI systems on five dimensions"
description: "Free AI risk assessment rubric: score data sensitivity, business impact, autonomy, user exposure and human oversight from 1 to 5 to get a Low, Moderate, High or Critical risk level."
permalink: /risk-scoring.html
---

# AI Risk Scoring Rubric: score AI systems on five dimensions

Score each AI system on five questions, from **1 (lowest risk)** to **5 (highest risk)**.
Score what the system can actually do and access today, not just what it is intended to do.

The same rules are implemented in [`aigov/risk.py`](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/blob/main/aigov/risk.py) and tested in
[`tests/test_risk.py`](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/blob/main/tests/test_risk.py).

## 1. Data Sensitivity: what is the most sensitive data the AI can access?

| Score | Meaning |
| --- | --- |
| 1 | Public information only. No personal or confidential data. |
| 2 | Routine internal business information with limited sensitivity. |
| 3 | Confidential business information or limited personal data. |
| 4 | Sensitive personal information, financial records, or commercially sensitive data. |
| 5 | Highly restricted information, such as credentials, extensive sensitive personal data, or data whose exposure could cause severe harm. |

## 2. Business Impact: what is the worst realistic result if the AI gets it wrong?

| Score | Meaning |
| --- | --- |
| 1 | Negligible. Errors are easily corrected with no real consequences. |
| 2 | Minor disruption, limited rework, or small productivity losses. |
| 3 | Noticeable disruption, customer dissatisfaction, financial loss, or reputational damage needing management attention. |
| 4 | Significant financial loss, serious customer harm, or substantial legal or regulatory exposure. |
| 5 | Severe or irreversible harm, major regulatory consequences, or threats to health, safety, or people's rights. |

## 3. Autonomy: how much can the AI do without a person approving it?

| Score | Meaning |
| --- | --- |
| 1 | Gives information or suggestions only. A person decides whether to use them. |
| 2 | Drafts content or recommendations that a person approves before use. |
| 3 | Performs limited, predefined actions within approved limits, under supervision. |
| 4 | Carries out important actions or decisions on its own, within set permissions. |
| 5 | Plans and carries out multi-step actions with broad permissions, affecting other systems, money, data, or people. |

## 4. User Exposure: who uses it or is affected by it?

| Score | Meaning |
| --- | --- |
| 1 | A small group of trained internal users. |
| 2 | One internal team or department. |
| 3 | Several departments or the whole organization. |
| 4 | Customers, partners, or other external people. |
| 5 | The public or a large external group, including vulnerable people or important decisions about them. |

## 5. Human Oversight: how well can people check and stop the AI?

For this question only, a higher score means **less** oversight and therefore more risk.

| Score | Meaning |
| --- | --- |
| 1 | A qualified person reviews every important output or action before it takes effect. |
| 2 | A person approves significant decisions, with clear escalation and the ability to intervene. |
| 3 | People review outputs periodically, but not every important action is approved first. |
| 4 | Review is limited or happens only after the AI has acted. |
| 5 | No meaningful oversight. AI actions cannot be reliably reviewed, stopped, or reversed. |

## Overall risk level

Rules are applied in this order:

| Overall risk | When it applies | What to do | Review every |
| --- | --- | --- | --- |
| Not Assessed | One or more scores are missing. | Complete all five scores before deciding anything. | 3 months |
| Critical — Review Required | Business Impact is 5, **or** Autonomy and Human Oversight are both 4 or more. | Escalate for specialist review. Do not launch or expand until risks and controls are formally approved. | 3 months |
| High | Any single score is 5, **or** the average is 4 or more. | Formal risk review with privacy, security, or compliance input; document safeguards; approve before launch. | 3 months |
| Moderate | Average from 3 to just under 4. | Owner review, check relevant controls, set up monitoring. | 6 months |
| Low | Average below 3. | Assign an owner, apply basic safeguards, review once a year. | 12 months |

Design choices:

- **One severe risk is never averaged away.** Any score of 5 makes the result at least High.
- **Acting alone with weak oversight is treated as Critical,** because that combination is where AI agents cause the most damage.
- A Low result does not remove the need for basic privacy, security, or legal checks.
- Reassess whenever the system's data, users, permissions, or safeguards change significantly.

This is a screening tool, not a legal classification or certification.
