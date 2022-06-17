
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
import pyropatch                    #import package
from pyrogram import Client

app = Client(...)
```

### Command Handler
```python
from pyropatch import command_handler                   #import package
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
from pyropatch import flood_handler                   #import package
from pyrogram import Client

app = Client(...)

# all floodwaits will automatically handled
app.send_message("me", "Flood handled with **Pyropatch**!")

```

### Listen
```python
from pyropatch import listen                   #import package
from pyrogram import Client

app = Client(...)

# listen for a message in a particular chat
m = app.listen_msg(chat_id, filters, timeout)

# listen for a callback data in a perticular message
u = app.listen_cdb(message, filters, timeout)
```

#### More Comming Soon
