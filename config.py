"""Модуль для описания классов конфигурации."""

from dataclasses import dataclass
from os import getenv

from dotenv import find_dotenv, load_dotenv


channel: dict = {

    -1001: [
        -10011,
        -10012,
        ],

    -1002: [
        -10021,
        -10022,
        ],

    -1003: [
        -10031,
        -10032,
        ],

}


@dataclass
class App:
    """API для телеграм-приложения."""

    api_id: int
    api_hash: str
    session: str
    system_version: str
    device_model: str


@dataclass
class Ids:
    """IDs для канала-стиллера и каналов-источников."""

    channel_ids: dict
    drop_author: bool


@dataclass
class Config:
    """Обобщенный класс конфигурации."""

    app: App
    ids: Ids


def load_config(path: str | None = None) -> Config:
    """Проверяет файл .env."""
    # Проверяет наличие файла .env.
    if not find_dotenv():
        exit('Отсутствует файл .env')

    # Загружает переменные окружения.
    load_dotenv()

    config = Config(
        app=App(
            api_id=int(getenv('api_id')),
            api_hash=getenv('api_hash'),
            session=getenv('session'),
            system_version=getenv('system_version'),
            device_model=getenv('device_model'),
        ),
        ids=Ids(
            channel_ids=channel,
            drop_author=bool(int(getenv('drop_author')))
        ),
    )

    # Проверяет наличие api_id и api_hash в файле .env.
    if None in (config.app.api_id, config.app.api_hash):
        exit('Отсутствуют api_id и/или api_hash в файле .env')

    # Возвращает заполненный экземпляр класса Config.
    return config
