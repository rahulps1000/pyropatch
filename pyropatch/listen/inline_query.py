import asyncio
import functools
from typing import Optional

import pyrogram

from ..utils import patch, patchable

loop = asyncio.get_event_loop()


class ListenerCanceled(Exception):
    pass


pyrogram.errors.ListenerCanceled = ListenerCanceled


async def temp(_, __):
    pass


@patch(pyrogram.client.Client)
class Client():
    @patchable
    async def listen_inline_query(
            self,
            user_id: int,
            filters=None,
            timeout: Optional[int] = None
    ):
        future = loop.create_future()
        future.add_done_callback(
            functools.partial(self.remove_inline_listener, user_id)
        )
        self.inline_listeners.update({
            str(user_id): {"future": future, "filters": filters}
        })
        return await asyncio.wait_for(future, timeout)

    @patchable
    def remove_inline_listener(
            self,
            user_id: int,
            future=None
    ):
        if future == self.inline_listeners[str(user_id)]["future"]:
            self.inline_listeners.pop(str(user_id), None)

    @patchable
    def cancel_inline_listener(
            self,
            user_id: int
    ):
        listener = self.inline_listeners.get(str(user_id))
        if not listener or listener['future'].done():
            return
        listener['future'].set_exception(ListenerCanceled())
        self.remove_inline_listener(user_id, listener['future'])


@patch(pyrogram.handlers.inline_query_handler.InlineQueryHandler)
class InlineQueryHandler():
    @patchable
    def __init__(self, callback: callable, filters=None, checker=False):
        self.checker = checker
        self.user_callback = callback
        self.old___init__(self.resolve_listener, filters)

    @patchable
    async def resolve_listener(self, client, update, *args):
        listener = client.inline_listeners.get(str(update.from_user.id))
        if self.checker:
            if listener and not listener['future'].done():
                listener['future'].set_result(update)
                await self.user_callback(client, update, *args)
            else:
                if listener and listener['future'].done():
                    client.remove_inline_listener(
                        user_id=update.from_user.id,
                        future=listener['future']
                    )
        else:
            await self.user_callback(client, update, *args)

    @patchable
    async def check(self, client, update):
        listener = client.inline_listeners.get(str(update.from_user.id))
        if self.checker:
            if listener and not listener['future'].done():
                return await listener['filters'](client, update) if callable(listener['filters']) else True
        if callable(self.filters):
            return await self.filters(client, update)
        return True
