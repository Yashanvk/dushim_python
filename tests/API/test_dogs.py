from tests.API.helpers.assertions import Assertions
import pytest
from requests import Response

@pytest.mark.dogs
def test_get_all_dogs(dogs_client):
    """
    Проверяем, что ответ пришел массивом
    """
    response: Response = dogs_client.get_all_dogs()
    Assertions.assert_json_is_list(response)
    Assertions.assert_status_code(response, 200)

@pytest.mark.dogs
def test_get_all_dogs_error(dogs_client):
    """
    Проверяем на несуществующий эндпоинт возращает 404
    """
    response: Response = dogs_client.get_all_dogs_error()
    Assertions.assert_status_code(response, 404)

