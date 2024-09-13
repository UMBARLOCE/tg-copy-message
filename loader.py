from telethon import TelegramClient
from config import load_config


config = load_config()

client = TelegramClient(
    api_id=config.client.api_id,
    api_hash=config.client.api_hash,
    session=config.client.session,
    system_version=config.client.system_version,
    device_model=config.client.device_model,
)
