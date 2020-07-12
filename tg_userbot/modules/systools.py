#My stuff
from tg_userbot.watcher import watcher
from tg_userbot import VERSION, PROJECT
from tg_userbot.language_processor import StatusText as msgRep

#Telethon stuff
from telethon import version

#Misc Imports
from platform import python_version, uname

#Module Global Variables
USER = uname().node # Maybe add a username in future

def rttCalc(): # To implement!
    return None

@watcher(outgoing=True, pattern=r"^\.status$")
async def statuschecker(stat):
    rtt = rttCalc()
    reply = msgRep.SYSTEM_STATUS + "`" + msgRep.ONLINE + "`" + "\n\n"
    reply += msgRep.UBOT + "`" + PROJECT + "`" + "\n"
    reply += msgRep.VER_TEXT + "`" + VERSION + "`" + "\n"
    if rtt:
        reply += msgRep.RTT + "`" + str(rtt) + "`" + "\n"
    else:
        reply += msgRep.RTT + "`" + msgRep.ERROR + "`" + "\n"
    reply += "\n"
    reply += msgRep.TELETON_VER + "`" + str(version.__version__) + "`" + "\n"
    reply += msgRep.PYTHON_VER + "`" + str(python_version()) + "`" + "\n"
    reply += msgRep.GITAPI_VER + "`" + msgRep.ERROR + "`" + "\n"
    reply += msgRep.CASAPI_VER + "`" + msgRep.ERROR + "`" + "\n"
    await stat.edit(reply)
    return