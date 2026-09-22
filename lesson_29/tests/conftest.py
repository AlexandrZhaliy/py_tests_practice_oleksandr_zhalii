import sys
import os

# so that `from db_connect import ...` / `from models import ...` works
# the same way it does for homework_29.py, without turning the project
# into an installable package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from db_connect import wait_for_db, init_db, get_session
from models import Result


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Runs once per test session: waits for Postgres and creates tables."""
    wait_for_db()
    init_db()
    yield


@pytest.fixture()
def db_session():
    """
    Gives each test its own SQLAlchemy session and cleans up any `results`
    rows the test created, so tests don't leak data into one another.
    """
    session = get_session()
    yield session
    session.query(Result).filter(Result.task_name.like("test_%")).delete(
        synchronize_session=False
    )
    session.commit()
    session.close()
