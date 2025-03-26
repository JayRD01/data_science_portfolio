import os
import json
import stat
import datetime as DT
from modules.abstracted import AbstractedClass


class DataFiles(AbstractedClass):
    def info_files(self):
        """
        Extracts metadata from the files already collected in self.filenames.
        Assumes that another class (like ExplorerHeavy or ExplorerLight) has already populated the sets.
        """
        file_details = []

        for file in self.filenames:
            try:
                if not os.path.exists(file):
                    print(f"Skipping missing file: {file}")
                    continue

                file_stat = os.stat(file)
                file_details.append({
                    "Filename": os.path.basename(file),
                    "Path": file,
                    "Size": file_stat.st_size,
                    "Created": DT.datetime.fromtimestamp(file_stat.st_ctime),
                    "Modified": DT.datetime.fromtimestamp(file_stat.st_mtime),
                    "Permissions": stat.filemode(file_stat.st_mode),
                    "Extension": os.path.splitext(file)[1]
                })

            except Exception as e:
                print(f"Error reading file {file}: {e}")

        return file_details

    def to_json(self, output_file: str = "metadata.json"):
        """
        Saves the file metadata to a JSON file.
        """
        file_details = self.info_files()

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(file_details, f, indent=4, default=str)
            print(f"File metadata saved to: {output_file}")
        except Exception as e:
            print(f"Error saving JSON file: {e}")

    def run(self, output_file: str = "metadata.json"):
        """
        Runs the process assuming self.filenames is already populated.
        """
        file_details = self.info_files()
        self.to_json(output_file)
        return file_details
