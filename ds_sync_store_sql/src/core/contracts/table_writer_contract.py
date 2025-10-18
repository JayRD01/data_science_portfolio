from abc import ABC, abstractmethod
from typing import Type
from sqlalchemy.orm import DeclarativeBase
from src.core.contracts.db_singleton_contract import DBSingletonContract


class TableWriterContract(ABC):
    """
    Abstract contract for inserting a single ORM row into the database.
    """

    def __init__(self, model: Type[DeclarativeBase], db: DBSingletonContract):
        self.model = model
        self.db = db

    @abstractmethod
    def insert_row(self, orm_obj: DeclarativeBase) -> None:
        """Attempts to insert a single ORM object into the database."""
        pass
