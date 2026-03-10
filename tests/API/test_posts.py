from tests.API.helpers.assertions import Assertions
import pytest
from requests import Response


@pytest.mark.posts
def test_posts(posts_api_client):
    """
    Проверяем, что пришел массив с posts
    """
    response : Response = posts_api_client.get_all_posts()
    Assertions.assert_status_code(response, 200)
    response = response.json()
    Assertions.assert_dict_has_key_and_value_not_nan_not_null(response[0], 'id')

@pytest.mark.posts
def test_get_nonexistent_post(posts_api_client):
    nonexistent_id = 999999
    response: Response = posts_api_client.get_id_posts(nonexistent_id)
    Assertions.assert_status_code(response, 404)