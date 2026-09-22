from playwright.sync_api import Page, Locator


class GaragePage:
    """Page is displayed for already authorized user"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Garage")