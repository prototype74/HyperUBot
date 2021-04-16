# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import event_log, fetch_user, format_chat_id, isRemoteCMD
from userbot.include.language_processor import AdminText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.version import VERSION
from telethon.errors import UserAdminInvalidError, ChatAdminRequiredError, AdminsTooMuchError, AdminRankEmojiNotAllowedError, ChatNotModifiedError
from telethon.tl.functions.channels import EditBannedRequest, EditAdminRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights, ChannelParticipantsAdmins, User, Channel, PeerUser, PeerChannel
from asyncio import sleep
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")


@ehandler.on(command="adminlist", hasArgs=True, outgoing=True)
async def adminlist(event):
    arg = event.pattern_match.group(1)
    if arg:
        try:
            arg = int(arg)
        except:
            pass

        try:
            chat = await event.client.get_entity(arg)
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.FAIL_CHAT)
            return
    else:
        chat = await event.get_chat()

    if not isinstance(chat, Channel):
        await event.edit(msgRep.NO_GROUP_CHAN_ARGS)
        return

    try:
        text = msgRep.ADMINS_IN_CHAT.format(chat.title) + ":\n\n"
        num = 1
        async for member in event.client.iter_participants(chat.id, filter=ChannelParticipantsAdmins):
            if member.deleted:
                text += f"{num}. {msgRep.DELETED_ACCOUNT}\n"
            elif member.username:
                text += f"{num}. @{member.username}\n"
            else:
                text += f"{num}. [{member.first_name}](tg://user?id={member.id})\n"
            num += 1
        await event.edit(text)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.UNABLE_GET_ADMINS)
    return


@ehandler.on(command="ban", hasArgs=True, outgoing=True)
async def ban(event):
    user, chat = await fetch_user(event, get_chat=True)

    if not user:
        return

    if not chat:
        await event.edit(msgRep.FAIL_CHAT)
        return

    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_CHAN_ARGS)
        return

    if user.is_self:
        await event.edit(msgRep.CANNOT_BAN_SELF)
        return

    remote = isRemoteCMD(event, chat.id)
    admin_perms = chat.admin_rights if hasattr(chat, "admin_rights") else None

    if admin_perms and not admin_perms.ban_users:
        await event.edit(msgRep.NO_BAN_PRIV)
        return

    try:
        # if view_messages is True then all ban permissions will be set to True too
        ban_perms = ChatBannedRights(until_date=None, view_messages=True)
        await event.client(EditBannedRequest(chat.id, user.id, ban_perms))
        name = f"[{user.first_name}](tg://user?id={user.id})" if user.first_name else msgRep.DELETED_ACCOUNT
        if remote:
            await event.edit(msgRep.BAN_SUCCESS_REMOTE.format(name, chat.title))
        else:
            await event.edit(msgRep.BAN_SUCCESS.format(name))
        if LOGGING:
            await event_log(event, "BAN", user_name=user.first_name, username=user.username, user_id=user.id,
                            chat_title=chat.title, chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=format_chat_id(chat) if remote else event.chat_id)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except UserAdminInvalidError:
        await event.edit(msgRep.CANNOT_BAN_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.BAN_FAILED)

    return


@ehandler.on(command="unban", hasArgs=True, outgoing=True)
async def unban(event):
    user, chat = await fetch_user(event, get_chat=True)

    if not user:
        return

    if not chat:
        await event.edit(msgRep.FAIL_CHAT)
        return

    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_CHAN_ARGS)
        return

    if user.is_self:
        await event.edit(msgRep.CANNOT_UNBAN_SELF)
        return

    remote = isRemoteCMD(event, chat.id)
    admin_perms = chat.admin_rights if hasattr(chat, "admin_rights") else None

    if admin_perms and not admin_perms.ban_users:
        await event.edit(msgRep.NO_BAN_PRIV)
        return

    try:
        unban_perms = ChatBannedRights(until_date=None, view_messages=False)
        await event.client(EditBannedRequest(chat.id, user.id, unban_perms))
        name = f"[{user.first_name}](tg://user?id={user.id})" if user.first_name else msgRep.DELETED_ACCOUNT
        if remote:
            await event.edit(msgRep.UNBAN_SUCCESS_REMOTE.format(name, chat.title))
        else:
            await event.edit(msgRep.UNBAN_SUCCESS.format(name))
        if LOGGING:
            await event_log(event, "UNBAN", user_name=user.first_name, username=user.username, user_id=user.id,
                            chat_title=chat.title, chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=format_chat_id(chat) if remote else event.chat_id)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(fmsgRep.UNBAN_FAILED)

    return


@ehandler.on(command="kick", hasArgs=True, outgoing=True)
async def kick(event):
    user, chat = await fetch_user(event, get_chat=True)

    if not user:
        return

    if not chat:
        await event.edit(msgRep.FAIL_CHAT)
        return

    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_CHAN_ARGS)
        return

    if user.is_self:
        await event.edit(msgRep.CANNOT_KICK_SELF)
        return

    remote = isRemoteCMD(event, chat.id)
    admin_perms = chat.admin_rights if hasattr(chat, "admin_rights") else None

    if admin_perms and not admin_perms.ban_users:
        await event.edit(msgRep.NO_BAN_PRIV)
        return

    try:
        await event.client.kick_participant(chat.id, user.id)
        name = f"[{user.first_name}](tg://user?id={user.id})" if user.first_name else msgRep.DELETED_ACCOUNT
        if remote:
            await event.edit(msgRep.KICK_SUCCESS_REMOTE.format(name, chat.title))
        else:
            await event.edit(msgRep.KICK_SUCCESS.format(name))
        if LOGGING:
            await event_log(event, "KICK", user_name=user.first_name, username=user.username, user_id=user.id,
                            chat_title=chat.title, chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=format_chat_id(chat) if remote else event.chat_id)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.KICK_FAILED)

    return


@ehandler.on(command="promote", hasArgs=True, outgoing=True)
async def promote(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        try:
            if isinstance(msg.from_id, PeerUser):
                user = await event.client.get_entity(msg.from_id.user_id)
            elif isinstance(msg.from_id, PeerChannel):
                await event.edit(msgRep.CANNOT_PROMOTE_CHANNEL)
                return
            else:
                await event.edit(msgRep.PERSON_ANONYMOUS)
                return
        except ValueError as e:
            await event.edit(f"`{msgRep.GET_ENTITY_FAILED}: {e}`")
            return
        arg = event.pattern_match.group(1)
        title = arg if len(arg) <= 16 else ""
    else:
        args_from_event = event.pattern_match.group(1).split(" ", 1)
        if len(args_from_event) == 2:
            sec_arg = args_from_event[1]
            title = sec_arg if len(sec_arg) <= 16 else ""
        else:
            title = ""
        if args_from_event[0]:
            try:
                user = await event.client.get_entity(args_from_event[0])
            except ValueError as e:
                await event.edit(f"`{msgRep.GET_ENTITY_FAILED}: {e}`")
                return
        else:
            user = None

    if not user:
        await event.edit(msgRep.NO_ONE_TO_PROMOTE)
        return

    if not type(user) is User:
        await event.edit(msgRep.NOT_USER)
        return

    if user.is_self:
        await event.edit(msgRep.CANNOT_PROMOTE_SELF)
        return

    chat = await event.get_chat()
    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_CHAN)
        return

    try:
        async for member in event.client.iter_participants(chat.id, filter=ChannelParticipantsAdmins):
            if user.id == member.id:
                if user.is_self:
                    await event.edit(msgRep.ADMIN_ALREADY_SELF)
                else:
                    await event.edit(msgRep.ADMIN_ALREADY)
                return
    except:
        pass

    try:
        if chat.creator:
            admin_perms = ChatAdminRights(add_admins=False, invite_users=True, change_info=True,
                                          ban_users=True, delete_messages=True, pin_messages=True)
        else:
            # get our own admin rights but set add_admin perm to False. If we aren't admin set empty permissions
            admin_perms = chat.admin_rights if chat.admin_rights else ChatAdminRights()
            if admin_perms.add_admins is not None and not admin_perms.add_admins:
                await event.edit(msgRep.ADD_ADMINS_REQUIRED)
                return
            if admin_perms.add_admins:
                admin_perms.add_admins = False
            if all(getattr(admin_perms, perm) is False for perm in vars(admin_perms)):
                await event.edit(msgRep.ADMIN_NOT_ENOUGH_PERMS)
                return
        await event.client(EditAdminRequest(chat.id, user.id, admin_perms, title))
        name = f"[{user.first_name}](tg://user?id={user.id})" if user.first_name else msgRep.DELETED_ACCOUNT
        await event.edit(msgRep.PROMOTE_SUCCESS.format(name))
        if LOGGING:
            await event_log(event, "PROMOTE", user_name=user.first_name, username=user.username, user_id=user.id,
                            chat_title=chat.title, chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=event.chat_id)
    except AdminsTooMuchError:
        await event.edit(msgRep.TOO_MANY_ADMINS)
    except AdminRankEmojiNotAllowedError:
        await event.edit(msgRep.EMOJI_NOT_ALLOWED)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.PROMOTE_FAILED)

    return


@ehandler.on(command="demote", hasArgs=True, outgoing=True)
async def demote(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        try:
            if isinstance(msg.from_id, PeerUser):
                user = await event.client.get_entity(msg.from_id.user_id)
            elif isinstance(msg.from_id, PeerChannel):
                await event.edit(msgRep.CANNOT_DEMOTE_CHANNEL)
                return
            else:
                await event.edit(msgRep.PERSON_ANONYMOUS)
                return
        except ValueError as e:
            await event.edit(f"`{msgRep.GET_ENTITY_FAILED}: {e}`")
            return
    else:
        arg_from_event = event.pattern_match.group(1)
        if arg_from_event:
            try:
                user = await event.client.get_entity(arg_from_event)
            except ValueError as e:
                await event.edit(f"`{msgRep.GET_ENTITY_FAILED}: {e}`")
                return
        else:
            user = None

    if not user:
        await event.edit(msgRep.NO_ONE_TO_DEMOTE)
        return

    if not type(user) is User:
        await event.edit(msgRep.NOT_USER)
        return

    if user.is_self:
        await event.edit(msgRep.CANNOT_DEMOTE_SELF)
        return

    chat = await event.get_chat()
    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_CHAN)
        return

    try:
        admins = []
        async for member in event.client.iter_participants(chat.id, filter=ChannelParticipantsAdmins):
            admins.append(member.id)
        if not user.id in admins:
            await event.edit(msgRep.DEMOTED_ALREADY)
            return
        user_is_admin = True if user.id in admins else False
    except:
        pass

    try:
        rm_admin_perms = ChatAdminRights(add_admins=None, invite_users=None, change_info=None,
                                         ban_users=None, delete_messages=None, pin_messages=None)
        if chat.admin_rights and not chat.admin_rights.add_admins:
            await event.edit(msgRep.ADD_ADMINS_REQUIRED)
            return
        await event.client(EditAdminRequest(chat.id, user.id, rm_admin_perms, ""))
        name = f"[{user.first_name}](tg://user?id={user.id})" if user.first_name else msgRep.DELETED_ACCOUNT
        await event.edit(msgRep.DEMOTE_SUCCESS.format(name))
        if LOGGING:
            await event_log(event, "DEMOTE", user_name=user.first_name, username=user.username, user_id=user.id,
                            chat_title=chat.title, chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=event.chat_id)
    except ChatAdminRequiredError:
        if user_is_admin:
            await event.edit(msgRep.CANNOT_DEMOTE_ADMIN)
        else:
            await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.DEMOTE_FAILED)

    return


@ehandler.on(command="mute", hasArgs=True, outgoing=True)
async def mute(event):
    user, chat = await fetch_user(event, get_chat=True)

    if not user:
        return

    if not chat:
        await event.edit(msgRep.FAIL_CHAT)
        return

    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_ARGS)
        return

    if hasattr(chat, "broadcast") and chat.broadcast:
        await event.edit(msgRep.NOT_MUTE_SUB_CHAN)
        return

    if user.is_self:
        await event.edit(msgRep.CANNOT_MUTE_SELF)
        return

    remote = isRemoteCMD(event, chat.id)
    admin_perms = chat.admin_rights if hasattr(chat, "admin_rights") else None

    if admin_perms and not admin_perms.ban_users:
        await event.edit(msgRep.NO_BAN_PRIV)
        return

    try:
        mute_perms = ChatBannedRights(until_date=None, send_messages=True, change_info=True, invite_users=True, pin_messages=True)
        await event.client(EditBannedRequest(chat.id, user.id, mute_perms))
        name = f"[{user.first_name}](tg://user?id={user.id})" if user.first_name else msgRep.DELETED_ACCOUNT
        if remote:
            await event.edit(msgRep.MUTE_SUCCESS_REMOTE.format(name, chat.title))
        else:
            await event.edit(msgRep.MUTE_SUCCESS.format(name))
        if LOGGING:
            await event_log(event, "MUTE", user_name=user.first_name, username=user.username, user_id=user.id,
                            chat_title=chat.title, chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=format_chat_id(chat) if remote else event.chat_id)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.MUTE_FAILED)

    return


@ehandler.on(command="unmute", hasArgs=True, outgoing=True)
async def unmute(event):
    user, chat = await fetch_user(event, get_chat=True)

    if not user:
        return

    if not chat:
        await event.edit(msgRep.FAIL_CHAT)
        return

    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_ARGS)
        return

    if hasattr(chat, "broadcast") and chat.broadcast:
        await event.edit(msgRep.NOT_UNMUTE_SUB_CHAN)
        return

    if user.is_self:
        await event.edit(msgRep.CANNOT_UNMUTE_SELF)
        return

    remote = isRemoteCMD(event, chat.id)
    admin_perms = chat.admin_rights if hasattr(chat, "admin_rights") else None

    if admin_perms and not admin_perms.ban_users:
        await event.edit(msgRep.NO_BAN_PRIV)
        return

    try:
        unmute_perms = ChatBannedRights(until_date=None, send_messages=None)
        await event.client(EditBannedRequest(chat.id, user.id, unmute_perms))
        name = f"[{user.first_name}](tg://user?id={user.id})" if user.first_name else msgRep.DELETED_ACCOUNT
        if remote:
            await event.edit(msgRep.UNMUTE_SUCCESS_REMOTE.format(name, chat.title))
        else:
            await event.edit(msgRep.UNMUTE_SUCCESS.format(name))
        if LOGGING:
            await event_log(event, "UNMUTE", user_name=user.first_name, username=user.username, user_id=user.id,
                            chat_title=chat.title, chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=format_chat_id(chat) if remote else event.chat_id)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.UNMUTE_FAILED)

    return


@ehandler.on(command="delaccs", outgoing=True)
async def delaccs(event):
    chat = await event.get_chat()
    if type(chat) is User:
        await event.edit(msgRep.NO_GROUP_CHAN)
        return

    deleted_accounts, rem_del_accounts = (0,)*2
    await event.edit(msgRep.TRY_DEL_ACCOUNTS)
    async for member in event.client.iter_participants(chat.id):
        if member.deleted:
            deleted_accounts += 1
            if chat.creator or (chat.admin_rights and chat.admin_rights.ban_users):
                try:
                    await event.client.kick_participant(chat.id, member.id)
                    await sleep(0.2)
                    rem_del_accounts += 1
                except:
                    pass

    if deleted_accounts > 0 and not rem_del_accounts:
        await event.edit(msgRep.DEL_ACCS_COUNT.format(deleted_accounts))
    elif rem_del_accounts > 0 and rem_del_accounts <= deleted_accounts:
        if not (deleted_accounts - rem_del_accounts) == 0:
            rem_accs_text = msgRep.REM_DEL_ACCS_COUNT.format(rem_del_accounts)
            rem_accs_excp_text = msgRep.REM_DEL_ACCS_COUNT_EXCP.format(deleted_accounts - rem_del_accounts)
            await event.edit(f"{rem_accs_text}`. `{rem_accs_excp_text}")
        else:
            await event.edit(msgRep.REM_DEL_ACCS_COUNT.format(rem_del_accounts))
        if LOGGING:
            await event_log(event, "DELACCS", chat_title=chat.title,
                            chat_link=chat.username if hasattr(chat, "username") else None,
                            chat_id=event.chat_id)
    else:
        await event.edit(msgRep.NO_DEL_ACCOUNTS)

    return


for cmd in ("adminlist", "ban", "unban", "kick", "promote", "demote", "mute", "unmute", "delaccs"):
    register_cmd_usage(cmd, usageRep.ADMIN_USAGE.get(cmd, {}).get("args"), usageRep.ADMIN_USAGE.get(cmd, {}).get("usage"))

register_module_desc(descRep.ADMIN_DESC)
register_module_info(
    name="Admininstration",
    authors="nunopenim, prototype74",
    version=VERSION
)
