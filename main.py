from telethon import TelegramClient, events
from config import load_config
from pprint import pprint


config = load_config()

client = TelegramClient(
    api_id=config.client.api_id,
    api_hash=config.client.api_hash,
    session=config.client.session,
)


# @client.on(events.Album(chats=config.ids.source_ids))
# async def handler_forward_to(event: events.Album.Event):
#     """Пересылает сообщения без ссылки на источник."""
#     await event.forward_to(config.ids.target_id)


# @client.on(events.NewMessage(chats=config.ids.source_ids))
# async def handler_forward_messages(event: events.NewMessage.Event):
#     """Пересылает сообщения со ссылкой на источник."""
#     await client.forward_messages(
#         entity=config.ids.target_id,
#         messages=event.message,
#     )


# @client.on(events.NewMessage(chats=config.ids.source_ids))
# async def handler_send_message(event: events.NewMessage.Event):
#     """Пересылает сообщения без ссылки на источник."""
#     await client.send_message(
#         entity=config.ids.target_id,
#         message=event.message,
#     )


@client.on(events.NewMessage(chats=config.ids.source_ids))
async def handler_send_message(event):
    """
    Внимание на grouped_id=13806529428482186
    int | None
    """
    print(event, end="\n\n")


client.start()
client.run_until_disconnected()
