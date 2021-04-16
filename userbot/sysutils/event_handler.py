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
from re import compile, sub

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

    def __removeRegEx(self, pattern: str) -> str:
        """
        Removes any word characters from pattern

        Args:
            pattern (string): pattern to remove word characters

        Returns:
            string without word characters
        """
        return sub(r"\W", "", pattern)

    def __isRegExCMD(self, pattern: str) -> bool:
        """
        Check if pattern has regular expressions

        Args:
            pattern (string): pattern to check for regex

        Returns:
            True if valid regex found else False
        """
        pattern_no_regex = self.__removeRegEx(pattern)
        if pattern == pattern_no_regex:
            return False
        try:
            compile(pattern)
        except:
            return False
        return True

    def on(self, pattern: str = None, command: str = None, alt: str = None, hasArgs: bool = False, **args):
        """
        Default listen on function which uses MessageEdited and NewMessage events.
        Recommended for outgoing messages/updates.

        Args:
            pattern (string): pattern to listen to (regex required; must be None; obsolete)
            command (string): command to listen to (must be None)
            alt (string): alternative way to 'command' (must be None)
            hasArgs (bool): whether 'command' takes arguments (default to False)

        Note:
            Argument 'command' is preferred, if pattern and command are used then pattern will be ignored.
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
            nonlocal command
            nonlocal alt
            pattern_no_cmd = False
            if not pattern and not command:
                return None
            if pattern and not command:
                command = pattern
                pattern_no_cmd = True
                self.log.info(f"[EventHandler.on()] parameter 'pattern' is obsolete, please update to "\
                              f"'command' instead (in function '{function.__name__}')")
            command_no_regex = self.__removeRegEx(command)  # remove any symbols from regex
            if alt:
                alt = self.__removeRegEx(alt)
            if not pre_register_cmd(command_no_regex, alt, hasArgs, function):
                self.log.error(f"Unable to add command '{command_no_regex}' in function '{function.__name__}' "\
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
                        command_no_regex = event.pattern_match.group(0).split(" ")[0][1:]
                    except:
                        pass
                    self.log.error(f"Command '{command_no_regex}' stopped due to an unhandled exception "
                                   f"in function '{function.__name__}'", exc_info=True if self.traceback else False)
                    try:  # in case editing messages isn't allowed (channels)
                        await event.edit(f"`{msgResp.CMD_STOPPED.format(f'{command_no_regex}.exe')}`")
                    except:
                        pass
            if not pattern_no_cmd:
                if self.__isRegExCMD(command):
                    command = self.__removeRegEx(command)  # TODO
                if alt:
                    command = fr"^\.(?:{command}|{alt})(?: |$)(.*)" if hasArgs else fr"^\.(?:{command}|{alt})$"
                else:
                    command = fr"^\.{command}(?: |$)(.*)" if hasArgs else fr"^\.{command}$"
            else:
                command = pattern  # 'restore' regex
            tgclient.add_event_handler(func_callback, MessageEdited(pattern=command, **args))
            tgclient.add_event_handler(func_callback, NewMessage(pattern=command, **args))
            return func_callback
        return decorator

    def on_NewMessage(self, pattern: str = None, command: str = None, alt: str = None, hasArgs: bool = False, **args):
        """
        Listen to NewMessage events only.

        Args:
            pattern (string): pattern to listen to (regex required; must be None; obsolete)
            command (string): command to listen to (must be None)
            alt (string): alternative way to 'command' (must be None)
            hasArgs (bool): whether 'command' takes arguments (default to False)

        Note:
            Argument 'command' is preferred, if pattern and command are used then pattern will be ignored.
            Function accepts any further arguments as supported by NewMessage events

        Example:
            from userbot.sysutils.event_handler import EventHandler
            ehandler = EventHandler()

            @ehandler.on(command="example", outgoing=True)
            async def example_handler(event):
                await event.edit("hi!")

        Returns:
            NewMessage.Event
        """
        def decorator(function):
            nonlocal command
            nonlocal alt
            pattern_no_cmd = False
            if not pattern and not command:
                return None
            if pattern and not command:
                command = pattern
                pattern_no_cmd = True
                self.log.info(f"[EventHandler.on_NewMessage()] parameter 'pattern' is obsolete, please update to "\
                              f"'command' instead (in function '{function.__name__}')")
            command_no_regex = self.__removeRegEx(command)
            if alt:
                alt = self.__removeRegEx(alt)
            if not pre_register_cmd(command_no_regex, alt, hasArgs, function):
                self.log.error(f"Unable to add command '{command_no_regex}' in function '{function.__name__}' "\
                                "to event handler as previous registration failed")
                return None
            async def func_callback(event):
                try:
                    await function(event)
                except Exception as e:
                    try:
                        command_no_regex = event.pattern_match.group(0).split(" ")[0][1:]
                    except:
                        pass
                    self.log.error(f"Command '{command_no_regex}' stopped due to an unhandled exception "
                                   f"in function '{function.__name__}'", exc_info=True if self.traceback else False)
                    try:
                        await event.edit(f"`{msgResp.CMD_STOPPED.format(f'{command_no_regex}.exe')}`")
                    except:
                        pass
            if not pattern_no_cmd:
                if self.__isRegExCMD(command):
                    command = self.__removeRegEx(command)  # TODO
                if alt:
                    command = fr"^\.(?:{command}|{alt})(?: |$)(.*)" if hasArgs else fr"^\.(?:{command}|{alt})$"
                else:
                    command = fr"^\.{command}(?: |$)(.*)" if hasArgs else fr"^\.{command}$"
            else:
                command = pattern
            tgclient.add_event_handler(func_callback, NewMessage(pattern=command, **args))
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
