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



async def temp(_, __):
    pass

@patch(pyrogram.client.Client)
class Client():

    @patchable
    async def start(self,*args, **kwargs):
        self.add_handler(pyrogram.handlers.CallbackQueryHandler(temp))
        await self.old_start(*args, **kwargs)

    @patchable
    async def listen_cbd(self, message:pyrogram.types.Message, filters=None, timeout=None):
        if not await check_cbd(message.reply_markup):
            raise NoCallbackException
        chat_id = message.chat.id
        msg_id = message.id
        msg = await self.get_messages(chat_id, msg_id)
        if not msg.from_user.is_self:
            raise NotSelfMessage
        future = loop.create_future()
        future.add_done_callback(
            functools.partial(self.remove_cbd_listener, chat_id, msg_id)
        )
        if self.cbd_listeners.get(chat_id,False):
            self.cbd_listeners[chat_id].update({
                msg_id: {"future": future, "filters": filters}
            })
        else:
            self.cbd_listeners.update({
                chat_id: {msg_id: {"future": future, "filters": filters}}
            })
        return await asyncio.wait_for(future, timeout)

    @patchable
    async def ask_cbd(self, chat_id, text, reply_markup: pyrogram.types.InlineKeyboardMarkup, filters=None, timeout=None, *args, **kwargs):
        if not await check_cbd(reply_markup):
            raise NoCallbackException
        request = await self.send_message(chat_id, text, reply_markup=reply_markup, *args, **kwargs)
        response = await self.listen_cbd(request, filters, timeout)
        response.request = request
        return response

    @patchable
    def remove_cbd_listener(self, chat_id, msg_id, future):
        if future == self.cbd_listeners[chat_id][msg_id]["future"]:
            self.cbd_listeners[chat_id].pop(msg_id, None)

    @patchable
    def cancel_cbd_listener(self, message: pyrogram.types.Message):
        chat_id = message.chat.id
        msg_id = message.id
        listener = self.cbd_listeners.get(chat_id, {}).get(msg_id)
        if not listener or listener['future'].done():
            return
        listener['future'].set_exception(ListenerCanceled())
        self.remove_cbd_listener(chat_id, msg_id, listener['future'])


@patch(pyrogram.handlers.callback_query_handler.CallbackQueryHandler)
class CallbackQueryHandler():
    @patchable
    def __init__(self, callback: callable, filters=None):
        self.user_callback = callback
        self.old___init__(self.resolve_listener, filters)

    @patchable
    async def resolve_listener(self, client, update, *args):
        listener = client.cbd_listeners.get(update.message.chat.id, {}).get(update.message.id)
        if listener and not listener['future'].done():
            listener['future'].set_result(update)
        else:
            if listener and listener['future'].done():
                client.clear_listener(update.message.chat.id, update.message.id, listener['future'])
            await self.user_callback(client, update, *args)

    @patchable
    async def check(self, client, update):
        listener = client.cbd_listeners.get(update.message.chat.id, {}).get(update.message.id)

        if listener and not listener['future'].done():
            return await listener['filters'](client, update) if callable(listener['filters']) else True

        return (
            await self.filters(client, update)
            if callable(self.filters)
            else True
        )