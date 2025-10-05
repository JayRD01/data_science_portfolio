from src.core.contracts.file_info_contract import FileInfo
from src.core.contracts.strategy_contract import StrategyMethodContract
from src.utils.root_path import RootPath

class StrategyManager:
    def __init__(self, strategy: StrategyMethodContract, rootpath: RootPath):
        self._strategy = strategy
        self._rootpath = rootpath

    def set_config(self, strategy: StrategyMethodContract, rootpath: RootPath) -> None:
        self._strategy = strategy
        self._rootpath = rootpath

    def explorer_strat(self) -> list[FileInfo]:
        root_path = str(self._rootpath)
        return self._strategy.explorer_strat(root_path)
