from .interfaces import FileInfo
from .interfaces import StrategyMethod
import os

class StrategyOs(StrategyMethod):
    """OS-backed strategy using os.scandir()."""
    def explorer_strat(self, root: str) -> list[FileInfo]:
        items: list[FileInfo] = []
        try:
            with os.scandir(root) as entries:
                for entry in entries:
                    try:
                        size = entry.stat(follow_symlinks=False).st_size if entry.is_file() else 0
                        items.append(FileInfo(name=entry.name, size=int(size)))
                    except (PermissionError, FileNotFoundError):
                        continue
        except FileNotFoundError:
            return []
        return items
