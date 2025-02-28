import json
from src.api_mixin import APIMixin


class Channel(APIMixin):
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        self.channel_dict = (self.get_service().channels()
                             .list(id=self.__channel_id, part='snippet,statistics').execute())

        self.title: str = self.channel_dict['items'][0]['snippet']['title']
        self.description: str = self.channel_dict['items'][0]['snippet']['description']
        self.url: str = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscribers: int = int(self.channel_dict['items'][0]['statistics']['subscriberCount'])
        self.video_count: int = int(self.channel_dict['items'][0]['statistics']['videoCount'])
        self.view_count: int = int(self.channel_dict['items'][0]['statistics']['viewCount'])

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    def __str__(self) -> str:
        """Строковое представление экземпляра класса"""
        return f'{self.title} ({self.url})'

    def __add__(self, other) -> int:
        """Сумма числа подписчиков нескольких каналов"""
        return self.subscribers + other.subscribers

    def __sub__(self, other) -> int:
        """Разность числа подписчиков нескольких каналов"""
        return self.subscribers - other.subscribers

    def __gt__(self, other) -> bool:
        """Сравнение (больше) числа подписчиков нескольких каналов"""
        return self.subscribers > other.subscribers

    def __ge__(self, other) -> bool:
        """Сравнение (больше либо равно) числа подписчиков нескольких каналов"""
        return self.subscribers >= other.subscribers

    def __lt__(self, other) -> bool:
        """Сравнение (меньше) числа подписчиков нескольких каналов"""
        return self.subscribers < other.subscribers

    def __le__(self, other) -> bool:
        """Сравнение (меньше либо равно) числа подписчиков нескольких каналов"""
        return self.subscribers <= other.subscribers

    def __eq__(self, other) -> bool:
        """Проверяет равенство числа подписчиков нескольких каналов"""
        return self.subscribers == other.subscribers

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_dict, indent=2, ensure_ascii=False))

    def to_json(self, filename: str) -> None:
        """
        Запись в указанный файл json
        :param filename: имя файла
        """
        with open(filename, "w", encoding='UTF-8') as file:
            json.dump(self.channel_dict, file, ensure_ascii=False)
