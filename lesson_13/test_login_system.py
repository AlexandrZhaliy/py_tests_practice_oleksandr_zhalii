from lesson_13.homework_13 import log_event
from unittest.mock import patch, MagicMock

# ======================== positive test for success status =================================
def test_log_event_success():
    with patch("lesson_13.homework_13.logging.getLogger") as mock_logger:
        logger = MagicMock()
        mock_logger.return_value = logger
        log_event("Alex", "success")
        logger.info.assert_called_once_with(
            "Login event - Username: Alex, Status: success"
        )

        logger.warning.assert_not_called()
        logger.error.assert_not_called()

# ======================== positive test for expired status =================================

def test_log_event_expired():
    with patch("lesson_13.homework_13.logging.getLogger") as mock_logger:
        logger = MagicMock()
        mock_logger.return_value = logger
        log_event("Alex", "expired")
        logger.warning.assert_called_once_with(
            "Login event - Username: Alex, Status: expired"
        )

        logger.info.assert_not_called()
        logger.error.assert_not_called()

# ======================== positive test for failed status =================================
def test_log_event_failed():
    with patch("lesson_13.homework_13.logging.getLogger") as mock_logger:
        logger = MagicMock()
        mock_logger.return_value = logger
        log_event("Alex", "failed")
        logger.error.assert_called_once_with(
            "Login event - Username: Alex, Status: failed"
        )

        logger.info.assert_not_called()
        logger.warning.assert_not_called()

# ========== negative test for status that differs from defined (success, expired, failed) ============================

def test_log_event_unknown_status_logs_error():
    with patch("lesson_13.homework_13.logging.getLogger") as mock_logger:
        logger = MagicMock()
        mock_logger.return_value = logger
        log_event("Alex", "undefined")
        logger.error.assert_called_once_with(
            "Login event - Username: Alex, Status: undefined"
        )

        logger.info.assert_not_called()
        logger.warning.assert_not_called()

# ======================== positive test for empty string (as username: str) =================================
def test_log_event_empty_username():
    with patch("lesson_13.homework_13.logging.getLogger") as mock_logger:
        logger = MagicMock()
        mock_logger.return_value = logger
        log_event("", "success")
        logger.info.assert_called_once_with(
            "Login event - Username: , Status: success"
        )

        logger.warning.assert_not_called()
        logger.error.assert_not_called()