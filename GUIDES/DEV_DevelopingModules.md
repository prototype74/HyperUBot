# HyperUBot Guide - Developing Modules for HyperUBot

## Before you start...

Before you start to create your own (hopefully not harmful) modules, you need to know few, yeah actually not few information:

- **You need to be familiar with Python**. We will not teach you how Python works though basic knowlegde about Python are enough
- Create a new Python script (yourscript.py)
- **Read everything below carefully!**
- Your new modules do belong to the `modules_user` (HyperUBot/userbot/modules_user) folder. **Do not move them to `modules` folder!**
- Read the docstrings of each class and/or function. Classes and functions without docstrings are most likely not to be meant to be imported in your modules especially if the name does begin with an underscore! (read below for more info)
- Last but not least, you will need patience, specially if it's your first time

## Allowed imports

Not everything in HyperUBot should be imported to modules as approx. 60% of the code is meant for HyperUBot's core stuff only.

Allowed imports are:

- `userbot.include` (all scripts)
- `userbot.sysutils.colors`
- `userbot.sysutils.configurations` (predefined functions only)
- `userbot.sysutils.errors`
- `userbot.sysutils.event_handler`
- `userbot.sysutils.properties` (class `Properties` only)
- `userbot.sysutils.registration` (predefined functions only)
- `userbot.sysutils.sys_funcs`
- `userbot` (`PROJECT`, `SAFEMODE` and `log` only)

But well being creative is much better than using the creativity of other people, isn't it?

## Knowing the basics

For a Python script to be minimally compatible with the bot, and having the possibility to be run as a command, you will need to import the `EventHandler`, from `userbot.sysutils.event_handler`. The EventHandler is capable to catch Telegram events with the help of Telethon such as new messages, edited messages, chat actions (join, leave etc.) and much more. After this, create a new EventHandler object, like the example below:


```python
from userbot.sysutils.event_handler import EventHandler  # The EventHandler object

ehandler = EventHandler()  # The specific handler of our new module
```

> Note: The code example above demonstrate a whole Python script (not just a part of it), same to the following codes. Your are free to copy the examples we made.

You can also pass a logger to `EventHandler` as parameter to log stuff to terminal and follow error traces easier:

```python
from userbot.sysutils.event_handler import EventHandler  # The EventHandler object
from logging import getLogger  # import getLogger

log = getLogger(__name__)  # pass the current module's name
ehandler = EventHandler(log)  # set logger as parameter to EventHandler
```

## The power of outgoing commands (the favorite of all coder)

Nearly used by all commands that are out there, the outgoing commands. There are rarely commands that do not listen to outgoing messages. Anyway let's start with your command now. First of all, due to the fact that almost all prefunctions of Telethon are asynchronous, your bot command functions should be asynchronous too to be able to use these functions with `await`. This can be done, while declaring a function, by using the keyword `async`. Before declaring the function, however, you should add a line referencing to the `EventHandler` you created (meant is `@ehandler.on()`), specifying the command that triggers that action. An example could be:

```python
from userbot.sysutils.event_handler import EventHandler
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)

@ehandler.on(command="example", hasArgs=True, outgoing=True)
async def action(event):
    await event.edit("This is an example!")
    # Your stuff
    return
```

- `command="example"` tells the `EventHandler` to which command it should listen to, to trigger the specific function (your function in this case). As soon as you send `.example` message in any chat, `EventHandler` will execute your function, in other words it will edit your `.example` message to `This is an example!`.
- `hasArgs=True` tells the `EventHandler` whether your command takes more than just `.example` e.g. `.example test`. We calling this **Arguments** (hasArgs -> has Arguments). Some of our commands we made do accept arguments as well for example .ban, .speedtest etc.
- `outgoing=True` tells the `EventHandler` to listen to outgoing messages only, so messages you do sent

> Note: You should guarantee that your command isn't already used by a different module, specially not by modules we made.

## The bad reputation of incoming commands (not that bad but neither good)

What's the opposite of outgoing? You think it's incoming? Well yes, that's true. Incoming commands do as you may thought already listen to incoming messages only. Coding wise it's pretty much similar to outgoing commands:

```python
from userbot.sysutils.event_handler import EventHandler
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)

@ehandler.on(command="example", hasArgs=True, incoming=True)  # Look to the left!
async def action(event):
    await event.reply("This is an example response!")
    # Your stuff
    return
```

The table turns: now your userbot will response to everyone who sent `.example` in any chat where you're a participant.

> Note: This is the start of the misery, people could abuse it to let your userbot spam in a chat. As consequence Telegram may ban your account, temporary or in worst case permanently for spamming! Use incoming feature if you can limit the access to it for certain or specific stuff only.

## Freedom for 'on' listeners! (but only if you're a Hackerman)

The EventHandler offers more than just the `on` listener (remember: `@ehandler.on()`) which is limited for certain stuff only like the pattern, prefix, etc. If you want your command to be executed with a different prefix (not to dots) you can simply use a different listener. We called it `on_Pattern` listener. It offers much more customization for the developer. However we can't explain every detail how it works here. Rather read the docstring of this listener in `event_handler.py` (sysutils folder).

Example usage of `on_Pattern`:

```python
from userbot.sysutils.event_handler import EventHandler
from telethon.events import NewMessage, MessageEdited
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)

@ehandler.on_Pattern(pattern=r"^\!example(?: |$)(.*)",  # regex of example command 
                     events=[NewMessage, MessageEdited],  # used events
                     name="example",  # the name of the command
                     prefix="!",  # prefix of the command
                     hasArgs=True,  # does it take arguments? regex should match too
                     outgoing=True)  # listen to outgoing messages only
async def example(event):
    await event.edit("example confirmed!")
    return
```

As soon as you send `!example` in any chat, `EventHandler` will edit it to `example confirmed!`. The example code above works the same to `on` functions we had in our examples before this. The difference is, it will now response to `!` and not to `.` anymore.

You see it's more complex and meant for devs who really want more than just the basics.

## How can I get a message, an user or even a whole chat info?

At this point you have to check out [Telethon docs](https://docs.telethon.dev/en/latest/), this is something you have to teach yourself. HyperUBot does offer some features that Telethon may not. Read the next stuff below or check out the functions we made in `include` folder or in `sys_funcs.py` script. Remember, read the docstrings!

## Extra configurations needed? No problemo! but not too complicated please.

If a specific configuration is required for your module, add your custom configuration to the existing configurations in your config file. HyperUBot loads all configurations independent from config.env, config.ini or config.py automatically, so any special instruction is not required to add custom configurations.

To get a certain configuration you need to import `configurations` from `userbot.sysutils`. A prefunction allows you to get any config stored in the global configs of HyperUBot which works as followed:

```python
getConfig(config_name[, default_value])
```

- `config_name`: is the name of your custom configuration
- `default_value (optional)`: default value in case `config_name` doesn't exist

getConfig() returns the value from `config_name` else from `default_value`. If `config_name` does not exist and `default_value` is not set, `None` will be returned instead

Example usage:

```python
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.configuration import getConfig  # import getConfig

ehandler = EventHandler()

@ehandler.on(command="myconfig", hasArgs=True, outgoing=True)
async def action(event):
    myConfig = getConfig("MYCUSTOMCONFIG")  # get your custom config
    await event.edit("This is my custom config: " + myConfig)
    return
```

## Store attributes in a file? Can I do that?

Sure why not. We made a `Properties` class which allow you to store you module attributes to a file. Pretty useful if you want your module to load them later after a reboot, or after a long pause. To do so, import `Properties` from `userbot.sysutils.properties`. Properties have 3 core functions: init_props(), getprop() and setprop()

Example usage:

```python
from userbot.sysutils.properties import Properties  # import Properties

props = Properties("myprops")  # setup file
props.init_props()  # initialize props, checks if prop file isn't used already
props.setprop("testKey", "testValue")  # store key 'testKey' to 'myprops' file
print(props.getprop("testKey"))  # get 'testKey' from 'myprops' file
```

This is the basic way to use Properties but it's also usable in command functions:

```python
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.properties import Properties
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)

props = Properties("myprops")
props.init_props()

@ehandler.on(command="example", hasArgs=True, outgoing=True)
async def action(event):
    props.setprop("testKey", "testValue")
    my_prop = props.getprop("testKey")
    if my_prop:
        await event.edit("This is my prop: " + my_prop)
    else:
        await event.edit("Seems like my prop is empty :-(")
    return
```

> Note: Uh oh! The docstrings are calling, they want you to read them. For real, you should :)

## I want to explain how my command works! And become famous!!1!1!!!11

HyperUBot allows to register your module and command usage(s) with 3 definitely simply functions which need to be imported from `userbot.sysutils.registrations`:

- `register_cmd_usage("name of cmd/feature", "it's arguments", "usage")` -> Register the usage of a command or feature
- `register_module_desc("description")` -> Register the description of a module
- `register_module_info("name", "author(s)", "version")` -> Register the info e.g version, author etc. of a module

As soon as your information are successfully registered, you can view them with the `.modules` or `.listcmds <your cmd>` commands

Example usage:

```python
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)

@ehandler.on(command="example", hasArgs=True, outgoing=True)
async def action(event):
    await event.edit("This is an example!")
    # Your stuff
    return


register_cmd_usage("example",
                   "[optional: <ID>]",
                   "Prints an example response")

register_module_desc("I'm an example module!")
register_module_info(
    name="Example",
    authors="mr.example",
    version="1.0"
)
```

Still not famous? Don't worry, we aren't either. Anyway, hopefully, the mechanic of developing own modules is now simple and understandable.


Happy coding!
