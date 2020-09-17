# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import LOGGING_CHATID
from userbot.include.language_processor import GeneralMessages as msgsLang
from telethon.tl.types import User
from telethon.tl.functions.users import GetFullUserRequest
from logging import getLogger
import os
from subprocess import check_output
from asyncio import create_subprocess_exec as asyncr
from asyncio.subprocess import PIPE as asyncPIPE
from shutil import which

log = getLogger(__name__)

async def fetch_user(event=None, full_user=False, get_chat=False, org_author=False):
    if not event:
        return (None, None) if get_chat else None
    if event.reply_to_msg_id:
        message = await event.get_reply_message()
        # focus to original author on forwarded messages if org_author is set to True
        if (not message.from_id and message.fwd_from and message.fwd_from.channel_id) or \
           (message.fwd_from and message.fwd_from.channel_id and org_author):
            if message.from_id:  # fallback to forwarder ID if not None
                user = message.from_id
            else:
                await event.edit(msgsLang.CHAT_NOT_USER)
                return (None, None) if get_chat else None
        elif message.fwd_from and message.fwd_from.from_id and org_author:
            user = message.fwd_from.from_id
        else:
            user = message.from_id
        chat_obj = await event.get_chat() if get_chat else None  # current chat
    else:
        try:
            # args_from_event becomes a list. it takes maximum of 2 arguments,
            # more than 2 will be appended to second element.
            args_from_event = event.pattern_match.group(1).split(" ", 1)
            if len(args_from_event) == 2:
                user, chat = args_from_event
                try:
                    chat = int(chat)  # chat ID given
                except:
                    pass

                try:
                    chat_obj = await event.client.get_entity(chat) if get_chat else None
                    if type(chat_obj) is User:  # entity is not a chat or channel object
                        chat_obj = None
                except Exception as e:
                    log.warning(e)
                    chat_obj = None
            else:
                user = args_from_event[0]
                chat_obj = await event.get_chat() if get_chat else None
        except Exception as e:
            log.warning(e)
            await event.edit(msgsLang.FAIL_FETCH_USER)
            return (None, None) if get_chat else None

        try:
            user = int(user)
        except:
            pass

        if not user:
            oh_look_its_me = await event.client.get_me()
            user = oh_look_its_me.id

    try:
        if full_user:
            user_obj = await event.client(GetFullUserRequest(user))
        else:
            user_obj = await event.client.get_entity(user)
            if not type(user_obj) is User:
               await event.edit(msgsLang.ENTITY_NOT_USER)
               user_obj = None
        return (user_obj, chat_obj) if get_chat else user_obj
    except Exception as e:
        log.warning(e)
        await event.edit(msgsLang.CALL_UREQ_FAIL)

    return (None, chat_obj) if get_chat else None

async def event_log(event, event_name: str, user_name=None, user_id=None, username=None, chat_title=None, chat_link=None, chat_id=None, custom_text=None):
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
        await event.client.send_message(LOGGING_CHATID, text)
    except Exception as e:
        log.warning(f"EVENT_LOG ({event_name}): {e}")
    return

def isRemoteCMD(event, chat_id: int) -> bool:
    try:
        chat_from_event = int(str(event.chat_id)[3:]) if str(event.chat_id).startswith("-100") else event.chat_id
        return True if not chat_id == chat_from_event else False
    except Exception as e:
        log.error(e)
    return False

# Systools/Webtools
def pinger(address):
    if os.name == "nt":
        output = check_output("ping -n 1 " + address + " | findstr time*", shell=True).decode()
        outS = output.splitlines()
        out = outS[0]
    else:
        out = check_output("ping -c 1 " + address + " | grep time=", shell=True).decode()
    splitOut = out.split(' ')
    under = False
    stringtocut = ""
    for line in splitOut:
        if (line.startswith('time=') or line.startswith('time<')):
            stringtocut = line
            break
    newstra = stringtocut.split('=')
    if len(newstra) == 1:
        under = True
        newstra = stringtocut.split('<')
    newstr = ""
    if os.name == 'nt':
        newstr = newstra[1].split('ms')
    else:
        newstr = newstra[1].split(' ')  # redundant split, but to try and not break windows ping
    ping_time = float(newstr[0])
    if os.name == 'nt' and under:
        return "<" + str(ping_time) + " ms"
    else:
        return str(ping_time) + " ms"

async def getGitReview():
    commit = msgsLang.ERROR
    if which("git") is not None:
        ver = await asyncr("git", "describe", "--all", "--long", stdout=asyncPIPE, stderr=asyncPIPE)
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())
        verdiv = verout.split("-")
        commit = verdiv[2]
    return commit

# Package Manager
def sizeStrMaker(value: int): #
    if value < 1024:
        return str(value) + " B"
    newval = float(value)
    if value > 1023 and value < 1024*1024:
        newval = newval / 1024
        return str(round(newval, 2)) + " kB"
    else:
        newval = newval / 1024 / 1024
        return str(round(newval, 2)) + " MB"
