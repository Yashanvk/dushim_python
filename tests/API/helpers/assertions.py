from requests import Response
from typing import Any

class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code: int) -> None:
        """
        Проверяет, что статус-код ответа соответствует ожидаемому.

        :param response: Объект ответа от requests.
        :param expected_code: Ожидаемый HTTP статус-код.
        :raises AssertionError: Если статус-код отличается от ожидаемого.
        """
        actual_code: int = response.status_code
        assert actual_code == expected_code, \
            f'Ожидался статус код "{expected_code}", но получен {actual_code}. Тело ответа {response.text}'

    @staticmethod
    def assert_json_has_key(response: Response, key: str) -> None:
        """
        Проверяет наличие ключа в JSON-ответе.

        :param response: Объект ответа от requests.
        :param key: Ключ, который должен присутствовать в JSON.
        :raises AssertionError: Если ключ отсутствует.
        """
        response_json: dict[str, Any] = response.json()
        assert key in response_json, \
            f'Ключ "{key}" отсутствует в JSON-ответе'

    @staticmethod
    def assert_json_has_key_value(response: Response, key: str, expected_value: Any) -> None:
        """
        Проверяет наличие ключа и соответствие его значения ожидаемому.

        :param response: Объект ответа от requests.
        :param key: Ключ, который должен присутствовать в JSON.
        :param expected_value: Ожидаемое значение по ключу.
        :raises AssertionError: Если ключ отсутствует или значение отличается.
        """
        response_json: dict[str, Any] = response.json()
        assert key in response_json, f'Ключ "{key}" отсутствует в JSON-ответе'
        actual_value: Any = response_json[key]
        assert actual_value == expected_value, (
            f'Значение по ключу "{key}" не соответствует ожиданию.\n'
            f'Ожидалось: {expected_value}\nПолучено: {actual_value}'
        )

    @staticmethod
    def assert_json_is_list(response: Response) -> None:
        """
        Проверяет, что JSON-ответ является списком.

        :param response: Объект ответа от requests.
        :raises AssertionError: Если JSON не является списком.
        """
        response_json: Any = response.json()
        assert isinstance(response_json, list), \
            f'Ожидался тип "list", но получен {type(response_json).__name__}. Тело ответа: {response.text}'

    @staticmethod
    def assert_json_is_dict(response: Response) -> None:
        """
        Проверяет, что JSON-ответ является dict'ом

        :param response: Объект ответа от requests.
        :raises AssertionError: Если JSON не является dict
        """
        response_json: Any = response.json()
        assert isinstance(response_json, dict), \
            f'Ожидался тип "dict", но получен {type(response_json).__name__}. Тело ответа: {response.text}'

    @staticmethod
    def assert_dict_has_key_value(response: dict[str, Any], key: str, expected_value: Any) -> None:
        """
        Проверяет наличие ключа и соответствие его значения ожидаемому.

        :param response: Словарь.
        :param key: Ключ, который должен присутствовать в JSON.
        :param expected_value: Ожидаемое значение по ключу.
        :raises AssertionError: Если ключ отсутствует или значение отличается.
        """
        assert key in response, f'Ключ "{key}" отсутствует в JSON-ответе'
        actual_value: Any = response[key]
        assert actual_value == expected_value, (
            f'Значение по ключу "{key}" не соответствует ожиданию.\n'
            f'Ожидалось: {expected_value}\nПолучено: {actual_value}'
        )

    @staticmethod
    def assert_dict_has_key_and_value_not_nan_not_null(response: dict[str, Any], key: str) -> None:
        """
        Проверяет наличие ключа и что знаяение не пустое

        :param response: Словарь.
        :param key: Ключ, который должен присутствовать в JSON.
        :raises AssertionError: Если ключ отсутствует или значение null
        """
        assert key in response, f'Ключ "{key}" отсутствует в JSON-ответе'
        value: Any = response[key]
        assert value is not None, f'Ключ "{key}" имеет значениие null'