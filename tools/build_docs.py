"""Build the GitHub Pages site in docs/ from the source files in this repository.

Run from the repository root:
    python tools/build_docs.py

Every page is generated, so the website can never drift from the data and specs.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPO = "https://github.com/olgarkadieva-byte/ai-governance-kit"
BLOB = REPO + "/blob/main/"
TREE = REPO + "/tree/main/"
IMPACT_DEMO = "https://olgarkadieva-byte.github.io/ai-impact-measurement/"
KIT = "https://smartailayer.notion.site/AI-Governance-Starter-Kit-3f0e47a9275080e480efd72a57a9442d"

# Relative links in source markdown that point at other generated pages.
PAGE_LINKS = {
    "../risk/scoring-rubric.md": "risk-scoring.html",
    "scoring-rubric.md": "risk-scoring.html",
    "../risk/eu-ai-act-tiers.md": "eu-ai-act-tiers.html",
    "eu-ai-act-tiers.md": "eu-ai-act-tiers.html",
}


def front_matter(title: str, description: str, permalink: str) -> str:
    return f'---\nlayout: default\ntitle: "{title}"\ndescription: "{description}"\npermalink: {permalink}\n---\n\n'


def rewrite_links(text: str, source_dir: str) -> str:
    """Point relative links at generated pages or at the files on GitHub."""

    def repl(match: re.Match) -> str:
        label, target = match.group(1), match.group(2)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        if target in PAGE_LINKS:
            return f"[{label}]({PAGE_LINKS[target]}{anchor})"
        resolved = (Path(source_dir) / target).as_posix()
        parts = []
        for part in resolved.split("/"):
            if part == "..":
                if parts:
                    parts.pop()
            elif part not in ("", "."):
                parts.append(part)
        path = "/".join(parts)
        base = TREE if target.endswith("/") or "." not in Path(path).name else BLOB
        return f"[{label}]({base}{path}{anchor})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def page_from_source(source: str, out: str, title: str, description: str, permalink: str) -> None:
    text = (ROOT / source).read_text(encoding="utf-8")
    text = re.sub(r"^# .*\n+", "", text, count=1)  # the layout renders the title
    body = rewrite_links(text, str(Path(source).parent))
    (DOCS / out).write_text(front_matter(title, description, permalink) + f"# {title}\n\n" + body, encoding="utf-8")


def controls_page() -> None:
    controls = sorted(json.loads((ROOT / "controls" / "ai-control-library.json").read_text(encoding="utf-8")), key=lambda c: c["id"])
    lines = [
        front_matter(
            "AI Control Library: 34 controls mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act",
            "Free library of 34 AI governance controls, including 8 for AI agents, each mapped to NIST AI RMF, ISO/IEC 42001 Annex A and EU AI Act articles. Download as CSV or JSON.",
            "/controls.html",
        ),
        "# AI Control Library",
        "",
        f"{len(controls)} practical AI governance controls, including {sum(1 for c in controls if c['id'].startswith('AGENT'))} for AI agents. "
        "Each control is mapped to the **NIST AI Risk Management Framework**, **ISO/IEC 42001** Annex A, and the **EU AI Act**, "
        "with implementation and verification guidance.",
        "",
        f"**Download:** [CSV]({BLOB}controls/ai-control-library.csv) · [JSON]({BLOB}controls/ai-control-library.json) · "
        f"[Framework coverage report]({BLOB}controls/framework-coverage.md) · [Use it in Notion]({KIT})",
        "",
        "The mapping is indicative: it shows where a control helps, not that implementing it makes an organization compliant or certifiable.",
        "",
    ]
    categories: dict[str, list] = {}
    for c in controls:
        categories.setdefault(c["category"], []).append(c)
    for category, items in categories.items():
        lines += [f"## {category}", ""]
        for c in items:
            lines += [
                f"### {c['id']} {c['name']}",
                "",
                c["description"],
                "",
                f"- **How to implement:** {c['implementation_guidance']}",
                f"- **How to verify:** {c['verification_guidance']}",
                f"- **Addresses risk:** {', '.join(c['applicable_risk'])}",
                f"- **NIST AI RMF:** {', '.join(c['nist_ai_rmf'])}",
                f"- **ISO/IEC 42001:** {', '.join(c['iso_iec_42001'])}",
                f"- **EU AI Act:** {', '.join(c['eu_ai_act'])}",
                "",
            ]
    (DOCS / "controls.md").write_text("\n".join(lines), encoding="utf-8")


def index_page() -> None:
    body = f"""{front_matter(
        "AI Governance Kit",
        "Free, framework-aligned AI governance toolkit: 34 AI controls (8 for AI agents) mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act, a five-dimension AI risk scoring model, and an EU AI Act tier screening guide.",
        "/",
    )}# AI Governance Kit

Practical, framework-aligned tools to govern AI systems: know what you run, how risky it is, and which safeguards protect it. Free to use.

| | |
| --- | --- |
| [**AI Control Library**](controls.html) | 34 controls, including 8 for AI agents, mapped to NIST AI RMF, ISO/IEC 42001 and the EU AI Act. Download as CSV or JSON. |
| [**AI Risk Scoring Rubric**](risk-scoring.html) | Score any AI system on five dimensions. One severe risk is never averaged away. |
| [**EU AI Act Tier Screening**](eu-ai-act-tiers.html) | Is your AI system prohibited, high-risk, subject to transparency rules, or minimal risk? |

## Two ways to use it

- **No-code:** duplicate the free [AI Governance Starter Kit for Notion]({KIT}). Set up in about an hour.
- **Data and code:** use the [GitHub repository]({REPO}) for CSV and JSON files and a tested Python package.

```bash
git clone {REPO}.git && cd ai-governance-kit
python -m aigov score --data 4 --impact 3 --autonomy 2 --exposure 4 --oversight 2
# AI system: Moderate (average 3.00, review every 6 months)
```

## Governance, then measurement

This kit answers "is this AI system safe, accountable and under control?". To answer "what did it actually change, and is it worth
what it costs?", use the companion tool [AI Impact Measurement]({IMPACT_DEMO}): adoption, time saved, cost and ROI against a control
group, with a keep / fix / retire verdict for every AI tool.

## Related reading

- [AI Agent Authorization: Why Consent Isn't Enough](https://olgasoffice.substack.com/p/consent-isnt-authorization-the-next)
- [AI Governance in 2026: Why Measurement Is the Hard Part](https://olgasoffice.substack.com/p/ai-governance-in-2026-the-hardest)
- [When Identity Is No Longer Human](https://olgasoffice.substack.com/p/when-identity-is-no-longer-human)

Created by [Olga Arkadieva](https://www.linkedin.com/in/olga-arkadieva-aigp-989677112/), AIGP · [Smart AI Layer](https://smartailayer.com) ·
Licensed [CC BY-NC 4.0]({BLOB}LICENSE). Not legal advice.
"""
    (DOCS / "index.md").write_text(body, encoding="utf-8")


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    index_page()
    controls_page()
    page_from_source(
        "risk/scoring-rubric.md",
        "risk-scoring.md",
        "AI Risk Scoring Rubric: score AI systems on five dimensions",
        "Free AI risk assessment rubric: score data sensitivity, business impact, autonomy, user exposure and human oversight from 1 to 5 to get a Low, Moderate, High or Critical risk level.",
        "/risk-scoring.html",
    )
    page_from_source(
        "risk/eu-ai-act-tiers.md",
        "eu-ai-act-tiers.md",
        "EU AI Act Risk Tier Screening Guide",
        "Screen an AI system against the EU AI Act tiers: prohibited practices, high-risk (Annex III), transparency obligations (Article 50) and minimal risk, with current application dates.",
        "/eu-ai-act-tiers.html",
    )
    print("Built docs/: index, controls, risk-scoring, eu-ai-act-tiers")


if __name__ == "__main__":
    main()
