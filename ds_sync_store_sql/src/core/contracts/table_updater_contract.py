from abc import ABC, abstractmethod
from typing import Type
from sqlalchemy.orm import DeclarativeBase
from src.core.contracts.db_singleton_contract import DBSingletonContract


class TableUpdaterContract(ABC):
    """
    Abstract contract for updating rows in a SQLAlchemy ORM table.

    Ensures:
    - The model is a valid SQLAlchemy declarative class.
    - The model defines required attributes ('id', 'name', 'price').
    - The database object provides session access.

    Subclasses must implement `update_row()` to define update behavior.
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
    def update_row(self, row_id: int, updates: dict) -> None:
        """
        Updates a row in the table based on its primary key.

        Parameters:
        - row_id: The ID of the row to update.
        - updates: A dictionary of field-value pairs to apply.

        Must be implemented by subclasses.
        """
        pass
