from tests.UI.pages.base_page import BasePage, Page

class LoginPage(BasePage):
    """
    методы работы с login_page
    """

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error = page.locator("[data-test='error']")

    def open_login_page(self):
        self.open_page()

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error.inner_text()

