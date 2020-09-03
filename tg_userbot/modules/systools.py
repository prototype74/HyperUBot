# My stuff
from tg_userbot import tgclient, VERSION, PROJECT, LOGGING, LOGGING_CHATID, MODULE_DESC, MODULE_DICT
from tg_userbot.include.aux_funcs import event_log
from tg_userbot.include.language_processor import (StatusText as msgRep, ModuleDescriptions as descRep,
                                                   ModuleUsages as usageRep)
from tg_userbot.include.aux_funcs import pinger, getGitReview
import tg_userbot.include.cas_api as cas
import tg_userbot.include.git_api as git

# Telethon stuff
from telethon import version
from telethon.events import NewMessage

# Misc Imports
from platform import python_version, uname
from datetime import datetime, timedelta
from uptime import uptime
from subprocess import check_output
from os.path import basename

# Module Global Variables
USER = uname().node # Maybe add a username in future
STARTTIME = datetime.now()

@tgclient.on(NewMessage(pattern=r"^\.status$", outgoing=True))
async def statuschecker(stat):
    global STARTTIME
    uptimebot = datetime.now() - STARTTIME
    uptime_hours = uptimebot.seconds // 3600  # (60 * 60)
    uptime_mins = uptimebot.seconds // 60 % 60
    uptime_secs = uptimebot.seconds % 60
    uptimeSTR = f"{uptimebot.days} " + msgRep.DAYS + f", {uptime_hours:02}:{uptime_mins:02}:{uptime_secs:02}"
    uptimemachine = uptime()
    uptime_machine_converted = timedelta(seconds=uptimemachine)
    uptime_machine_array = str(uptime_machine_converted).split(" days, ")
    if len(uptime_machine_array) < 2:
        uptime_machine_days = 0
        uptime_machine_time = uptime_machine_array[0].split(":")
    else:
        uptime_machine_days = uptime_machine_array[0]
        uptime_machine_time = uptime_machine_array[1].split(":")
    uptime_machine_hours = uptime_machine_time[0]
    if int(uptime_machine_hours) < 10:
        uptime_machine_hours = "0" + uptime_machine_hours
    uptime_machine_minutes = uptime_machine_time[1]
    uptime_machine_seconds = uptime_machine_time[2].split(".")[0]
    uptimeMacSTR = f"{uptime_machine_days} " + msgRep.DAYS + f", {uptime_machine_hours}:{uptime_machine_minutes}:{uptime_machine_seconds}"
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
    reply += msgRep.MAC_UPTIMETXT + uptimeMacSTR + "\n"
    reply += "\n"
    reply += msgRep.TELETON_VER + "`" + str(version.__version__) + "`" + "\n"
    reply += msgRep.PYTHON_VER + "`" + str(python_version()) + "`" + "\n"
    reply += msgRep.GITAPI_VER + "`" + git.vercheck() + "`" + "\n"
    reply += msgRep.CASAPI_VER + "`" + cas.vercheck() + "`" + "\n"
    await stat.edit(reply)
    return

@tgclient.on(NewMessage(pattern=r"^\.shutdown$", outgoing=True))
async def shutdown(power_off):
    await power_off.edit(msgRep.SHUTDOWN)
    if LOGGING:
        await power_off.client.send_message(LOGGING_CHATID, event_log("SHUTDOWN", custom_text=msgRep.SHUTDOWN_LOG))
    await power_off.client.disconnect()

@tgclient.on(NewMessage(pattern=r"^\.sysd$", outgoing=True))
async def sysd(event):
    try:
        result = check_output("neofetch --stdout", shell=True).decode()
        await event.edit(f"`{result}`")
    except:
        await event.edit(msgRep.SYSD_NEOFETCH_REQ)
    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.SYSTOOLS_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.SYSTOOLS_USAGE})
