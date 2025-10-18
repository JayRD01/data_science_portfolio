from abc import ABC, abstractmethod
from typing import Type
from sqlalchemy.orm import DeclarativeBase
from src.core.contracts.db_singleton_contract import DBSingletonContract


class TableReaderContract(ABC):
    """
    Abstract contract for reading and displaying ORM table data.
    This interface defines the minimal behavior expected from any table reader.
    """

    def __init__(self, model: Type[DeclarativeBase], db: DBSingletonContract):
        self.model = model
        self.db = db

    @abstractmethod
    def show_table(self) -> None:
        """Prints the entire table in a formatted view."""
        pass
