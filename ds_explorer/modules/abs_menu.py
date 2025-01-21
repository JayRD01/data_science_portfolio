from abc import ABC, abstractmethod

class AbstractMenu(ABC):
    @abstractmethod
    def display(self):
        """Display the menu interface."""
        pass

    @abstractmethod
    def handle_input(self):
        """Handle user input."""
        pass
