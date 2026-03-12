# conftest.py
import os
import logging
from dataclasses import dataclass

import pytest
from dotenv import load_dotenv

# Импорты твоих API-клиентов
from tests.API.api_frame.api_todos import Todos
from tests.API.api_frame.spacex_api_capsules import Capsules
from tests.API.api_frame.posts_api import Posts
from utilities.logging import LastLinesFileHandler


# ---------------------------------------------------------
# 1. Добавляем CLI-параметр для выбора .env файла
# ---------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--env-file",
        action="store",
        default=".env",
        help="Путь к .env файлу (например .env.stage)"
    )


# ---------------------------------------------------------
# 2. Загружаем .env и настраиваем логирование
# ---------------------------------------------------------
def pytest_configure(config):
    """Загружаем .env ДО фикстур и настраиваем логирование."""
    env_file = config.getoption("--env-file")

    if not os.path.exists(env_file):
        raise RuntimeError(f"Файл окружения не найден: {env_file}")

    load_dotenv(env_file)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            LastLinesFileHandler("test.log", encoding="utf-8")
        ]
    )

    logging.info(f".env загружен: {env_file}")


# ---------------------------------------------------------
# 2.1 Логируем ошибки тестов
# ---------------------------------------------------------
def pytest_runtest_logreport(report):
    if report.failed:
        logging.error(f"Ошибка в тесте {report.nodeid}: {report.longrepr}")


# ---------------------------------------------------------
# 3. Конфигурация URL через dataclass
# ---------------------------------------------------------
@dataclass
class Config:
    base_url: str
    todos_url: str
    posts_url: str
    ui_url: str


@pytest.fixture(scope="session")
def config():
    """Создаёт объект конфигурации и валидирует переменные окружения."""
    cfg = Config(
        base_url=os.getenv("BASE_URL"),
        todos_url=os.getenv("TODOS_URL"),
        posts_url=os.getenv("POSTS_URL"),
        ui_url=os.getenv("UI_URL")
    )

    missing = [name for name, value in cfg.__dict__.items() if not value]
    if missing:
        pytest.fail(f"Отсутствуют переменные окружения: {', '.join(missing)}")

    return cfg


# ---------------------------------------------------------
# 4. API-клиенты
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def capsules_client(config):
    return Capsules(config.base_url)


@pytest.fixture(scope="session")
def todos_api_client(config):
    return Todos(config.todos_url)


@pytest.fixture(scope="session")
def posts_api_client(config):
    return Posts(config.posts_url)


# ---------------------------------------------------------
# 5. Playwright Page
# ---------------------------------------------------------
@pytest.fixture()
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
