from pathlib import Path

class RootPath:
    def __init__(self, marker=".here", root="."):
        self.root = self.resolve(Path(root), marker)

    def resolve(self, start_path: Path, marker: str) -> str:
        search_path = start_path.resolve()
        for directory in [search_path] + list(search_path.parents):
            marker_path = directory / marker
            if marker_path.exists():
                return str(directory)
        
        # Mejor mensaje de error si no se encuentra
        raise FileNotFoundError(
            f"\n❌ Marker file '{marker}' not found.\n"
            f"👉 Please create a '{marker}' file at the root of your project.\n"
            f"   Example:\n"
            f"   touch /path/to/your/project/{marker}\n"
            f"\n🔍 Search started from: {search_path}\n"
        )

    def __str__(self):
        return self.root
