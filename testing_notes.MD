## [BUG] Excessive traversal after reaching max_depth with os.scandir()

- **Problem description:**
  When using `os.scandir()` to traverse directories, the program continued exploring subdirectories even after reaching the maximum depth (`max_depth`) because it used `continue`, which does not stop recursion.

- **Observed symptom:**
  The program kept traversing directories beyond the allowed depth, unnecessarily consuming system resources.

- **Solution applied:**
  Replaced `continue` with `return` to stop recursion immediately once `max_depth` is reached.

- **Affected file:** `modules/explorer_heavy.py`

- **Related test:** `tests/test_leaf_node_depth.py`