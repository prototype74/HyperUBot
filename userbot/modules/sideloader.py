# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient

# Telethon stuff
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^\.sideload$", outgoing=True))
async def sideload(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        file = msg.file
        if not file.name.endswith(".py"):
            await event.edit("IDIOT, this is not a .py file")
            return
        await event.edit("Yup, this is a .py file")
        return
    else:
        await event.edit("Bruh, reply to a fucking file, dumbass")
        return
