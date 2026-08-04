from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parents[2]   # lesson_14

file1 = BASE_DIR/"initial_data"/"work_with_csv_samples"/"r-m-c.csv"
file2 = BASE_DIR/"initial_data"/"work_with_csv_samples"/"random-michaels.csv"
result = BASE_DIR/"homework_execution"/"resulting-files"/"result_Zhalii.csv"

unique_rows = set()

for file in (file1, file2):
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            unique_rows.add(tuple(row))

with open(result, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(unique_rows)

print(f"Unique rows: {len(unique_rows)}")