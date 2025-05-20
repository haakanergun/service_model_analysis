"""Simple service model analysis functions."""

from dataclasses import dataclass
from typing import List

@dataclass
class ServiceRecord:
    service_id: int
    duration_minutes: int


def average_duration(records: List[ServiceRecord]) -> float:
    """Return the average service duration from a list of records."""
    if not records:
        return 0.0
    total = sum(r.duration_minutes for r in records)
    return total / len(records)
