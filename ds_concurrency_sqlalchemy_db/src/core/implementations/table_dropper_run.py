from src.core.contracts.table_dropper_contract import TableDropperContract
from threading import Lock
from sqlalchemy import select


class TableDropper(TableDropperContract):
    _lock = Lock()

    def __init__(self, model, db):
        self.model = model
        self.db = db

    def drop_row(self, row_id: int) -> None:
        with TableDropper._lock:
            try:
                with self.db.get_session() as session:
                    row = session.get(self.model, row_id)
                    if row:
                        session.delete(row)
                        session.commit()
                        print(f"Row {row_id} deleted.")
                    else:
                        print(f"Row {row_id} not found.")
            except Exception as e:
                print(f"Failed to delete row {row_id}: {type(e).__name__} — {e}")
