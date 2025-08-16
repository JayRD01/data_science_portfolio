# main.py
from models.interfaces import StrategyManager
from models.os_strategy import StrategyOs
from models.pathlib_strategy import StrategyPathlib
from models.fs_strategy import StrategyFS
from fs.osfs import OSFS

if __name__ == "__main__":
    # 1) Stategy Os System
    manager = StrategyManager(StrategyOs())
    results = manager.explorer_strat(".")
    print(f"[OS] Found {len(results)} entries:")
    for fi in results[:5]:
        print(f" - {fi.name} ({fi.size} bytes)")

    # 2) Strategy Pathlib
    manager.set_strategy(StrategyPathlib())
    results = manager.explorer_strat(".")
    print(f"\n[Pathlib] Found {len(results)} entries:")
    for fi in results[:5]:
        print(f" - {fi.name} ({fi.size} bytes)")

    # 3) Strategy PyFilesystem2
    osfs = OSFS(".")
    manager.set_strategy(StrategyFS(osfs))
    results = manager.explorer_strat("/")
    print(f"\n[FS/OSFS] Found {len(results)} entries:")
    for fi in results[:5]:
        print(f" - {fi.name} ({fi.size} bytes)")
