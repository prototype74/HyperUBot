# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot._core.access_controller import _protectedAccess
from userbot.include.aux_funcs import event_log
from userbot.include.language_processor import (SideloaderText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from logging import getLogger
import json
import os
import sys

if getConfig("SIDELOAD_NO_REBOOT"):
    from userbot._core.module_loader import import_module

log = getLogger(__name__)
ehandler = EventHandler(log)


def _update_module_source(filename: str):
    if not filename:
        return
    pkg_lists = os.path.join(".", "userbot", "userdata", "package_lists.json")
    if not os.path.exists(pkg_lists):
        return
    pkg_data = {}
    try:
        with open(pkg_lists, "r") as pkg_json:
            pkg_data = json.load(pkg_json)
        pkg_json.close()
    except Exception:
        log.error("Failed to read JSON", exc_info=True)
        return

    module_sources = pkg_data.get("module_sources", [])
    new_data = {"name": filename,
                "author": "Unknown",
                "repo": "Unknown",
                "version": "Unknown",
                "size": 0}
    for i, module in enumerate(module_sources):
        mod_name = module.get("name", "")
        if filename == mod_name:
            module_sources[i] = new_data
            break
    else:
        module_sources.append(new_data)

    pkg_data["module_sources"] = module_sources

    try:
        with open(pkg_lists, "w") as pkg_json:
            json.dump(pkg_data, pkg_json, indent=4)
        pkg_json.close()
        log.info("Module sources list updated")
    except Exception:
        log.error("Failed to write JSON", exc_info=True)
    return


def _validate_code(name) -> bool:
    try:
        if os.path.exists(name) and os.path.isfile(name):
            with open(name, "rb") as script_file:
                compile(script_file.read(),
                        filename=os.path.basename(name),
                        mode="exec")
            script_file.close()
        return True
    except Exception as e:
        log.error(f"Validation for '{os.path.basename(name)}' failed",
                  exc_info=True)
    return False


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
        dest_path = os.path.join(".", "userbot", "modules_user", file.name)
        file_name = file.name[:-3]
        await event.edit(msgRep.DLOADING)
        if os.path.isfile(dest_path) and OVR_WRT_CAUT:
            log.info(f"Module '{file_name}' installed already")
            await event.edit(msgRep.MODULE_EXISTS.format(file.name))
            return
        await event.client.download_media(message=msg, file=dest_path)
        if not _validate_code(dest_path):
            await event.edit(msgRep.NOT_PY_FILE)
            try:
                os.remove(dest_path)
            except OSError:
                pass
            return
        _update_module_source(file_name)
        log.info(f"Module '{file_name}' has been installed to userpace")
        if getConfig("LOGGING"):
            await event_log(event, "SIDELOAD",
                            custom_text=msgRep.LOG.format(file.name))
        if getConfig("SIDELOAD_NO_REBOOT"):
            await event.edit(msgRep.SUCCESS.format(file.name))
            import_module(file_name, True)
        else:
            await event.edit(msgRep.REBOOT_INFO)
    else:
        await event.edit(msgRep.INVALID_FILE)
    return


if getConfig("ALLOW_SIDELOAD"):
    register_cmd_usage(
        "sideload",
        usageRep.SIDELOADER_USAGE.get("sideload", {}).get("args"),
        usageRep.SIDELOADER_USAGE.get("sideload", {}).get("usage")
    )
else:
    register_cmd_usage("sideload", None, None)

register_module_desc(descRep.SIDELOADER_DESC)
register_module_info(
    name="Sideloader",
    authors="nunopenim, prototype74",
    version=VERSION
)


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=(["_update_module_source", "_validate_code"] +
           (["import_module"] if getConfig("SIDELOAD_NO_REBOOT") else [])),
    warn_msg=("Access to protected attribute from Sideloader denied"
              "(requested by {1}:{2})"),
    mlogger=log
)
