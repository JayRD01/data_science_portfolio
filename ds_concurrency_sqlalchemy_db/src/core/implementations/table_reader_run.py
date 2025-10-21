from src.core.contracts.table_reader_contract import TableReaderContract
from sqlalchemy import select
from threading import Lock
from typing import Any


class TableReader(TableReaderContract):
    _lock = Lock()

    def __init__(self, model: Any, db: Any):
        self.model = model
        self.db = db

    def show_table(self) -> None:
        with TableReader._lock:
            try:
                with self.db.get_session() as session:
                    rows = session.scalars(select(self.model)).all()
                    # SCALARS - Executes a SELECT * FROM <table> and returns only the ORM instances
                    # (not raw tuples or column values).
                    # Example: if self.model = ProductORM, this returns a list like:
                    # [ProductORM(id=1, name='Laptop', price=1299.99),
                    # ProductORM(id=2, name='Mouse', price=49.99), ...]

            except Exception as e:
                print(f"Failed to retrieve data: {type(e).__name__} — {e}")
                return

            if not rows:
                print("No data found in table.")
                return

            # Defensive check: ensure model has expected attributes
            required_fields = ["id", "name", "price"]
            for field in required_fields:
                if not hasattr(self.model, field):
                    print(f"Model is missing required field: '{field}'")
                    return

            print(f"{'ID':<5} {'Name':<20} {'Price':>10}")
            print("-" * 37)

            for row in rows:
                try:
                    print(f"{row.id:<5} {row.name:<20} ${row.price:>9.2f}")
                except AttributeError as attr_err:
                    print(f"Skipped row due to missing attribute: {attr_err}")
