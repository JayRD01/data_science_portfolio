from abc import ABC, abstractmethod


class AbstractedClass(ABC):
    def __init__(self, root_path: str, max_depth: int = 4, output_file: str = "metadata.json"):
        """
        Common initializer for all explorer subclasses.
        """
        self.visited_dir = set()         # Set to store visited directories
        self.filenames = set()           # Set to store discovered files
        self.root_path = root_path       # Root path to start exploration
        self.max_depth = max_depth       # Max depth (-1 means unlimited)
        self.output_file = output_file   # Out put file

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
