import re
from typing import List, Union

import pyrogram

from ..utils import patch, patch2, patchable, get_commands_from_filters


@patch(pyrogram.client.Client)
class Client():
    @patchable
    def __init__(self, *args, **kwargs):
        self.commands = {}
        self.old___init__(*args, **kwargs)

    @patchable
    async def auto_set_commands(self):
        cmd_list = []
        for cmd, info in self.commands.items():
            cmd_list.append(pyrogram.types.BotCommand(command=cmd, description=info))
        return await self.set_bot_commands(cmd_list)


@patch(pyrogram.methods.utilities.add_handler.AddHandler)
class AddHandler():
    @patchable
    def add_handler(
            self: "pyrogram.Client",
            handler: "Handler",
            group: int = 0
    ):
        if isinstance(handler, pyrogram.handlers.MessageHandler):
            cmd_list = get_commands_from_filters(handler.filters)
            if cmd_list:
                for cmd in cmd_list:
                    self.commands.update(cmd)

        return self.old_add_handler(handler, group)


def new_command(commands: Union[str, List[str]], info: str = "", prefixes: Union[str, List[str]] = "/",
                case_sensitive: bool = False):
    """Filter commands, i.e.: text messages starting with "/" or any other custom prefix.
    Parameters:
        commands (``str`` | ``list``):
            The command or list of commands as string the filter should look for.
            Examples: "start", ["start", "help", "settings"]. When a message text containing
            a command arrives, the command itself and its arguments will be stored in the *command*
            field of the :obj:`~pyrogram.types.Message`.
        info (``str``, *optional*):
            A short information of the command.
        prefixes (``str`` | ``list``, *optional*):
            A prefix or a list of prefixes as string the filter should look for.
            Defaults to "/" (slash). Examples: ".", "!", ["/", "!", "."], list(".:!").
            Pass None or "" (empty string) to allow commands with no prefix at all.
        case_sensitive (``bool``, *optional*):
            Pass True if you want your command(s) to be case sensitive. Defaults to False.
            Examples: when True, command="Start" would trigger /Start but not /start.
    """
    command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

    async def func(flt, client: Client, message: pyrogram.types.Message):
        try:
            client.username
        except AttributeError:
            temp = await client.get_me()
            client.username = temp.username
        finally:
            username = client.username or ""
        text = message.text or message.caption
        message.command = None

        if not text:
            return False

        for prefix in flt.prefixes:
            if not text.startswith(prefix):
                continue

            without_prefix = text[len(prefix):]

            for cmd in flt.commands:
                if not re.match(rf"^(?:{cmd}(?:@?{username})?)(?:\s|$)", without_prefix,
                                flags=re.IGNORECASE if not flt.case_sensitive else 0):
                    continue

                without_command = re.sub(rf"{cmd}(?:@?{username})?\s?", "", without_prefix, count=1,
                                         flags=re.IGNORECASE if not flt.case_sensitive else 0)

                # match.groups are 1-indexed, group(1) is the quote, group(2) is the text
                # between the quotes, group(3) is unquoted, whitespace-split text

                # Remove the escape character from the arguments
                message.command = [cmd] + [
                    re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                    for m in command_re.finditer(without_command)
                ]

                return True

        return False

    commands = commands if isinstance(commands, list) else [commands]
    commands = {c if case_sensitive else c.lower() for c in commands}

    prefixes = [] if prefixes is None else prefixes
    prefixes = prefixes if isinstance(prefixes, list) else [prefixes]
    prefixes = set(prefixes) if prefixes else {""}

    return pyrogram.filters.create(
        func,
        "CommandFilter",
        commands=commands,
        info=info,
        prefixes=prefixes,
        case_sensitive=case_sensitive
    )


pyrogram.filters.command = new_command
