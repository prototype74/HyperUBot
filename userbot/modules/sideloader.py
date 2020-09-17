# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient, OS

# Telethon stuff
from telethon.events import NewMessage

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
            await event.edit("IDIOT, this is not a .py file")
            return
        tgclient.download_media(msg, file_name=USER_MODULES_DIR + file.name)
        await event.edit("I think the download was finished?")
        return
    else:
        await event.edit("Bruh, reply to a fucking file, dumbass")
        return
