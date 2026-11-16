"""Risk scoring for AI systems.

Implements the five-dimension scoring model used in the AI Governance Starter Kit
(Step 2 of the Notion template). Each dimension is scored 1 (lowest risk) to 5
(highest risk). The rules are deliberately simple so that a non-specialist can
apply them by hand, and so that a single severe risk is never averaged away.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from enum import Enum
from typing import Optional


class RiskLevel(str, Enum):
    NOT_ASSESSED = "Not Assessed"
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    CRITICAL = "Critical — Review Required"


# Months until the next scheduled review, by risk level.
REVIEW_INTERVAL_MONTHS = {
    RiskLevel.CRITICAL: 3,
    RiskLevel.HIGH: 3,
    RiskLevel.MODERATE: 6,
    RiskLevel.LOW: 12,
    RiskLevel.NOT_ASSESSED: 3,
}


@dataclass(frozen=True)
class RiskScores:
    """Scores from 1 (lowest risk) to 5 (highest risk).

    data_sensitivity: most sensitive data the AI can access.
    business_impact: worst realistic result if the AI gets it wrong.
    autonomy: how much the AI can do without a person approving it.
    user_exposure: who uses it or is affected by it.
    human_oversight: how well people can check and stop the AI.
        A higher score means LESS oversight and therefore more risk.
    """

    data_sensitivity: Optional[int] = None
    business_impact: Optional[int] = None
    autonomy: Optional[int] = None
    user_exposure: Optional[int] = None
    human_oversight: Optional[int] = None

    def __post_init__(self) -> None:
        for f in fields(self):
            value = getattr(self, f.name)
            if value is None:
                continue
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{f.name} must be an integer from 1 to 5, got {value!r}")
            if not 1 <= value <= 5:
                raise ValueError(f"{f.name} must be between 1 and 5, got {value}")

    def values(self) -> list[Optional[int]]:
        return [getattr(self, f.name) for f in fields(self)]

    @property
    def is_complete(self) -> bool:
        return all(v is not None for v in self.values())

    @property
    def average(self) -> Optional[float]:
        if not self.is_complete:
            return None
        vals = [v for v in self.values() if v is not None]
        return round(sum(vals) / len(vals), 2)


def classify(scores: RiskScores) -> RiskLevel:
    """Return the overall risk level.

    Rules, applied in order:
      1. Any score missing                                      -> Not Assessed
      2. Business Impact is 5, or Autonomy >= 4 AND
         Human Oversight >= 4 (acts alone with weak oversight) -> Critical — Review Required
      3. Any single score is 5, or the average is 4 or more     -> High
      4. Average is 3 or more                                   -> Moderate
      5. Otherwise                                              -> Low
    """
    if not scores.is_complete:
        return RiskLevel.NOT_ASSESSED

    if scores.business_impact == 5 or (scores.autonomy >= 4 and scores.human_oversight >= 4):
        return RiskLevel.CRITICAL

    avg = scores.average
    if max(v for v in scores.values() if v is not None) == 5 or avg >= 4:
        return RiskLevel.HIGH
    if avg >= 3:
        return RiskLevel.MODERATE
    return RiskLevel.LOW


def review_interval_months(level: RiskLevel) -> int:
    """Months between scheduled reviews for a given risk level."""
    return REVIEW_INTERVAL_MONTHS[level]
