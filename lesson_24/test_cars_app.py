import logging
import pytest


BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger(__name__)

# ================== Tests ========================
@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 10),
            ("engine_volume", 7),
            ("brand", 3),
            ("price", 15),
            ("year", 20),
            (None, 5),
        ]
    )
    def test_search_cars(self, sort_by, limit):
        logger.info(
            "Searching cars: sort_by=%s, limit=%s",
            sort_by,
            limit
        )
        params = {
            "sort_by": sort_by,
            "limit": limit
        }
        response = self.session.get(
            f"{BASE_URL}/cars",
            params=params
        )
        logger.info(
            "Response status: %s",
            response.status_code
        )
        assert response.status_code == 200
        cars = response.json()
        assert isinstance(cars, list)
        assert len(cars) == limit

        if sort_by:
            values = [car[sort_by] for car in cars]
        else:
            values = [car["brand"] for car in cars]
        assert values == sorted(values)

        logger.info(
            "Test passed: sort_by=%s, limit=%s",
            sort_by,
            limit
        )