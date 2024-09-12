from telethon import TelegramClient, events
from config import load_config


config = load_config()
client = TelegramClient(
    api_id=config.client.api_id,
    api_hash=config.client.api_hash,
    session=config.client.session,
)


@client.on(events.Album(chats=config.ids.source_ids))
async def handler_forward_to(event: events.Album.Event):
    """
    Со ссылкой на источник.
    В сообщении помещается 10 вложений; остаток помещается в следующее сообщение.

    Поддерживает подпись альбома.

    Отправляет альбом от 2-х фото.
    Отправляет альбом от 2-х файлов.
    """
    await event.forward_to(config.ids.target_id)


@client.on(events.NewMessage(chats=config.ids.source_ids))
async def handler_forward_messages(event: events.NewMessage.Event):
    """
    Со ссылкой на источник.
    Отправляет текст.
    Отправляет текст со ссылкой.
    Отправляет текст с 1 картинкой одним блоком.

    Картинки более одной отправляются отдельными сообщениями,
    при этом текст прилипает к одной из картинок.

    Вылетает raise ValueError('Request was unsuccessful {} time(s)'
    при отправке более 6 фото за раз.
    """
    if event.message.grouped_id:
        return
    
    await client.forward_messages(
        entity=config.ids.target_id,
        messages=event.message,
    )


if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
