from pyrogram.filters import AndFilter, OrFilter, InvertFilter
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup
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
        await sleep(time.value)
        return await handle_flood_wait(func, *args, **kwargs)


async def check_cbd(buttons: InlineKeyboardMarkup):
    if not buttons:
        return False
    for button_row in buttons.inline_keyboard:
        for button in button_row:
            if button.callback_data:
                return True
    return False