# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import event_log
from userbot.include.language_processor import (SideloaderText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig, setConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.sysutils.sys_funcs import isWindows
from userbot.version import VERSION
import os
from logging import getLogger
import time

log = getLogger(__name__)
ehandler = EventHandler(log)
USER_MODULES_DIR = os.path.join(".", "userbot", "modules_user")


@ehandler.on(command="sideload", alt="install", hasArgs=True, outgoing=True)
async def sideload(event):
    if not getConfig("ALLOW_SIDELOAD"):
        return
    OVR_WRT_CAUT = True
    cmd_args = event.pattern_match.group(1).split(" ", 1)
    if cmd_args[0].lower() == "force":
        OVR_WRT_CAUT = False
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        file = msg.file
        if not file.name.endswith(".py"):
            await event.edit(msgRep.NOT_PY_FILE)
            return
        dest_path = os.path.join(USER_MODULES_DIR, file.name)
        await event.edit(msgRep.DLOADING)
        if os.path.isfile(dest_path) and OVR_WRT_CAUT:
            log.info(f"Module '{file.name[:-3]}' installed already")
            await event.edit(msgRep.MODULE_EXISTS.format(file.name))
            return
        await event.client.download_media(message=msg, file=dest_path)
        log.info(f"Module '{file.name[:-3]}' has been installed to userpace")
        await event.edit(msgRep.SUCCESS.format(file.name))
        if getConfig("LOGGING"):
            await event_log(event, "SIDELOAD",
                            custom_text=msgRep.LOG.format(file.name))
        if isWindows():
            log.info("Manual reboot required to load sideloaded module")
            await event.edit(msgRep.REBOOT_WIN)
        else:
            # TODO: proper implementation
            log.info("Rebooting userbot...")
            time.sleep(1)
            await event.edit(msgRep.RBT_CPLT)
            setConfig("REBOOT", True)
            await event.client.disconnect()
    else:
        await event.edit(msgRep.INVALID_FILE)
    return


if getConfig("ALLOW_SIDELOAD"):
    register_cmd_usage("sideload",
                       usageRep.SIDELOADER_USAGE.get(
                           "sideload", {}).get("args"),
                       usageRep.SIDELOADER_USAGE.get(
                           "sideload", {}).get("usage"))
else:
    register_cmd_usage("sideload", None, None)

register_module_desc(descRep.SIDELOADER_DESC)
register_module_info(
    name="Sideloader",
    authors="nunopenim, prototype74",
    version=VERSION
)
