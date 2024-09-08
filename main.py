from telethon import TelegramClient, events
from config import load_config


config = load_config()

client = TelegramClient(
    api_id=config.client.api_id,
    api_hash=config.client.api_hash,
    session=config.client.session,
)


@client.on(events.NewMessage(chats=config.ids.source_ids))
async def handler_forward_messages(event: events.NewMessage.Event):
    """
    Копирует входящие сообщения
    из source_ids
    в target_id.
    """
    await client.forward_messages(
        entity=config.ids.target_id,
        messages=event.message,
    )


client.start()
client.run_until_disconnected()
