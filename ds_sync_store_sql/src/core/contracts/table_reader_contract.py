from abc import ABC, abstractmethod
from typing import Type
from sqlalchemy.orm import DeclarativeBase
from src.core.contracts.db_singleton_contract import DBSingletonContract


class TableReaderContract(ABC):
    """
    Abstract contract for reading and displaying ORM table data.

    Ensures:
    - The model is a valid SQLAlchemy declarative class.
    - The model defines required attributes ('id', 'name', 'price').
    - The database object exposes a session interface.

    Subclasses must implement `show_table()` to define how data is displayed.
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
    def show_table(self) -> None:
        """Prints the entire table in a formatted view."""
        pass
