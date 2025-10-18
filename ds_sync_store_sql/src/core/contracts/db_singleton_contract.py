from typing import Protocol, runtime_checkable
from sqlalchemy.orm import Session

@runtime_checkable
class DBSingletonContract(Protocol):
    """
    - Contract for database access layer.

    This protocol defines the expected interface for any class that acts
    as a database singleton. It allows runtime validation using:

        isinstance(obj, DBSingletonContract)

    - Promotes duck typing and modular architecture  
    - Ideal for test suites, preview runners, and audit-friendly pipelines  
    - Keeps your DB layer inspectable and swappable
    """

    # Expected method to obtain a session (can be wrapped in a context manager)
    def get_session(self) -> Session:
        """Returns a SQLAlchemy session object. Should be wrapped in a context manager."""
        ...
