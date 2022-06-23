from ..utils import patch, patchable
import pyrogram
from pyrogram.errors.exceptions.flood_420 import FloodWait
from asyncio import sleep


@patch(pyrogram.client.Client)
class Client():
    @patchable
    async def invoke(self, *args, **kwargs):
        try:
            return await self.old_invoke(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.invoke(*args, **kwargs)

    @patchable
    async def resolve_peer(self, *args, **kwargs):
        try:
            return await self.old_resolve_peer(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.resolve_peer(*args, **kwargs)

    @patchable
    async def save_file(self, *args, **kwargs):
        try:
            return await self.old_save_file(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.save_file(*args, **kwargs)
