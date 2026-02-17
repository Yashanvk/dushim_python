from tests.API.api_frame.base_api import BaseApi
import requests

class Capsules(BaseApi):
    CAPSULES: str = "/capsules"

    def list_capsules(self)-> requests.Response:
        """
        Получение списка всех капсул
        :return: список всех капсул
        """
        return self.get_request(self.CAPSULES)