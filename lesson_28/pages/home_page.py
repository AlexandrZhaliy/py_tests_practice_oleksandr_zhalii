from playwright.sync_api import Page, Locator


class HomePage:
    """Page is displayed for yet unauthorized user"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def sign_up_button(self) -> Locator:
        return self.page.get_by_role("button", name="Sign up")
