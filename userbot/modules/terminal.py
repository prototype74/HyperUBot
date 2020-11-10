# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO, VERSION
from userbot.include.aux_funcs import module_info, terminal
from userbot.include.language_processor import TerminalText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from telethon.events import NewMessage
from os.path import basename

@tgclient.on(NewMessage(pattern=r"^\.shell(?: |$)(.*)", outgoing=True))
async def bash(command):
    commandArray = command.text.split(" ")
    del(commandArray[0])
    cmd_output = terminal(commandArray)
    if cmd_output == None:
        cmd_output = msgRep.BASH_ERROR
    output = "$ " + commandArray[0] + "\n\n" + cmd_output
    await command.edit("`" + output + "`")
    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.TERMINAL_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.TERMINAL_USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Terminal", version=VERSION)})
