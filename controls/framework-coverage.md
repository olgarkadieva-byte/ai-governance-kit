# Framework coverage

Generated from `ai-control-library.json` (34 controls) by `tools/build_controls.py`.
The mapping is indicative: it shows where a control helps, not that implementing it makes an
organization compliant or certifiable.

## NIST AI RMF functions

| Item | Controls | IDs |
| --- | ---: | --- |
| Govern | 6 | AGENT-003, AGENT-008, GOV-001, GOV-005, GOV-006, PRIV-004 |
| Map | 6 | AGENT-007, MON-004, PRIV-001, PRIV-002, PRIV-004, QUAL-001 |
| Measure | 9 | AGENT-005, MON-001, MON-002, QUAL-001, QUAL-002, QUAL-003, QUAL-004, QUAL-005, SEC-003 |
| Manage | 26 | AGENT-001, AGENT-002, AGENT-003, AGENT-004, AGENT-005, AGENT-006, AGENT-007, AGENT-008, GOV-002, GOV-003, GOV-004, GOV-006, MON-001, MON-003, MON-004, PRIV-001, PRIV-002, PRIV-003, PRIV-005, PRIV-006, QUAL-005, SEC-001, SEC-002, SEC-003, SEC-004, SEC-005 |

## ISO/IEC 42001 Annex A areas

| Item | Controls | IDs |
| --- | ---: | --- |
| A.3 Internal organization | 4 | AGENT-003, GOV-001, GOV-005, MON-003 |
| A.5 Impact assessment | 2 | MON-004, QUAL-004 |
| A.6 AI system life cycle | 14 | AGENT-001, AGENT-005, GOV-005, MON-001, MON-002, QUAL-001, QUAL-002, QUAL-003, QUAL-005, SEC-001, SEC-002, SEC-003, SEC-004, SEC-005 |
| A.7 Data for AI systems | 8 | AGENT-007, PRIV-001, PRIV-002, PRIV-003, PRIV-005, PRIV-006, QUAL-002, QUAL-004 |
| A.8 Information for interested parties | 2 | GOV-006, MON-003 |
| A.9 Use of AI systems | 10 | AGENT-001, AGENT-002, AGENT-003, AGENT-004, AGENT-006, AGENT-008, GOV-002, GOV-003, GOV-004, SEC-004 |
| A.10 Third-party relationships | 1 | PRIV-004 |

## EU AI Act articles

| Item | Controls | IDs |
| --- | ---: | --- |
| Art. 9 Risk management | 2 | MON-004, QUAL-001 |
| Art. 10 Data governance | 7 | AGENT-007, PRIV-001, PRIV-002, PRIV-003, PRIV-005, QUAL-002, QUAL-004 |
| Art. 11 Technical documentation | 1 | GOV-005 |
| Art. 12 Record-keeping | 3 | AGENT-005, AGENT-008, GOV-005 |
| Art. 13 Transparency to deployers | 1 | PRIV-004 |
| Art. 14 Human oversight | 8 | AGENT-001, AGENT-002, AGENT-003, AGENT-004, AGENT-008, GOV-002, GOV-003, GOV-004 |
| Art. 15 Accuracy, robustness & cybersecurity | 15 | AGENT-001, AGENT-003, AGENT-006, AGENT-007, MON-002, PRIV-006, QUAL-001, QUAL-002, QUAL-003, QUAL-005, SEC-001, SEC-002, SEC-003, SEC-004, SEC-005 |
| Art. 26 Deployer obligations | 5 | AGENT-005, GOV-001, MON-001, MON-003, PRIV-004 |
| Art. 50 Transparency to people | 1 | GOV-006 |
| Art. 72 Post-market monitoring | 2 | MON-001, MON-002 |
| Art. 73 Serious incident reporting | 1 | MON-003 |

## Controls by category

| Category | Controls |
| --- | ---: |
| AI Agent Authorization & Action Boundaries | 8 |
| Human Oversight & Accountability | 6 |
| Monitoring, Incident Response & Auditability | 4 |
| Privacy & Data Protection | 6 |
| Quality, Reliability & Testing | 5 |
| Security & Access Management | 5 |
