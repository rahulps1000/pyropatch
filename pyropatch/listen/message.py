# this code snippet is created using
# https://github.com/usernein/pyromod/blob/master/pyromod/listen/listen.py

from ..utils import patch, patchable
import pyrogram
import asyncio
import functools

loop = asyncio.get_event_loop()


class ListenerCanceled(Exception):
    pass


pyrogram.errors.ListenerCanceled = ListenerCanceled


@patch(pyrogram.client.Client)
class Client():

    @patchable
    async def listen_message(self, chat_id, filters=None, timeout=None):
        if type(chat_id) != int:
            chat = await self.get_chat(chat_id)
            chat_id = chat.id
        future = loop.create_future()
        future.add_done_callback(
            functools.partial(self.remove_message_listener, chat_id)
        )
        self.msg_listeners.update({
            chat_id: {"future": future, "filters": filters}
        })
        return await asyncio.wait_for(future, timeout)

    @patchable
    async def ask_message(self, chat_id, text, filters=None, timeout=None, *args, **kwargs):
        request = await self.send_message(chat_id, text, *args, **kwargs)
        response = await self.listen_message(chat_id, filters, timeout)
        response.request = request
        return response

    @patchable
    def remove_message_listener(self, chat_id, future):
        if future == self.msg_listeners[chat_id]["future"]:
            self.msg_listeners.pop(chat_id, None)

    @patchable
    def cancel_message_listener(self, chat_id):
        listener = self.msg_listeners.get(chat_id)
        if not listener or listener['future'].done():
            return
        listener['future'].set_exception(ListenerCanceled())
        self.remove_message_listener(chat_id, listener['future'])


@patch(pyrogram.handlers.message_handler.MessageHandler)
class MessageHandler():
    @patchable
    def __init__(self, callback: callable, filters=None, checker=False):
        self.checker = checker
        self.user_callback = callback
        self.old___init__(self.resolve_listener, filters)

    @patchable
    async def resolve_listener(self, client, message, *args):
        listener = client.msg_listeners.get(message.chat.id)
        if self.checker:
            if listener and not listener['future'].done():
                if (
                    await listener['filters'](client, message) 
                    if callable(listener['filters']) 
                    else True
                ):
                    listener['future'].set_result(message)
                    await self.user_callback(client, message, *args)
        else:
            await self.user_callback(client, message, *args)

    @patchable
    async def check(self, client, update):
        listener = client.msg_listeners.get(update.chat.id)
        if self.checker:
            if listener and not listener['future'].done():
                return await listener['filters'](client, update) if callable(listener['filters']) else True
        if callable(self.filters):
            return await self.filters(client, update)
        return True
