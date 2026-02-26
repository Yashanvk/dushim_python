from tests.API.api_frame.base_api import BaseApi
import requests

class Todos(BaseApi):
    TODOS_API: str = "/todos"
    ID_TODOS: str = "/todos/{id}"

    def get_all_todos(self)-> requests.Response:
        """
        Получение списка тудушек
        :return: список всех туду
        """
        return self.get_request(self.TODOS_API)

    def get_id_todos(self,id_todos:int)-> requests.Response:
        """
        Получение списка тудушек
        :return: конкретный айди
        """
        return self.get_request(self.ID_TODOS.format(id=id_todos))
