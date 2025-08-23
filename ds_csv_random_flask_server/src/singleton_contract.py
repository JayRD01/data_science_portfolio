from typing import Dict, Type, Any, Protocol, runtime_checkable
from threading import Lock

@runtime_checkable
class SingletonInterface(Protocol):
    """
    Protocol to define the required interface for classes that will be
    decorated with SingletonContract. You can add required methods if needed.
    """
    def __init__(self, *args, **kwds): 
        pass
    # Additional method signatures can be added here if needed
    
class SingletonContract:
    """
    Thread-safe Singleton decorator that ensures only one instance of the
    decorated class exists. It also validates that the class implements the
    SingletonInterface protocol.
    """
    _instances: Dict[Type, Any] = {}  # Stores one instance per class
    _lock: Lock = Lock()              # Ensures thread-safe access

    def __init__(self, cls: Type[SingletonInterface]):
        # Validation 1: Ensure the decorated object is a class
        if not isinstance(cls, type):
            raise TypeError(f"{cls} must be a class type")

        # Validation 2: Ensure the class implements SingletonInterface
        if not issubclass(cls, SingletonInterface):
            raise TypeError(f"{cls.__name__} must implement SingletonInterface")

        self._cls = cls  # Store the class reference for instantiation

    def __call__(self, *args, **kwds) -> SingletonInterface:
        # First check: avoid locking if instance already exists
        if self._cls not in self._instances:
            with self._lock:  # Thread-safe block
                # Second check: ensure no other thread created the instance
                if self._cls not in self._instances:
                    self._instances[self._cls] = self._cls(*args, **kwds)

        # Return the existing or newly created instance
        return self._instances[self._cls]
