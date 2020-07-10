# My stuff
from tg_userbot.watcher import watcher

# Telethon Stuff
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.errors.rpcerrorlist import UserIdInvalidError

# Various vars for ease of customization
BANNED_RIGHTS = ChatBannedRights(until_date=None, view_messages=True, send_messages=True, send_media=True, send_stickers=True, send_gifs=True, send_games=True, send_inline=True, embed_links=True)
UNBANNED_RIGHTS = ChatBannedRights(until_date=None, send_messages=None, send_media=None, send_stickers=None, send_gifs=None, send_games=None, send_inline=None, embed_links=None)

@watcher(outgoing=True, pattern=r"^\.ban(?: |$)(.*)")
async def ban(banning):
    chat = banning.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await banning.edit("`Not admin!`")
        return
    user = await get_user_from_event(banning)
    if not user:
        return
    await banning.edit("`Banning user...`")
    try:
        await banning.client(EditBannedRequest(banning.chat_id, user.id, BANNED_RIGHTS))
    except:
        await banning.edit("`No Perms!`")
        return
    try:
        reply = await banning.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await banning.edit("`No message del Perms!`")
        return
    await bon.edit("`{}` was banned!".format(str(user.id)))
    return

@watcher(outgoing=True, pattern=r"^\.unban(?: |$)(.*)")
async def unban(unbanner):
    chat = await unbanner.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await unbanner.edit("`Not admin!`")
        return
    user = await get_user_from_event(unbanner)
    if not user:
        return
    await unbanner.edit("`Unbanning user...`")
    try:
        await unbanner.client(EditBannedRequest(unbon.chat_id, user.id, UNBANNED_RIGHTS))
        await unbanner.edit("`Unbanned Successfully`")
    except UserIdInvalidError:
        await unbanner.edit("`UserID Invalid`")
    return
