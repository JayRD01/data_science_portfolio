from modules.explorer import ExplorerDir
from modules.main_menu import MainMenu


if __name__ == "__main__":
    # Instancia de ExplorerDir
    expl_dr = ExplorerDir()

    # Ejecuta la exploración y crea metadata.json
    expl_dr.run()

    # Configuración del archivo de metadatos
    metadata_file = "metadata.json"

    # Verifica si el archivo existe antes de iniciar el menú
    import os
    if not os.path.exists(metadata_file):
        print(f"Error: {metadata_file} not found.")
    else:
        # Ejecuta el menú interactivo
        menu = MainMenu(metadata_file=metadata_file)
        menu.handle_input()
