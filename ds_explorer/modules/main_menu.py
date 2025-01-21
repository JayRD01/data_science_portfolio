import os
import json
from modules.abs_menu import AbstractMenu
import msvcrt # Import msvcrt (Microsoft C Runtime), used for Windows-specific keyboard input handling

class MainMenu(AbstractMenu):
    def __init__(self, metadata_file):
        self.metadata_file = os.path.abspath(metadata_file)  # Ruta absoluta para metadata.json
        self.buttons = ["Options", "Tools", "Exit"]
        self.menus = {
            "Options": ["[1] View Files", "[2] Edit File", "[3] Exit"],
            "Tools": ["[1] Analyze Data"],
            "Exit": ["[1] Confirm Exit", "[2] Cancel"]
        }
        self.selected_button = 0

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display(self, show_submenu=False):
        self.clear_screen()
        for i, button in enumerate(self.buttons):
            if i == self.selected_button:
                print(f"\033[42m\033[1m  {button.upper()}  \033[0m", end=" ")
            else:
                print(f"  {button}  ", end=" ")
        print("\n" + "=" * 50)
        if show_submenu:
            sub_menu = self.menus[self.buttons[self.selected_button]]
            print("\nSubmenu Options:")
            for option in sub_menu:
                print(f"  {option}")

    def handle_input(self):
        while True:
            self.display()
            print("\nUse arrow keys to navigate. Press Enter to select. Esc to exit.")
            key = msvcrt.getch()
            if key == b'\x1b':  # Esc key
                print("Goodbye!")
                break
            elif key == b'\xe0':  # Arrow keys
                arrow = msvcrt.getch()
                if arrow == b'M':  # Right arrow
                    self.selected_button = (self.selected_button + 1) % len(self.buttons)
                elif arrow == b'K':  # Left arrow
                    self.selected_button = (self.selected_button - 1) % len(self.buttons)
            elif key == b'\r':  # Enter key
                self.execute_action()

    def execute_action(self):
        action = self.buttons[self.selected_button]
        if action == "Options":
            self.display_options()
        elif action == "Tools":
            print("\n[Analyze Data] is under construction!")
            input("\nPress any key to return...")
        elif action == "Exit":
            print("Goodbye!")
            exit()

    def display_options(self):
        while True:
            self.display(show_submenu=True)
            choice = input("\nChoose an option: ")
            if choice == "1":  # View Files
                self.view_files()
            elif choice == "3":  # Exit
                break

    def view_files(self):
        try:
            if not os.path.exists(self.metadata_file):
                raise FileNotFoundError(f"File {self.metadata_file} does not exist.")

            with open(self.metadata_file, "r") as f:
                metadata = json.load(f)

            print("\nMetadata Contents:")
            for item in metadata:
                print(f"\nFile Name: {item['FileName']}")
                print(f"  Created: {item['Created']}")
                print(f"  Modified: {item['Modified']}")
                print(f"  Last Accessed: {item['LastAcces']}")
                print(f"  Directory: {item['Directory']}")
                print(f"  Size: {item['Size']} bytes")
                print(f"  File Type: {item['type_file']}")

        except Exception as e:
            print(f"Error loading metadata: {e}")
        input("\nPress any key to return...")
