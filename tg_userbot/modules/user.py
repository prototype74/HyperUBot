# My Stuff
from tg_userbot.include.watcher import watcher
from tg_userbot import BOTLOG, BOTLOG_CHATID, bot
from tg_userbot.include.language_processor import UserText as msgRep

# Telethon stuff
from telethon.tl.types import User, Chat, Channel

# Misc Imports
from asyncio import sleep

@watcher(outgoing=True, pattern=r"^\.kickme$")
async def kickme(leave):
    await leave.edit(msgRep.LEAVING)
    await sleep(0.1) #wait to avoid bad stuff
    await leave.client.kick_participant(leave.chat_id, 'me')
    if BOTLOG:
        await leave.client.send_message(BOTLOG_CHATID, msgRep.KICKME_LOG.format(leave.chat.title, leave.chat.id))
    return

@watcher(outgoing=True, pattern=r"^\.stats$")
async def stats(event):
    result = ""
    users = 0
    groups = 0
    super_groups = 0
    channels = 0
    bots = 0
    await event.edit(msgRep.STATS_PROCESSING)
    dialogs = await bot.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                bots += 1
            else:
                users += 1
        elif isinstance(currrent_entity, Chat):
            groups += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                channels += 1
            else:
                super_groups += 1
        else: # Should never reach this!
            print(d + ": Unrecognized chat type")
    result += msgRep.STATS_USERS.format(users)
    result += msgRep.STATS_BOTS.format(bots)
    result += msgRep.STATS_SUPER_GROUPS.format(super_groups)
    result += msgRep.STATS_GROUPS.format(groups)
    result += msgRep.STATS_CHANNELS.format(channels)
    await event.edit(result)
    return