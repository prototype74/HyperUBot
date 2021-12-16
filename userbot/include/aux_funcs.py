# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.language_processor import GeneralMessages as msgsLang
from userbot.sysutils.configuration import getConfig
from telethon.tl.types import PeerChannel, Channel, User
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.users import GetFullUserRequest
from logging import getLogger
from subprocess import check_output
from asyncio import create_subprocess_exec as asyncr
from asyncio.subprocess import PIPE as asyncPIPE
from shutil import which
from icmplib import ping

log = getLogger(__name__)


async def fetch_user(event=None, full_user=False,
                     get_chat=False, org_author=False):
    return await fetch_entity(event, full_user, get_chat, org_author)


async def fetch_entity(event=None, full_obj=False,
                       get_chat=False, org_author=False):
    """
    Fetch an user or channel (and a target chat) information from event

    Args:
        event (Event): any event e.g. NewMessage
        full_obj (bool): fetch ChatFull/UserFull object instead.
                         Does not work with groups.
        get_chat (bool): fetches Chat/Channel object too.
                         This changes the return to a tuple
        org_author (bool): focus to original author of a replied message

    Example:
        @ehandler.on(command="example", outgoing=True)
        async def example_handler(event):
            user, chat = fetch_entity(event, get_chat=True)
            await event.edit(f"hi {user.first_name}, welcome in {chat.title}!")

    Returns:
        - Channel/User object (default) or
        - ChatFull/UserFull object if full_obj is set to True or
        - A tuple ((Channel/User, Chat/Channel) or
          (ChatFull/UserFull, Chat/Channel)) if get_chat is set to True
    """
    if not event:
        return (None, None) if get_chat else None
    if event.reply_to_msg_id:
        message = await event.get_reply_message()
        if message.fwd_from and message.fwd_from.from_id and org_author:
            # focus to original author from forwarded messages
            if isinstance(message.fwd_from.from_id, PeerChannel):
                entity = f"-100{message.fwd_from.from_id.channel_id}"
                entity = int(entity)
            else:
                entity = message.fwd_from.from_id.user_id
        elif isinstance(message.from_id, PeerChannel):
            entity = f"-100{message.from_id.channel_id}"
            entity = int(entity)
        else:
            entity = (message.from_id.user_id
                    if message.from_id else message.sender_id)
        chat_obj = await event.get_chat() if get_chat else None  # current chat
        if not entity:
            await event.edit(msgsLang.PERSON_ANONYMOUS)
            return (None, None) if get_chat else None
    else:
        try:
            # args_from_event becomes a list. it takes maximum of 2 arguments,
            # more than 2 will be appended to second element.
            args_from_event = event.pattern_match.group(1).split(" ", 1)
            if len(args_from_event) == 2:
                entity, chat = args_from_event
                try:
                    chat = int(chat)  # chat ID given
                except ValueError:
                    pass

                try:
                    chat_obj = (await event.client.get_entity(chat)
                                if get_chat else None)
                    # entity is not a chat or channel object
                    if isinstance(chat_obj, User):
                        chat_obj = None
                except Exception as e:
                    log.warning(e)
                    chat_obj = None
            else:
                entity = args_from_event[0]
                chat_obj = await event.get_chat() if get_chat else None
        except Exception as e:
            log.warning(e)
            await event.edit(msgsLang.FAIL_FETCH_ENTITY)
            return (None, None) if get_chat else None

        try:
            entity = int(entity)
        except ValueError:
            pass

        if not entity:
            oh_look_its_me = await event.client.get_me()
            entity = oh_look_its_me.id

    try:
        if full_obj:
            try:
                if str(entity).startswith("-100"):
                    raise Exception(
                        "Forcefully triggered channel check")
                entity_obj = await event.client(GetFullUserRequest(entity))
            except Exception:
                entity_obj = await event.client(GetFullChannelRequest(entity))
                for c in entity_obj.chats:
                    if (entity_obj.full_chat.id == c.id) and not c.broadcast:
                       raise Exception(f"Entity '{entity}' is not a channel")
        else:
            entity_obj = await event.client.get_entity(entity)
            if not isinstance(entity_obj, (Channel, User)) or \
               (isinstance(entity_obj, Channel) and not entity_obj.broadcast):
                await event.edit(msgsLang.UNSUPPORTED_ENTITY)
                entity_obj = None
        return (entity_obj, chat_obj) if get_chat else entity_obj
    except Exception as e:
        log.warning(e)
        await event.edit(msgsLang.CANT_FETCH_REQ.format(entity))
    return (None, chat_obj) if get_chat else None


async def event_log(event, event_name: str, user_name=None,
                    user_id=None, username=None, chat_title=None,
                    chat_link=None, chat_id=None, custom_text=None):
    """
    Log any event by sending a message to the targeted chat

    Args:
        event (Event): any event e.g. NewMessage
        event_name (str): name of event (not Telethon event) e.g. ban
        user_name: name of user. Default to None
        user_id: ID from user. Default to None
        username: username from user. Default to None
        chat_title: Title of the specific chat. Default to None
        chat_link: link of the specific chat e.g. @example. Default to None
        chat_id: link of the specific chat e.g. -100123456789. Default to None
        custom_text: any custom text e.g. a note to the event. Default to None

    Example:
        @ehandler.on(command="example", outgoing=True)
        async def example_handler(event):
            user = fetch_user(event)
            await event_log(event, "BAN", user_name=user.first_name,
                            chat_id=event.chat_id)
    """
    log_chat_id = getConfig("LOGGING_CHATID")

    if not log_chat_id:
        log.warning(f"EVENT_LOG logging event '{event_name}' failed: "
                    "LOGGING_CHATID is not set")
        return

    text = f"**{event_name}**\n"
    if user_name and user_id and not username:
        text += f"{msgsLang.LOG_USER}: [{user_name}](tg://user?id={user_id})\n"
    elif user_name:
        text += f"{msgsLang.LOG_USER}: {user_name}\n"
    if username:
        text += f"{msgsLang.LOG_USERNAME}: @{username}\n"
    if user_id:
        text += f"{msgsLang.LOG_USER_ID}: `{user_id}`\n"
    if chat_title:
        text += f"{msgsLang.LOG_CHAT_TITLE}: {chat_title}\n"
    if chat_link:
        text += f"{msgsLang.LOG_CHAT_LINK}: @{chat_link}\n"
    if chat_id:
        text += f"{msgsLang.LOG_CHAT_ID}: `{chat_id}`\n"
    if custom_text:
        text += f"{custom_text}"

    try:
        await event.client.send_message(log_chat_id, text)
    except Exception as e:
        log.warning(f"EVENT_LOG ({event_name}): {e}")
    return


def isRemoteCMD(event, chat_id: int) -> bool:
    """
    Check if chat id from event matches chat_id. By this we can ensure if
    the command is remotely used.

    Args:
        event (Event): any event e.g. NewMessage
        chat_id (int): ID from targeted chat

    Example:
        @ehandler.on(command="example", outgoing=True)
        async def example_handler(event):
            user, chat = fetch_user(event, get_chat=True)
            isRemote = isRemoteCMD(event.chat_id, chat.id)
            if isRemote:
                await event.edit("Remote!")
            else:
                await event.edit("Not remote")

    Returns:
        A boolean
    """
    try:
        chat_from_event = (int(str(event.chat_id)[3:])
                           if str(event.chat_id).startswith("-100") else
                           event.chat_id)
        return True if not chat_id == chat_from_event else False
    except Exception as e:
        log.error(e)
    return False


def format_chat_id(chat) -> int:
    """
    Formats the chat id to a correct formation

    Args:
        chat (Channel/Chat): any chat object

    Example:
        @ehandler.on(command="example", outgoing=True)
        async def example_handler(event):
            user, chat = fetch_user(event, get_chat=True)
            await event.client.edit(format_chat_id(chat))

    Returns:
        An Integer
    """
    chat_id = chat.id
    try:
        if (hasattr(chat, "broadcast") and chat.broadcast) or \
           (hasattr(chat, "megagroup") and chat.megagroup):
            chat_id = f"-100{chat_id}"
        else:
            chat_id = f"-{chat_id}"
        chat_id = int(chat_id)
    except Exception as e:
        log.error(f"Failed to format chat id")
    return chat_id


# Systools/Webtools
def pinger(address: str) -> str:
    """
    Ping an IP or DNS server from given address

    Args:
        address (str): IP/DNS address e.g. "8.8.8.8"

    Example:
        ping = pinger("8.8.8.8")

    Returns:
        Ping result as a string
    """
    try:
        result = ping(address, count=1, interval=0.1,
                      timeout=2, privileged=False)
        return f"{result.avg_rtt} ms"
    except Exception:
        try:
            out = check_output(["ping", "-c", "1", address]).decode()
            out = out.split("\n")
            rtt_line = ""
            for elem in out:
                if "min/avg/max" in elem:
                    rtt_line = elem
                    break
            rtt_line = rtt_line.replace(" ", "")
            rtt_line = rtt_line.split("=")[-1]
            rtt_line = rtt_line.split("/")[0]
            return f"{rtt_line} ms"
        except Exception as e:
            log.warning(f"pinger: {e}")
    return "-- ms"


async def getGitReview():
    """
    Get the last commit ID from .git inside root directory. Returns 'None'
    if git is not detected.

    Example:
        commit = getGitReview()

    Returns:
        Commit ID as string else None
    """
    try:
        if which("git") is not None:
            ver = await asyncr("git", "describe", "--all", "--long",
                               stdout=asyncPIPE, stderr=asyncPIPE)
            stdout, stderr = await ver.communicate()
            verout = str(
                stdout.decode().strip()) + str(stderr.decode().strip())
            verdiv = verout.split("-")
            commit = verdiv[2]
        return commit
    except Exception:
        return None


# Package Manager
def sizeStrMaker(size: float, value: int = 0):
    """
    Convert given byte size recursively to a readable size

    Args:
        size (float): size in bytes
        value (int): just keep it 0

    Example:
        readable_size = sizeStrMaker(2048)
        print(readable_size)

    Returns:
        Converted size as string
    """
    if size < 1024:
        size_units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
        return str(round(size, 2)) + " " + size_units[value]
    size /= 1024
    value += 1
    return sizeStrMaker(size, value)
