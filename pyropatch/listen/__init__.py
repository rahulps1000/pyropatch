from .message import *
from .callback import *
import pyrogram
from ..utils import patch2,patchable

@patch2(pyrogram.client.Client)
class Client():
    @patchable
    def __init__(self, *args, **kwargs):
        self.cbd_listeners = {}
        self.msg_listeners = {}
        self.inline_listeners = {}
        self.old2___init__(*args, **kwargs)