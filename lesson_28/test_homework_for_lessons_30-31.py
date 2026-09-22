from playwright.sync_api import expect


def test_user_registration(submit_registration, garage_page):
    """Successfully authorized user is able to see the Garage page."""
    expect(garage_page.heading).to_be_visible()