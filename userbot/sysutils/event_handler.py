# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient
from userbot.include.language_processor import SystemUtilitiesText as msgResp
from telethon.events import ChatAction, MessageEdited, NewMessage
from logging import getLogger, Logger
from re import sub


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

    def on(self, pattern: str, **args):
        """
        Default listen on function which uses MessageEdited and NewMessage events.
        Recommended for outgoing messages/updates.

        Args:
            pattern (string): pattern to listen to (regex recommended)

        Note:
            Function accepts any further arguments as supported by MessageEdited and NewMessage events

        Example:
            from userbot.sysutils.event_handler import EventHandler
            ehandler = EventHandler()

            @ehandler.on(r"^\.example$", outgoing=True)
            async def example_handler(event):
                await event.edit("hi!")

        Returns:
            MessageEdited.Event or NewMessage.Event
        """
        def decorator(function):
            async def func_callback(event):
                try:
                    await function(event)
                except Exception as e:
                    # This block will be executed if the function, where the events are
                    # being used, has no own exception handler(s)
                    pattern_no_regex = sub(r"\W", "", pattern)  # remove any symbols from regex
                    self.log.error(f"Command '{pattern_no_regex}' stopped due to an unhandled exception "
                                   f"in function '{function.__name__}'", exc_info=True if self.traceback else False)
                    try:  # in case editing messages isn't allowed (channels)
                        await event.edit(f"`{msgResp.CMD_STOPPED.format(f'{pattern_no_regex}.exe')}`")
                    except:
                        pass
            tgclient.add_event_handler(func_callback, MessageEdited(pattern=pattern, **args))
            tgclient.add_event_handler(func_callback, NewMessage(pattern=pattern, **args))
            return func_callback
        return decorator

    def on_NewMessage(self, pattern: str, **args):
        """
        Listen to NewMessage events only.

        Args:
            pattern (string): pattern to listen to (regex recommended)

        Note:
            Function accepts any further arguments as supported by NewMessage events

        Example:
            from userbot.sysutils.event_handler import EventHandler
            ehandler = EventHandler()

            @ehandler.on_NewMessage(r"^\.example$", outgoing=True)
            async def example_handler(event):
                await event.edit("hi!")

        Returns:
            NewMessage.Event
        """
        def decorator(function):
            async def func_callback(event):
                try:
                    await function(event)
                except Exception as e:
                    pattern_no_regex = sub(r"\W", "", pattern)
                    self.log.error(f"Command '{pattern_no_regex}' stopped due to an unhandled exception "
                                   f"in function '{function.__name__}'", exc_info=True if self.traceback else False)
                    try:
                        await event.edit(f"`{msgResp.CMD_STOPPED.format(f'{pattern_no_regex}.exe')}`")
                    except:
                        pass
            tgclient.add_event_handler(func_callback, NewMessage(pattern=pattern, **args))
            return func_callback
        return decorator

    def on_ChatAction(self, **args):
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
            tgclient.add_event_handler(func_callback, ChatAction(**args))
            return func_callback
        return decorator
