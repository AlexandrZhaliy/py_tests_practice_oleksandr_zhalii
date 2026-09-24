import random
import string
import pytest

import os
from dotenv import load_dotenv

from pages.home_page import HomePage
from pages.signup_modal import SignupModal
from pages.garage_page import GaragePage


load_dotenv()
BASE_URL = os.getenv("BASE_URL")
assert BASE_URL, "BASE_URL is not configured in .env"

QAUTO_LOGIN = os.getenv("QAUTO_LOGIN")
assert QAUTO_LOGIN, "QAUTO_LOGIN is not configured in .env"

QAUTO_PASSWORD = os.getenv("QAUTO_PASSWORD")
assert QAUTO_PASSWORD, "QAUTO_PASSWORD is not configured in .env"

# =============== Authenticate session ===============
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "http_credentials": {
            "username": QAUTO_LOGIN,
            "password": QAUTO_PASSWORD,
        },
    }


# =============== Page Objects ===============
# NOTE: action logic has been moved into @allure.step-decorated methods on  the page objects for better Allure visibility

@pytest.fixture
def home_page(page):
    return HomePage(page).open(BASE_URL)


@pytest.fixture
def signup_modal(page):
    return SignupModal(page)


@pytest.fixture
def garage_page(page):
    return GaragePage(page)


# =============== Data ===============
@pytest.fixture
def user_data():
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return {
        "name": "Test",
        "last_name": "User",
        "email": f"aqa_{suffix}@example.com",
        "password": "1qaz2WSX3edc!",
    }