import logging
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_DIR = Path(__file__).resolve().parents[2]
XML_FILE = BASE_DIR/"initial_data"/"work_with_xml_samples"/"groups.xml"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def get_incoming_by_group_number(xml_file: Path, group_number: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == group_number:
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text
            return None
    return None

if __name__ == "__main__":
    group_number = input("Enter group number: ")

    result = get_incoming_by_group_number(XML_FILE, group_number)

    if result is not None:
        logger.info(
            "Group %s -> timingExbytes/incoming = %s",
            group_number,
            result
        )
    else:
        logger.info("Group %s not found", group_number)