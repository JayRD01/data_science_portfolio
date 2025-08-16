from .interfaces import FileInfo
from .interfaces import StrategyMethod
from fs.base import FS
import fs.errors as fserrors

class StrategyFS(StrategyMethod):
    """PyFilesystem2-backed strategy."""
    def __init__(self, fs_obj: FS):
        self.fs: FS = fs_obj

    def explorer_strat(self, root: str) -> list[FileInfo]:
        items: list[FileInfo] = []
        try:
            # Request the 'details' namespace to be able to read 'size'
            for info in self.fs.scandir(root, namespaces=['details']):
                try:
                    # Info: name, is_dir and details such as size
                    name = info.name
                    is_dir = info.is_dir  # True if it's a directory
                    size = 0
                    if not is_dir:
                        # 'size' may not be present -> default to 0
                        size_val = info.get('details', 'size')  # None if not available
                        size = int(size_val) if size_val is not None else 0
                    items.append(FileInfo(name=name, size=size))
                except (fserrors.PermissionDenied, fserrors.ResourceNotFound):
                    continue
        except fserrors.ResourceNotFound:
            return []
        return items
