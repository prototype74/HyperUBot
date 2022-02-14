# Copyright 2020-2022 nunopenim @github
# Copyright 2020-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import format_chat_id
from userbot.include.language_processor import (ChatInfoText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon.errors import (ChannelInvalidError, ChannelPrivateError,
                             ChannelPublicGroupNaError, ChatAdminRequiredError)
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import (GetHistoryRequest,
                                            GetFullChatRequest,
                                            GetExportedChatInvitesRequest)
from telethon.tl.types import (ChannelParticipantCreator,
                               ChatParticipantCreator,
                               MessageActionChannelMigrateFrom,
                               ChannelParticipantsAdmins, Chat, Channel,
                               PeerChannel)
from datetime import datetime
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    if event.reply_to_msg_id and not chat:
        replied_msg = await event.get_reply_message()
        if replied_msg.from_id and isinstance(replied_msg.from_id,
                                              PeerChannel):
            chat = replied_msg.from_id.channel_id
        elif (replied_msg.fwd_from and
              replied_msg.fwd_from.from_id and
              isinstance(replied_msg.fwd_from.from_id, PeerChannel)):
            chat = replied_msg.fwd_from.from_id.channel_id
        else:
            await event.edit(msgRep.REPLY_NOT_CHANNEL)
            return None
    else:
        try:
            chat = int(chat)
        except ValueError:
            pass

    if not chat:
        chat = event.chat_id

    try:
        if not isinstance(chat, int):
            # if input is not an ID, skip GetFullChatRequest as it
            # accepts only integers
            raise Exception("'chat' is not an integer")
        chat_info = await event.client(GetFullChatRequest(chat))
        return chat_info
    except Exception:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
            return chat_info
        except ChannelInvalidError:
            await event.edit(msgRep.INVALID_CH_GRP)
        except ChannelPrivateError:
            await event.edit(msgRep.PRV_BAN)
        except ChannelPublicGroupNaError:
            await event.edit(msgRep.NOT_EXISTS)
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.CANNOT_GET_CHATINFO.format(chat))
    return None


async def fetch_info(chat, event):
    chat_obj_info = None
    for c in chat.chats:
        if c.id == chat.full_chat.id:
            chat_obj_info = c
            break
    broadcast = (chat_obj_info.broadcast
                 if hasattr(chat_obj_info, "broadcast") else False)
    chat_type = msgRep.CHANNEL if broadcast else msgRep.GROUP
    chat_title = chat_obj_info.title
    warn_emoji = u"\u26A0"
    try:
        msg_info = await event.client(
            GetHistoryRequest(peer=chat_obj_info.id,
                              offset_id=0,
                              offset_date=datetime(2010, 1, 1),
                              add_offset=-1,
                              limit=1,
                              max_id=0,
                              min_id=0,
                              hash=0))
    except Exception:
        msg_info = None
    first_msg_valid = (True if msg_info and msg_info.messages and
                       msg_info.messages[0].id == 1 else False)
    owner_id, owner_firstname, owner_username = (None,)*3
    admins = 0
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = (msg_info.messages[0].action.title
                    if first_msg_valid and type(msg_info.messages[0].action) is
                    MessageActionChannelMigrateFrom and
                    msg_info.messages[0].action.title != chat_title else None)
    dc_id = (chat.full_chat.chat_photo.dc_id
             if hasattr(chat.full_chat.chat_photo, "dc_id") else
             msgRep.UNKNOWN)
    description = chat.full_chat.about
    members = (chat.full_chat.participants_count
               if hasattr(chat.full_chat, "participants_count") else
               chat_obj_info.participants_count)
    banned_users = (chat.full_chat.kicked_count
                    if hasattr(chat.full_chat, "kicked_count") else None)
    restricted_users = (chat.full_chat.banned_count
                        if hasattr(chat.full_chat, "banned_count") else None)
    members_online = (chat.full_chat.online_count
                      if hasattr(chat.full_chat, "online_count") else 0)
    group_stickers = (chat.full_chat.stickerset.title
                      if hasattr(chat.full_chat, "stickerset") and
                      chat.full_chat.stickerset else None)
    messages_viewable = (msg_info.count if msg_info and
                         hasattr(msg_info, "count") else None)
    messages_sent = (chat.full_chat.read_inbox_max_id
                     if hasattr(chat.full_chat, "read_inbox_max_id") else None)
    messages_sent_alt = (chat.full_chat.read_outbox_max_id
                         if hasattr(chat.full_chat,
                                    "read_outbox_max_id") else None)
    if messages_sent and messages_viewable:
        deleted_messages = ((messages_sent - messages_viewable)
                            if messages_sent >= messages_viewable else 0)
    elif messages_sent_alt and messages_viewable:
        deleted_messages = ((messages_sent_alt - messages_viewable)
                            if messages_sent_alt >= messages_viewable else 0)
    else:
        deleted_messages = 0
    username = ("@" + chat_obj_info.username
                if hasattr(chat_obj_info, "username") and
                chat_obj_info.username else None)
    chat_type_priv_or_public = (msgRep.CHAT_PUBLIC
                                if username else msgRep.CHAT_PRIVATE)
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = len(bots_list) if bots_list else 0
    supergroup = (True if hasattr(chat_obj_info, "megagroup") and
                  chat_obj_info.megagroup else False)
    gigagroup = (True if hasattr(chat_obj_info, "gigagroup") and
                 chat_obj_info.gigagroup else False)
    slowmode = (msgRep.YES_BOLD if hasattr(chat_obj_info,
                                           "slowmode_enabled") and
                chat_obj_info.slowmode_enabled else msgRep.NO)
    slowmode_time = (chat.full_chat.slowmode_seconds
                     if hasattr(chat_obj_info, "slowmode_enabled") and
                     chat_obj_info.slowmode_enabled else None)
    restricted = (msgRep.YES_BOLD if hasattr(chat_obj_info, "restricted") and
                  chat_obj_info.restricted else msgRep.NO)
    verified = (msgRep.YES_BOLD if hasattr(chat_obj_info, "verified") and
                chat_obj_info.verified else msgRep.NO)
    linked_chat_id = (chat.full_chat.linked_chat_id
                      if hasattr(chat.full_chat, "linked_chat_id") else None)
    linked_chat = msgRep.YES_BOLD if linked_chat_id is not None else msgRep.NO
    linked_chat_title = None
    linked_chat_username = None
    if linked_chat_id is not None and chat.chats:
        for c in chat.chats:
            if c.id == linked_chat_id:
                linked_chat_title = c.title
                if c.username is not None:
                    linked_chat_username = "@" + c.username
                break

    try:
        is_channel_obj = True if isinstance(chat_obj_info, Channel) else False
        async for admin in (
            event.client.iter_participants(entity=chat.full_chat.id,
                                           filter=(ChannelParticipantsAdmins()
                                                   if is_channel_obj else
                                                   None))):
            if isinstance(admin.participant, (ChannelParticipantCreator,
                                              ChatParticipantCreator)):
                owner_id = admin.id
                owner_username = ("@" + admin.username
                                  if admin.username else None)
                if not is_channel_obj:
                    break
            if is_channel_obj:
                admins += 1
    except Exception:
        pass

    caption = msgRep.CHATINFO
    caption += msgRep.CHAT_ID.format(format_chat_id(chat_obj_info))
    caption += msgRep.CHAT_TYPE.format(chat_type, chat_type_priv_or_public)
    if not broadcast:
        if gigagroup:
            group_type = msgRep.GROUP_TYPE_GIGAGROUP
        elif supergroup:
            group_type = msgRep.GROUP_TYPE_SUPERGROUP
        else:
            group_type = msgRep.GROUP_TYPE_NORMAL
        caption += f"{msgRep.GROUP_TYPE}: {group_type}\n"
    if chat_title:
        caption += msgRep.CHAT_NAME.format(chat_title)
    if former_title:  # Meant is the very first title
        caption += msgRep.FORMER_NAME.format(former_title)
    if username:
        caption += f"Link: {username}\n"
    if owner_username:
        caption += msgRep.OWNER.format(owner_username)
    elif owner_id and owner_firstname:
        caption += msgRep.OWNER_WITH_URL.format(owner_id, owner_firstname)
    if created:
        caption += msgRep.CREATED_NOT_NULL.format(
            created.date().strftime('%b %d, %Y'),
            created.time(),
            created.tzinfo)
    else:
        caption += msgRep.CREATED_NULL.format(
            chat_obj_info.date.date().strftime('%b %d, %Y'),
            chat_obj_info.date.time(),
            chat_obj_info.date.tzinfo,
            warn_emoji)
    caption += msgRep.DCID.format(dc_id)
    if messages_viewable is not None:
        caption += msgRep.VIEWABLE_MSG.format(messages_viewable)
    if deleted_messages:
        caption += msgRep.DELETED_MSG.format(deleted_messages)
    if messages_sent:
        caption += msgRep.SENT_MSG.format(messages_sent)
    elif messages_sent_alt:
        caption += msgRep.SENT_MSG_PRED.format(messages_sent_alt, warn_emoji)
    if members:
        caption += msgRep.MEMBERS.format(members)
    if admins:
        caption += msgRep.ADMINS.format(admins)
    if bots_list:
        caption += msgRep.BOT_COUNT.format(bots)
    if members_online:
        caption += msgRep.ONLINE_MEM.format(members_online)
    if restricted_users:
        caption += msgRep.RESTRICTED_COUNT.format(restricted_users)
    if banned_users:
        caption += msgRep.BANNEDCOUNT.format(banned_users)
    if group_stickers:
        caption += msgRep.GRUP_STICKERS.format(
            chat.full_chat.stickerset.short_name,
            group_stickers)
    caption += "\n"
    if broadcast or supergroup:
        caption += msgRep.LINKED_CHAT.format(linked_chat)
        if linked_chat_title:
            caption += msgRep.LINKED_CHAT_TITLE.format(linked_chat_title)
        if linked_chat_username:
            caption += f"> Link: {linked_chat_username}\n"
        caption += "\n"
    if not broadcast:
        caption += msgRep.SLW_MODE.format(slowmode)
        if hasattr(chat_obj_info, "slowmode_enabled") and \
           chat_obj_info.slowmode_enabled:
            caption += msgRep.SLW_MODE_TIME.format(slowmode_time)
        else:
            caption += "\n\n"
    if hasattr(chat_obj_info, "restricted"):
        caption += msgRep.RESTR.format(restricted)
        if chat_obj_info.restricted:
            caption += msgRep.PFORM.format(
                chat_obj_info.restriction_reason[0].platform)
            caption += msgRep.REASON.format(
                chat_obj_info.restriction_reason[0].reason)
            caption += msgRep.TEXT.format(
                chat_obj_info.restriction_reason[0].text)
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
        caption += msgRep.SCAM
    if hasattr(chat_obj_info, "verified"):
        caption += msgRep.VERFIED.format(verified)
    if description:
        caption += msgRep.DESCRIPTION.format(description)
    return caption


@ehandler.on(command="chatinfo", hasArgs=True, outgoing=True)
async def chatinfo(event):
    await event.edit(msgRep.CHAT_ANALYSIS)

    chat = await get_chatinfo(event)

    if not chat:
        return

    try:
        caption = await fetch_info(chat, event)
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        log.error(e, exc_info=True)
        await event.edit(msgRep.EXCEPTION)
    return


@ehandler.on(command="chatid", outgoing=True)
async def chatid(event):
    chat = await event.get_chat()
    if isinstance(chat, (Chat, Channel)):
        await event.edit(msgRep.CID_TEXT.format(event.chat_id))
    else:
        await event.edit(msgRep.CID_NO_GROUP)
    return


@ehandler.on(command="getlink", hasArgs=True, outgoing=True)
async def chatid(event):
    arg = event.pattern_match.group(1)
    if arg:
        try:
            arg = int(arg)
        except ValueError:
            pass

        try:
            chat = await event.client.get_entity(arg)
        except Exception:
            await event.edit(msgRep.LINK_INVALID_ID)
            return
    else:
        chat = await event.get_chat()

    if not isinstance(chat, (Chat, Channel)):
        await event.edit(msgRep.LINK_INVALID_ID_GROUP)
        return

    try:
        result = await event.client(GetExportedChatInvitesRequest(chat.id,
                                                                  "me", 0))
        text = msgRep.LINK_TEXT.format(chat.title) + ":\n"
        if result.invites:
            for link in result.invites:
                if link.permanent and not link.revoked:
                    text += link.link
                    break
            await event.edit(text)
        else:
            await event.edit(msgRep.NO_LINK)
    except ChatAdminRequiredError:
        if chat.admin_rights and not chat.admin_rights.invite_users:
            await event.edit(msgRep.NO_INVITE_PERM)
        else:
            await event.edit(msgRep.NO_ADMIN_PERM)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.UNABLE_GET_LINK)
    return


for cmd in ("chatinfo", "chatid", "getlink"):
    register_cmd_usage(
        cmd,
        usageRep.CHATINFO_USAGE.get(cmd, {}).get("args"),
        usageRep.CHATINFO_USAGE.get(cmd, {}).get("usage")
    )

register_module_desc(descRep.CHATINFO_DESC)
register_module_info(
    name="Chat Info",
    authors="nunopenim, prototype74",
    version=VERSION
)
