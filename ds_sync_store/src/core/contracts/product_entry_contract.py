from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True, slots=True)
class ProductEntryContract:
    """
    Immutable and validated data contract for a product row.

    This class represents a single row in a product table—whether in memory,
    a database, or a test fixture. It enforces strict typing and defensive
    validation to ensure data integrity and auditability.

    Fields:
    - id: Optional unique identifier (can be None for new/unpersisted entries)
    - name: Required non-empty product name
    - price: Required non-negative price value

    Designed for use in inspectable pipelines, test suites, and data ingestion
    flows where clarity, consistency, and contract enforcement are critical.
    """
    id: Optional[int]
    name: str
    price: float

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, int):
            raise TypeError("id must be int | None")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("price must be a non-negative number")
