from playwright.sync_api import TimeoutError, Error, expect, Page

class BasePage:
    """
    базовые методы для работы с ui

    """
    def __init__(self, page: Page, base_url: str, timeout: int=30000):
        self.page = page
        self.timeout = timeout
        self.base_url = base_url

    def open_page(self, endpoint: str="") -> None:
        full_url = f"{self.base_url}/{endpoint}"
        try:
            self.page.goto(full_url, timeout=self.timeout)
            expect(self.page).to_have_url(full_url)
        except TimeoutError:
            raise AssertionError(f"Страница не открылась {full_url}")
        except Error as e:
            raise AssertionError(f"Ошибка при переходе на страницу {full_url}:{str(e)}")
