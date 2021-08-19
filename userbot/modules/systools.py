# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import PROJECT, SAFEMODE
from userbot.include.aux_funcs import (event_log, sizeStrMaker, pinger,
                                       getGitReview)
from userbot.include.language_processor import (SystemToolsText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep,
                                                getBotLangCode, getBotLang)
from userbot.sysutils.configuration import getConfig, setConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.sysutils.sys_funcs import isWindows
from userbot.version import VERSION
import userbot.include.cas_api as cas
import userbot.include.git_api as git
from telethon import version
from platform import python_version
from datetime import datetime, timedelta
from uptime import uptime
from subprocess import check_output
from logging import getLogger
from os.path import getsize, isdir, isfile, join
from shutil import disk_usage
import time
from os import listdir

log = getLogger(__name__)
ehandler = EventHandler(log)
STARTTIME = datetime.now()


def textProgressBar(barLength: int, totalVal, usedVal) -> str:
    used_percentage = round((usedVal * 100 / totalVal), 2)
    bar_used_length = used_percentage * barLength / 100

    if bar_used_length > barLength:
        bar_used_length = barLength
    elif bar_used_length < 0:
        bar_used_length = 0

    bar_used = "#" * int(bar_used_length)
    bar_free = "-" * int(barLength - bar_used_length)
    return f"[{(bar_used + bar_free)}] {used_percentage}%"


@ehandler.on(command="status", outgoing=True)
async def statuschecker(stat):
    global STARTTIME
    uptimebot = datetime.now() - STARTTIME
    uptime_hours = uptimebot.seconds // 3600  # (60 * 60)
    uptime_mins = uptimebot.seconds // 60 % 60
    uptime_secs = uptimebot.seconds % 60
    uptimeSTR = (f"{uptimebot.days} " + msgRep.DAYS +
                 f", {uptime_hours:02}:{uptime_mins:02}:{uptime_secs:02}")
    uptimemachine = uptime()
    uptime_machine_converted = timedelta(seconds=uptimemachine)
    uptime_machine_array = str(uptime_machine_converted).split(" days, ")
    # The package uses "days" when days up is equal or above 2,
    # which fucks up math.
    if len(uptime_machine_array) == 1:
        uptime_machine_array = str(uptime_machine_converted).split(" day, ")
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
    uptimeMacSTR = (f"{uptime_machine_days} " + msgRep.DAYS +
                    f", {uptime_machine_hours}:{uptime_machine_minutes}:"
                    f"{uptime_machine_seconds}")
    commit = None
    try:
        commit = await getGitReview()
    except:
        pass
    rtt = pinger("1.1.1.1")  # cloudfare's
    reply = f"**{msgRep.SYSTEM_STATUS}**\n\n"
    reply += msgRep.UBOT + "`" + PROJECT + "`" + "\n"
    reply += msgRep.VER_TEXT + "`" + VERSION + "`" + "\n"
    if commit:
        reply += msgRep.COMMIT_NUM + "`" + commit + "`" + "\n"
    reply += msgRep.SAFEMODE + f"{msgRep.ON if SAFEMODE else msgRep.OFF}\n"
    reply += msgRep.LANG + f"{getBotLang()} ({getBotLangCode().upper()})\n"
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


@ehandler.on(command="storage", outgoing=True)
async def storage(event):
    def list_dirs(source) -> list:
        listed_dirs = []
        for name in listdir(source):
            srcname = join(source, name)
            listed_dirs.append(srcname)
            if isdir(srcname):
                for elem in list_dirs(srcname):
                    listed_dirs.append(elem)
        return listed_dirs
    def getSizeFromPath(path) -> int:
        listed_paths = list_dirs(path)
        size = getsize(path)
        for name in listed_paths:
            size += getsize(name)
        return size

    ubot_size = getSizeFromPath(".")
    sys_size = getSizeFromPath(join(".", "userbot", "modules"))
    user_size = getSizeFromPath(join(".", "userbot", "modules_user"))
    userdata_size = getSizeFromPath(getConfig("USERDATA"))
    try:
        tmpdl_size = getSizeFromPath(getConfig("TEMP_DL_DIR"))
    except:
        tmpdl_size = 0

    hdd = disk_usage("./")
    result = f"**{msgRep.STORAGE}**\n\n"
    result += f"__{msgRep.GENERAL}__\n"
    result += f"`{msgRep.STORAGE_TOTAL}: {sizeStrMaker(hdd.total)}`\n"
    result += f"`{msgRep.STORAGE_USED}: {sizeStrMaker(hdd.used)}`\n"
    result += f"`{msgRep.STORAGE_FREE}: {sizeStrMaker(hdd.free)}`\n\n"
    result += f"__{msgRep.USED_BY_HYPERUBOT}__\n"
    result += f"`{msgRep.STORAGE_TOTAL}: {sizeStrMaker(ubot_size)}`\n"
    result += f"`{msgRep.STORAGE_SYSTEM}: {sizeStrMaker(sys_size)}`\n"
    result += f"`{msgRep.STORAGE_USER}: {sizeStrMaker(user_size)}`\n"
    result += f"`{msgRep.STORAGE_USERDATA}: {sizeStrMaker(userdata_size)}`\n"
    result += f"`{msgRep.STORAGE_TEMP_DL}: {sizeStrMaker(tmpdl_size)}`\n\n"
    result += (f"`{msgRep.STORAGE_HDD} "
               f"{textProgressBar(22, hdd.total, hdd.used)}`")
    await event.edit(result)


@ehandler.on(command="shutdown", outgoing=True)
async def shutdown(power_off):
    await power_off.edit(msgRep.SHUTDOWN)
    if getConfig("LOGGING"):
        await event_log(power_off, "SHUTDOWN", custom_text=msgRep.SHUTDOWN_LOG)
    await power_off.client.disconnect()


@ehandler.on(command="reboot", hasArgs=True, outgoing=True)
async def restart(power_off):  # Totally not a shutdown kang *sips whiskey*
    if isWindows():
        await power_off.edit(msgRep.RESTART_UNSUPPORTED)
        return
    cmd_args = power_off.pattern_match.group(1).split(" ", 1)
    if cmd_args[0] == "safemode":
        setConfig("REBOOT_SAFEMODE", True)
    setConfig("REBOOT", True)
    await power_off.edit(msgRep.RESTART)
    time.sleep(1)  # just so we can actually see a message
    if getConfig("LOGGING"):
        await event_log(power_off, "RESTART", custom_text=msgRep.RESTART_LOG)
    await power_off.edit(msgRep.RESTARTED)
    await power_off.client.disconnect()


@ehandler.on(command="sysd", outgoing=True)
async def sysd(event):
    try:
        await event.edit(msgRep.SYSD_GATHER_INFO)
        result = check_output("neofetch --stdout", shell=True).decode()
        await event.edit(f"`{result}`")
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.SYSD_NEOFETCH_REQ)
    return


@ehandler.on(command="sendlog", outgoing=True)
async def send_log(event):
    chat = await event.get_chat()
    await event.edit(msgRep.UPLD_LOG)
    time.sleep(1)
    try:
        await event.client.send_file(chat, "hyper.log")
        await event.edit(msgRep.SUCCESS_UPLD_LOG)
    except Exception as e:
        log.error(f"Failed to upload HyperUBot log file: {e}")
        await event.edit(msgRep.FAILED_UPLD_LOG)
    return


for cmd in ("status", "storage", "shutdown", "reboot", "sysd", "sendlog"):
    register_cmd_usage(cmd,
                       usageRep.SYSTOOLS_USAGE.get(cmd, {}).get("args"),
                       usageRep.SYSTOOLS_USAGE.get(cmd, {}).get("usage"))

register_module_desc(descRep.SYSTOOLS_DESC)
register_module_info(
    name="System Tools",
    authors="nunopenim, prototpye74",
    version=VERSION
)
