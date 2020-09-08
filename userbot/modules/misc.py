# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient, MODULE_DESC, MODULE_DICT
from userbot.include.language_processor import MiscText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep

# Telethon stuff
from telethon.events import NewMessage
from telethon.tl.types import InputMediaDice

# Misc stuff
from os.path import basename
import random
import time

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
    await rolling.client.send_message(rolling.to_id, file=InputMediaDice("🎲"))
    await rolling.delete()
    return

@tgclient.on(NewMessage(pattern=r"^\.rand(?: |$)(.*)", outgoing=True))
async def randomizer(msg):
    limit1 = 0
    limit2 = 0
    arguments = msg.text.split(" ")
    if len(arguments) != 3:
        await msg.edit(msgRep.RAND_INVLD_ARGS)
        return
    try:
        limit1 = int(arguments[1])
    except ValueError:
        await msg.edit(msgRep.FRST_LIMIT_INVALID)
        return
    try:
        limit2 = int(arguments[2])
    except ValueError:
        await msg.edit(msgRep.SCND_LIMIT_INVALID)
        return
    if limit1 > limit2:
        temp = limit1
        limit1 = limit2
        limit2 = temp
    rand_num = random.randint(limit1, limit2)
    await msg.edit(msgRep.RAND_NUM_GEN.format(limit1, limit2, rand_num))
    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.MISC_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.MISC_USAGE})
