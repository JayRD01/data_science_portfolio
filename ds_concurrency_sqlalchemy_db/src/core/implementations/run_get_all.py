from src.core.implementations.db_singleton_run import _DatabaseSingleton
from src.core.implementations.product_orm_run import ProductORM
from sqlalchemy import select
import logging


def run_get_all():
    logging.info("[GET] Retrieving all products...")
    db = _DatabaseSingleton()

    with db.get_session() as session:
        results = session.scalars(select(ProductORM)).all()

        logging.info(f"[GET] Found {len(results)} products:")
        for product in results:
            logging.info(f"[GET] ID: {product.id} | {product.name} — ${product.price}")
