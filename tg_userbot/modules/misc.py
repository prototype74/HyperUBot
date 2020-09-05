# My stuff
from tg_userbot import tgclient
from tg_userbot.include.language_processor import MiscText as msgRep

# Telethon stuff
from telethon.events import NewMessage

# Misc stuff
import random
import time
import emoji

@tgclient.on(NewMessage(pattern=r"^\.coinflip$", outgoing=True))
async def coinflipper(coin):
    retStr = msgRep.COIN_LANDED_VAL
    await coin.edit(msgRep.THRWING_COIN)
    time.sleep(3) # gives more character if we wait a bit
    number = random.randint(1, 10000)
    if (number % 2 == 0):
        retStr += msgRep.HEADS
    else:
        retStr += msgRep.TAILS
    await coin.edit(retStr)
    return

@tgclient.on(NewMessage(pattern=r"^\.dice$", outgoing=True))
async def dice(rolling):
    await rolling.edit("🎲")
    return
