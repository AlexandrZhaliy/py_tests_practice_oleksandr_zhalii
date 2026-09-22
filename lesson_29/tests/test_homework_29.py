"""
Tests that verify the application works correctly, as required by the
homework:
  - connection to the database
  - insert, update and delete of records
  - selecting data from the database
"""
from sqlalchemy import text

from models import Result


def test_connection_to_database(db_session):
    """The DB connection is alive and can execute a trivial query."""
    result = db_session.execute(text("SELECT 1")).scalar()
    assert result == 1


def test_insert_record(db_session):
    row = Result(task_name="test_insert", value=42)
    db_session.add(row)
    db_session.commit()

    saved = db_session.query(Result).filter_by(task_name="test_insert").first()
    assert saved is not None
    assert saved.value == 42


def test_update_record(db_session):
    row = Result(task_name="test_update", value=1)
    db_session.add(row)
    db_session.commit()

    row.value = 100
    db_session.commit()

    updated = db_session.query(Result).filter_by(task_name="test_update").first()
    assert updated.value == 100


def test_delete_record(db_session):
    row = Result(task_name="test_delete", value=7)
    db_session.add(row)
    db_session.commit()
    row_id = row.id

    db_session.delete(row)
    db_session.commit()

    deleted = db_session.query(Result).filter_by(id=row_id).first()
    assert deleted is None


def test_select_multiple_records(db_session):
    db_session.add_all(
        [
            Result(task_name="test_select_a", value=1),
            Result(task_name="test_select_b", value=2),
            Result(task_name="test_select_c", value=3),
        ]
    )
    db_session.commit()

    rows = (
        db_session.query(Result)
        .filter(Result.task_name.like("test_select_%"))
        .order_by(Result.task_name)
        .all()
    )
    assert [r.task_name for r in rows] == ["test_select_a", "test_select_b", "test_select_c"]
    assert [r.value for r in rows] == [1, 2, 3]
