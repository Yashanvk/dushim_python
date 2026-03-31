import pytest
from tests.UI.pages.login_page import LoginPage


@pytest.fixture
def authorized_page(page, config):
    login_page = LoginPage(page, config.ui_url)
    login_page.open_login_page()
    login_page.login(config.username, config.password)
    return page
