from pyrogram.file_id import FileId, FileType, PHOTO_TYPES, DOCUMENT_TYPES
from pyrogram.filters import AndFilter, OrFilter, InvertFilter
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import raw
from asyncio import sleep

def patch(obj):
    def is_patchable(item):
        return getattr(item[1], 'patchable', False)

    def wrapper(container):
        for name, func in filter(is_patchable, container.__dict__.items()):
            old = getattr(obj, name, None)
            setattr(obj, 'old_' + name, old)
            setattr(obj, name, func)
        return container

    return wrapper

def patch2(obj):
    def is_patchable(item):
        return getattr(item[1], 'patchable', False)

    def wrapper(container):
        for name, func in filter(is_patchable, container.__dict__.items()):
            old = getattr(obj, name, None)
            setattr(obj, 'old2_' + name, old)
            setattr(obj, name, func)
        return container

    return wrapper


def patchable(func):
    func.patchable = True
    return func


def get_commands_from_filters(filters):
    if isinstance(filters, AndFilter) or isinstance(filters, OrFilter):
        cmds = []
        cmds.extend(get_commands_from_filters(filters.base) or [])
        cmds.extend(get_commands_from_filters(filters.other) or [])
        return cmds
    # elif isinstance(filters, InvertFilter):
    #     return get_commands_from_filters(filters.base)
    elif hasattr(filters, 'commands'):
        cmds = {}
        for cm in filters.commands:
            cmds[cm] = filters.info
        return [cmds]


async def handle_flood_wait(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except FloodWait as time:
        await sleep(time.x)
        return await handle_flood_wait(func, *args, **kwargs)


async def check_cbd(buttons: InlineKeyboardMarkup):
    if not buttons:
        return False
    for button_row in buttons.inline_keyboard:
        for button in button_row:
            if button.callback_data:
                return True
    return False


# https://github.com/subinps/pyrogram/tree/inline-m/pyrogram/utils.py#81-113
def get_input_file_from_file_id(
    file_id: str,
    expected_file_type: FileType = None):
    try:
        decoded = FileId.decode(file_id)
    except Exception:
        raise ValueError(f'Failed to decode "{file_id}". The value does not represent an existing local file, '
                         f'HTTP URL, or valid file id.')

    file_type = decoded.file_type

    if expected_file_type is not None and file_type != expected_file_type:
        raise ValueError(f'Expected: "{expected_file_type}", got "{file_type}" file_id instead')

    if file_type in (FileType.THUMBNAIL, FileType.CHAT_PHOTO):
        raise ValueError(f"This file_id can only be used for download: {file_id}")

    if file_type in PHOTO_TYPES:
        return raw.types.InputPhoto(
            id=decoded.media_id,
            access_hash=decoded.access_hash,
            file_reference=decoded.file_reference
        )

    if file_type in DOCUMENT_TYPES:
        return raw.types.InputDocument(
            id=decoded.media_id,
            access_hash=decoded.access_hash,
            file_reference=decoded.file_reference
        )

    raise ValueError(f"Unknown file id: {file_id}")
