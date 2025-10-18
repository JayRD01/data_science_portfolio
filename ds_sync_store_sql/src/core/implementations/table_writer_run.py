from src.core.contracts.table_writer_contract import TableWriterContract
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from threading import Lock
from typing import Any


class TableWriter(TableWriterContract):
    _lock = Lock()

    def __init__(self, model: Any, db: Any):
        self.model = model
        self.db = db

    def insert_row(self, orm_obj: Any) -> None:
        with TableWriter._lock:
            try:
                with self.db.get_session() as session:
                    # Optional: check if ID already exists
                    if orm_obj.id is not None:
                        exists = session.scalar(
                            select(self.model).where(self.model.id == orm_obj.id)
                        )
                        if exists:
                            print(
                                f"Row with ID {orm_obj.id} already exists. Skipping insert."
                            )
                            return

                    session.add(orm_obj)
                    print(f"Inserted: {orm_obj.name} (${orm_obj.price})")

            except IntegrityError as e:
                print(f"Integrity error: {e.orig}")
            except Exception as e:
                print(f"Unexpected error: {type(e).__name__} — {e}")
