from sqlalchemy.orm import DeclarativeBase
from typing import Protocol, runtime_checkable

# Declarative base — imported by all ORM models
class Base(DeclarativeBase):
    """
    Gold plating layer for ORM models.

    This class acts as a thin declarative wrapper that transforms
    regular Python classes into database-mapped entities via SQLAlchemy.
    Think of it as applying a polished finish to raw metal—ready for
    inspection, persistence, and interaction.
    """
    pass


@runtime_checkable
class ORMBaseContract(Protocol):
    """
    Runtime-checkable contract for ORM compatibility.

    This protocol defines a structural expectation: any class that exposes
    an inner class named 'ORMBase' inheriting from SQLAlchemy's DeclarativeBase
    is considered compliant.

    - Enables dynamic validation using isinstance(obj, ORMBaseContract)
    - Promotes duck typing and modular architecture
    - Ideal for test suites, preview runners, and audit-friendly pipelines

    Use this to enforce declarative structure without requiring inheritance,
    making your ORM layers more flexible and inspectable.
    """
    class ORMBase(DeclarativeBase): ...
