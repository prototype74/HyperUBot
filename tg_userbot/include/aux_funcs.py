# Auxiliary functions used in the entire project, to keep the code clean.
# Nuno Penim, 2020

# My imports
from tg_userbot.include.language_processor import GeneralMessages as msgsLang

# Telethon imports
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.functions.users import GetFullUserRequest

# Misc imports
import os
from subprocess import check_output
from asyncio import create_subprocess_exec as asyncr
from asyncio.subprocess import PIPE as asyncPIPE
from shutil import which

# Admin tools
async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(msgsLang.GET_USER_FROM_EVENT_FAIL)
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj

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

async def getGitReview():
    commit = msgsLang.ERROR
    if which("git") is not None:
        ver = await asyncr("git", "describe", "--all", "--long", stdout=asyncPIPE, stderr=asyncPIPE)
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())
        verdiv = verout.split("-")
        commit = verdiv[2]
    return commit

# User module
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1).split(' ', 2)[0]
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user
