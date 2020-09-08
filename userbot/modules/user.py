# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My Stuff
from userbot import tgclient, LOGGING, MODULE_DESC, MODULE_DICT
from userbot.include.aux_funcs import event_log
from userbot.include.language_processor import (UserText as msgRep, ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.include.aux_funcs import fetch_user

# Telethon stuff
from telethon.events import NewMessage
from telethon.tl.types import User, Chat, Channel
from telethon.tl.functions.contacts import GetBlockedRequest
from telethon.tl.functions.photos import GetUserPhotosRequest

# Misc Imports
from asyncio import sleep
from logging import getLogger
from os.path import basename


log = getLogger(__name__)


@tgclient.on(NewMessage(pattern=r"^\.kickme$", outgoing=True))
async def kickme(leave):
    await leave.edit(msgRep.LEAVING)
    await sleep(0.1) #wait to avoid bad stuff
    await leave.client.kick_participant(leave.chat_id, 'me')
    if LOGGING:
        await event_log(leave, "KICKME", chat_title=leave.chat.title, chat_id=leave.chat.id)
    return

@tgclient.on(NewMessage(pattern=r"^\.stats$", outgoing=True))
async def stats(event):
    (groups, channels, super_groups, bots, users, unknown, total,
     group_owner, group_admin, super_group_owner, super_group_admin,
     bot_blocked, user_blocked, total_blocks, channel_owner,
     channel_admin) = (0,)*16
    blocked_ids = []

    await event.edit(msgRep.STATS_PROCESSING)

    try:
        block_obj = await event.client(GetBlockedRequest(offset=0, limit=0))
        if block_obj.blocked:
            for user in block_obj.blocked:
                blocked_ids.append(user.user_id)
            total_blocks = len(blocked_ids)
    except:
        pass

    async for dialog in tgclient.iter_dialogs(ignore_migrated=True):
        total += 1
        if isinstance(dialog.entity, Chat):
            groups += 1
            if dialog.entity.creator:
                group_owner += 1
            elif dialog.entity.admin_rights:
                group_admin += 1
        elif isinstance(dialog.entity, Channel):
            if dialog.entity.broadcast:
                channels += 1
                if dialog.entity.creator:
                    channel_owner += 1
                elif dialog.entity.admin_rights:
                    channel_admin += 1
            elif dialog.entity.megagroup:
                super_groups += 1
                if dialog.entity.creator:
                    super_group_owner += 1
                elif dialog.entity.admin_rights:
                    super_group_admin += 1
            else:
                unknown += 1
        elif isinstance(dialog.entity, User):
            if dialog.entity.bot:
                bots += 1
                if dialog.entity.id in blocked_ids:
                    bot_blocked += 1
            else:
                users += 1
                if dialog.entity.id in blocked_ids:
                    user_blocked += 1
        else:
            unknown += 1

    result = f"**{msgRep.STATS_HEADER}:**\n\n"
    result += msgRep.STATS_USERS.format(users) + "\n"
    result += "> " + msgRep.STATS_BLOCKED.format(user_blocked) + "\n\n"
    result += msgRep.STATS_BOTS.format(bots) + "\n"
    result += "> " + msgRep.STATS_BLOCKED.format(bot_blocked) + "\n\n"
    result += msgRep.STATS_BLOCKED_TOTAL.format(total_blocks) + "\n\n"
    result += msgRep.STATS_GROUPS.format(groups) + "\n"
    result += "> " + msgRep.STATS_SGC_OWNER.format(group_owner) + "\n"
    result += "> " + msgRep.STATS_GROUPS_ADMIN.format(group_admin) + "\n\n"
    result += msgRep.STATS_SUPER_GROUPS.format(super_groups) + "\n"
    result += "> " + msgRep.STATS_SGC_OWNER.format(super_group_owner) + "\n"
    result += "> " + msgRep.STATS_SG_ADMIN.format(super_group_admin) + "\n\n"
    result += msgRep.STATS_CHANNELS.format(channels) + "\n"
    result += "> " + msgRep.STATS_SGC_OWNER.format(channel_owner) + "\n"
    result += "> " + msgRep.STATS_CHAN_ADMIN.format(channel_admin) + "\n"
    result += "\n" + msgRep.STATS_UNKNOWN.format(unknown) + "\n\n" if unknown else "\n"
    result += f"{msgRep.STATS_TOTAL}: **{total}**\n"

    await event.edit(result)

    return

@tgclient.on(NewMessage(pattern=r"^\.info(?: |$)(.*)", outgoing=True))
async def info(event):  # .info command
    await event.edit(msgRep.FETCH_INFO)

    full_user_obj = await fetch_user(event=event, full_user=True, org_author=True)
    if not full_user_obj:  # fetch_user() will return an error msg if something failed
        return

    try:
        caption = await fetch_info(full_user_obj, event)
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        log.error(e)
        await event.edit(msgRep.FAILED_FETCH_INFO)

    return

async def fetch_info(replied_user, event):
    try:
        user_pfps = await event.client(GetUserPhotosRequest(user_id=replied_user.user.id, offset=42, max_id=0, limit=80))
        user_pfps_count = user_pfps.count if hasattr(user_pfps, "count") else 0
    except:
        user_pfps_count = 0
    user_id = replied_user.user.id
    user_deleted = replied_user.user.deleted
    user_self = replied_user.user.is_self
    first_name = replied_user.user.first_name if not user_deleted else msgRep.DELETED_ACCOUNT
    last_name = replied_user.user.last_name if replied_user.user.last_name else None
    dc_id = msgRep.UNKNOWN
    if replied_user.profile_photo:
        if hasattr(replied_user.profile_photo, "dc_id"):
            dc_id = replied_user.profile_photo.dc_id
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = f"<b>{msgRep.YES}</b>" if replied_user.user.bot else msgRep.NO
    scam = f"<b>{msgRep.YES}</b>" if replied_user.user.scam else msgRep.NO
    restricted = f"<b>{msgRep.YES}</b>" if replied_user.user.restricted else msgRep.NO
    verified = f"<b>{msgRep.YES}</b>" if replied_user.user.verified else msgRep.NO
    username = "@{}".format(username) if username else None
    user_bio = msgRep.USR_NO_BIO if not user_bio else user_bio
    profile_link = f"<a href=\"tg://user?id={user_id}\">link</a>"

    caption = f"<b>{msgRep.USR_INFO}:</b>\n\n"
    caption += f"{msgRep.USR_ID}: <code>{user_id}</code>\n"
    caption += f"{msgRep.FIRST_NAME}: {first_name}\n"
    if last_name:
        caption += f"{msgRep.LAST_NAME}: {last_name}\n"
    if username:
        caption += f"{msgRep.USERNAME}: {username}\n"
    caption += f"{msgRep.DCID}: {dc_id}\n"
    if user_pfps_count:
        caption += f"{msgRep.PROF_PIC_COUNT}: {user_pfps_count}\n"
    if not user_deleted:
        caption += f"{msgRep.PROF_LINK}: {profile_link}\n"
    caption += f"{msgRep.ISBOT}: {is_bot}\n"
    caption += f"{msgRep.SCAMMER}: {scam}\n"
    caption += f"{msgRep.ISRESTRICTED}: {restricted}\n"
    caption += f"{msgRep.ISVERIFIED}: {verified}\n\n"
    caption += f"{msgRep.BIO}:\n<code>{user_bio}</code>\n\n"
    if user_self:
        caption += f"{msgRep.COMMON_SELF}"
    else:
        caption += f"{msgRep.COMMON}: {common_chat}"

    return caption

MODULE_DESC.update({basename(__file__)[:-3]: descRep.USER_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.USER_USAGE})
