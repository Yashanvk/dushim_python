import random
from requests import Response
from typing import List, Dict, Any

class Helpers:
    @staticmethod
    def get_random_items_by_completed_flag(
        response: Response,
        count: int,
        completed_flag: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Возвращает случайные элементы из JSON-ответа, отфильтрованные по флагу 'completed'.

        :param response: Объект ответа requests, содержащий JSON-массив задач.
        :param count: Количество случайных элементов, которые нужно вернуть.
        :param completed_flag: Значение флага 'completed', по которому фильтруются элементы.
        :return: Список словарей, соответствующих отфильтрованным и случайно выбранным элементам.
        :raises ValueError: Если ответ не является валидным JSON или недостаточно подходящих элементов.
        """
        try:
            response_json: Any = response.json()
        except ValueError:
            raise ValueError("Ответ не является валидным JSON")

        completed_items: List[Dict[str, Any]] = [
            item for item in response_json
            if item.get("completed") is completed_flag
        ]

        if len(completed_items) < count:
            raise ValueError(
                f"Недостаточно объектов с completed={completed_flag}: "
                f"нужно {count}, найдено {len(completed_items)}"
            )

        return random.sample(completed_items, count)