# this module makes the connection to the database
# tables creation is done via init_db()
# same idea as lesson_21/db_connect.py, but adapted to run inside Docker:
# - connection is retried a few times, because the postgres container may still be starting up when the app/tests container starts
# - a fresh Session is handed out per call instead of one shared global session, so tests can use isolated sessions

import os
import time

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def wait_for_db(retries: int = 15, delay: float = 2.0) -> None:
    """
    Tries to open and immediately close a connection to Postgres several
    times before giving up. Needed because `docker run` for the app
    container can start before Postgres inside its own container has
    finished initializing and started accepting connections.
    """
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            with engine.connect() as connection:
                print(f"[db_connect] Database connection successful! (attempt {attempt})")
                return
        except Exception as exc:  # noqa: BLE001 - we want to retry on any driver error
            last_error = exc
            print(f"[db_connect] Attempt {attempt}/{retries} failed: {exc}. Retrying in {delay}s...")
            time.sleep(delay)

    raise ConnectionError(f"Could not connect to the database after {retries} attempts: {last_error}")


def init_db() -> None:
    """Creates all tables described in models.py, if they don't exist yet."""
    Base.metadata.create_all(engine)
    print("[db_connect] Tables created successfully!")


def get_session():
    """Returns a new SQLAlchemy session bound to the configured engine."""
    return SessionLocal()
