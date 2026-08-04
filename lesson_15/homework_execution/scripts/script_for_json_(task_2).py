import json
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

JSON_FOLDER = BASE_DIR / "initial_data" / "work_with_json"
LOG_FILE = (
    BASE_DIR /"homework_execution"/"resulting-files"/"json_Zhalii.log"
)

logger = logging.getLogger("json_validator")
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def validate_json_files(folder: Path):
    if not folder.exists():
        print(f"Folder not found: {folder}")
        return
    valid_count = 0
    invalid_count = 0

    for json_file in folder.glob("*.json"):
        try:
            with open(json_file, "r", encoding="utf-8") as file:
                json.load(file)

            print(f"[OK] {json_file.name}")
            valid_count += 1

        except json.JSONDecodeError as error:
            logger.error("%s - %s", json_file.name, error)
            print(f"[INVALID] {json_file.name}")
            invalid_count += 1

        except Exception as error:
            logger.error("%s - %s", json_file.name, error)
            print(f"[ERROR] {json_file.name}")
            invalid_count += 1
    print(f"\nValid: {valid_count}")
    print(f"Invalid: {invalid_count}")

if __name__ == "__main__":
    validate_json_files(JSON_FOLDER)