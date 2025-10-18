from __future__ import annotations
from contextlib import contextmanager
from typing import Iterator
import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class _DatabaseSingleton:
    _instance: "_DatabaseSingleton | None" = None
    _lock = threading.Lock()
    _init_lock = threading.Lock()  # lock to prevent races during initialization

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    # Magic method __new__ runs *before* the instance is created
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, url: str = "sqlite:///data/products.db", echo: bool = False):
        # Idempotent: avoid re-initializing if the instance already exists
        if hasattr(self, "_initialized") and self._initialized:
            return

        # Double checked locking to be safe in multi-threaded startup
        with self._init_lock:
            if hasattr(self, "_initialized") and self._initialized:
                return

            self.engine = create_engine(
                url,  # if no .db file exists, SQLite creates it automatically
                echo=echo,  # when False, it hides every SQL/interaction from the console (safer defaults)
                future=True,
                connect_args={"check_same_thread": False},  # SQLite + threads
            )

            # Think of sessionmaker as a “messaging app” to talk to the database (like WhatsApp).
            # It needs:
            #   - bind: the “language” allowed in our group (the Engine).
            #   - expire_on_commit: like “auto-delete messages after 24h” — we keep it OFF to retain data after commit.
            #   - class_: like the group rules (no insults, no obscene photos) — here we use Session to enforce ORM rules.
            self.SessionLocal = sessionmaker(
                bind=self.engine,
                expire_on_commit=False,
                class_=Session,
            )
            self._initialized = True

    @contextmanager
    def get_session(self) -> Iterator[Session]:
        """Context manager to obtain/close a session."""
        session = self.SessionLocal()
        try:
            # #### yield (pause 1) | 1st phase dedicated to opening/handing out the DB session
            yield session
            session.commit()
        except Exception:
            # Everything inside this block represents our error handling
            # for operations performed within the DB session
            session.rollback()
            raise
        finally:
            # #### yield (pause 2) | 3rd phase dedicated to closing the DB session
            session.close()
