import os
from typing import Protocol, runtime_checkable
from src.core.contracts.file_info_contract import FileInfo

@runtime_checkable
class StrategyMethodContract(Protocol):
    """
    Contract for cross-backend filesystem exploration strategies (os, pathlib, PyFilesystem2).

    Implementations MUST provide:
      - explorer_strat(root): list[FileInfo]

    Expectations:
      - `root` is a path within the backend (e.g., "/" or "subdir/").
        Accept `str` or `os.PathLike[str]` so it works with both plain strings and pathlib paths.
      - Return a concrete `list[FileInfo]` (never None).
      - For directories or unknown sizes, set FileInfo.size = 0.
      - Skip entries that raise backend-specific errors (e.g., permissions, race conditions)
        and still return a coherent list.
      - Do NOT follow symlinks when determining size/type.
      - If `root` does not exist or cannot be opened, return an empty list.
    """

    def explorer_strat(self, root: str | os.PathLike[str]) -> list[FileInfo]:
        ...
