# My stuff
from tg_userbot import tgclient

# Telethon stuff
from telethon.events import NewMessage

# Misc imports
from subprocess import check_output

@tgclient.on(NewMessage(pattern=r"^\.bash(?: |$)(.*)", outgoing=True))
async def bash(command):
    commandArray = command.text.split(" ")
    bashCmd = ""
    for word in commandArray: #building the command
        if not word == ".bash":
            bashCmd += word + " "
    print(bashCmd)
    return