#!/bin/sh
set -e

echo "=== Running the application (saves a result to Postgres) ==="
python homework_29.py

echo ""
echo "=== Running the test suite (connect / insert / update / delete / select) ==="
pytest -v
