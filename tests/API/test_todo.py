from helpers.assertions import Assertions
from helpers.helpers import Helpers
import logging
import pytest
from requests import Response

@pytest.mark.todos
def test_successful_todo(get_todo_data) -> None:
    """
    Проверяет успешное получение списка задач.
    Ожидается статус-код 200 и JSON-ответ в виде списка.
    """
    reg_response: Response = get_todo_data.todo_list()
    logging.info(reg_response.json())
    Assertions.assert_json_is_list(reg_response)
    Assertions.assert_status_code(reg_response, 200)

@pytest.mark.todos
def test_todo_list_invalid_endpoint(get_todo_data) -> None:
    """
    Проверяет обработку некорректного endpoint.
    Ожидается статус-код 404.
    """
    reg_response: Response = get_todo_data.todo_list(valid=False)
    Assertions.assert_status_code(reg_response, 404)

@pytest.mark.todos
@pytest.mark.parametrize("todo_id, expected_status", [
    (1, 200),
    (2, 200),
    (9999, 404),
])
def test_todo_by_id(get_todo_data, todo_id: int, expected_status: int) -> None:
    """
    Проверяет получение задачи по ID.
    Для существующих ID ожидается 200, для несуществующего — 404.
    """
    response: Response = get_todo_data.todo_list(todo_id=todo_id)
    logging.info(response.json())
    Assertions.assert_status_code(response, expected_status)

@pytest.mark.todos
def test_my_todos2(get_todo_data, get_default_count_todo_items: int) -> None:
    """
    Проверяет выбор случайных задач с completed=False.
    Ожидается, что будет выбрано ровно get_default_count_todo_items элементов.
    """
    reg_response: Response = get_todo_data.todo_list()
    selected_items = Helpers.get_random_items_by_completed_flag(
        response=reg_response,
        count=get_default_count_todo_items,
        completed_flag=False
    )
    logging.info(f"Количество выбранных элементов: {len(selected_items)}")
    assert len(selected_items) == get_default_count_todo_items
