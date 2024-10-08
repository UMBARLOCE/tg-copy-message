"""Модуль для запуска программы."""

from loader import client, config

from telethon import events


for entity, chats in config.ids.channel_ids.items():


    @client.on(events.Album(chats=chats))
    async def foo_album(event: events.Album.Event, entity=entity) -> None:
        """Отправляет альбом со ссылкой на источник."""
        await event.forward_to(
            entity=entity,
            drop_author=config.ids.drop_author,
        )


    @client.on(events.NewMessage(chats=chats))
    async def foo_message(event: events.NewMessage.Event, entity=entity) -> None:
        """Отправляет сообщение со ссылкой на источник."""
        if event.message.grouped_id:
            return

        await client.forward_messages(
            entity=entity,
            messages=event.message,
            drop_author=config.ids.drop_author,
        )


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
