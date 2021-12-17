# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.language_processor import (MiscText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon.tl.types import InputMediaDice
import random
import time

ehandler = EventHandler()


@ehandler.on(command="coinflip", outgoing=True)
async def coinflipper(coin):
    retStr = msgRep.COIN_LANDED_VAL
    await coin.edit(msgRep.THRWING_COIN)
    time.sleep(3)  # gives more character if we wait a bit
    number = random.randint(1, 10000)
    if (number % 2 == 0):
        retStr += msgRep.HEADS
    else:
        retStr += msgRep.TAILS
    await coin.edit(retStr)
    return


@ehandler.on(command="dice", outgoing=True)
async def dice(rolling):
    await rolling.client.send_message(rolling.to_id, file=InputMediaDice("🎲"))
    await rolling.delete()
    return


@ehandler.on(command="rand", hasArgs=True, outgoing=True)
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


for cmd in ("coinflip", "dice", "rand"):
    register_cmd_usage(
        cmd,
        usageRep.MISC_USAGE.get(cmd, {}).get("args"),
        usageRep.MISC_USAGE.get(cmd, {}).get("usage")
    )

register_module_desc(descRep.MISC_DESC)
register_module_info(
    name="Miscellaneous",
    authors="nunopenim, prototype74",
    version=VERSION
)
