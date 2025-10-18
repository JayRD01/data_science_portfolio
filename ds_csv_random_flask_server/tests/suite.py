import unittest
from tests.test_csv_file_is_replaced import TestCsvReplacement

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCsvReplacement))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())