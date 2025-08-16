from abc import ABC, abstractmethod
from pydantic import BaseModel
from .root_path import RootPath


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
    def __init__(self, strategy: StrategyMethod, rootpath: RootPath):
        self._strategy: StrategyMethod = strategy
        self._rootpath = rootpath

    def set_config(self, strategy: StrategyMethod, rootpath: RootPath) -> None:
        self._strategy = strategy
        self._rootpath = rootpath

    def explorer_strat(self) -> list[FileInfo]:
        resolved_root = self._rootpath.resolve()
        return self._strategy.explorer_strat(resolved_root)
