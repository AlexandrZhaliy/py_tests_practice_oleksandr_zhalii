import logging
from datetime import datetime

KEY = "TSTFEED0300|7E3E|0400"
logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def analyze_heartbeat(filename):
    filtered_log = []

    # ============ required logs filtering ===================
    with open(filename, "r") as file:
        for line in file:
            if KEY in line:
                filtered_log.append(line)

    # ================= logs analysis =======================
    for current_line, next_line in zip(filtered_log, filtered_log[1:]):
        current_position = current_line.find("Timestamp ")
        current_timestamp = current_line[
            current_position + len("Timestamp "):
            current_position + len("Timestamp ") + 8
        ]

        next_position = next_line.find("Timestamp ")
        next_timestamp = next_line[
            next_position + len("Timestamp "):
            next_position + len("Timestamp ") + 8
        ]

        current_time = datetime.strptime(current_timestamp, "%H:%M:%S")
        next_time = datetime.strptime(next_timestamp, "%H:%M:%S")

        heartbeat = (current_time - next_time).total_seconds()

        if 31 < heartbeat < 33:
            logging.warning(
                f"Heartbeat is {heartbeat} seconds at {current_timestamp}"
            )
        elif heartbeat >= 33:
            logging.error(
                f"Heartbeat is {heartbeat} seconds at {current_timestamp}"
            )

analyze_heartbeat("hblog.txt")
