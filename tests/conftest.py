# conftest.py
import os
import logging
import pytest
from dotenv import load_dotenv
from tests.API.api_frame.spacex_api_capsules import Capsules


# ✅ Загружаем .env один раз при старте pytest
load_dotenv()

# 🔧 Логирование
def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("test.log")
        ]
    )
    logging.info("Логирование инициализировано через conftest.py")

# 🌐 BASE_URL из .env
@pytest.fixture(scope="session")
def get_base_url() -> str:
    base_url = os.getenv("BASE_URL")
    if not base_url:
        pytest.fail("BASE_URL не задан в .env")
    return base_url

# 📦 API-клиент
@pytest.fixture()
def capsules_client(get_base_url):
    return Capsules(get_base_url)

# 🧭 Playwright Page
@pytest.fixture()
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
