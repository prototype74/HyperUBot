# HyperUBot Guide - Developing Modules for HyperUBot

## Requirements

You might need some python knowledge for this, or at least some other programming language knowledge.

## Knowing the basics

For a python script to be minimally compatible with the bot, and having the possibility to be run as a command, you will need to import the EventHandler, from the bot's system utilities. After this, create a new EventHandler object, like the example below:

```python
from userbot.sysutils.event_handler import EventHandler # The event handler object

ehandler = EventHandler() # The specific handler of our new module
```

## Outgoing commands (the most common solution)

Due to Telethon's way of handling things, your bot command functions should be asynchronous. This can be done, while declaring a function, by using the keyword "async". Before declaring the function, however, you should add a line referencing to the Event Handler you created, specifying the command that triggers that action. An example could be:

```python
@ehandler.on(pattern=r"^\.mycommand(?: |$)(.*)", outgoing=True)
async def action(event):
    # Do things, using or not using the event variable
    return
```

This will perform an action if the account in which the bot is running sends the message ".mycommand". 

## Incoming commands

Analogously, you also have the possibility to make an account "answer" commands by others. This is done in a similar fashion of the Outgoing solution:

```python
@ehandler.on(pattern=r"^\.mycommand(?: |$)(.*)", incoming=True)
async def action(event):
    # Do things, using or not using the event variable
    return
```

In this example, if another account sends the user a message ".mycommand", the host account will do certain actions. This should be done carefully and keeping in mind that any user could potentially use you and your account could perform actions without your consent. A good safety measure would be adding an extra config class with a list of authorized users, and then check if the user that called the command is authorized to do such.

## Extra configurations

The recommended way of storing the configurations for your module is to create a new class in the config.py file. If using env, you should only import what you need. An example of a config.py file with a new class:

```python
class ConfigClass(object): # This is the bot's config class
    API_KEY = None
    API_HASH = None
    STRING_SESSION = None
    UBOT_LANG = "en"
    LOGGING = False
    LOGGING_CHATID = 0
    TEMP_DL_DIR = "./downloads"
    COMMUNITY_REPOS = []

class ExampleConfigClass(object):
    EXAMPLE1 = None
```

Considering that your module's configurations are stored in this new ExampleConfigClass, all you need to do is to import it into your module. To do this, on the top of the module, write:

```python
from userbot.config import ExampleConfigClass as cfg
```

With this done, if you need to access a configuration field in a function, all you need to do is:

```python
async def function(event):
    # some code
    configurationNeededHere = cfg.EXAMPLE1
```

Hopefully, this mechanic is now simple.
