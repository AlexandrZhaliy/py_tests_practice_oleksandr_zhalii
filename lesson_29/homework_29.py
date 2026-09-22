"""
Homework 29 - "Dockerize everything"

A small application that:
  1. connects to a PostgreSQL database,
  2. does some "work" (here: computes squares of a few numbers),
  3. saves the result of that work into the database.

This script is the "application" referenced in the homework task; the actual
verification (insert / update / delete / select) is done separately by the
pytest tests in tests/test_homework_29.py so the app and its tests stay
independent, like on the lesson_21 example.
"""
from db_connect import wait_for_db, init_db, get_session
from models import Result


def compute_results():
    """Some business logic of "our app": compute squares of 1..5."""
    return [{"task_name": f"square_of_{n}", "value": n * n} for n in range(1, 6)]


def save_results(results: list[dict]) -> None:
    session = get_session()
    try:
        for item in results:
            session.add(Result(task_name=item["task_name"], value=item["value"]))
        session.commit()
        print(f"[homework_29] Saved {len(results)} result(s) to the database.")
    finally:
        session.close()


def print_all_results() -> None:
    session = get_session()
    try:
        rows = session.query(Result).order_by(Result.id).all()
        print("[homework_29] Current contents of the results table:")
        for row in rows:
            print(f"  - {row}")
    finally:
        session.close()


def main():
    wait_for_db()
    init_db()
    results = compute_results()
    save_results(results)
    print_all_results()


if __name__ == "__main__":
    main()