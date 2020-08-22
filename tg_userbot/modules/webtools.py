# My imports
from tg_userbot.include.aux_funcs import pinger
from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import WebToolsText as msgRep

DEFAULT_ADD = "1.0.0.1"

@watcher(outgoing=True, pattern=r"^\.rtt$")
async def rtt(message):
    rtt = pinger(DEFAULT_ADD)
    await message.edit(msgRep.PING_SPEED + rtt)
    return
