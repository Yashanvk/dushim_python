

from tests.API.helpers.assertions import Assertions
import pytest
from requests import Response

@pytest.mark.capsules
def test_get_all_capsules(capsules_client):
    """
    Проверяем, что ответ пришел массивом
    """
    response: Response = capsules_client.get_capsule()
    Assertions.assert_json_is_list(response)
    Assertions.assert_status_code(response, 200)

@pytest.mark.capsules
def test_get_capsule_serial(capsules_client):
    """
    Проверяем, что вернули соответствующий объект
    """
    capsules_serial:str="C102"
    response: Response = capsules_client.get_capsule(capsules_serial)
    Assertions.assert_status_code(response, 200)
    Assertions.assert_json_has_key_value(response,  "capsule_serial", capsules_serial)
    Assertions.assert_json_is_dict(response)

@pytest.mark.capsules
def test_get_capsule_upcoming(capsules_client):
    """
        Проверяем, что вернули соответствующий объект
    """
    response: Response = capsules_client.test_get_capsule_upcoming()
    Assertions.assert_status_code(response, 200)
    response = response.json()
    Assertions.assert_dict_has_key_value(response[0], "original_launch", None)
    Assertions.assert_dict_has_key_value(response[-1], "original_launch", None)

@pytest.mark.capsules
def test_get_capsule_past(capsules_client):
    """
        Проверяем, что вернули соответствующий объект
    """
    response: Response = capsules_client.test_get_capsule_past()
    Assertions.assert_status_code(response, 200)
    response = response.json()
    Assertions.assert_dict_has_key_and_value_not_nan_not_null(response[0], "original_launch")
    Assertions.assert_dict_has_key_and_value_not_nan_not_null(response[-1], "original_launch")
