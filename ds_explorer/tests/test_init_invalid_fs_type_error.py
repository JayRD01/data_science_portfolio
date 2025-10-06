import unittest
from src.core.implementations.fs_strategy_run import StrategyFS
import fs

class TestInitInvalidFSTypeError(unittest.TestCase):
    def test_invalid_fs_path_type_error(self):
        with self.assertRaises(TypeError):
            StrategyFS(path=123, include_dirs=True)
            
    def test_invalid_fs_include_dir_type_error(self):
        with self.assertRaises(TypeError):
            StrategyFS(path=fs.open_fs('.'), include_dirs='yes')
            
            

