from abc import ABC, abstractmethod
from typing import Type
from sqlalchemy.orm import DeclarativeBase
from src.core.contracts.db_singleton_contract import DBSingletonContract


class TableWriterContract(ABC):
    """
    Abstract contract for inserting a single ORM object into a SQLAlchemy-managed table.

    Ensures:
    - The model is a valid SQLAlchemy declarative class.
    - The model defines required attributes ('id', 'name', 'price').
    - The database object provides session access.

    Subclasses must implement `insert_row()` to define insertion behavior.
    """

    def __init__(self, model: Type[DeclarativeBase], db: DBSingletonContract):
        if not isinstance(model, type):
            raise TypeError("Expected a class, not an instance.")

        if not issubclass(model, DeclarativeBase):
            raise TypeError("Model must inherit from DeclarativeBase.")

        for attr in ("id", "name", "price"):
            if not hasattr(model, attr):
                raise ValueError(f"Model is missing required attribute: '{attr}'")

        self.model = model
        self.db = db

    @abstractmethod
    def insert_row(self, orm_obj: DeclarativeBase) -> None:
        """
        Inserts a single ORM object into the database.

        Parameters:
        - orm_obj: An instance of the model to be persisted.

        Must be implemented by subclasses.
        """
        pass
