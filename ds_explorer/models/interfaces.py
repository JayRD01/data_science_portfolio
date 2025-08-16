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


class StrategyManager:
    def __init__(self, strategy: StrategyMethod):
        self._strategy: StrategyMethod = strategy

    def set_strategy(self, strategy: StrategyMethod) -> None:
        self._strategy = strategy

    def explorer_strat(self, root: str) -> list[FileInfo]:
        return self._strategy.explorer_strat(root)
