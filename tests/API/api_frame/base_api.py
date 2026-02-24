import requests
import logging
from typing import Any, Dict, Optional

class BaseApi:
    def __init__(self, base_url: str) -> None:
        """
        Инициализирует экземпляр API-клиента.

        :param base_url: Базовый URL для всех запросов.
        """
        self.base_url: str = base_url
        self.session: requests.Session = requests.session()

    def _send_request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        """
        Отправляет HTTP-запрос с указанным методом и параметрами.

        :param method: Метод HTTP-запроса ('GET', 'POST', 'PUT' и т.д.).
        :param endpoint: Эндпоинт (добавляется к base_url).
        :param kwargs: Дополнительные параметры для requests.request (headers, json, params и т.д.).
        :return: Объект ответа requests.Response.
        """
        url: str = f'{self.base_url}{endpoint}'
        try:
            response: requests.Response = self.session.request(method, url, **kwargs)
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка запроса: {e}")
            raise

        if response.status_code >= 400:
            logging.warning(f"HTTP {response.status_code}: {response.text}")

        return response

    def get_request(self, endpoint: str, **kwargs: Any) -> requests.Response:
        """
        Выполняет GET-запрос к указанному endpoint.

        :param endpoint: Эндпоинт.
        :param kwargs: Дополнительные параметры запроса.
        :return: Объект ответа requests.Response.
        """
        return self._send_request('GET', endpoint, **kwargs)

    def post_request(self, endpoint: str, **kwargs: Any) -> requests.Response:
        """
        Выполняет POST-запрос к указанному endpoint.

        :param endpoint: Эндпоинт.
        :param kwargs: Дополнительные параметры запроса.
        :return: Объект ответа requests.Response.
        """
        return self._send_request('POST', endpoint, **kwargs)

    def put_request(self, endpoint: str, **kwargs: Any) -> requests.Response:
        """
        Выполняет PUT-запрос к указанному endpoint.

        :param endpoint: Эндпоинт.
        :param kwargs: Дополнительные параметры запроса.
        :return: Объект ответа requests.Response.
        """
        return self._send_request('PUT', endpoint, **kwargs)

    def delete_request(self, endpoint: str, **kwargs: Any) -> requests.Response:
        """
        Выполняет DELETE-запрос к указанному endpoint.

        :param endpoint: Эндпоинт.
        :param kwargs: Дополнительные параметры запроса.
        :return: Объект ответа requests.Response.
        """
        return self._send_request('DELETE', endpoint, **kwargs)