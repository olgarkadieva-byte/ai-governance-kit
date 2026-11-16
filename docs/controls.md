---
layout: default
title: "AI Control Library: 34 controls mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act"
description: "Free library of 34 AI governance controls, including 8 for AI agents, each mapped to NIST AI RMF, ISO/IEC 42001 Annex A and EU AI Act articles. Download as CSV or JSON."
permalink: /controls.html
---


# AI Control Library

34 practical AI governance controls, including 8 for AI agents. Each control is mapped to the **NIST AI Risk Management Framework**, **ISO/IEC 42001** Annex A, and the **EU AI Act**, with implementation and verification guidance.

**Download:** [CSV](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/blob/main/controls/ai-control-library.csv) · [JSON](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/blob/main/controls/ai-control-library.json) · [Framework coverage report](https://github.com/olgarkadieva-byte/ai-governance-measurement-kit/blob/main/controls/framework-coverage.md) · [Use it in Notion](https://smartailayer.notion.site/AI-Governance-Starter-Kit-3f0e47a9275080e480efd72a57a9442d)

The mapping is indicative: it shows where a control helps, not that implementing it makes an organization compliant or certifiable.

## AI Agent Authorization & Action Boundaries

### AGENT-001 Action Allowlist

Define which actions an AI agent may execute and explicitly prohibit others.

- **How to implement:** Configure allowlisted actions and test denied operations.
- **How to verify:** Action policy and denial tests
- **Addresses risk:** Autonomy, Business Impact, Human Oversight
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.6 AI system life cycle, A.9 Use of AI systems
- **EU AI Act:** Art. 14 Human oversight, Art. 15 Accuracy, robustness & cybersecurity

### AGENT-002 Transaction Limits

Set thresholds for financial, customer-impacting, or irreversible actions.

- **How to implement:** Require additional approval above defined thresholds.
- **How to verify:** Threshold configuration and test cases
- **Addresses risk:** Autonomy, Business Impact, Human Oversight
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.9 Use of AI systems
- **EU AI Act:** Art. 14 Human oversight

### AGENT-003 Identity and Delegated Authority

Verify the requesting user and scope agent authority to that user's permissions.

- **How to implement:** Bind actions to authorized principals and validate permission checks.
- **How to verify:** Authorization design and access tests
- **Addresses risk:** Autonomy, Data Sensitivity, Human Oversight
- **NIST AI RMF:** Govern, Manage
- **ISO/IEC 42001:** A.3 Internal organization, A.9 Use of AI systems
- **EU AI Act:** Art. 14 Human oversight, Art. 15 Accuracy, robustness & cybersecurity

### AGENT-004 External Action Confirmation

Require explicit confirmation before high-impact external messages, changes, or transactions.

- **How to implement:** Introduce confirmation checkpoints for consequential actions.
- **How to verify:** Confirmation flow and QA results
- **Addresses risk:** Autonomy, Business Impact, Human Oversight
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.9 Use of AI systems
- **EU AI Act:** Art. 14 Human oversight

### AGENT-005 Agent Execution Traceability

Record agent tool calls, approvals, and action outcomes for investigation.

- **How to implement:** Log trace IDs and outcomes without unnecessary sensitive content.
- **How to verify:** Trace samples and logging specification
- **Addresses risk:** Autonomy, Business Impact, Human Oversight
- **NIST AI RMF:** Measure, Manage
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 12 Record-keeping, Art. 26 Deployer obligations

### AGENT-006 Runaway Loop and Budget Limits

Cap how many steps, tool calls, tokens, and dollars an AI agent can spend on one task so it cannot loop or run up costs unchecked.

- **How to implement:** Set per-task limits on steps, tool calls, run time, and spend; stop the agent and alert its owner when a limit is hit.
- **How to verify:** Configured limits and a test run that triggers each limit
- **Addresses risk:** Autonomy, Business Impact
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.9 Use of AI systems
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

### AGENT-007 Agent Memory and Context Hygiene

Control what an AI agent remembers between tasks and what documents, emails, or web pages it reads, so untrusted or sensitive content does not carry over.

- **How to implement:** Define what the agent may store and for how long; separate memory per user or customer; treat retrieved content as untrusted data, never as instructions.
- **How to verify:** Memory policy and a test showing one user's data does not appear in another user's session
- **Addresses risk:** Autonomy, Data Sensitivity
- **NIST AI RMF:** Map, Manage
- **ISO/IEC 42001:** A.7 Data for AI systems
- **EU AI Act:** Art. 10 Data governance, Art. 15 Accuracy, robustness & cybersecurity

### AGENT-008 Sub-Agent and Delegation Limits

When an AI agent hands work to other agents or tools, the receiving agent gets no more permission than the original agent, and the chain of delegation is recorded.

- **How to implement:** Pass down only the permissions each sub-task needs; limit how many levels deep delegation can go; log which agent acted on whose behalf.
- **How to verify:** Delegation policy and a log showing a full delegation chain for one task
- **Addresses risk:** Autonomy, Human Oversight, Business Impact
- **NIST AI RMF:** Govern, Manage
- **ISO/IEC 42001:** A.9 Use of AI systems
- **EU AI Act:** Art. 12 Record-keeping, Art. 14 Human oversight

## Human Oversight & Accountability

### GOV-001 Named Accountable Owner

Assign a responsible business owner to each AI use case.

- **How to implement:** Record owner, decision authority, and escalation contact.
- **How to verify:** Approved ownership register
- **Addresses risk:** Business Impact, Autonomy, Human Oversight
- **NIST AI RMF:** Govern
- **ISO/IEC 42001:** A.3 Internal organization
- **EU AI Act:** Art. 26 Deployer obligations

### GOV-002 Human Approval Gates

Require meaningful human approval before defined consequential AI actions.

- **How to implement:** Identify approval thresholds and block execution without authorization.
- **How to verify:** Approval workflow and test evidence
- **Addresses risk:** Autonomy, Business Impact, Human Oversight
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.9 Use of AI systems
- **EU AI Act:** Art. 14 Human oversight

### GOV-003 Human Override and Shutdown

Provide ways to interrupt, override, or disable AI actions when necessary.

- **How to implement:** Implement kill switch or equivalent controls and rehearse intervention.
- **How to verify:** Shutdown test and runbook
- **Addresses risk:** Autonomy, Business Impact, Human Oversight
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.9 Use of AI systems
- **EU AI Act:** Art. 14 Human oversight

### GOV-004 Escalation for Uncertain Outputs

Route low-confidence, ambiguous, or high-stakes cases to qualified humans.

- **How to implement:** Define escalation triggers and measure handling performance.
- **How to verify:** Escalation rules and case samples
- **Addresses risk:** Business Impact, User Exposure, Human Oversight
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.9 Use of AI systems
- **EU AI Act:** Art. 14 Human oversight

### GOV-005 Decision and Accountability Record

Document significant AI-assisted decisions, reviewers, and approvals.

- **How to implement:** Log decision rationale and approval evidence appropriate to the use case.
- **How to verify:** Decision log and approval records
- **Addresses risk:** Business Impact, Autonomy, Human Oversight
- **NIST AI RMF:** Govern
- **ISO/IEC 42001:** A.3 Internal organization, A.6 AI system life cycle
- **EU AI Act:** Art. 11 Technical documentation, Art. 12 Record-keeping

### GOV-006 AI Disclosure to People

Tell people when they are interacting with an AI system or seeing AI-generated content.

- **How to implement:** Add a clear notice to AI chat interfaces and label AI-generated images, audio, video, or text published to the public.
- **How to verify:** Screenshots of the notice and labels in each customer-facing channel
- **Addresses risk:** User Exposure
- **NIST AI RMF:** Govern, Manage
- **ISO/IEC 42001:** A.8 Information for interested parties
- **EU AI Act:** Art. 50 Transparency to people

## Monitoring, Incident Response & Auditability

### MON-001 Operational Monitoring

Track AI errors, failures, usage anomalies, and service reliability.

- **How to implement:** Define alerts, thresholds, and response ownership.
- **How to verify:** Monitoring dashboard and alert tests
- **Addresses risk:** Business Impact, Autonomy, User Exposure
- **NIST AI RMF:** Measure, Manage
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 26 Deployer obligations, Art. 72 Post-market monitoring

### MON-002 Safety and Quality Monitoring

Sample production outcomes for harmful, incorrect, or policy-violating behavior.

- **How to implement:** Review representative outputs and trend failure rates.
- **How to verify:** Quality review records and trend report
- **Addresses risk:** User Exposure, Autonomy, Business Impact
- **NIST AI RMF:** Measure
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity, Art. 72 Post-market monitoring

### MON-003 AI Incident Response

Establish triage, containment, escalation, and recovery procedures for AI incidents.

- **How to implement:** Add AI scenarios to incident plans and conduct a tabletop exercise.
- **How to verify:** Incident playbook and exercise notes
- **Addresses risk:** User Exposure, Business Impact, Autonomy
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.3 Internal organization, A.8 Information for interested parties
- **EU AI Act:** Art. 26 Deployer obligations, Art. 73 Serious incident reporting

### MON-004 Periodic Risk Reassessment

Reassess risk after material changes and at a defined review interval.

- **How to implement:** Trigger reviews for model, data, tool, scope, and deployment changes.
- **How to verify:** Review schedule and completed reassessments
- **Addresses risk:** Data Sensitivity, Business Impact, Autonomy, User Exposure, Human Oversight
- **NIST AI RMF:** Map, Manage
- **ISO/IEC 42001:** A.5 Impact assessment
- **EU AI Act:** Art. 9 Risk management

## Privacy & Data Protection

### PRIV-001 Data Minimization

Limit collection, processing, and retention to information necessary for the approved AI purpose.

- **How to implement:** Document approved data fields, remove unnecessary inputs, and periodically review access.
- **How to verify:** Approved data inventory and minimization review
- **Addresses risk:** Data Sensitivity
- **NIST AI RMF:** Map, Manage
- **ISO/IEC 42001:** A.7 Data for AI systems
- **EU AI Act:** Art. 10 Data governance

### PRIV-002 Personal Data Handling

Define lawful and authorized handling of personal data across prompts, outputs, logs, and vendors.

- **How to implement:** Map personal-data flows and verify handling requirements with privacy counsel.
- **How to verify:** Data flow map and privacy review
- **Addresses risk:** Data Sensitivity, User Exposure
- **NIST AI RMF:** Map, Manage
- **ISO/IEC 42001:** A.7 Data for AI systems
- **EU AI Act:** Art. 10 Data governance

### PRIV-003 Retention and Deletion

Define and enforce retention periods and deletion processes for AI inputs, outputs, and logs.

- **How to implement:** Set retention schedules and test deletion where supported.
- **How to verify:** Retention policy and deletion test records
- **Addresses risk:** Data Sensitivity
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.7 Data for AI systems
- **EU AI Act:** Art. 10 Data governance

### PRIV-004 Vendor Data Use Review

Review provider terms, training use, subprocessors, and data processing safeguards before approval.

- **How to implement:** Complete vendor review and document permitted data uses.
- **How to verify:** Vendor assessment and approved terms
- **Addresses risk:** Data Sensitivity, Business Impact
- **NIST AI RMF:** Govern, Map
- **ISO/IEC 42001:** A.10 Third-party relationships
- **EU AI Act:** Art. 13 Transparency to deployers, Art. 26 Deployer obligations

### PRIV-005 Sensitive Data Redaction

Remove or mask sensitive data before AI processing where practical.

- **How to implement:** Implement redaction rules and test for leaks and over-redaction.
- **How to verify:** Redaction test results and configuration
- **Addresses risk:** Data Sensitivity
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.7 Data for AI systems
- **EU AI Act:** Art. 10 Data governance

### PRIV-006 AI Data Access Restrictions

Limit the data each AI system can read to what its approved purpose requires, using existing data permissions.

- **How to implement:** Give each AI system read access only to approved data sources through existing permission controls; block restricted data by default.
- **How to verify:** Access configuration and a test showing restricted data is not returned
- **Addresses risk:** Data Sensitivity, Autonomy
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.7 Data for AI systems
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

## Quality, Reliability & Testing

### QUAL-001 Use Case Acceptance Criteria

Define measurable success, safety, and failure criteria before deployment.

- **How to implement:** Set task-level acceptance thresholds and test against representative cases.
- **How to verify:** Acceptance criteria and evaluation report
- **Addresses risk:** Business Impact, User Exposure, Human Oversight
- **NIST AI RMF:** Map, Measure
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 9 Risk management, Art. 15 Accuracy, robustness & cybersecurity

### QUAL-002 Representative Evaluation Set

Test AI against realistic, diverse, and challenging scenarios relevant to intended use.

- **How to implement:** Maintain versioned evaluation cases including edge cases.
- **How to verify:** Evaluation dataset inventory and results
- **Addresses risk:** User Exposure, Business Impact, Data Sensitivity
- **NIST AI RMF:** Measure
- **ISO/IEC 42001:** A.6 AI system life cycle, A.7 Data for AI systems
- **EU AI Act:** Art. 10 Data governance, Art. 15 Accuracy, robustness & cybersecurity

### QUAL-003 Output Accuracy and Grounding

Assess factual correctness and grounding for relevant AI outputs.

- **How to implement:** Measure unsupported claims and introduce validation where appropriate.
- **How to verify:** Accuracy report and sample audits
- **Addresses risk:** Business Impact, User Exposure, Human Oversight
- **NIST AI RMF:** Measure
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

### QUAL-004 Bias and Fairness Evaluation

Evaluate harmful performance differences across relevant populations or scenarios.

- **How to implement:** Define applicable fairness measures and review subgroup outcomes.
- **How to verify:** Fairness evaluation and remediation log
- **Addresses risk:** Business Impact, User Exposure, Data Sensitivity
- **NIST AI RMF:** Measure
- **ISO/IEC 42001:** A.5 Impact assessment, A.7 Data for AI systems
- **EU AI Act:** Art. 10 Data governance

### QUAL-005 Regression Testing

Retest quality and safety after model, prompt, data, or tool changes.

- **How to implement:** Run versioned tests before production changes and compare results.
- **How to verify:** Regression reports and release approvals
- **Addresses risk:** Business Impact, Autonomy, User Exposure
- **NIST AI RMF:** Measure, Manage
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

## Security & Access Management

### SEC-001 Role-Based Access Control

Grant AI platform access according to approved job roles and responsibilities.

- **How to implement:** Define roles, restrict privileged access, and review grants regularly.
- **How to verify:** Access matrix and access review
- **Addresses risk:** Data Sensitivity, Autonomy
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

### SEC-002 Credential and Secret Protection

Keep credentials and API keys out of prompts, model outputs, and unprotected logs.

- **How to implement:** Use secrets management, rotation, and leakage detection.
- **How to verify:** Secret scanning and rotation records
- **Addresses risk:** Data Sensitivity, Autonomy
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

### SEC-003 Prompt Injection Defense

Test and constrain AI behavior when processing untrusted instructions or retrieved content.

- **How to implement:** Test prompt injection scenarios and enforce tool/data boundaries.
- **How to verify:** Adversarial test report and mitigation evidence
- **Addresses risk:** Autonomy, Business Impact
- **NIST AI RMF:** Measure, Manage
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

### SEC-004 Tool Permission Boundaries

Limit which tools and resources AI systems can invoke and under what conditions.

- **How to implement:** Apply scoped permissions and deny unauthorized tool actions.
- **How to verify:** Permission configuration and negative tests
- **Addresses risk:** Autonomy, Data Sensitivity
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.6 AI system life cycle, A.9 Use of AI systems
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity

### SEC-005 Environment and Change Security

Separate development and production access and review changes to AI configurations.

- **How to implement:** Require change approvals, versioning, and rollback procedures.
- **How to verify:** Change records and rollback test
- **Addresses risk:** Business Impact, Autonomy
- **NIST AI RMF:** Manage
- **ISO/IEC 42001:** A.6 AI system life cycle
- **EU AI Act:** Art. 15 Accuracy, robustness & cybersecurity
