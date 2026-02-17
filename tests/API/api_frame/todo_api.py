from tests.API.api_frame.base_api import BaseApi
from typing import Optional
import requests

class TodoApi(BaseApi):
    REG_ENDPOINT: str = 'todos'

    def todo_list(self, valid: bool = True, todo_id: Optional[int] = None) -> requests.Response:
        """
        Получает список задач или конкретную задачу по ID.

        :param valid: Флаг, указывающий, использовать ли корректный endpoint ('todos').
                      Если False — добавляется лишняя 's' для имитации некорректного запроса.
        :param todo_id: Идентификатор задачи. Если указан — запрашивается конкретная задача.
        :return: Объект ответа requests.Response.
        """
        endpoint: str = self.REG_ENDPOINT if valid else self.REG_ENDPOINT + "s"
        if todo_id is not None:
            endpoint += f"/{todo_id}"
        return self.get_request(endpoint)