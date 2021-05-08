# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .registration import pre_register_cmd
from userbot import tgclient
from userbot.include.language_processor import SystemUtilitiesText as msgResp
from telethon.events import ChatAction, MessageEdited, NewMessage
from logging import getLogger, Logger
from re import match

class EventHandler:
    def __init__(self, log: Logger = None, traceback: bool = True):
        """
        Initialize EventHandler to catch Telethon Events such as NewMessage or ChatAction

        Args:
            log (Logger): passing an already existing logger. Default None
            logging (boolean): Create a traceback in case of unhandled exceptions. Default True

        Example:
            from userbot.sysutils.event_handler import EventHandler
            from logging import getLogger

            log = getLogger(__name__)
            ehandler = EventHandler()  # initialize with default logger
            ehandler = EventHandler(log)  # initialize with an already existing logger
            ehandler = EventHandler(log, False)  # initialize with an already existing logger without Tracebacks
        """
        self.log = log if isinstance(log, Logger) else getLogger(__name__)
        self.traceback = traceback

    def __checkCmdValidity(self, command: str) -> bool:
        """
        Check if command string is valid to alphabetic and/or numeric only.
        Special characters will cause the validity to fail

        Args:
            command (string): command to check

        Returns:
            True if command string is valid else False
        """
        try:
            return True if match("^[A-Za-z0-9]*$", command) else False
        except:
            pass
        return False

    def on(self, command: str, alt: str = None,
           hasArgs: bool = False, ignore_edits: bool = False, *args, **kwargs):
        """
        Default listen on function which uses MessageEdited and NewMessage events.
        Recommended for outgoing messages/updates.

        Args:
            command (string): command to listen to (must not be None)
            alt (string): alternative way to 'command' (must be None)
            hasArgs (bool): whether 'command' takes arguments (default to False)
            ignore_edits (bool): ignore edited messages (default to False)

        Note:
            Function accepts any further arguments as supported by MessageEdited and NewMessage events

        Example:
            from userbot.sysutils.event_handler import EventHandler
            ehandler = EventHandler()

            @ehandler.on(command="example", outgoing=True)
            async def example_handler(event):
                await event.edit("hi!")

        Returns:
            MessageEdited.Event or NewMessage.Event
        """
        def decorator(function):
            if not function:
                return None
            if not callable(function):
                return None
            if not command:
                self.log.error(f"Command in function '{function.__name__}' must not be empty.")
                return None
            if not self.__checkCmdValidity(command):
                self.log.error(f"Validity check for '{command}' in function '{function.__name__}' "\
                               "failed. Special characters are not allowed.")
                return None
            if alt and not self.__checkCmdValidity(alt):
                self.log.error(f"Validity check for '{alt}' (alternative command of '{command}') "\
                               f"in function '{function.__name__}' failed. "\
                               "Special characters are not allowed.")
                return None
            if not pre_register_cmd(command, alt, hasArgs, ".", False, False, function):
                self.log.error(f"Unable to add command '{command}' in function '{function.__name__}' "\
                                "to event handler as previous registration failed")
                return None
            async def func_callback(event):
                try:
                    await function(event)
                except Exception as e:
                    # This block will be executed if the function, where the events are
                    # being used, has no own exception handler(s)
                    try:
                        # get current executed command
                        curr_cmd = event.pattern_match.group(0).split(" ")[0][1:]
                    except:
                        curr_cmd = command
                    self.log.error(f"Command '{curr_cmd}' stopped due to an unhandled exception "
                                   f"in function '{function.__name__}'", exc_info=True if self.traceback else False)
                    try:  # in case editing messages isn't allowed (channels)
                        await event.edit(f"`{msgResp.CMD_STOPPED.format(f'{curr_cmd}.exe')}`")
                    except:
                        pass
            if alt:
                cmd_regex = fr"^\.(?:{command}|{alt})(?: |$)(.*)" if hasArgs else fr"^\.(?:{command}|{alt})$"
            else:
                cmd_regex = fr"^\.{command}(?: |$)(.*)" if hasArgs else fr"^\.{command}$"
            try:
                if not ignore_edits:
                    tgclient.add_event_handler(func_callback, MessageEdited(pattern=cmd_regex, *args, **kwargs))
                tgclient.add_event_handler(func_callback, NewMessage(pattern=cmd_regex, *args, **kwargs))
            except Exception as e:
                self.log.error(f"Failed to add command '{command}' to client "\
                               f"(in function '{function.__name__}')",
                               exc_info=True if self.traceback else False)
                return None
            return func_callback
        return decorator

    def on_NewMessage(self, command: str, alt: str = None,
                      hasArgs: bool = False, *args, **kwargs):
        """
        Listen to NewMessage events only.

        Args:
            command (string): command to listen to (must not be None)
            alt (string): alternative way to 'command' (must be None)
            hasArgs (bool): whether 'command' takes arguments (default to False)

        Note:
            Function accepts any further arguments as supported by NewMessage events

        Example:
            from userbot.sysutils.event_handler import EventHandler
            ehandler = EventHandler()

            @ehandler.on_NewMessage(command="example", outgoing=True)
            async def example_handler(event):
                await event.edit("hi!")

        Returns:
            NewMessage.Event
        """
        return self.on(command, alt, hasArgs, True, *args, **kwargs)

    def on_ChatAction(self, *args, **kwargs):
        """
        Listen to chat activities (join, leave, new pinned message etc.) in any or certain chats.

        Note:
            Function accepts any further arguments as supported by ChatAction events

        Example:
            from userbot.sysutils.event_handler import EventHandler
            ehandler = EventHandler()

            @ehandler.on_ChatAction()
            async def example_handler(event):
                if event.user_joined:
                    await event.reply("Welcome!")

        Returns:
            ChatAction.Event
        """
        def decorator(function):
            async def func_callback(event):
                try:
                    await function(event)
                except Exception as e:
                    self.log.error(f"Function '{function.__name__}' stopped due to an unhandled exception",
                                   exc_info=True if self.traceback else False)
            try:
                tgclient.add_event_handler(func_callback, ChatAction(*args, **kwargs))
            except Exception as e:
                self.log.error(f"Failed to add a chat action feature to client "\
                               f"(in function '{function.__name__}')",
                               exc_info=True if self.traceback else False)
                return None
            return func_callback
        return decorator

    def on_Pattern(self, pattern: str, events, name: str, prefix: str = ".",
                   hasArgs: bool = False, no_space_arg: bool = False,
                   no_cmd: bool = False, *args, **kwargs):
        """
        Listen to given pattern depending on Event(s). This event handler gives the
        most freedom, however you should guarantee that your pattern doesn't
        cause conflicts with other registered commands/patterns!

        Args:
            pattern (string): pattern to listen to (must not be None)
            events: Event to add to client. Also supported as list of Events (must not be None)
            name: name of feature. should match pattern but without regex, not
                  required to match patttern if no_cmd is set. (must not be None)
            prefix (string): the prefix used at the beginning of your pattern
                             e.g. .example, /example or !example. Default is dot.
                             This is set automatically to a 'string wise none' if no_cmd is set.
            hasArgs (bool): whether pattern takes arguments, default to False, stays False if no_cmd is set
            no_space_arg (bool): removes the space between command and argument in usage info
            no_cmd (bool): if pattern is no command to handle (default to False)

        Note:
            1. **args should be arguments supported by the events. If a parameter is not
               supported by an event, this handler may not work then.
            2. Alternative commands not supported

        Example:
            from userbot.sysutils.event_handler import EventHandler
            from telethon.events import NewMessage, MessageEdited
            ehandler = EventHandler()

            @ehandler.on_Pattern(pattern=r"^\!example(?: |$)(.*)",
                                 events=[NewMessage, MessageEdited],
                                 name="example",
                                 prefix="!",
                                 hasArgs=True,
                                 outgoing=True)
            async def example(event):
                await event.edit("example confirmed!")
                return

            # auto reply to a certain person
            @ehandler.on_Pattern(pattern=r"^Hi Paul$",
                                 events=NewMessage,
                                 name="autoreplytopaul",
                                 chats=[123456789],
                                 no_cmd=True,
                                 incoming=True)
            async def autoreplytopaul(event):
                await event.client.send_message(event.chat_id, "Oh, hi Mark")
                return

        Returns:
            the given Event(s) from events
        """
        def decorator(function):
            if not function:
                return None
            if not callable(function):
                return None
            if not name:
                self.log.error(f"Name of command/feature in function '{function.__name__}' "\
                               "must not be empty.")
                return None
            if not pre_register_cmd(name, None, hasArgs if not no_cmd else False,
                                    prefix if not no_cmd else "", no_space_arg, no_cmd, function):
                self.log.error(f"Unable to add command/feature '{name}' in function '{function.__name__}' "\
                                "to event handler as previous registration failed")
                return None
            async def func_callback(event):
                try:
                    await function(event)
                except Exception as e:
                    if not no_cmd:
                        self.log.error(f"Command '{name}' stopped due to an unhandled exception "
                                       f"in function '{function.__name__}'",
                                       exc_info=True if self.traceback else False)
                        try:
                            await event.edit(f"`{msgResp.CMD_STOPPED.format(f'{name}.exe')}`")
                        except:
                            pass
                    else:
                        self.log.error(f"Feature '{name}' stopped due to an unhandled exception "
                                       f"in function '{function.__name__}'",
                                       exc_info=True if self.traceback else False)
            try:
                if isinstance(events, list):
                    for event in events:
                        tgclient.add_event_handler(func_callback, event(pattern=pattern, *args, **kwargs))
                else:
                    tgclient.add_event_handler(func_callback, events(pattern=pattern, *args, **kwargs))
            except Exception as e:
                self.log.error(f"Failed to add command/feature '{name}' to client "\
                               f"(in function '{function.__name__}')",
                               exc_info=True if self.traceback else False)
                return None
            return func_callback
        return decorator
