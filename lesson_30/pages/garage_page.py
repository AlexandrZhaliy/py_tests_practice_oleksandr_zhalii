import allure
from playwright.sync_api import Page, Locator, expect


class GaragePage:
    """Page is displayed for already authorized user"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Garage")

    @allure.step("Assert Garage page is visible")
    def assert_is_open(self) -> None:
        expect(self.heading).to_be_visible()