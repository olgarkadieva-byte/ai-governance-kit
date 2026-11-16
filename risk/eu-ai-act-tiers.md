# EU AI Act tier screening

The EU AI Act sorts AI systems by what they are used for, not by how advanced they are.
Work down this list and stop at the first tier that fits.

| Tier | Typical examples | What it means |
| --- | --- | --- |
| Prohibited (Art. 5) | Social scoring; manipulating or exploiting vulnerable people; emotion recognition at work or in schools; untargeted scraping of facial images to build recognition databases; predicting crime from profiling alone | Do not use. These practices have been banned since 2 February 2025. |
| High-risk (Annex III) | Hiring, promotion, firing, or worker monitoring; credit scoring; pricing life or health insurance; deciding access to education or public benefits; biometric identification | Requirements for risk management, data governance, logging, human oversight, accuracy, and documentation. Under the Digital Omnibus on AI, these apply from 2 December 2027. |
| Transparency obligations (Art. 50) | Chatbots that talk to people; AI-generated or edited images, audio, or video; AI-generated text published to inform the public | Tell people they are dealing with AI and label AI-generated content. Applies from 2 August 2026. See control `GOV-006`. |
| Minimal risk | Spam filters, meeting summaries, internal drafting tools, code assistants | No specific requirements for the system itself. Good governance practice still applies. |

Notes:

- Most organizations are **deployers**: they use AI built by someone else. Deployer duties for high-risk systems are in Article 26: follow the provider's instructions, assign trained people to oversee the system, monitor it, and keep logs.
- The `eu_ai_act` field in [`controls/ai-control-library.csv`](../controls/ai-control-library.csv) shows which articles each control helps with. Most of those articles (9 to 15, 72, 73) apply to high-risk systems.
- AI embedded in products regulated under Annex I (for example medical devices or machinery) follows a later timeline.
- Dates reflect the Digital Omnibus on AI as adopted in 2026. Check for later changes.

This is a screening aid, not legal advice. Confirm any Prohibited or High-risk result with legal counsel.
