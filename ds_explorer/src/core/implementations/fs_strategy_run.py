from fs.base import FS
from fs import errors as fserrors
from src.core.contracts.file_info_contract import FileInfo

class StrategyFS:
    """
    PyFilesystem2-backed strategy implementation.

    - Lists entries under `root` and returns minimal metadata as FileInfo.
    - Directories (or entries without size info) report size=0.
    - Swallows permission/not-found errors per-entry and continues.
    """

    def __init__(self, path: FS, include_dirs: bool = True) -> None:
        if not isinstance(path, FS):
            raise TypeError(f"Expected FS instance, got {type(path).__name__}")
        if not isinstance(include_dirs, bool):
            raise TypeError(f"Expected bool for include_dirs, got {type(include_dirs).__name__}")

        self.path: FS = path
        self.include_dirs: bool = include_dirs

    def explorer_strat(self, root: str) -> list[FileInfo]:
        """
        Explore `root` and return minimal FileInfo entries.

        Guarantees:
        - Never returns None.
        - Returns an empty list if `root` does not exist or is not a directory.
        """
        if not isinstance(root, str):
            raise TypeError(f"Expected str for root, got {type(root).__name__}")

        items: list[FileInfo] = []

        try:
            # Ask for extended metadata when available (size, type, timestamps)
            for entry in self.path.scandir(root, namespaces=["details"]):
                try:
                    is_dir = entry.is_dir
                    if is_dir and not self.include_dirs:
                        continue

                    size = 0
                    if not is_dir:
                        size_val = entry.get("details", "size", None)  # Optional[Any]
                        try:
                            size = int(size_val) if size_val is not None else 0
                        except (TypeError, ValueError):
                            size = 0

                    items.append(FileInfo(name=entry.name, size=size, is_dir=is_dir))

                except (fserrors.PermissionDenied, fserrors.ResourceNotFound):
                    # Skip entries we cannot access or that disappear mid-iteration
                    continue

        except (fserrors.ResourceNotFound, fserrors.DirectoryExpected):
            # Root doesn't exist, became unavailable, or points to a file
            return items

        return items
