from __future__ import annotations

import unittest
import tempfile
import os
import pathlib
import fs
from fs import errors as fserrors

from src.core.contracts.file_info_contract import FileInfo
from src.core.contracts.strategy_contract import StrategyMethodContract
from src.core.implementations.os_strategy_run import StrategyOs
from src.core.implementations.fs_strategy_run import StrategyFS
from src.core.implementations.pathlib_strategy import StrategyPathlib
from src.utils.root_path import RootPath


class TestStrategies(unittest.TestCase):
    def setUp(self):
        # Real OS temporary folder
        self._tmp = tempfile.TemporaryDirectory()
        self.rootpath = self._tmp.name
        os.makedirs(os.path.join(self.rootpath, 'subdir_os'))
        pathlib.Path(self.rootpath, 'subdir_pathlib').mkdir(parents=True, exist_ok=True)

        self.fsys = fs.open_fs(f'osfs://{self.rootpath}')
        self.fsys.makedir('subdir_fs', recreate=True)
        pathlib.Path(self.rootpath, 'hello.txt').write_text('hi', encoding='utf-8')
        pathlib.Path(self.rootpath, '.here').write_text('marker', encoding='utf-8')

        # Strategies under test
        self.strategies = [
            StrategyOs(),
            StrategyFS(path=self.fsys, include_dirs=True),
            StrategyPathlib(),
        ]

        # Project root resolver (via marker file)
        self.root = RootPath(marker='.here', root='.')

    def tearDown(self):
        self.fsys.close()
        self._tmp.cleanup()

    def _resolve_root(self, strat) -> str:
        # For the FS-backed strategy use ".", others use the temp root path
        return '.' if isinstance(strat, StrategyFS) else self.rootpath

    def test_runtime_check(self):
        for strat in self.strategies:
            self.assertIsInstance(
                strat, StrategyMethodContract,
                f"DuckTyping test has been failed {type(strat).__name__}"
            )

    def test_lists_base_entries(self):
        for strat in self.strategies:
            root = self._resolve_root(strat)
            with self.subTest(strategy=type(strat).__name__, root=root):
                items = strat.explorer_strat(root=root)
                names = {i.name for i in items}

                self.assertTrue(all(isinstance(i, FileInfo) for i in items))
                self.assertIn("hello.txt", names)
                self.assertIn("subdir_os", names)
                self.assertIn("subdir_fs", names)
                self.assertIn("subdir_pathlib", names)

    # @unittest.skip('Work in progress')
    def test_explorer_nonexistent_root(self):
        for strat in self.strategies:
            root = self._resolve_root(strat)
            with self.subTest(strategy=type(strat).__name__, root=root):
                items = strat.explorer_strat(root="does-not-exist")
                self.assertEqual(items, [])

    def test_explorer_invalid_path_raises(self):
        # Always-invalid across platforms (NUL char variants)
        bad_inputs = ["\x00", "\x00bad", "bad\x00", "bad\x00path", "/\x00", "\\\x00"]

        # Windows-only reserved names
        if os.name == "nt":
            bad_inputs += ["con", "aux", "nul", "prn", "com1", "lpt1", "CON:", "NUL", "PRN"]

        for strat in self.strategies:
            for bad in bad_inputs:
                with self.subTest(strategy=type(strat).__name__, invalid_path=repr(bad)):
                    with self.assertRaises(Exception) as cm:
                        strat.explorer_strat(bad)

                    self.assertIsInstance(
                        cm.exception,
                        (fserrors.InvalidPath, ValueError, OSError),
                        msg=f"Unexpected exception type for {type(strat).__name__}: {type(cm.exception).__name__}",
                    )

    # @unittest.skip('Work in progress')
    def test_explorer_non_string_root_raises(self):
        for strat in self.strategies:
            with self.subTest(strategy=type(strat).__name__):
                with self.assertRaises(TypeError):
                    strat.explorer_strat(root=123)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()

# Run the test suite with unittest’s discovery, suppressing warnings and buffering output.
# Variant A (verbose): shows each test name and status (uncomment to use)
# python -m unittest discover -s tests -p "test_*.py" -b -v

# Variant B (quiet): minimal output; hides prints unless a test fails (this one runs)
# python -W ignore -m unittest discover -s tests -p "test_*.py" -b -q

# Flags explained:
# -W ignore       → silence all Python warnings for this run
# -m unittest     → run the unittest module as a script
# discover        → auto-discover tests
# -s tests        → search in the 'tests' directory
# -p "test_*.py"  → match test files by pattern
# -b              → buffer stdout/stderr; only show prints on failures/errors
# -v              → verbose output (list every test with OK/FAIL)  [use either -v or -q, not both]
# -q              → quiet output (minimal)
