"""Data model for the expense tracker."""

from dataclasses import asdict, dataclass, field
from datetime import date


@dataclass
class Expense:
    amount: float
    category: str
    description: str = ""
    date: str = field(default_factory=lambda: date.today().isoformat())

    def __post_init__(self):
        # Runs automatically after the dataclass __init__: normalise and validate.
        self.amount = round(float(self.amount), 2)
        self.category = self.category.strip().lower()
        if self.amount <= 0:
            raise ValueError("amount must be positive")
        date.fromisoformat(self.date)  # raises ValueError for bad dates

    @property
    def month(self) -> str:
        return self.date[:7]  # "2026-11-06" -> "2026-11"

    def to_dict(self) -> dict:
        return asdict(self)
