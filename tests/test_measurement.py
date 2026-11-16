import pytest

from aigov.measurement import (
    KpiResult,
    adoption_rate,
    payback_periods,
    repeat_usage_rate,
    tasks_to_break_even,
    time_saved_hours,
)


def test_adoption_rate_uses_eligible_users():
    assert adoption_rate(active_users=30, eligible_users=40) == 75.0


def test_adoption_rate_rejects_zero_denominator():
    with pytest.raises(ValueError):
        adoption_rate(1, 0)


def test_repeat_usage_rate():
    assert repeat_usage_rate(returning_users=12, first_time_users=40) == 30.0


def test_time_saved_matches_article_example():
    # 25 minutes manually, 8 minutes with AI including review, 100 completed tasks.
    assert time_saved_hours(25, 8, 100) == 28.3


def test_payback_matches_article_example():
    # 120 development hours; 15 minutes saved per task -> 480 tasks to break even.
    assert tasks_to_break_even(120, 15) == 480


def test_payback_periods():
    assert payback_periods(development_hours=120, net_hours_saved_per_period=30) == 4.0


def test_no_payback_when_tool_saves_no_time():
    assert payback_periods(120, 0) is None
    assert tasks_to_break_even(120, 0) is None


def test_kpi_target_met_when_lower_is_better():
    assert KpiResult(baseline=15, target=8, actual=7.5, lower_is_better=True).status == "Target met"


def test_kpi_improving_but_not_at_target():
    assert KpiResult(baseline=15, target=8, actual=11, lower_is_better=True).status == "Improving"


def test_guardrail_breach_overrides_kpi_success():
    result = KpiResult(baseline=15, target=8, actual=7, lower_is_better=True, guardrail_held=False)
    assert result.status == "Not on track (guardrail breached)"
