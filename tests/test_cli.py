import json

import pytest

from aigov.__main__ import main


def test_score_prints_level(capsys):
    assert main(["score", "--data", "4", "--impact", "3", "--autonomy", "2", "--exposure", "4", "--oversight", "2"]) == 0
    assert "Moderate" in capsys.readouterr().out


@pytest.mark.parametrize("bad", ["9", "0", "x"])
def test_score_out_of_range_is_a_usage_error(bad, capsys):
    with pytest.raises(SystemExit) as exc:
        main(["score", "--data", bad, "--impact", "3", "--autonomy", "2", "--exposure", "4", "--oversight", "2"])
    assert exc.value.code == 2
    assert "1 to 5" in capsys.readouterr().err


def test_score_file_errors_are_friendly(tmp_path, capsys):
    assert main(["score-file", str(tmp_path / "nope.json")]) == 2
    assert "file not found" in capsys.readouterr().err
    bad = tmp_path / "bad.json"
    bad.write_text("{not json")
    assert main(["score-file", str(bad)]) == 2
    assert "not valid JSON" in capsys.readouterr().err
    wrong = tmp_path / "wrong.json"
    wrong.write_text(json.dumps([{"name": "X"}]))
    assert main(["score-file", str(wrong)]) == 2
    assert "risk_scores" in capsys.readouterr().err
