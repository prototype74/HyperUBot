# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.language_processor import (TerminalText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.sysutils.sys_funcs import isWindows
from userbot.version import VERSION
from logging import getLogger
from os import path, remove
from subprocess import Popen, PIPE
from telethon.errors import ChatSendMediaForbiddenError, MessageTooLongError

if isWindows():
    import shlex

log = getLogger(__name__)
ehandler = EventHandler(log)
USE_BIN_BASH = getConfig("TERMINAL_USE_BIN_BASH")  # POSIX only


async def outputAsFile(event, output_text) -> bool:
    temp_file = path.join(getConfig("USERDATA"), "shell_output.txt")
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
        log.warning(f"[Shell] Send media is not allowed in chat "
                    f"'{event.chat_id}'")
        await event.edit(f"`{msgRep.BASH_SEND_FILE_MTLO}`")
    except Exception as e:
        log.error(e, exc_info=True)
        await event.edit(f"`{msgRep.BASH_SEND_FILE_FAILED}`")

    remove(temp_file)
    return


@ehandler.on(command="shell", alt="terminal", hasArgs=True, outgoing=True)
async def terminal(event):
    full_cmd_str = event.pattern_match.group(1)
    cmd_output = None
    try:
        if isWindows():
            full_cmd_str = f"powershell {full_cmd_str}"
            cmds = shlex.split(full_cmd_str)
            proc = Popen(cmds, stdout=PIPE, stderr=PIPE)
        else:  # POSIX systems
            executor = None
            if isinstance(USE_BIN_BASH, bool) and USE_BIN_BASH:
                executor = "/bin/bash"
            proc = Popen(full_cmd_str, shell=True, executable=executor,
                         stdout=PIPE, stderr=PIPE)
        cmd_output, cmd_error = proc.communicate()
        if proc.returncode or cmd_error:
            cmd_output = cmd_error
        cmd_output = ("".join([chr(char) for char in cmd_output])
                      if cmd_output is not None else msgRep.BASH_ERROR)
    except Exception as e:
        log.error(e, exc_info=True)
        cmd_output = msgRep.BASH_ERROR
    try:
        await event.edit(f"`$ {full_cmd_str}\n\n{cmd_output}`")
    except MessageTooLongError:
        log.info("Shell output is too large. "
                 "Trying to upload output as a file...")
        await outputAsFile(event, cmd_output)
    return


register_cmd_usage("shell",
                   usageRep.TERMINAL_USAGE.get("shell", {}).get("args"),
                   usageRep.TERMINAL_USAGE.get("shell", {}).get("usage"))

register_module_desc(descRep.TERMINAL_DESC)
register_module_info(
    name="Terminal",
    authors="nunopenim, prototype74",
    version=VERSION
)
