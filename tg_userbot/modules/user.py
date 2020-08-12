# My Stuff
from tg_userbot.include.watcher import watcher
from tg_userbot import BOTLOG, BOTLOG_CHATID
from tg_userbot.include.language_processor import UserText as msgRep

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
