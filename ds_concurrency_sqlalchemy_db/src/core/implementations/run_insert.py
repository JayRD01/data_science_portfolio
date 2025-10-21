from dataclasses import asdict
from src.core.implementations.db_singleton_run import _DatabaseSingleton
from src.core.implementations.product_orm_run import ProductORM
from src.core.contracts.product_entry_contract import ProductEntryContract
import logging


def run_insert():
    logging.info("[INSERT] Starting product insertion...")
    db = _DatabaseSingleton()

    product = ProductEntryContract(id=None, name="SSD 1TB", price=149.99)
    orm_product = ProductORM(**asdict(product))

    with db.get_session() as session:
        session.add(orm_product)  # Queue the object for insertion

    logging.info(f"[INSERT] Product inserted: {product.name} (${product.price}) ✅")
