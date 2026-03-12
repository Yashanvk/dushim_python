import pytest
import re
from playwright.sync_api import expect

@pytest.mark.ui
def test_login(page, config):
    """
        Успешный логин
    """
    page.goto(config.ui_url)
    #page.wait_for_timeout(10000)
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile(".*inventory"))






