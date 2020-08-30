# My stuff
from tg_userbot import tgclient, HELP_DICT
from tg_userbot.include.language_processor import TerminalText as msgRep, HelpDesignations as helpRep

# Telethon stuff
from telethon.events import NewMessage

# Misc imports
from subprocess import check_output, CalledProcessError
from sys import executable

@tgclient.on(NewMessage(pattern=r"^\.shell(?: |$)(.*)", outgoing=True))
async def bash(command):
    commandArray = command.text.split(" ")
    bashCmd = ""
    for word in commandArray: # building the command
        if not word == ".shell": # Probably I should find a way not to have this hardcoded
            bashCmd += word + " "
    try:
        cmd_output = check_output(bashCmd, shell=True).decode()
    except CalledProcessError:
        cmd_output = msgRep.BASH_ERROR
    output = "$ " + bashCmd + "\n\n" + cmd_output
    await command.edit("`" + output + "`")
    return

@tgclient.on(NewMessage(pattern=r"^\.python(?: |$)(.*)", outgoing=True))
async def python(command):
    commandArray = command.text.split(" ")
    python_instruction = ""
    for word in commandArray:
        if not word == ".python":  # Probably I should find a way not to have this hardcoded
            python_instruction += word + " "
    command_for_bash = executable + " -c " + '"' + python_instruction + '"'
    try:
        cmd_output = check_output(command_for_bash, shell=True).decode()
    except CalledProcessError:
        cmd_output = msgRep.BASH_ERROR
    output = msgRep.PYTHON_INSTRUCTION + " `" + python_instruction + "`\n\n"
    output +=  msgRep.PYTHON_RESULT + "`" + cmd_output + "`"
    await command.edit(output)
    return

HELP_DICT.update({"terminal":helpRep.TERMINAL_HELP})