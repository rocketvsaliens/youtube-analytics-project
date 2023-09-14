import os
from googleapiclient.discovery import build


class APIMixin:
    """Класс, который отвечает за подключение к API"""
    __API_KEY = os.getenv('YT_API_KEY')

    @classmethod
    def get_service(cls) -> object:
        service = build('youtube', 'v3', developerKey=cls.__API_KEY)
        return service
