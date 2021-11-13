# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import pinger
from userbot.include.language_processor import (WebToolsText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon import functions
from dateutil.parser import parse
from logging import getLogger
from os import path, remove
from speedtest import Speedtest
from urllib.request import urlretrieve

log = getLogger(__name__)
ehandler = EventHandler(log)


@ehandler.on(command="rtt", outgoing=True)
async def rtt(message):
    rtt = pinger("1.0.0.1")
    await message.edit(msgRep.PING_SPEED + rtt)
    return


@ehandler.on(command="dc", outgoing=True)
async def datacenter(event):
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(msgRep.DCMESSAGE.format(result.country,
                                             result.this_dc,
                                             result.nearest_dc))
    return


@ehandler.on(command="ping", hasArgs=True, outgoing=True)
async def ping(args):
    commandParser = str(args.message.message).split(' ')
    if len(commandParser) != 2:
        await args.edit(msgRep.BAD_ARGS)
    else:
        dns = commandParser[1]
        try:
            duration = pinger(dns)
        except Exception as e:
            log.warning(e)
            await args.edit(msgRep.INVALID_HOST)
            return
        await args.edit(msgRep.PINGER_VAL.format(dns, duration))
    return


@ehandler.on(command="speedtest", hasArgs=True, outgoing=True)
async def speedtest(event):
    arg_from_event = event.pattern_match.group(1)
    chat = await event.get_chat()
    share_as_pic = True if arg_from_event.lower() == "pic" else False
    if share_as_pic:
        # if speedtest is send to a group and send media is
        # not allowed then skip 'pic' argument
        if (hasattr(chat, "default_banned_rights") and
                not chat.creator and not chat.admin_rights and
                chat.default_banned_rights.send_media):
            share_as_pic = False  # disable
    process = None
    all_test_passed = False
    check_mark = u"\u2705"
    warning = u"\u26A0"
    try:
        process = (f"**Speedtest by Ookla**\n\n"
                   f"- {msgRep.SPD_TEST_SELECT_SERVER}...")
        await event.edit(process)
        s = Speedtest()
        s.get_best_server()
        process = (f"**Speedtest by Ookla**\n\n"
                   f"- {msgRep.SPD_TEST_SELECT_SERVER} {check_mark}\n"
                   f"- {msgRep.SPD_TEST_DOWNLOAD}...")
        await event.edit(process)
        s.download()
        process = (f"**Speedtest by Ookla**\n\n"
                   f"- {msgRep.SPD_TEST_SELECT_SERVER} {check_mark}\n"
                   f"- {msgRep.SPD_TEST_DOWNLOAD} {check_mark}\n"
                   f"- {msgRep.SPD_TEST_UPLOAD}...")
        await event.edit(process)
        s.upload()
        process = (f"**Speedtest by Ookla**\n\n"
                   f"- {msgRep.SPD_TEST_SELECT_SERVER} {check_mark}\n"
                   f"- {msgRep.SPD_TEST_DOWNLOAD} {check_mark}\n"
                   f"- {msgRep.SPD_TEST_UPLOAD} {check_mark}")
        all_test_passed = True
        if share_as_pic:
            s.results.share()
        result = s.results.dict()
        if not result:
            await event.edit(process + "\n\n" +
                             f"`{msgRep.SPD_FAILED}: {msgRep.SPD_NO_RESULT}`")
            return
    except MemoryError as me:
        log.error(me)
        if not all_test_passed:
            process = process[:-3] + f" {warning}"
            await event.edit(process + "\n\n" +
                             f"`{msgRep.SPD_FAILED}: {msgRep.SPD_NO_MEMORY}`")
        else:
            await event.edit(process + "\n\n" +
                             f"`{msgRep.SPD_FAILED}: {msgRep.SPD_NO_MEMORY}`")
        return
    except Exception as e:
        log.error(e)
        if not all_test_passed:
            process = process[:-3] + f" {warning}"
            await event.edit(process + "\n\n" + msgRep.SPD_FAILED)
        else:
            await event.edit(process + "\n\n" + msgRep.SPD_FAILED)
        return

    if share_as_pic:
        try:
            await event.edit(process + "\n\n" + f"{msgRep.SPD_PROCESSING}...")
            png_file = path.join(getConfig("TEMP_DL_DIR"), "speedtest.png")
            urlretrieve(result["share"], png_file)
            await event.client.send_file(chat.id, png_file)
            await event.delete()
            remove(png_file)
        except Exception as e:
            log.error(e)
            await event.edit(msgRep.SPD_FAIL_SEND_RESULT)
    else:
        # Convert speed to Mbit/s
        down_in_mbits = round(result["download"] / 10**6, 2)
        up_in_mbits = round(result["upload"] / 10**6, 2)
        # Convert speed to MB/s (real speed?)
        down_in_mb = round(result["download"] / ((10**6) * 8), 2)
        up_in_mb = round(result["upload"] / ((10**6) * 8), 2)
        time = parse(result["timestamp"])
        ping = result["ping"]
        isp = result["client"]["isp"]
        host = result["server"]["sponsor"]
        host_cc = result["server"]["cc"]

        text = "<b>Speedtest by Ookla</b>\n\n"
        text += (f"<b>{msgRep.SPD_TIME}</b>: "
                 f"<code>{time.strftime('%B %d, %Y')} - "
                 f"{time.strftime('%H:%M:%S')} {time.tzname()}</code>\n")
        text += (f"<b>{msgRep.SPD_DOWNLOAD}</b>: "
                 f"<code>{down_in_mbits}</code> "
                 f"{msgRep.SPD_MEGABITS} (<code>{down_in_mb}</code> "
                 f"{msgRep.SPD_MEGABYTES})\n")
        text += (f"<b>{msgRep.SPD_UPLOAD}</b>: "
                 f"<code>{up_in_mbits}</code> {msgRep.SPD_MEGABITS} "
                 f"(<code>{up_in_mb}</code> {msgRep.SPD_MEGABYTES})\n")
        text += f"<b>{msgRep.SPD_PING}</b>: <code>{ping}</code> ms\n"
        text += f"<b>{msgRep.SPD_ISP}</b>: {isp}\n"
        text += f"<b>{msgRep.SPD_HOSTED_BY}</b>: {host} ({host_cc})\n"
        await event.edit(text, parse_mode="html")
    return


for cmd in ("dc", "ping", "rtt", "speedtest"):
    register_cmd_usage(cmd,
                       usageRep.WEBTOOLS_USAGE.get(cmd, {}).get("args"),
                       usageRep.WEBTOOLS_USAGE.get(cmd, {}).get("usage"))

register_module_desc(descRep.WEBTOOLS_DESC)
register_module_info(
    name="Web Tools",
    authors="nunopenim, prototype74",
    version=VERSION
)
