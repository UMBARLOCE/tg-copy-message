from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv, find_dotenv


@dataclass
class Tg_Client:
    api_id: int
    api_hash: str
    session: str
    system_version: str
    device_model: str


@dataclass
class Channel_ids:
    target_id: int
    source_ids: list[int]


@dataclass
class Config:
    client: Tg_Client
    ids: Channel_ids


def load_config(path: str | None = None) -> Config:
    """
    Проверяет наличие файла .env.
    Загружает переменные окружения.
    Возвращает заполненный экземпляр класса Config.
    """

    if not find_dotenv():
        exit("Отсутствует файл .env")

    load_dotenv()

    return Config(
        client=Tg_Client(
            api_id=int(getenv("api_id")),
            api_hash=getenv("api_hash"),
            session=getenv("session"),
            system_version=getenv("system_version"),
            device_model=getenv("device_model"),
        ),
        ids=Channel_ids(
            target_id=int(getenv("target_id")),
            source_ids=list(map(int, getenv("source_ids").split(", "))),
        ),
    )
