# My stuff
from tg_userbot import tgclient, log, MODULE_DESC, MODULE_DICT
from tg_userbot.include.language_processor import (ChatInfoText as msgRep, ModuleDescriptions as descRep,
                                                   ModuleUsages as usageRep)

# Telethon stuff
from telethon.errors import ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError
from telethon.events import NewMessage
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.utils import get_input_location

# Misc imports
from datetime import datetime
from math import sqrt
from os.path import basename

@tgclient.on(NewMessage(pattern=r"^\.chatinfo(?: |$)(.*)", outgoing=True))
async def info(event):
    await event.edit(msgRep.CHAT_ANALYSIS)

    chat = await get_chatinfo(event)

    if not chat:
        return

    caption = await fetch_info(chat, event)

    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        log.error(f"{basename(__file__)[:-3]}: {e}")
        await event.edit(msgRep.EXCEPTION)
    return

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.edit(msgRep.INVALID_CH_GRP)
            return None
        except ChannelPrivateError:
            await event.edit(msgRep.PRV_BAN)
            return None
        except ChannelPublicGroupNaError:
            await event.edit(msgRep.NOT_EXISTS)
            return None
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return chat_info

async def fetch_info(chat, event):
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = u"\u26A0"
    try:
        msg_info = await event.client(GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1), add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except:
        msg_info = None
    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Deleted Account"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = msgRep.UNKNOWN
        location = str(e)

    # Prototype's spaghetti, although already salted by me
    description = chat.full_chat.about
    members = chat.full_chat.participants_count if hasattr(chat.full_chat, "participants_count") else chat_obj_info.participants_count
    admins = chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    banned_users = chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    restricted_users = chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    members_online = chat.full_chat.online_count if hasattr(chat.full_chat, "online_count") else 0
    group_stickers = chat.full_chat.stickerset.title if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset else None
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    if messages_sent and messages_viewable:
        deleted_messages = (messages_sent - messages_viewable) if messages_sent >= messages_viewable else 0
    elif messages_sent_alt and messages_viewable:
        deleted_messages = (messages_sent_alt - messages_viewable) if messages_sent_alt >= messages_viewable else 0
    else:
        deleted_messages = 0
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = True if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup else False
    is_supergroup = msgRep.YES_BOLD if supergroup else msgRep.NO
    slowmode = msgRep.YES_BOLD if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else msgRep.NO
    slowmode_time = chat.full_chat.slowmode_seconds if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else None
    restricted = msgRep.YES_BOLD if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted else msgRep.NO
    verified = msgRep.YES_BOLD if hasattr(chat_obj_info, "verified") and chat_obj_info.verified else msgRep.NO
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None
    linked_chat_id = chat.full_chat.linked_chat_id if hasattr(chat.full_chat, "linked_chat_id") else None
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
    # End of spaghetti block

    if admins is None:
        try:
            participants_admins = await event.client(GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(), offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except:
            pass
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = msgRep.CHATINFO
    caption += msgRep.CHAT_ID.format(chat_obj_info.id)
    caption += msgRep.CHATTYPE.format(chat_type)
    if chat_title is not None:
        caption += msgRep.CHAT_NAME.format(chat_title)
    if former_title is not None:  # Meant is the very first title
        caption += msgRep.FORMER_NAME.format(former_title)
    if username is not None:
        caption += msgRep.CHAT_TYPE_PUBLIC
        caption += f"Link: {username}\n"
    else:
        caption += msgRep.CHAT_TYPE_PRIVATE
    if creator_username is not None:
        caption += msgRep.CREATOR.format(creator_username)
    elif creator_valid:
        caption += msgRep.CREATOR_WITH_URL.format(creator_id, creator_firstname)
    if created is not None:
        caption += msgRep.CREATED_NOT_NULL.format(created.date().strftime('%b %d, %Y'), created.time(), created.tzinfo)
    else:
        caption += msgRep.CREATED_NULL.format(chat_obj_info.date.date().strftime('%b %d, %Y'), chat_obj_info.date.time(), chat_obj_info.date.tzinfo, warn_emoji)
    caption += msgRep.DCID.format(dc_id)
    if exp_count is not None:
        chat_level = int((1 + sqrt(1 + 7 * exp_count / 14)) / 2)
        caption += msgRep.CHAT_LEVEL.format(chat_level)
    if messages_viewable is not None:
        caption += msgRep.VIEWABLE_MSG.format(messages_viewable)
    if deleted_messages:
        caption += msgRep.DELETED_MSG.format(deleted_messages)
    if messages_sent:
        caption += msgRep.SENT_MSG.format(messages_sent)
    elif messages_sent_alt:
        caption += msgRep.SENT_MSG_PRED.format(messages_sent_alt, warn_emoji)
    if members is not None:
        caption += msgRep.MEMBERS.format(members)
    if admins is not None:
        caption += msgRep.ADMINS.format(admins)
    if bots_list:
        caption += msgRep.BOT_COUNT.format(bots)
    if members_online:
        caption += msgRep.ONLINE_MEM.format(members_online)
    if restricted_users is not None:
        caption += msgRep.RESTRICTED_COUNT.format(restricted_users)
    if banned_users is not None:
        caption += msgRep.BANNEDCOUNT.format(banned_users)
    if group_stickers is not None:
        caption += msgRep.GRUP_STICKERS.format(chat.full_chat.stickerset.short_name, group_stickers)
    caption += "\n"
    if broadcast or supergroup:
        caption += msgRep.LINKED_CHAT.format(linked_chat)
        if linked_chat_title is not None:
            caption += msgRep.LINKED_CHAT_TITLE.format(linked_chat_title)
        if linked_chat_username is not None:
            caption += f"> Link: {linked_chat_username}\n"
        caption += "\n"
    if not broadcast:
        caption += msgRep.SLW_MODE.format(slowmode)
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
            caption += msgRep.SLW_MODE_TIME.format(slowmode_time)
        else:
            caption += "\n\n"
    if not broadcast:
        caption += msgRep.SPER_GRP.format(is_supergroup)
    if hasattr(chat_obj_info, "restricted"):
        caption += msgRep.RESTR.format(restricted)
        if chat_obj_info.restricted:
            caption += msgRep.PFORM.format(chat_obj_info.restriction_reason[0].platform)
            caption += msgRep.REASON.format(chat_obj_info.restriction_reason[0].reason)
            caption += msgRep.TEXT.format(chat_obj_info.restriction_reason[0].text)
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
        caption += msgRep.SCAM
    if hasattr(chat_obj_info, "verified"):
        caption += msgRep.VERFIED.format(verified)
    if description:
        caption += msgRep.DESCRIPTION.format(description)
    return caption

MODULE_DESC.update({basename(__file__)[:-3]: descRep.CHATINFO_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.CHATINFO_USAGE})
