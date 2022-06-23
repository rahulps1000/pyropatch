
# Pyropatch

An advanced monkeypatcher add-on for Pyrogram




## Installation

Install pyropatch with pip

```cmd
  pip install pyropatch
```
    
## Usage/Examples
### All patches
> * Command Handler
> * Flood Handler
> * Listen

```python
from pyropatch import pyropatch                    #apply all patches
from pyrogram import Client

app = Client(...)
```

### Command Handler
```python
from pyropatch import command_handler                   #apply command handler
from pyrogram import Client

app = Client(...)

#pass info along with commands in command filter
@app.on_message(filters.command(commands='start',info='Check Bot is Alive'))

# to set bot commands from the command available on bot
app.auto_set_commands()

# to get all the commands available in bot
app.commands
```
### Flood Handler
```python
from pyropatch import flood_handler                   #apply flood handler
from pyrogram import Client

app = Client(...)

# all floodwaits will automatically handled
app.send_message("me", "Flood handled with **Pyropatch**!")

```

### Listen
```python
from pyropatch import listen                   #apply listen
from pyrogram import Client

app = Client(...)
# listen for a message in a particular chat
m = app.listen_message(chat_id=chat_id, filters=filters, timeout=timeout)

# listen for a callback data in a particular message
u = app.listen_callback(chat_id=chat_id, message_id=message_id, filters=filters, timeout=timeout)
u = app.listen_callback(inline_message_id=inline_message_id, filters=filters, timout=timeout)

# listen for an inline query 
u = app.listen_inline_query(user_id=user_id, filters=filters, timeout=timeout)

# listen for an inline result 
u = app.listen_inline_result(user_id=user_id, filters=filters, timeout=timeout)
```

#### More Comming Soon

##### Special thanks to [Pyromod](https://github.com/usernein/pyromod)
