from src.core.contracts.file_info_contract import FileInfo
import pathlib

class StrategyPathlib():
    """Pathlib-backed strategy."""
    def explorer_strat(self, root: str) -> list[FileInfo]:
        if not isinstance(root, str):
            raise TypeError(f"Expected str for root, got {type(root).__name__}")
        
        items: list[FileInfo] = []
        p = pathlib.Path(root)
        try:
            for entry in p.iterdir():
                try:
                    size = entry.stat().st_size if entry.is_file() else 0
                    items.append(FileInfo(name=entry.name, size=int(size), is_dir=entry.is_dir()))
                except (PermissionError, FileNotFoundError):
                    continue
        except FileNotFoundError:
            return items
        return items
