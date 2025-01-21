import os
import json
import time
from .abstracter import ComposerMeths

class ExplorerDir(ComposerMeths):
    def __init__(self, directory: str = None, output_file: str = "metadata.json", max_depth: int = 2):
        """
        Directory: By using ternary operators, we first set a value of None if the user forgets to send 
        a directory. Then, using os.path.abspath, we set the current directory path.
        Max_depth: Maximum depth for directory traversal. Defaults to 2.
        """
        self.directory = directory if directory else os.path.dirname(os.path.abspath(__file__))  # Base directory
        # Save output file one level up from the current directory
        self.output_file = os.path.join(os.path.dirname(self.directory), output_file)
        
        self.details_file = []
        self.max_depth = max_depth

    def spyder_dir(self):
        """
        Scan the directory up to the max_depth and collect file metadata.
        """
        base_depth = self.directory.count(os.path.sep)

        for paths_name, _, files_name in os.walk(self.directory): #os.walk() - return: paths list, currentDir list, files list 
            current_depth = paths_name.count(os.path.sep) - base_depth #os.path.sep - return: ej home/desktop/folder = slashes (///) 
            if current_depth > self.max_depth:
                continue
            for file in files_name:
                path_now = os.path.join(paths_name, file)
                if os.path.isfile(path_now):
                    self.details_file.append({
                        "FileName": file,
                        "Created": time.ctime(os.stat(path_now).st_ctime),
                        "Modified": time.ctime(os.stat(path_now).st_mtime),
                        "LastAcces": time.ctime(os.stat(path_now).st_atime),
                        "Directory": os.path.dirname(path_now),
                        "Size": os.stat(path_now).st_size,
                        "type_file": os.path.splitext(file)[1]  # Extract file extension
                    })

    def json_saver(self):
        with open(self.output_file, "w") as json_file:
            json.dump(self.details_file, json_file, indent=4)

    def run(self):
        self.spyder_dir()
        time.sleep(2)  # Optional delay
        self.json_saver()
        print(f"Process completed, metadata saved to {self.output_file}")
