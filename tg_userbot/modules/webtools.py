# My imports
from tg_userbot.include.aux_funcs import pinger
from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import WebToolsText as msgRep

# Telethon stuff
from telethon import functions

# Misc imports
import speedtest

DEFAULT_ADD = "1.0.0.1"

@watcher(outgoing=True, pattern=r"^\.rtt$")
async def rtt(message):
    rtt = pinger(DEFAULT_ADD)
    await message.edit(msgRep.PING_SPEED + rtt)
    return

@watcher(outgoing=True, pattern=r"^\.dc$")
async def datacenter(event):
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(msgRep.DCMESSAGE.format(result.country, result.this_dc, result.nearest_dc))
    return

@watcher(outgoing=True, pattern=r"^\.ping(?: |$)?")
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
