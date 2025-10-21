from src.core.implementations.db_singleton_run import _DatabaseSingleton
from src.core.implementations.product_orm_run import ProductORM
from sqlalchemy import update
import logging


def run_update():
    logging.info("[UPDATE] Updating product with ID = 1...")
    db = _DatabaseSingleton()

    with db.get_session() as session:
        result = session.execute(
            update(ProductORM)
            .where(ProductORM.id == 1)
            .values(name="SSD 1TB PRO", price=179.99)
        )

        # result.rowcount tells how many rows were affected (optional)
        logging.info(f"[UPDATE] Rows affected: {result.rowcount} ✅")
