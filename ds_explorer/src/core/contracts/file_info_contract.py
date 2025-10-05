from __future__ import annotations
from pydantic import BaseModel, ConfigDict

class FileInfo(BaseModel):
    """
    Minimal, validated metadata.
    Fields:
        name: Basename of the resource (file or directory).
        size: Size in bytes (0 for directories or when unknown).
    """
    name: str
    size: int = 0
    is_dir: bool = False

    # Pydantic v2: immutable model (hashable/comparable), prevents mutation.
    model_config: ConfigDict = ConfigDict(frozen=True)
