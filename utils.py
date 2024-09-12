# @client.on(events.NewMessage(chats=config.ids.source_ids))
# async def handler_send_message(event: events.NewMessage.Event):
#     """
#     Без ссылки на источник.
#     Отправляет текст.
#     Отправляет текст со ссылкой.
#     Отправляет текст с 1 картинкой одним блоком.

#     Картинки более одной отправляются отдельными сообщениями,
#     при этом текст прилипает к одной из картинок.

#     Ошибок нет при отправке более 6 сообщений.
#     """
#     await client.send_message(
#         entity=config.ids.target_id,
#         message=event.message,
#     )