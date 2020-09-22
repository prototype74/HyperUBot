# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, OS, LOGGING, MODULE_DESC, MODULE_DICT
from userbot.include.aux_funcs import event_log
from userbot.include.language_processor import SideloaderText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from telethon.events import NewMessage
import sys
import os
from logging import getLogger
from os.path import basename
import time

log = getLogger(__name__)

if " " not in sys.executable:
    EXECUTABLE = sys.executable
else:
    EXECUTABLE = '"' + sys.executable + '"'

if OS and OS.startswith("win"):
    USER_MODULES_DIR = ".\\userbot\\modules_user\\"
else:
    USER_MODULES_DIR = "./userbot/modules_user/"

@tgclient.on(NewMessage(pattern=r"^\.sideload(?: |$)(.*)", outgoing=True))
async def sideload(event):
    OVR_WRT_CAUT = True
    cmd_args = event.pattern_match.group(1).split(" ", 1)
    if cmd_args[0] == "force":
        OVR_WRT_CAUT = False
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        file = msg.file
        if not file.name.endswith(".py"):
            await event.edit(msgRep.NOT_PY_FILE)
            return
        dest_path = USER_MODULES_DIR + file.name
        await event.edit(msgRep.DLOADING)
        if os.path.isfile(dest_path) and OVR_WRT_CAUT:
            log.info(f"Module '{file.name[:-3]}' installed already")
            await event.edit(msgRep.MODULE_EXISTS.format(file.name))
            return
        await event.client.download_media(message=msg, file=dest_path)
        log.info(f"Module '{file.name[:-3]}' has been installed to userpace")
        await event.edit(msgRep.SUCCESS.format(file.name))
        if LOGGING:
            await event_log(event, "SIDELOAD", custom_text=msgRep.LOG.format(file.name))
        log.info("Rebooting userbot...")
        time.sleep(1)
        args = [EXECUTABLE, "-m", "userbot"]
        await event.edit(msgRep.RBT_CPLT)
        os.execle(sys.executable, *args, os.environ)
        await event.client.disconnect()
        return
    else:
        await event.edit(msgRep.INVALID_FILE)
        return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.SIDELOADER_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.SIDELOADER_USAGE})
