import os
from modules.abstracted import AbstractedClass


class TreeBuilder(AbstractedClass):
    def structure(self, visited_dir: set, root_path: str, limit: int = 10, blocklist: list = None):
        """
        Prints the directory structure in a tree-like format.

        Args:
            visited_dir (set): A set of visited directories.
            root_path (str): The root directory.
            limit (int): Max number of items to display per directory.
            blocklist (list): List of directory names to exclude from display.
        """
        if not visited_dir:
            print("No directories visited.")
            return

        if blocklist is None:
            blocklist = []

        for directory in sorted(visited_dir):
            # Skip directories in the blocklist
            if any(blocked in directory for blocked in blocklist):
                continue

            try:
                # Calculate relative depth of the directory
                depth = directory.count(os.sep) - root_path.count(os.sep)
                print(f"{'|     ' * depth}|-- {os.path.basename(directory)}")

                # List contents of the directory, up to the specified limit
                if os.path.isdir(directory):
                    items = os.listdir(directory)
                    total_items = len(items)
                    displayed_items = items[:limit]

                    for item in displayed_items:
                        print(f"{'|     ' * (depth + 1)}|-- {item}")

                    if total_items > limit:
                        print(
                            f"{'|     ' * (depth + 1)}|-- ... {total_items - limit} more items")

            except PermissionError:
                print(f"Permission Denied: {directory}")
            except FileNotFoundError:
                print(f"File Not Found: {directory}")
            except Exception as e:
                print(f"Unexpected error in '{directory}': {e}")

    def run(self, visited_dir: set, root_path: str, blocklist: list = None):
        """
        Public method to execute the tree structure display.

        Args:
            visited_dir (set): Set of visited directories.
            root_path (str): The root directory.
            blocklist (list): Optional list of directory names to ignore.
        """
        try:
            self.structure(visited_dir, root_path, blocklist=blocklist)
        except Exception as e:
            print(f"An error occurred while building the tree structure: {e}")
