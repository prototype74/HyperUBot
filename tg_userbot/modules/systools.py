# My stuff
from tg_userbot import VERSION, PROJECT
from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import StatusText as msgRep
from tg_userbot.include.aux_funcs import pinger, getGitReview

# Telethon stuff
from telethon import version

# Misc Imports
from platform import python_version, uname
from asyncio import sleep
from datetime import datetime

# Module Global Variables
USER = uname().node # Maybe add a username in future
STARTTIME = datetime.now()

@watcher(outgoing=True, pattern=r"^\.status$")
async def statuschecker(stat):
    global STARTTIME
    uptime = datetime.now() - STARTTIME
    uptime_hours = uptime.seconds // 3600  # (60 * 60)
    uptime_mins = uptime.seconds // 60 % 60
    uptime_secs = uptime.seconds % 60
    uptimeSTR = f"{uptime.days} " + msgRep.DAYS + f", {uptime_hours:02}:{uptime_mins:02}:{uptime_secs:02}"
    commit = await getGitReview()
    rtt = pinger("1.1.1.1") #cloudfare's
    reply = msgRep.SYSTEM_STATUS + "`" + msgRep.ONLINE + "`" + "\n\n"
    reply += msgRep.UBOT + "`" + PROJECT + "`" + "\n"
    reply += msgRep.VER_TEXT + "`" + VERSION + "`" + "\n"
    reply += msgRep.COMMIT_NUM + "`" + commit + "`" + "\n"
    if rtt:
        reply += msgRep.RTT + "`" + str(rtt) + "`" + "\n"
    else:
        reply += msgRep.RTT + "`" + msgRep.ERROR + "`" + "\n"
    reply += msgRep.BOT_UPTIMETXT + uptimeSTR + "\n"
    reply += "\n"
    reply += msgRep.TELETON_VER + "`" + str(version.__version__) + "`" + "\n"
    reply += msgRep.PYTHON_VER + "`" + str(python_version()) + "`" + "\n"
    reply += msgRep.GITAPI_VER + "`" + msgRep.ERROR + "`" + "\n"
    reply += msgRep.CASAPI_VER + "`" + msgRep.ERROR + "`" + "\n"
    await stat.edit(reply)
    return

@watcher(outgoing=True, pattern=r"^\.kickme$")
async def kickme(leave):
    await leave.edit("`Leaving chat`")
    await sleep(0.1) #wait to avoid bad stuff
    await leave.client.kick_participant(leave.chat_id, 'me')
