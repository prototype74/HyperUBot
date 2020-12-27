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
from userbot.sysutils.event_handler import EventHandler
from os.path import basename
from subprocess import check_output, CalledProcessError

ehandler = EventHandler()

@ehandler.on(pattern=r"^\.shell(?: |$)(.*)", outgoing=True)
async def bash(command):
    full_cmd_str = command.pattern_match.group(1)
    commandArray = command.text.split(" ")
    del(commandArray[0])
    cmd_output = shell_runner(commandArray)
    if cmd_output is None:
        cmd_output = msgRep.BASH_ERROR
    output = "$ " + full_cmd_str + "\n\n" + cmd_output
    await command.edit("`" + output + "`")
    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.TERMINAL_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.TERMINAL_USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Terminal", version=VERSION)})
