from .interfaces import FileInfo
from .interfaces import StrategyMethod
import pathlib

class StrategyPathlib(StrategyMethod):
    """Pathlib-backed strategy."""
    def explorer_strat(self, root: str) -> list[FileInfo]:
        items: list[FileInfo] = []
        p = pathlib.Path(root)
        if not p.exists():
            return []
        try:
            for entry in p.iterdir():
                try:
                    size = entry.stat().st_size if entry.is_file() else 0
                    items.append(FileInfo(name=entry.name, size=int(size)))
                except (PermissionError, FileNotFoundError):
                    continue
        except PermissionError:
            return items
        return items
