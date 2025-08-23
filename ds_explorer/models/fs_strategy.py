from .strategy_protocols import FileInfo
from .strategy_protocols import StrategyMethod
from fs.base import FS
import fs.errors as fserrors

class StrategyFS(StrategyMethod):
    """PyFilesystem2-backed strategy."""
    def __init__(self, fs_obj: FS):
        self.fs: FS = fs_obj

    def explorer_strat(self, root: str) -> list[FileInfo]:
        items: list[FileInfo] = []
        try:
            for entry in self.fs.scandir(root, namespaces=['details']):
                try:
                    # entry: name, is_dir and details such as size
                    name = entry.name
                    is_dir = entry.is_dir  
                    size = 0
                    if not is_dir:
                        # 'size' may not be present -> default to 0
                        size_val = entry.get('details', 'size')  # None if not available
                        size = int(size_val) if size_val is not None else 0
                    items.append(FileInfo(name=name, size=size))
                except (fserrors.PermissionDenied, fserrors.ResourceNotFound):
                    continue
        except fserrors.ResourceNotFound:
            return items
        return items
