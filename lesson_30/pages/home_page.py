import allure
from playwright.sync_api import Page, Locator


class HomePage:
    """Page is displayed for yet unauthorized user"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def sign_up_button(self) -> Locator:
        return self.page.get_by_role("button", name="Sign up")

    @allure.step("Open home page")
    def open(self, base_url: str) -> "HomePage":
        self.page.goto(base_url)
        return self

    @allure.step("Open signup modal")
    def open_signup_modal(self) -> None:
        self.sign_up_button.click()