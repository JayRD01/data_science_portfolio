import unittest
from unittest.mock import MagicMock
from fs.memoryfs import MemoryFS
from src.core.implementations.fs_strategy_run import StrategyFS

class TestStrategyFSBehavior(unittest.TestCase):
    def setUp(self):
        self.fs = MemoryFS()
        self.fs.makedir('dir_should_be_skipped') 
        self.fs.create('file_should_be_included.txt')
        self.fs.create('bad_file.txt')  
        self.strategy_include_off = StrategyFS(path=self.fs, include_dirs=False)
        self.strategy_include_on = StrategyFS(path=self.fs, include_dirs=True)

    def tearDown(self):
        self.fs.close()

    def test_excludes_directories_when_include_dirs_false(self):
        result = self.strategy_include_off.explorer_strat(root='.')
        names = [entry.name for entry in result]
        self.assertIn('file_should_be_included.txt', names)
        self.assertNotIn('dir_should_be_skipped', names)

    def test_size_fallback_to_zero_on_error(self):
        result = self.strategy_include_on.explorer_strat(root='.')
        sizes = [entry.size for entry in result]
        self.assertIn(0, sizes)

    def test_mocked_entry_triggers_typeerror_fallback(self):
        mock_entry = MagicMock()
        mock_entry.name = 'mocked.txt'
        mock_entry.is_dir = False
        mock_entry.get.return_value = ['not', 'an', 'int']  

        self.strategy_include_on.path.scandir = MagicMock(return_value=[mock_entry])

        result = self.strategy_include_on.explorer_strat(root='.')
        self.assertEqual(result[0].size, 0)  
