# My stuff
from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import DeletionsText as msgRep

# Telethon stuff
from telethon.errors import rpcbaseerrors

# Misc imports
from asyncio import sleep

@watcher(outgoing=True, pattern=r"^\.purge$")
async def purger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    count = 0
    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []
    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(purg.chat_id, msgRep.PURGE_COMPLETE.format(str(count)))
    await sleep(3)
    await done.delete()

@watcher(outgoing=True, pattern=r"^\.del$")
async def deleteThis(rep):
    msg_src = await rep.get_reply_message()
    if rep.reply_to_msg_id:
        try:
            await msg_src.delete()
            await rep.delete()
        except rpcbaseerrors.BadRequestError:
            await rep.edit(msgRep.DEL_FAILED)