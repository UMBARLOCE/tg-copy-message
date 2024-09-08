from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv, find_dotenv


# if not find_dotenv():
#     exit("Отсутствует файл .env")
#     # TG_BOT_TOKEN = input("Введите TOKEN телеграм-бота:\n")
#     # with open(".env", "w", encoding="utf-8") as file:
#     #     file.write(f"TG_BOT_TOKEN = {TG_BOT_TOKEN}\n")

# load_dotenv()

# # https://my.telegram.org/apps

# api_id = getenv("api_id")
# api_hash = getenv("api_hash")
# session = getenv("session")
# target_id = getenv("target_id")
# source_id = getenv("source_id")


@dataclass
class Tg_Client:
    api_id: int
    api_hash: str
    session: str
    system_version: str


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
        ),
        ids=Channel_ids(
            target_id=int(getenv("target_id")),
            source_ids=list(map(int, getenv("source_ids").split(', '))),
        ),
    )
