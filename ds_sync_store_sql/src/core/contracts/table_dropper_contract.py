from abc import ABC, abstractmethod
from typing import Type
from sqlalchemy.orm import DeclarativeBase
from src.core.contracts.db_singleton_contract import DBSingletonContract


class TableDropperContract(ABC):
    """
    Abstract contract for safely deleting rows from a SQLAlchemy ORM table.

    This contract enforces:
    - That the provided model is a valid SQLAlchemy declarative class.
    - That the model defines required attributes (e.g. 'id', 'name', 'price').
    - That any subclass implements the `drop_row()` method to perform deletion logic.

    Intended for use in modular, contract-driven architectures where table operations
    are abstracted and validated before execution.
    """

    def __init__(self, model: Type[DeclarativeBase], db: DBSingletonContract):
        if not isinstance(model, type):
            raise TypeError("Expected a class, not an instance.")

        if not issubclass(model, DeclarativeBase):
            raise TypeError("Model must inherit from DeclarativeBase.")

        for attr in ["id", "name", "price"]:
            if not hasattr(model, attr):
                raise ValueError(f"Model is missing required attribute: '{attr}'")

        self.model = model
        self.db = db

    @abstractmethod
    def drop_row(self, row_id: int) -> None:
        """
        Deletes a row from the table based on its primary key.

        Parameters:
        - row_id: The ID of the row to delete.

        Must be implemented by subclasses.
        """
        pass
