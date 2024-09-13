"""Модуль для запуска программы."""
from telethon import events
from loader import client, config


@client.on(events.Album(chats=config.ids.source_ids))
async def handler_forward_to(event: events.Album.Event):
    """Отправляет альбом со ссылкой на источник."""
    await event.forward_to(config.ids.target_id)


@client.on(events.NewMessage(chats=config.ids.source_ids))
async def handler_forward_messages(event: events.NewMessage.Event):
    """Отправляет сообщение со ссылкой на источник."""
    if event.message.grouped_id:
        return 

    await client.forward_messages(
        entity=config.ids.target_id,
        messages=event.message,
    )


if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
