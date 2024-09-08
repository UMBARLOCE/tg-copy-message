from os import getenv
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Отсутствует файл .env")
    # TG_BOT_TOKEN = input("Введите TOKEN телеграм-бота:\n")
    # with open(".env", "w", encoding="utf-8") as file:
    #     file.write(f"TG_BOT_TOKEN = {TG_BOT_TOKEN}\n")

load_dotenv()

api_id = getenv("api_id")
api_hash = getenv("api_hash")
api_session = getenv("api_session")
target_id = getenv("target_id")
source_id = getenv("source_id")
