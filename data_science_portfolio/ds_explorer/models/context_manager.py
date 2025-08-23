from models.strategy_protocols import StrategyMethod, FileInfo
from models.root_path import RootPath

class StrategyManager:
    def __init__(self, strategy: StrategyMethod, rootpath: RootPath):
        self._strategy = strategy
        self._rootpath = rootpath

    def set_config(self, strategy: StrategyMethod, rootpath: RootPath) -> None:
        self._strategy = strategy
        self._rootpath = rootpath

    def explorer_strat(self) -> list[FileInfo]:
        root_path = str(self._rootpath)
        return self._strategy.explorer_strat(root_path)
