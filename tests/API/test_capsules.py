import requests

from tests.API.helpers.assertions import Assertions
import pytest
from requests import Response

@pytest.mark.capsules
def test_get_all_capsules(capsules_client):
    """
    Проверяем, что ответ пришел массивом
    """
    response: Response = capsules_client.list_capsules()
    Assertions.assert_json_is_list(response)
    Assertions.assert_status_code(response, 200)