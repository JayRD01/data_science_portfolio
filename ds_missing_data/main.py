# ─────────────────────────────────────────────────────────────
#  Execution Note:
# This script must be executed from the directory where `main.py` is located.
# This ensures that the RootPath class can accurately locate the `.here` marker
# and dynamically resolve the correct project root directory.
# Example:
#   cd path/to/ds_explorer
#   python main.py
# ─────────────────────────────────────────────────────────────
from models.context_manager import StrategyManager
from models.os_strategy import StrategyOs
from models.pathlib_strategy import StrategyPathlib
from models.fs_strategy import StrategyFS
from models.root_path import RootPath
from fs.osfs import OSFS

if __name__ == "__main__":
    root_path_obj = RootPath(marker=".here", root=".")
    root_path = str(root_path_obj)  # ✅ get full path as string
    print(f"Resolved root path: {root_path}")

    # 1) OS Strategy
    manager = StrategyManager(StrategyOs(), root_path_obj)
    results = manager.explorer_strat()
    print(f"[OS] Found {len(results)} entries:")
    for fi in results[:5]:
        print(f" - {fi.name} ({fi.size} bytes)")

    # 2) Pathlib Strategy
    manager.set_config(StrategyPathlib(), root_path_obj)
    results = manager.explorer_strat()
    print(f"\n[Pathlib] Found {len(results)} entries:")
    for fi in results[:5]:
        print(f" - {fi.name} ({fi.size} bytes)")

    # 3) FS Strategy
    osfs = OSFS(root_path)
    manager.set_config(StrategyFS(osfs), root_path_obj)
    results = manager.explorer_strat()
    print(f"\n[FS/OSFS] Found {len(results)} entries:")
    for fi in results[:5]:
        print(f" - {fi.name} ({fi.size} bytes)")
