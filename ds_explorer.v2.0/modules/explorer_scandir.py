import os
from modules.abstracted import AbstractedClass


class ExplorerHeavy(AbstractedClass):
    def explorer_scandir(self):
        # Initialize the stack with the root directory and starting depth (0)
        stack = [(self.root_path, 0)]  # Tuples: (path, current depth)

        while stack:
            # Extract the current directory and its depth from the stack
            dir_current, current_depth = stack.pop()

            # Check if we've reached or exceeded the max depth
            # max_depth == -1 means "no depth limit", which is common in dev tools
            if self.max_depth != -1 and current_depth >= self.max_depth:
                continue  # Skip further processing at this depth

            try:
                # Attempt to scan the contents of the current directory
                with os.scandir(dir_current) as entries:
                    for entry in entries:
                        full_path = entry.path  # Full path of current entry

                        try:
                            # If the entry is a directory, track it and push it to the stack
                            if entry.is_dir(follow_symlinks=False):
                                self.visited_dir.add(full_path)
                                # Increase depth by 1
                                stack.append((full_path, current_depth + 1))

                            # If it's a file, simply add to the found files set
                            elif entry.is_file():
                                self.filenames.add(full_path)

                        except Exception as e:
                            # Catch errors like broken symlinks or permission issues on entry
                            print(
                                f"Error processing entry '{entry.name}': {e}")

            except PermissionError:
                print(f"Permission denied: {dir_current}")
            except FileNotFoundError:
                print(f"Directory not found: {dir_current}")
            except Exception as e:
                print(f"Unexpected error accessing {dir_current}: {e}")

        # Return the collected results
        return self.visited_dir, self.filenames

    def run(self):
        """
        Implements the abstract 'run' method.
        Executes the scanning process and returns the results.
        """
        return self.explorer_scandir()
