import pytest
import re
from playwright.sync_api import expect

@pytest.mark.ui
@pytest.mark.parametrize("username", [
    ("standard_user"),
    ("problem_user"),
    ("performance_glitch_user"),
    ("error_user"),
    ("visual_user")
])
def test_login(page, config, username):
    """
        Успешный логин
    """
    page.goto(config.ui_url)
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile(".*inventory"))


@pytest.mark.ui
@pytest.mark.parametrize("username,password,error_text", [
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("standard_user", "secret_sauce111", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out"),
])
def test_wrong_login(page, config, username, password, error_text):
    """
       Неуспешный логин, параметризированный тест
    """
    page.goto(config.ui_url)
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    locator = page.locator("[data-test='error']")
    expect(locator).to_contain_text(error_text)


