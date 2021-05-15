# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import shell_runner
from userbot.include.language_processor import TerminalText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.version import VERSION
from logging import getLogger
from os import path, remove
from telethon.errors import ChatSendMediaForbiddenError, MessageTooLongError

log = getLogger(__name__)
ehandler = EventHandler(log)


async def outputAsFile(event, output_text) -> bool:
    temp_file = path.join(getConfig("TEMP_DL_DIR"), "shell_output.txt")
    try:
        with open(temp_file, "w") as output_file:
            output_file.write(output_text)
        output_file.close()
    except IOError as io:
        log.warning(io, exc_info=True)
        await event.edit(f"`{msgRep.BASH_CRT_FILE_FAILED_RO}`")
        return
    except Exception as e:
        log.error(e, exc_info=True)
        await event.edit(f"`{msgRep.BASH_CRT_FILE_FAILED}`")
        return

    try:
        await event.client.send_file(event.chat_id, temp_file)
        await event.delete()  # delete message (not output file)
    except ChatSendMediaForbiddenError:
        log.warning(f"[Shell] Send media is not allowed in chat '{event.chat_id}'")
        await event.edit(f"`{msgRep.BASH_SEND_FILE_MTLO}`")
    except Exception as e:
        log.error(e, exc_info=True)
        await event.edit(f"`{msgRep.BASH_SEND_FILE_FAILED}`")

    remove(temp_file)
    return


@ehandler.on(command="shell", hasArgs=True, outgoing=True)
async def bash(command):
    full_cmd_str = command.pattern_match.group(1)
    commandArray = command.text.split(" ")
    del(commandArray[0])
    cmd_output = shell_runner(commandArray)
    if cmd_output is None:
        cmd_output = msgRep.BASH_ERROR
    output = "$ " + full_cmd_str + "\n\n" + cmd_output
    try:
        await command.edit("`" + output + "`")
    except MessageTooLongError:
        log.info("Shell output is too large. Trying to upload output as a file...")
        await outputAsFile(command, output)
    return


register_cmd_usage("shell", usageRep.TERMINAL_USAGE.get("shell", {}).get("args"), usageRep.TERMINAL_USAGE.get("shell", {}).get("usage"))
register_module_desc(descRep.TERMINAL_DESC)
register_module_info(
    name="Terminal",
    authors="nunopenim, prototype74",
    version=VERSION
)
