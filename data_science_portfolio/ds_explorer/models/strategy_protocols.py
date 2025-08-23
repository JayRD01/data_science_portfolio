from abc import ABC, abstractmethod
from pydantic import BaseModel

class FileInfo(BaseModel):
    name: str
    size: int

    class Config:
        frozen = True  # immutable

class StrategyMethod(ABC):
    @abstractmethod
    def explorer_strat(self, root: str) -> list[FileInfo]:
        """Returns a list of FileInfo objects representing the items found in 'root'."""
        pass
