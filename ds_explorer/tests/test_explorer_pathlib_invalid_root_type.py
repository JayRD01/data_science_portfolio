import unittest
from src.core.implementations.pathlib_strategy import StrategyPathlib

class TestExplorerPathlibInvalidRooType(unittest.TestCase):
    def test_root_not_str_or_path_raises_type_error(self):
        with self.assertRaises(TypeError):
            StrategyPathlib().explorer_strat(root=123)
