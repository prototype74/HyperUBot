# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient, OS

# Telethon stuff
from telethon.events import NewMessage

# Misc imports
import sys
import os
import time

if " " not in sys.executable:
    EXECUTABLE = sys.executable
else:
    EXECUTABLE = '"' + sys.executable + '"'

if OS and OS.startswith("win"):
    USER_MODULES_DIR = ".\\userbot\\modules_user\\"
else:
    USER_MODULES_DIR = "./userbot/modules_user/"

@tgclient.on(NewMessage(pattern=r"^\.sideload$", outgoing=True))
async def sideload(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        file = msg.file
        if not file.name.endswith(".py"):
            await event.edit("This is not a valid .py file! Cannot sideload this.")
            return
        await event.edit("`Downloading...`")
        await event.client.download_media(message=msg, file=USER_MODULES_DIR + file.name)
        await event.edit("Successfully installed `{}`! Rebooting...".format(file.name))
        time.sleep(1)
        args = [EXECUTABLE, "-m", "userbot"]
        await event.edit("Reboot complete!")
        os.execle(sys.executable, *args, os.environ)
        await event.client.disconnect()
        return
    else:
        await event.edit("Please reply to a valid file!")
        return
