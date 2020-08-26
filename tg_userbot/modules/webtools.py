# My imports
from tg_userbot.include.aux_funcs import pinger, speed_convert
from tg_userbot.include.language_processor import WebToolsText as msgRep, HelpDesignations as helpRep
from tg_userbot import tgclient, HELP_DICT

# Telethon stuff
from telethon import functions
from telethon.events import NewMessage

# Misc imports
import speedtest

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

@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.speedtest$"))
async def speedtester(message):
    await message.edit(msgRep.SPD_START)
    test = speedtest.Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    await  message.edit(msgRep.SPD_END.format(result['timestamp'], speed_convert(result['download']), speed_convert(result['upload']), result['ping'], result['client']['isp']))
    return

HELP_DICT.update({"webtools":helpRep.WEBTOOLS_HELP})
