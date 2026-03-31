import pytest
import re
from playwright.sync_api import expect
from tests.UI.pages.login_page import LoginPage

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
    login_page = LoginPage(page, config.ui_url)
    login_page.open_login_page()
    login_page.login(username, config.password)
    expect(page).to_have_url(re.compile(".*inventory"))


@pytest.mark.ui
def test_login_fixture(page, authorized_page):
    """
        Успешный логин
    """
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
    login_page = LoginPage(page, config.ui_url)
    login_page.open_login_page()
    login_page.login(username, password)
    expect(login_page.error).to_contain_text(error_text)
    