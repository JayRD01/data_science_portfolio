import unittest
from src.core.implementations.os_strategy_run import StrategyOs

class TestExplorerOSInvalidRooType(unittest.TestCase):
    def test_root_not_str_or_path_raises_type_error(self):
        with self.assertRaises(TypeError):
            StrategyOs().explorer_strat(root=123)
