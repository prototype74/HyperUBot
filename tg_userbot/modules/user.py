# My Stuff
from tg_userbot.include.watcher import watcher

# Misc Imports
from asyncio import sleep

@watcher(outgoing=True, pattern=r"^\.kickme$")
async def kickme(leave):
    await leave.edit("`Leaving chat`")
    await sleep(0.1) #wait to avoid bad stuff
    await leave.client.kick_participant(leave.chat_id, 'me')
