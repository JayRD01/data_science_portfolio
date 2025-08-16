from pathlib import Path

class RootPath:
    def __init__(self, root: str, marker: str = ".here"):
        self.root = root
        self.marker = marker

    def resolve(self) -> str:
        parent = Path(self.root).parent
        try:
            for entry in parent.iterdir():
                if entry.is_file() and entry.name == self.marker:
                    print("File '.here' found, setting root dynamically.")
                    return str(entry.resolve().parent)
        except (PermissionError, FileNotFoundError):
            print("'.here' file not found, using default root.")
        return str(self.root)
