from src.core.contracts.file_info_contract import FileInfo
import os

class StrategyOs():
    """OS-backed strategy using os.scandir()."""
    def explorer_strat(self, root: str) -> list[FileInfo]:
        if not isinstance(root, str):
            raise TypeError(f"Expected str for root, got {type(root).__name__}")
        
        items: list[FileInfo] = []
        try:
            with os.scandir(root) as entries:
                for entry in entries:
                    try:
                        size = entry.stat(follow_symlinks=False).st_size if entry.is_file() else 0
                        items.append(FileInfo(name=entry.name, size=int(size), is_dir=entry.is_dir()))
                    except (PermissionError, FileNotFoundError):
                        continue
        except FileNotFoundError:
            return []
        return items
