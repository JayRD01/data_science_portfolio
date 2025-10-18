import unittest
import os
from src.generator_contract import InfoContract
from src.generator_run import generatorBuilder

class TestCsvReplacement(unittest.TestCase):
    def _get_creation_time(self, path: str) -> float:
        """
        Returns the file's creation timestamp.
        On Windows, this is reliable as the actual creation time.
        On Unix-based systems, it may reflect metadata changes instead.
        """
        return os.stat(path).st_ctime

    def test_csv_file_is_replaced(self):
        path = os.path.abspath(os.path.join(os.getcwd(), 'data', 'random_data.csv'))
        config = InfoContract(rows=100_000, cols=6, missingdata=0.2)
        generator = generatorBuilder(random=config)

        before = self._get_creation_time(path)
        generator.dataframe_gen()
        after = self._get_creation_time(path)

        self.assertNotEqual(before, after, "Creation time did not change. File was not replaced.")

if __name__ == "__main__":
    unittest.main()
