# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import MODULE_DESC, MODULE_DICT, MODULE_INFO, VERSION
from userbot.include.aux_funcs import module_info, shell_runner
from userbot.include.language_processor import TerminalText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from logging import getLogger
from os import remove
from os.path import basename
from subprocess import check_output, CalledProcessError
from telethon.errors import ChatSendMediaForbiddenError, MessageTooLongError

log = getLogger(__name__)
ehandler = EventHandler(log)


async def outputAsFile(event, output_text) -> bool:
    temp_file = getConfig("TEMP_DL_DIR") + "shell_output.txt"
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


@ehandler.on(pattern=r"^\.shell(?: |$)(.*)", outgoing=True)
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


MODULE_DESC.update({basename(__file__)[:-3]: descRep.TERMINAL_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.TERMINAL_USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Terminal", version=VERSION)})
