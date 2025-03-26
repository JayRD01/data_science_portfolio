from modules.explorer_scandir import ExplorerHeavy
from modules.explorer_walk import ExplorerLight
from modules.tree_builder import TreeBuilder
from modules.data_files import DataFiles

if __name__ == "__main__":
    # --- User-configurable settings ---
    root_path = "/home/"
    max_depth = 3
    blocklist = [".git", "__pycache__", "node_modules"]
    output_json = "metadata.json"

    # --- Choose explorer mode ---
    # Set to True for ExplorerLight (os.walk), False for ExplorerHeavy (os.scandir)
    # Note: os.scandir is faster, more efficient, and ideal for deep directory searches.
    use_light = False

    # --- Initialize the selected explorer ---
    if use_light:
        print("Using ExplorerLight (os.walk)")
        explorer = ExplorerLight(root_path=root_path, max_depth=max_depth)
    else:
        print("Using ExplorerHeavy (os.scandir)")
        explorer = ExplorerHeavy(root_path=root_path, max_depth=max_depth)

    # --- Run directory exploration ---
    visited_dirs, filenames = explorer.run()
    print(f"Visited directories: {len(visited_dirs)}")

    # --- TREE DISPLAY (optional) ---
    """
    tree = TreeBuilder(root_path=root_path, max_depth=max_depth)
    print(f"Directory structure for: {root_path}")
    tree.run(visited_dir=visited_dirs, root_path=root_path, blocklist=blocklist)
    """

    # --- File metadata extraction ---
    detailer = DataFiles(root_path=root_path,
                         max_depth=max_depth, output_file=output_json)
    detailer.visited_dir = visited_dirs
    detailer.filenames = filenames

    metadata = detailer.run(output_json)

    # --- Summary ---
    print(f"File metadata saved in: {output_json}")
    print(f"Total files detailed: {len(metadata)}")
