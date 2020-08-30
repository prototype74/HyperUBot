# My imports
from tg_userbot import tgclient, HELP_DICT, TEMP_DL_DIR
from tg_userbot.include.aux_funcs import pinger
from tg_userbot.include.language_processor import WebToolsText as msgRep, HelpDesignations as helpRep

# Telethon stuff
from telethon import functions
from telethon.events import NewMessage

# Misc imports
from dateutil.parser import parse
from os import remove
from speedtest import Speedtest
from urllib.request import urlretrieve


DEFAULT_ADD = "1.0.0.1"

@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.rtt$"))
async def rtt(message):
    rtt = pinger(DEFAULT_ADD)
    await message.edit(msgRep.PING_SPEED + rtt)
    return

@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.dc$"))
async def datacenter(event):
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(msgRep.DCMESSAGE.format(result.country, result.this_dc, result.nearest_dc))
    return

@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.ping(?: |$)?"))
async def ping(args):
    commandParser = str(args.message.message).split(' ')
    if len(commandParser) != 2:
        await args.edit(msgRep.BAD_ARGS)
    else:
        dns = commandParser[1]
        try:
            duration = pinger(dns)
        except:
            await args.edit(msgRep.INVALID_HOST)
            return
        await args.edit(msgRep.PINGER_VAL.format(dns, duration))
    return

@tgclient.on(NewMessage(pattern=r"^\.speedtest(?: |$)(.*)", outgoing=True))
async def speedtest(event):
    arg_from_event = event.pattern_match.group(1)
    chat =  await event.get_chat()
    share_as_pic = True if arg_from_event.lower() == "pic"  else False
    if share_as_pic:
        # if speedtest is send to a group and send media is not allowed then skip 'pic' argument
        if hasattr(chat, "default_banned_rights") and not chat.creator and not chat.admin_rights and \
           chat.default_banned_rights.send_media:
            share_as_pic = False  # disable
    await event.edit(msgRep.SPD_START)
    try:
        s = Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        if share_as_pic:
            s.results.share()
        result = s.results.dict()
        if not result:
            await event.edit(f"`{msgRep.SPD_FAILED}: {msgRep.SPD_NO_RESULT}`")
            return
    except MemoryError:
        await event.edit(f"`{msgRep.SPD_FAILED}: {msgRep.SPD_NO_MEMORY}`")
    except Exception as e:
        await event.edit(f"`{msgRep.SPD_FAILED}: {e}`")

    if share_as_pic:
        try:
            png_file = TEMP_DL_DIR + "speedtest.png"
            urlretrieve(result["share"], png_file)
            await event.client.send_file(chat.id, png_file)
            await event.delete()
            remove(png_file)
        except Exception as e:
            await event.edit(f"`{msgRep.SPD_FAIL_SEND_RESULT}: {e}`")
    else:
        # Convert speed to Mbit/s
        down_in_mbits = round(result["download"] / 10**6, 2)
        up_in_mbits = round(result["upload"] / 10**6 , 2)
        # Convert speed to MB/s (real speed?)
        down_in_mb = round(result["download"] / ((10**6) * 8), 2)
        up_in_mb = round(result["upload"] / ((10**6) * 8), 2)
        time = parse(result["timestamp"])
        ping = result["ping"]
        isp = result["client"]["isp"]
        host = result["server"]["sponsor"]
        host_cc = result["server"]["cc"]

        text = "<b>Speedtest by Ookla</b>\n\n"
        text += f"<b>{msgRep.SPD_TIME}</b>: <code>{time.strftime('%B %d, %Y')} - {time.strftime('%H:%M:%S')} {time.tzname()}</code>\n"
        text += f"<b>{msgRep.SPD_DOWNLOAD}</b>: <code>{down_in_mbits}</code> {msgRep.SPD_MEGABITS} (<code>{down_in_mb}</code> {msgRep.SPD_MEGABYTES})\n"
        text += f"<b>{msgRep.SPD_UPLOAD}</b>: <code>{up_in_mbits}</code> {msgRep.SPD_MEGABITS} (<code>{up_in_mb}</code> {msgRep.SPD_MEGABYTES})\n"
        text += f"<b>{msgRep.SPD_PING}</b>: <code>{ping}</code> ms\n"
        text += f"<b>{msgRep.SPD_ISP}</b>: {isp}\n"
        text += f"<b>{msgRep.SPD_HOSTED_BY}</b>: {host} ({host_cc})\n"
        await event.edit(text, parse_mode="html")

    return

HELP_DICT.update({"webtools":helpRep.WEBTOOLS_HELP})
