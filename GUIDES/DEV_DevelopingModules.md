# HyperUBot Guide - Developing Modules for HyperUBot

## Requirements

You might need some Python knowledge for this, or at least some other programming language knowledge.

## Knowing the basics

For a Python script to be minimally compatible with the bot, and having the possibility to be run as a command, you will need to import the EventHandler, from the bot's system utilities. After this, create a new EventHandler object, like the example below:

```python
from userbot.sysutils.event_handler import EventHandler  # The EventHandler object

ehandler = EventHandler()  # The specific handler of our new module
```

You can also pass a logger to EventHandler to identify traces easier:

```python
from userbot.sysutils.event_handler import EventHandler  # The EventHandler object
from logging import getLogger  # import getLogger

log = getLogger(__name__)  # pass the current module's name
ehandler = EventHandler(log)  # set logger as parameter to EventHandler
```

## Outgoing commands (the most common solution)

Due to Telethon's way of handling things, your bot command functions should be asynchronous. This can be done, while declaring a function, by using the keyword "async". Before declaring the function, however, you should add a line referencing to the EventHandler you created, specifying the command that triggers that action. An example could be:

```python
from userbot.sysutils.event_handler import EventHandler
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)

@ehandler.on(command="example", hasArgs=True, outgoing=True)
async def action(event):
    await event.edit("This is an example!")
    # Do things, using or not using the event variable
    return
```

This will perform an action if the account in which the bot is running sends the message ".mycommand". 

## Incoming commands

Analogously, you also have the possibility to make an account "answer" commands by others. This is done in a similar fashion of the Outgoing solution:

```python
from userbot.sysutils.event_handler import EventHandler
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)

@ehandler.on(command="example", hasArgs=True, incoming=True)
async def action(event):
    await event.reply("This is an example response!")
    # Do things, using or not using the event variable
    return
```

In this example, if another account sends the user a message ".mycommand", the host account will do certain actions. This should be done carefully and keeping in mind that any user could potentially use you and your account could perform actions without your consent. A good safety measure would be adding an extra config class with a list of authorized users, and then check if the user that called the command is authorized to do such.

## Extra configurations

If a specific configuration is required for your module, add your custom configuration to the existing configurations in your config file. HyperUBot loads all configurations independent from config.env or config.py automatically, so any special instruction is not required to add custom configurations.

## Get a certain configuration

To get a certain configuration you need to import the configuration Util from sysutils of HyperUBot. A prefunction allows you to get any config stored in the global dictionary which works as followed:

```python
getConfig(config_name[, default_value])
```

config_name: is the name of your custom configuration\
default_value (optional): default value in case config_name doesn't exist\
getConfig() returns the value from config_name else from default_value

Example usage:

```python
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.configuration import getConfig  # import getConfig

ehandler = EventHandler()

@ehandler.on(command="myconfig", hasArgs=True, outgoing=True)
async def action(event):
    myConfig = getConfig("myCustomConfig")  # get your custom config
    await event.edit("This is my custom config: " + myConfig)
    return
```

if `config_name` does not exist and `default_value` is not set, `None` will be returned instead


Hopefully, this mechanic is now simple and have fun developing modules!
