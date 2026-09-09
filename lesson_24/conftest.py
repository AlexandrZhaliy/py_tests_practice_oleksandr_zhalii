import logging
from pathlib import Path
import pytest
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "http://127.0.0.1:8080"

# ==================== logging =======================
LOG_FILE = Path(__file__).parent / "test_search.log"

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)

logger = logging.getLogger(__name__)

# =============== Auth fixture ====================
@pytest.fixture(scope="class")
def auth_session(request):
    session = requests.Session()
    logger.info("Starting authentication")
    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    session.headers.update({
        "Authorization": f"Bearer {access_token}"
    })

    request.cls.session = session

    logger.info("Authentication successful")
    yield session
    session.close()
    logger.info("Session closed")