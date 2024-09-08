from telethon import TelegramClient, events
from config import (
    api_id, api_hash, api_session, 
    target_id, 
    source_id
)





client = TelegramClient(api_session, api_id, api_hash)



@client.on(events.NewMessage(chats=source_id))
async def handler_forward_messages(event: events.NewMessage.Event):
    """
    Копирует входящие сообщения 
    из source_id 
    в target_id.
    """
    await client.forward_messages(
        entity=target_id,
        messages=event.message,
    )


client.start()
client.run_until_disconnected()
