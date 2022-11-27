from typing import Optional

from ..utils import patch, patchable, check_cbd
import pyrogram
import asyncio
import functools

loop = asyncio.get_event_loop()


class ListenerCanceled(Exception):
    pass


pyrogram.errors.ListenerCanceled = ListenerCanceled


class NoCallbackException(Exception):
    def __init__(self):
        self.message = "A Callback button is required."


pyrogram.errors.NoCallbackException = NoCallbackException


class NotSelfMessage(Exception):
    def __init__(self):
        self.message = "Cannot listen to other users Callback Data"


pyrogram.errors.NotSelfMessage = NotSelfMessage


@patch(pyrogram.client.Client)
class Client():
    @patchable
    async def listen_callback(
            self,
            chat_id: Optional[int] = None,
            message_id: Optional[int] = None,
            inline_message_id: Optional[str] = None,
            filters=None,
            timeout: Optional[int] = None
    ):
        if chat_id:
            if not message_id:
                raise TypeError("message_id is required")
            msg = await self.get_messages(chat_id, message_id)
            if msg.from_user and not msg.from_user.is_self:
                raise NotSelfMessage
            # For listening to a callback button in a channel's post
            elif msg.sender_chat and not msg.chat.id == msg.sender_chat.id:
                raise NotSelfMessage
            if not await check_cbd(msg.reply_markup):
                raise NoCallbackException
            key = f'{chat_id}:{message_id}'
        elif inline_message_id:
            key = inline_message_id
        else:
            raise TypeError("chat_id or inline_message_id is required")
        future = loop.create_future()
        future.add_done_callback(
            functools.partial(self.remove_callback_listener,
                              chat_id, message_id, inline_message_id)
        )
        self.cbd_listeners.update({
            key: {"future": future, "filters": filters}
        })
        return await asyncio.wait_for(future, timeout)

    @patchable
    async def ask_callback(self, chat_id, text, reply_markup: pyrogram.types.InlineKeyboardMarkup, filters=None,
                           timeout=None, *args, **kwargs):
        if not await check_cbd(reply_markup):
            raise NoCallbackException
        request = await self.send_message(chat_id, text, reply_markup=reply_markup, *args, **kwargs)
        response = await self.listen_callback(
            chat_id=request.chat.id,
            message_id=request.id,
            filters=filters,
            timeout=timeout
        )
        response.request = request
        return response

    @patchable
    def remove_callback_listener(
            self,
            chat_id: Optional[int] = None,
            msg_id: Optional[int] = None,
            inline_message_id: Optional[str] = None,
            future=None
    ):
        if chat_id:
            if not msg_id:
                raise TypeError("message_id is required")
            key = f'{chat_id}:{msg_id}'
        elif inline_message_id:
            key = inline_message_id
        else:
            raise TypeError("chat_id or inline_message_id is required")
        if future == self.cbd_listeners[key]["future"]:
            self.cbd_listeners.pop(key, None)

    @patchable
    def cancel_callback_listener(
            self,
            chat_id: Optional[int] = None,
            msg_id: Optional[int] = None,
            inline_message_id: Optional[str] = None
    ):
        if chat_id:
            if not msg_id:
                raise TypeError("message_id is required")
            key = f'{chat_id}:{msg_id}'
        elif inline_message_id:
            key = inline_message_id
        else:
            raise TypeError("chat_id or inline_message_id is required")
        listener = self.cbd_listeners.get(key)
        if not listener or listener['future'].done():
            return
        listener['future'].set_exception(ListenerCanceled())
        self.remove_callback_listener(
            chat_id, msg_id, inline_message_id, listener['future'])


@patch(pyrogram.handlers.callback_query_handler.CallbackQueryHandler)
class CallbackQueryHandler():
    @patchable
    def __init__(self, callback: callable, filters=None, checker=False):
        self.checker = checker
        self.user_callback = callback
        self.old___init__(self.resolve_listener, filters)

    @patchable
    async def resolve_listener(self, client, update, *args):
        if update.message:
            key = f'{update.message.chat.id}:{update.message.id}'
        elif update.inline_message_id:
            key = update.inline_message_id
        else:
            raise TypeError("chat_id or inline_message_id is required")
        listener = client.cbd_listeners.get(key)
        if self.checker:
            if listener and not listener['future'].done():
                listener['future'].set_result(update)
                await self.user_callback(client, update, *args)
            else:
                if listener and listener['future'].done():
                    client.remove_callback_listener(chat_id=update.message.chat.id if update.message else None,
                                                msg_id=update.message.id if update.message else None,
                                                inline_message_id=update.inline_message_id, future=listener['future'])
        else:
            await self.user_callback(client, update, *args)

    @patchable
    async def check(self, client, update):
        if update.message:
            key = f'{update.message.chat.id}:{update.message.id}'
        elif update.inline_message_id:
            key = update.inline_message_id
        else:
            raise TypeError("chat_id or inline_message_id is required")
        listener = client.cbd_listeners.get(key)
        if self.checker:
            if listener and not listener['future'].done():
                return await listener['filters'](client, update) if callable(listener['filters']) else True
        if callable(self.filters):
            return await self.filters(client, update)
        return True
