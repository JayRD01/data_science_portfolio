from src.core.implementations.db_singleton_run import _DatabaseSingleton
from src.core.implementations.product_orm_run import ProductORM
from sqlalchemy import delete
import logging


def run_delete():
    logging.info("[DELETE] Deleting product with ID = 2...")
    db = _DatabaseSingleton()

    with db.get_session() as session:
        result = session.execute(delete(ProductORM).where(ProductORM.id == 2))

        logging.info(f"[DELETE] Rows deleted: {result.rowcount} ✅")
