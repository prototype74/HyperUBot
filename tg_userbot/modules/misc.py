# My stuff
from tg_userbot import tgclient

# Telethon stuff
from telethon.events import NewMessage

# Misc stuff
import random
import time

@tgclient.on(NewMessage(pattern=r"^\.coinflip$", outgoing=True))
async def coinflipper(coin):
    number = random.randint(1, 10000)
    retStr = "COIN_LANDED_VAL"
    temp = ": "
    await coin.edit("THRWING_COIN")
    time.sleep(3) # gives more character if we wait a bit
    if number % 2 == 0:
        retStr += temp + "HEADS"
    else:
        retStr += temp + "TAILS"
    await coin.edit(retStr)
    return
