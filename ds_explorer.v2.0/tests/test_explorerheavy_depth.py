import unittest
import os
import shutil
from modules.explorer_scandir import ExplorerHeavy


class TestExplorerHeavyDepth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a controlled environment for testing."""
        cls.root_path = "test_environment"
        cls.max_depth = 3

        # Directory structure
        structure = [
            "level1",
            "level1/level2",
            "level1/level2/level3",
            "level1/level2/level3/level4",
            "level1/level2/level3/level4/level5",
        ]

        # Create directories
        for path in structure:
            dir_path = os.path.join(cls.root_path, path)
            os.makedirs(dir_path, exist_ok=True)

    def test_explore_max_depth(self):
        """
        Verify that ExplorerHeavy does not explore beyond the specified max_depth.
        """
        explorer = ExplorerHeavy(
            root_path=self.root_path, max_depth=self.max_depth)
        visited_dirs, _ = explorer.run()

        # Direct check for directories exceeding max_depth
        over_depth_dirs = [
            dir_path for dir_path in visited_dirs
            if (dir_path.count(os.sep) - self.root_path.count(os.sep)) > self.max_depth
        ]

        self.assertEqual(len(over_depth_dirs), 0,
                         f"Explorer went beyond max_depth: {over_depth_dirs}")

    @classmethod
    def tearDownClass(cls):
        """Clean up the test environment after tests."""
        if os.path.exists(cls.root_path):
            shutil.rmtree(cls.root_path)
            print("Test environment cleaned up.")


if __name__ == "__main__":
    unittest.main()
