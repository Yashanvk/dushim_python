from tests.API.api_frame.base_api import BaseApi
import requests

class Capsules(BaseApi):
    CAPSULES: str = "/capsules"
    UPCOMING: str = "/capsules/upcoming"
    PAST: str = "/capsules/past"

    def get_capsule(self,capsule_serial:str="")-> requests.Response:
        """
        Получение списка капсул/ капсулы по серии
        :param capsule_serial: серия капсулы
        :return: список всех капсул
        """
        return self.get_request(self.CAPSULES + "/" + capsule_serial)

    def test_get_capsule_upcoming(self) -> requests.Response:
        """
        :return: Массив предстоящих капсул
        """
        return self.get_request(self.UPCOMING)

    def test_get_capsule_past(self) -> requests.Response:
        """
        :return: Массив предстоящих капсул
        """
        return self.get_request(self.PAST)
