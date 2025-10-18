from src.core.contracts.table_updater_contract import TableUpdaterContract
from sqlalchemy import select, update
from threading import Lock


class TableUpdater(TableUpdaterContract):
    _lock = Lock()

    def __init__(self, model, db):
        self.model = model
        self.db = db

    def update_row(self, row_id: int, updates: dict) -> None:
        with TableUpdater._lock:
            try:
                with self.db.get_session() as session:
                    stmt = (
                        update(self.model)
                        .where(self.model.id == row_id)
                        .values(**updates)
                    )
                    session.execute(stmt)
                    session.commit()
                    print(f"✅ Updated row {row_id} with {updates}")
            except Exception as e:
                print(f"Update failed: {type(e).__name__} — {e}")
