"""Модуль для загрузки конфигураций и создания экземпляра клиента."""

from config import load_config

from telethon import TelegramClient


config = load_config()

client = TelegramClient(
    api_id=config.app.api_id,
    api_hash=config.app.api_hash,
    session=config.app.session,
    system_version=config.app.system_version,
    device_model=config.app.device_model,
)
