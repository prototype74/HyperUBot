# My stuff
from tg_userbot.include.language_processor import AdminText as msgRep, HelpDesignations as helpRep
from tg_userbot.include.watcher import watcher
from tg_userbot.include.aux_funcs import get_user_from_event
from tg_userbot import BOTLOG, BOTLOG_CHATID, HELP_DICT

# Telethon Stuff
from telethon.errors import BadRequestError, UserAdminInvalidError, ChatAdminRequiredError, AdminsTooMuchError
from telethon.tl.functions.channels import EditBannedRequest, EditAdminRequest
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.types import ChatAdminRights, ChatBannedRights, User, ChannelParticipantsAdmins
from telethon.tl.functions.messages import UpdatePinnedMessageRequest

# Misc
from asyncio import sleep

# Various vars for ease of customization
BANNED_RIGHTS = ChatBannedRights(until_date=None, view_messages=True, send_messages=True, send_media=True, send_stickers=True, send_gifs=True, send_games=True, send_inline=True, embed_links=True)
UNBANNED_RIGHTS = ChatBannedRights(until_date=None, send_messages=None, send_media=None, send_stickers=None, send_gifs=None, send_games=None, send_inline=None, embed_links=None)
KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
ADMIN_RIGHTS = ChatAdminRights(add_admins=False, invite_users=True, change_info=False, ban_users=True, delete_messages=True, pin_messages=True)
DEMOTE_RIGHTS = ChatAdminRights(add_admins=None, invite_users=None, change_info=None, ban_users=None, delete_messages=None, pin_messages=None)
USER_URL = "tg://user?id="

# Maybe add: admin list, user list

@watcher(outgoing=True, pattern=r"^\.ban(?: |$)(.*)")
async def ban(banning):
    chat = await banning.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await banning.edit(msgRep.NOT_ADMIN)
        return
    user = await get_user_from_event(banning)
    if not user:
        return
    await banning.edit(msgRep.BANNING_USER)
    try:
        await banning.client(EditBannedRequest(banning.chat_id, user.id, BANNED_RIGHTS))
    except:
        await banning.edit(msgRep.NO_PERMS)
        return
    try:
        reply = await banning.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await banning.edit(msgRep.NO_MSG_DEL_PERMS)
        return
    await banning.edit(msgRep.BANNED_SUCCESSFULLY.format(str(user.id)))
    if BOTLOG:
        await banning.client.send_message(BOTLOG_CHATID, msgRep.BANLOG.format(user.first_name, USER_URL + str(user.id), banning.chat.title, banning.chat.id))
    return

@watcher(outgoing=True, pattern=r"^\.unban(?: |$)(.*)")
async def unban(unbanner):
    chat = await unbanner.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await unbanner.edit(msgRep.NO_PERMS)
        return
    user = await get_user_from_event(unbanner)
    if not user:
        return
    await unbanner.edit(msgRep.UNBANNING_USER)
    try:
        await unbanner.client(EditBannedRequest(unbanner.chat_id, user.id, UNBANNED_RIGHTS))
        await unbanner.edit(msgRep.UNBANNED_SUCCESSFULLY)
        if BOTLOG:
            await unbanner.client.send_message(BOTLOG_CHATID, msgRep.UNBANLOG.format(user.first_name, USER_URL + str(user.id), unbanner.chat.title, unbanner.chat.id))
    except UserIdInvalidError:
        await unbanner.edit(msgRep.USERID_INVALID)
    return

@watcher(outgoing=True, pattern=r"^\.kick(?: |$)(.*)")
async def kick(kicker):
    chat = await kicker.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await kicker.edit(msgRep.NOT_ADMIN)
        return
    user = await get_user_from_event(kicker)
    if not user:
        await kicker.edit(msgRep.FAILED_FETCH_USER)
        return
    await kicker.edit(msgRep.KICKING_USER)
    try:
        await kicker.client(EditBannedRequest(kicker.chat_id, user.id, KICK_RIGHTS))
        await sleep(1) # sync
    except BadRequestError:
        await kicker.edit(msgRep.NO_PERMS)
        return
    await kicker.client(EditBannedRequest(kicker.chat_id, user.id, ChatBannedRights(until_date=None)))
    await kicker.edit(msgRep.KICKED_SUCCESSFULLY.format(str(user.id)))
    if BOTLOG:
        await kicker.client.send_message(BOTLOG_CHATID, msgRep.KICKLOG.format(user.first_name, USER_URL + str(user.id), kicker.chat.title, kicker.chat.id))
    return

@watcher(outgoing=True, pattern=r"^\.promote(?: |$)(.*)")
async def promote(promt):
    chat = await promt.get_chat()
    if isinstance(chat, User):
        await promt.edit(msgRep.ONLY_CHAN_GROUPS)
        return
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await promt.edit(msgRep.NOT_ADMIN)
        return
    get_user = await get_user_from_event(promt)
    if isinstance(get_user, tuple):
        user, rank = get_user
    else:
        user = get_user
        rank = ""
    if not rank:
        rank = ""
    if user:
        pass
    else:
        return
    if not isinstance(user, User):
        await promt.edit(msgRep.NOT_USER)
        return
    try:
        async for member in promt.client.iter_participants(promt.chat_id, filter=ChannelParticipantsAdmins):
            if user.id == member.id:
                if user.is_self:
                    await promt.edit(msgRep.PROMT_SELF)
                else:
                    await promt.edit(msgRep.ADM_ALRD)
                return
    except ChatAdminRequiredError:
        await promt.edit(msgRep.NOT_ADMIN)
        return
    await promt.edit(msgRep.PROMTING_USER)
    try:
        if creator:
            await promt.client(EditAdminRequest(promt.chat_id, user.id, ADMIN_RIGHTS, rank))
        else:
            admin.add_admins = False
            if all(getattr(admin, right) is False for right in vars(admin)):
                return await promt.edit(msgRep.NO_ADD_ADM_RIGHT)
            await promt.client(EditAdminRequest(promt.chat_id, user.id, admin, rank))
        await promt.edit(msgRep.PRMT_SUCCESS)
    except AdminsTooMuchError:
        await promt.edit(msgRep.TOO_MANY_ADM)
        return
    except BadRequestError:
        await promt.edit(msgRep.NO_PERMS)
        return
    if BOTLOG:
        await promt.client.send_message(BOTLOG_CHATID, msgRep.PROMT_LOG.format(user.first_name, USER_URL + str(user.id), promt.chat.title, promt.chat.id))
    return

@watcher(outgoing=True, pattern=r"^\.demote(?: |$)(.*)")
async def demote(dmt):
    chat = await dmt.get_chat()
    if isinstance(chat, User):
        await dmt.edit(msgRep.ONLY_CHAN_GROUPS)
        return
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await dmt.edit(msgRep.NOT_ADMIN)
        return
    get_user = await get_user_from_event(dmt)
    if isinstance(get_user, tuple):
        user, rank = get_user
    else:
        user = get_user
        rank = ""
    if not rank:
        rank = ""
    if user:
        pass
    else:
        return
    if not isinstance(user, User):
        await dmt.edit(msgRep.NOT_USER)
        return
    try:
        admins_list = []
        async for member in dmt.client.iter_participants(dmt.chat_id, filter=ChannelParticipantsAdmins):
            admins_list.append(member.id)
        if user.id not in admins_list:
            await dmt.edit(msgRep.ALREADY_NOT_ADM)
            return
    except ChatAdminRequiredError:
        await dmt.edit(msgRep.NOT_ADMIN)
        return
    if user.is_self:
        await dmt.edit(msgRep.DMT_MYSELF)
        return
    await dmt.edit(msgRep.DMTING_USER)
    try:
        await dmt.client(EditAdminRequest(dmt.chat_id, user.id, DEMOTE_RIGHTS, rank))
        await dmt.edit(msgRep.DMTED_SUCCESSFULLY)
    except BadRequestError:
        await dmt.edit(msgRep.NO_PERMS)
        return
    if BOTLOG:
        await dmt.client.send_message(BOTLOG_CHATID, msgRep.DMT_LOG.format(user.first_name, USER_URL + str(user.id), dmt.chat.title, dmt.chat.id))
    return

@watcher(outgoing=True, pattern=r"^\.delusers(?: |$)(.*)")
async def delusers(deleter):
    con = deleter.pattern_match.group(1) # gets argument, if any
    del_u = 0
    del_status = msgRep.NO_DEl_USERS
    if not deleter.is_group:
        await deleter.edit(msgRep.ONLY_CHAN_GROUPS)
        return
    if con != "clean":
        await deleter.edit(msgRep.SEARCHING_DEL_USERS)
        async for user in deleter.client.iter_participants(deleter.chat_id):
            if user.deleted:
                del_u += 1
        if del_u > 0:
            del_status = msgRep.FOUND_DEL_ACCS.format(str(del_u))
        await deleter.edit(del_status)
        return
    chat = await deleter.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await deleter.edit(msgRep.NOT_ADMIN)
        return
    await deleter.edit(msgRep.DELETING_ACCS)
    del_u = 0
    del_a = 0
    async for user in deleter.client.iter_participants(deleter.chat_id):
        if user.deleted:
            try:
                await deleter.client(EditBannedRequest(deleter.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await deleter.edit(msgRep.NO_BAN_PERMS)
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await deleter.client(EditBannedRequest(deleter.chat_id, user.id, UNBANNED_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = msgRep.DEL_ALL_SUCCESFULLY.format(str(del_u))
    if del_a > 0:
        del_status = msgRep.DEL_SOME_SUCCESSFULLY.format(str(del_u), str(del_a))
    await deleter.edit(del_status)
    if BOTLOG:
        await deleter.client.send_message(BOTLOG_CHATID, msgRep.CLEAN_DELACC_LOG.format(str(del_u)))
    return

@watcher(outgoing=True, pattern=r"^\.mute(?: |$)(.*)")
async def mute(muter):
    chat = await muter.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await muter.edit(msgRep.NOT_ADMIN)
        return
    user = await get_user_from_event(muter)
    if not user:
        return
    await muter.edit(msgRep.MUTING_USR)
    try:
        await muter.client(EditBannedRequest(muter.chat_id, user.id, MUTE_RIGHTS))
    except BadRequestError:
        await muter.edit(msgRep.NO_PERMS)
        return
    await muter.edit(msgRep.USER_MUTED)
    if BOTLOG:
        await muter.client.send_message(BOTLOG_CHATID, msgRep.MUTE_LOG.format(user.first_name, USER_URL + str(user.id), muter.chat.title, muter.chat_id))
    return

@watcher(outgoing=True, pattern=r"^\.unmute(?: |$)(.*)")
async def unmute(unmuter):
    chat = await unmuter.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await unmuter.edit(msgRep.NOT_ADMIN)
        return
    user = await get_user_from_event(unmuter)
    if not user:
        return
    await unmuter.edit(msgRep.UNMUTING_USR)
    try:
        await unmuter.client(EditBannedRequest(unmuter.chat_id, user.id, UNMUTE_RIGHTS))
    except BadRequestError:
        await unmuter.edit(msgRep.NO_PERMS)
        return
    await unmuter.edit(msgRep.USER_UNMUTED)
    if BOTLOG:
        await unmuter.client.send_message(BOTLOG_CHATID, msgRep.UNMUTE_LOG.format(user.first_name, USER_URL + str(user.id), unmuter.chat.title, unmuter.chat_id))
    return

@watcher(outgoing=True, pattern=r"^\.pin(?: |$)(.*)")
async def pin(msg):
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await msg.edit(msgRep.NOT_ADMIN)
        return
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        await msg.edit(msgRep.MSG_NOT_FOUND_PIN)
        return
    options = msg.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await msg.client(UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await msg.edit(msgRep.NO_PERMS)
        return
    await msg.edit(msgRep.PINNED_SUCCESSFULLY)
    return

HELP_DICT.update({"admin":helpRep.ADMIN_HELP})