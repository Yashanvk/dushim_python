import pytest
import requests

from tests.API.helpers.assertions import Assertions
from requests import Response

@pytest.mark.todos
def test_todos(todos_api_client):
    """
    Проверяем, что пришел массив с todos
    """
    response : Response = todos_api_client.get_all_todos()
    Assertions.assert_status_code(response, 200)
    response = response.json()
    Assertions.assert_dict_has_key_and_value_not_nan_not_null(response[0], 'id')

@pytest.mark.todos
def test_todos_id(todos_api_client):
    """
    Проверяем, что пришел объект с todos
    """
    response: Response = todos_api_client.get_id_todos(193)
    Assertions.assert_json_has_key_value(response, 'id', 193)
    Assertions.assert_status_code(response, 200)
