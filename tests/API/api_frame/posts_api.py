from tests.API.api_frame.base_api import BaseApi
import requests

class Posts(BaseApi):
    POSTS_API: str = "/posts"
    ID_POSTS: str = "/posts/{id}"

    def get_all_posts(self)-> requests.Response:
        """
        Получение списка posts
        :return: список всех posts
        """
        return self.get_request(self.POSTS_API)

    def get_id_posts(self,id_posts:int)-> requests.Response:
        """
        Получение списка posts
        :return: конкретный айди
        """
        return self.get_request(self.ID_POSTS.format(id=id_posts))

    def post_posts(self, body:dict)-> requests.Response:
        """
        Создание объекта
        :param body: тело запроса
        :return: возвращает созданный объект
        """
        return self.post_request(self.POSTS_API, json=body)

