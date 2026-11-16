import json
from pathlib import Path

import pytest

from aigov.risk import RiskLevel, RiskScores, classify, review_interval_months

EXAMPLES = json.loads((Path(__file__).parent.parent / "examples" / "ai-systems.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("system", EXAMPLES, ids=[s["name"] for s in EXAMPLES])
def test_worked_examples_match_the_notion_kit(system):
    assert classify(RiskScores(**system["risk_scores"])).value == system["expected_risk_level"]


def test_missing_score_is_not_assessed():
    assert classify(RiskScores(2, 2, 2, 2, None)) is RiskLevel.NOT_ASSESSED


def test_low_average_is_low():
    assert classify(RiskScores(1, 2, 2, 2, 1)) is RiskLevel.LOW


def test_average_of_three_is_moderate():
    assert classify(RiskScores(3, 3, 3, 3, 3)) is RiskLevel.MODERATE


def test_average_just_under_four_is_moderate():
    assert classify(RiskScores(4, 4, 3, 4, 3)) is RiskLevel.MODERATE


def test_any_five_with_moderate_average_is_high():
    assert classify(RiskScores(3, 3, 3, 5, 3)) is RiskLevel.HIGH


def test_single_five_is_never_averaged_away():
    # Average is 1.8, but Data Sensitivity is 5.
    assert classify(RiskScores(5, 1, 1, 1, 1)) is RiskLevel.HIGH


def test_business_impact_five_is_critical():
    assert classify(RiskScores(1, 5, 1, 1, 1)) is RiskLevel.CRITICAL


def test_autonomous_with_weak_oversight_is_critical():
    assert classify(RiskScores(2, 2, 4, 2, 4)) is RiskLevel.CRITICAL


def test_autonomous_with_strong_oversight_is_not_critical():
    assert classify(RiskScores(2, 2, 4, 2, 2)) is RiskLevel.LOW


@pytest.mark.parametrize("bad", [0, 6, -1])
def test_out_of_range_scores_are_rejected(bad):
    with pytest.raises(ValueError):
        RiskScores(bad, 1, 1, 1, 1)


def test_non_integer_scores_are_rejected():
    with pytest.raises(TypeError):
        RiskScores(2.5, 1, 1, 1, 1)


@pytest.mark.parametrize(
    "level, months",
    [
        (RiskLevel.CRITICAL, 3),
        (RiskLevel.HIGH, 3),
        (RiskLevel.MODERATE, 6),
        (RiskLevel.LOW, 12),
        (RiskLevel.NOT_ASSESSED, 3),
    ],
)
def test_review_intervals(level, months):
    assert review_interval_months(level) == months
