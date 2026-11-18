import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

NIST = {"Govern", "Map", "Measure", "Manage"}
RISKS = {"Data Sensitivity", "Business Impact", "Autonomy", "User Exposure", "Human Oversight"}



def test_every_control_is_complete_and_mapped():
    controls = json.loads((ROOT / "controls" / "ai-control-library.json").read_text(encoding="utf-8"))
    ids = [c["id"] for c in controls]
    assert len(ids) == len(set(ids)), "control IDs must be unique"
    for c in controls:
        for field in ["name", "category", "description", "implementation_guidance", "verification_guidance"]:
            assert c[field], f"{c['id']} is missing {field}"
        assert c["applicable_risk"] and set(c["applicable_risk"]) <= RISKS, c["id"]
        assert c["nist_ai_rmf"] and set(c["nist_ai_rmf"]) <= NIST, c["id"]
        assert c["iso_iec_42001"] and all(x.startswith("A.") for x in c["iso_iec_42001"]), c["id"]
        assert c["eu_ai_act"] and all(x.startswith("Art. ") for x in c["eu_ai_act"]), c["id"]


def test_csv_matches_json():
    controls = json.loads((ROOT / "controls" / "ai-control-library.json").read_text(encoding="utf-8"))
    with (ROOT / "controls" / "ai-control-library.csv").open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert sorted(r["id"] for r in rows) == sorted(c["id"] for c in controls)
