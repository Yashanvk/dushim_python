from tests.API.api_frame.base_api import BaseApi
import requests

class Dogs(BaseApi):
    DOGS_API: str = "/dogs"
    DOGS_ERROR: str = "/dog"

    def get_all_dogs(self)-> requests.Response:
        """
        Получение списка dogs
        :return: список всех dogs
        """
        return self.get_request(self.DOGS_API)

    def get_all_dogs_error(self) -> requests.Response:
        """
        Ображение к несуществующему эндпоинту
        :return: ошибку 404
        """
        return self.get_request(self.DOGS_ERROR)

