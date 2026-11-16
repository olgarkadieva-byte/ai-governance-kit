"""Measurement formulas for AI tools.

These functions implement the productivity and value metrics described in
measurement/telemetry-spec.md. They are intentionally small and explicit so
that every number in an AI value report can be traced to a definition.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


def adoption_rate(active_users: int, eligible_users: int) -> float:
    """Percentage of eligible users who are active.

    The denominator must be the people the tool is intended for, not the whole
    company. Measuring a tool built for one engineering team against every
    employee produces a misleading number.
    """
    if eligible_users <= 0:
        raise ValueError("eligible_users must be greater than zero")
    if active_users < 0 or active_users > eligible_users:
        raise ValueError("active_users must be between 0 and eligible_users")
    return round(active_users / eligible_users * 100, 1)


def repeat_usage_rate(returning_users: int, first_time_users: int) -> float:
    """Percentage of people who came back after first trying the tool."""
    if first_time_users <= 0:
        raise ValueError("first_time_users must be greater than zero")
    if returning_users < 0 or returning_users > first_time_users:
        raise ValueError("returning_users must be between 0 and first_time_users")
    return round(returning_users / first_time_users * 100, 1)


def time_saved_hours(
    baseline_minutes_per_task: float,
    ai_minutes_per_task: float,
    completed_tasks: int,
) -> float:
    """Hours saved across successfully completed tasks.

    ai_minutes_per_task must include the time a person spends reviewing and
    correcting the AI's output. Otherwise the benefit is overstated.
    Only count tasks that reached a successful outcome.
    """
    if baseline_minutes_per_task < 0 or ai_minutes_per_task < 0:
        raise ValueError("task durations cannot be negative")
    if completed_tasks < 0:
        raise ValueError("completed_tasks cannot be negative")
    saved_minutes = (baseline_minutes_per_task - ai_minutes_per_task) * completed_tasks
    return round(saved_minutes / 60, 1)


def payback_periods(development_hours: float, net_hours_saved_per_period: float) -> Optional[float]:
    """Number of periods (e.g. weeks or months) to recover development effort.

    Development Effort Payback = Development Hours / Net Hours Saved per Period.
    Returns None when the tool is not saving time, because it never pays back.
    """
    if development_hours < 0:
        raise ValueError("development_hours cannot be negative")
    if net_hours_saved_per_period <= 0:
        return None
    return round(development_hours / net_hours_saved_per_period, 1)


def tasks_to_break_even(development_hours: float, minutes_saved_per_task: float) -> Optional[int]:
    """How many successfully completed tasks are needed to recover development effort."""
    if minutes_saved_per_task <= 0:
        return None
    tasks = development_hours * 60 / minutes_saved_per_task
    whole = int(tasks)
    return whole if whole == tasks else whole + 1


@dataclass(frozen=True)
class KpiResult:
    """Compare a KPI against its baseline and target, with a guardrail check."""

    baseline: float
    target: float
    actual: float
    lower_is_better: bool = False
    guardrail_held: bool = True

    @property
    def status(self) -> str:
        if not self.guardrail_held:
            return "Not on track (guardrail breached)"
        improved = self.actual < self.baseline if self.lower_is_better else self.actual > self.baseline
        met = self.actual <= self.target if self.lower_is_better else self.actual >= self.target
        if met:
            return "Target met"
        if improved:
            return "Improving"
        return "Not on track"
