import allure
from playwright.sync_api import Page, Locator


class SignupModal:
    def __init__(self, page: Page):
        self.page = page

    @property
    def name_input(self) -> Locator:
        return self.page.locator("#signupName")

    @property
    def last_name_input(self) -> Locator:
        return self.page.locator("#signupLastName")

    @property
    def email_input(self) -> Locator:
        return self.page.locator("#signupEmail")

    @property
    def password_input(self) -> Locator:
        return self.page.locator("#signupPassword")

    @property
    def repeat_password_input(self) -> Locator:
        return self.page.locator("#signupRepeatPassword")

    @property
    def register_button(self) -> Locator:
        return self.page.get_by_role("button", name="Register")

    @allure.step("Fill signup form with generated user data")
    def fill_signup_form(self, user_data: dict) -> "SignupModal":
        self.name_input.fill(user_data["name"])
        self.last_name_input.fill(user_data["last_name"])
        self.email_input.fill(user_data["email"])
        self.password_input.fill(user_data["password"])
        self.repeat_password_input.fill(user_data["password"])
        return self

    @allure.step("Submit registration form")
    def submit_registration(self) -> None:
        self.register_button.click()