# My stuff
from tg_userbot import tgclient, HELP_DICT
from tg_userbot.include.language_processor import TerminalText as msgRep, HelpDesignations as helpRep

# Telethon stuff
from telethon.events import NewMessage

# Misc imports
from subprocess import check_output, CalledProcessError

@tgclient.on(NewMessage(pattern=r"^\.shell(?: |$)(.*)", outgoing=True))
async def bash(command):
    commandArray = command.text.split(" ")
    bashCmd = ""
    for word in commandArray: #building the command
        if not word == ".bash":
            bashCmd += word + " "
    try:
        cmd_output = check_output(bashCmd, shell=True).decode()
    except CalledProcessError:
        cmd_output = msgRep.BASH_ERROR
    output = "$ " + bashCmd + "\n\n" + cmd_output
    await command.edit("`" + output + "`")
    return

HELP_DICT.update({"terminal":helpRep.TERMINAL_HELP})