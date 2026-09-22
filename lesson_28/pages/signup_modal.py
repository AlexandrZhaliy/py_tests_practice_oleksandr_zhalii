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
