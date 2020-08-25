# Auxiliary functions used in the entire project, to keep the code clean.
# Nuno Penim, 2020

# My imports
from tg_userbot.include.language_processor import GeneralMessages as msgsLang

# Telethon imports
from telethon.tl.types import User
from telethon.tl.functions.users import GetFullUserRequest

# Misc imports
import os
from subprocess import check_output
from asyncio import create_subprocess_exec as asyncr
from asyncio.subprocess import PIPE as asyncPIPE
from shutil import which


async def fetch_user(event=None, full_user=False, get_chat=False):
    if not event:
        return (None, None) if get_chat else None
    if event.reply_to_msg_id:
        message = await event.get_reply_message()
        # focus to original author on forwarded messages
        if message.fwd_from is not None and message.fwd_from.channel_id is not None:
            await event.edit(msgsLang.CHAT_NOT_USER)
            return (None, None) if get_chat else None
        elif message.fwd_from is not None and message.fwd_from.from_id is not None:
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
                except:
                    chat_obj = None
            else:
                user = args_from_event[0]
                chat_obj = await event.get_chat() if get_chat else None
        except Exception as e:
            await event.edit(f"`{msgsLang.FAIL_FETCH_USER}: {e}`")
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
        await event.edit(f"`{msgsLang.CALL_UREQ_FAIL}: {e}`")

    return (None, chat_obj) if get_chat else None


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

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

def speed_convert(size):
    power = 2 ** 10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

async def getGitReview():
    commit = msgsLang.ERROR
    if which("git") is not None:
        ver = await asyncr("git", "describe", "--all", "--long", stdout=asyncPIPE, stderr=asyncPIPE)
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())
        verdiv = verout.split("-")
        commit = verdiv[2]
    return commit
