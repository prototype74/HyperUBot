# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import event_log, fetch_entity
from userbot.include.language_processor import (UserText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon.tl.types import User, Chat, Channel, PeerChannel, PeerChat
from telethon.tl.types.users import UserFull
from telethon.tl.functions.contacts import GetBlockedRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)


@ehandler.on(command="id", alt="userid", hasArgs=True, outgoing=True)
async def userid(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        sender = msg.sender
        org_author = msg.forward.sender if msg.forward else None
        if not sender and not org_author:
            await event.edit(msgRep.UNABLE_GET_IDS)
            return

        if sender:
            if isinstance(sender, Channel):
                sender_link = (f"[{sender.title}]"
                               f"(https://t.me/{sender.username})"
                               if sender.username else sender.title)
                sender.id = int(f"-100{sender.id}")
            else:
                sender_link = (f"[{sender.first_name}]"
                               f"(tg://user?id={sender.id})")

        if org_author:
            if isinstance(org_author, Channel):
                org_author_link = (f"[{org_author.title}]"
                                   f"(https://t.me/{sender.username})"
                                   if org_author.username
                                   else org_author.title)
                org_author.id = int(f"-100{org_author.id}")
            else:
                org_author_link = (f"[{org_author.first_name}]"
                                   f"(tg://user?id={sender.id})")

        if sender and org_author:
            if not sender == org_author:
                text = (f"**{msgRep.ORIGINAL_AUTHOR}**:\n" +
                        msgRep.DUAL_HAS_ID_OF.format(org_author_link,
                                                     org_author.id) + "\n\n")
                text += (f"**{msgRep.FORWARDER}**:\n" +
                         msgRep.DUAL_HAS_ID_OF.format(sender_link, sender.id))
            else:
                if hasattr(sender, "deleted") and sender.deleted:
                    text = msgRep.DEL_HAS_ID_OF.format(sender.id)
                elif hasattr(sender, "is_self") and sender.is_self:
                    text = msgRep.MY_ID.format(sender.id)
                else:
                    text = msgRep.DUAL_HAS_ID_OF.format(sender_link, sender.id)
        elif sender and not org_author:
            if msg.fwd_from and msg.fwd_from.from_name:
                text = (f"**{msgRep.ORIGINAL_AUTHOR}**:\n" +
                        msgRep.ID_NOT_ACCESSIBLE.format(
                            msg.fwd_from.from_name) + "\n\n")
                text += (f"**{msgRep.FORWARDER}**:\n" +
                         msgRep.DUAL_HAS_ID_OF.format(sender_link, sender.id))
            else:
                if hasattr(sender, "deleted") and sender.deleted:
                    text = msgRep.DEL_HAS_ID_OF.format(sender.id)
                elif hasattr(sender, "is_self") and sender.is_self:
                    text = msgRep.MY_ID.format(sender.id)
                else:
                    text = msgRep.DUAL_HAS_ID_OF.format(sender_link, sender.id)
        elif not sender and org_author:
            text = msgRep.ORG_HAS_ID_OF.format(org_author_link, org_author.id)
    else:
        entity_obj = await fetch_entity(event)

        if not entity_obj:
            return

        if hasattr(entity_obj, "deleted") and entity_obj.deleted:
            text = msgRep.DEL_HAS_ID_OF.format(entity_obj.id)
        elif hasattr(entity_obj, "is_self") and  entity_obj.is_self:
            text = msgRep.MY_ID.format(entity_obj.id)
        else:
            if isinstance(entity_obj, Channel):
                entity_link = (f"[{entity_obj.title}]"
                               f"(https://t.me/{entity_obj.username})"
                               if entity_obj.username else entity_obj.title)
                entity_obj.id = int(f"-100{entity_obj.id}")
            else:
                entity_link = (f"[{entity_obj.first_name}]"
                             "(tg://user?id={entity_obj.id})")
            text = msgRep.DUAL_HAS_ID_OF.format(entity_link, entity_obj.id)
    await event.edit(text)
    return


@ehandler.on(command="kickme", alt="leave", outgoing=True)
async def kickme(leave):
    if not isinstance(leave.message.peer_id, (PeerChannel, PeerChat)):
        await leave.edit(msgRep.CANNOT_LEAVE)
        return
    await leave.edit(msgRep.LEAVING)
    await leave.client.kick_participant(leave.chat_id, 'me')
    if getConfig("LOGGING"):
        await event_log(leave, "KICKME", chat_title=leave.chat.title,
                        chat_id=leave.chat_id)
    return


@ehandler.on(command="stats", outgoing=True)
async def stats(event):
    (groups, channels, super_groups, bots, users, unknown, total,
     group_owner, group_admin, super_group_owner, super_group_admin,
     total_blocks, channel_owner, channel_admin) = (0,)*14

    await event.edit(msgRep.STATS_PROCESSING)

    try:
        blocked_ids = []
        block_obj = await event.client(GetBlockedRequest(offset=0,
                                                         limit=2147483647))
        if block_obj.blocked:
            for user in block_obj.blocked:
                blocked_ids.append(user.peer_id.user_id)
            total_blocks = len(blocked_ids)
    except Exception:
        log.error("Failed to list blocked accounts", exc_info=True)
        blocked_ids = []

    async for dialog in event.client.iter_dialogs(ignore_migrated=True):
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
            else:
                users += 1
        else:
            unknown += 1

    result = f"**{msgRep.STATS_HEADER}**\n\n"
    result += msgRep.STATS_USERS.format(users) + "\n"
    result += msgRep.STATS_BOTS.format(bots) + "\n"
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
    result += "\n" + (msgRep.STATS_UNKNOWN.format(unknown) + "\n\n"
                      if unknown else "\n")
    result += f"{msgRep.STATS_TOTAL}: **{total}**\n"
    await event.edit(result)
    return


@ehandler.on(command="info", hasArgs=True, outgoing=True)
async def info(event):
    await event.edit(msgRep.FETCH_INFO)

    full_user_obj = await fetch_entity(event=event, full_obj=True,
                                       org_author=True)
    # fetch_entity() will return an error msg if something failed
    if not full_user_obj:
        return

    if not isinstance(full_user_obj, UserFull):
        await event.edit(msgRep.INFO_PERSONS_ONLY)
        return

    try:
        caption = await fetch_info(full_user_obj, event)
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        log.error(e)
        await event.edit(msgRep.FAILED_FETCH_INFO)
    return


def _getUserObjFromFullUser(fulluser_obj, user_id) -> User:
    if fulluser_obj and hasattr(fulluser_obj, "users") and fulluser_obj.users:
        for user in fulluser_obj.users:
            if user_id == user.id:
                return user
    return None


async def fetch_info(full_user_obj, event):
    user_id = full_user_obj.full_user.id
    user_obj = _getUserObjFromFullUser(full_user_obj, user_id)
    if not user_obj:
        # makes no sense to keep fetching infos if 80% of them will be missing
        raise Exception("UserFull does not include target User object")
    try:
        user_pfps = await event.client(
            GetUserPhotosRequest(user_id=user_id,
                                 offset=42,
                                 max_id=0,
                                 limit=80))
        user_pfps_count = (user_pfps.count
                           if hasattr(user_pfps, "count") else 0)
    except Exception:
        user_pfps_count = 0
    user_deleted = user_obj.deleted
    user_self = user_obj.is_self
    first_name = (user_obj.first_name
                  if not user_deleted else msgRep.DELETED_ACCOUNT)
    last_name = user_obj.last_name if user_obj.last_name else None
    dc_id = msgRep.UNKNOWN
    if full_user_obj.full_user.profile_photo:
        if hasattr(full_user_obj.full_user.profile_photo, "dc_id"):
            dc_id = full_user_obj.full_user.profile_photo.dc_id
    common_chat = full_user_obj.full_user.common_chats_count
    username = user_obj.username
    user_bio = full_user_obj.full_user.about
    is_bot = f"<b>{msgRep.YES}</b>" if user_obj.bot else msgRep.NO
    premium = f"<b>{msgRep.YES}</b>" if user_obj.premium else msgRep.NO
    scam = f"<b>{msgRep.YES}</b>" if user_obj.scam else msgRep.NO
    restricted = (f"<b>{msgRep.YES}</b>"
                  if user_obj.restricted else msgRep.NO)
    verified = (f"<b>{msgRep.YES}</b>"
                if user_obj.verified else msgRep.NO)
    username = "@{}".format(username) if username else None
    user_bio = msgRep.USR_NO_BIO if not user_bio else user_bio
    profile_link = f"<a href=\"tg://user?id={user_id}\">link</a>"

    caption = f"<b>{msgRep.USR_INFO}</b>\n\n"
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
    caption += f"{msgRep.PREMIUM}: {premium}\n"
    caption += f"{msgRep.SCAMMER}: {scam}\n"
    caption += f"{msgRep.ISRESTRICTED}: {restricted}\n"
    caption += f"{msgRep.ISVERIFIED}: {verified}\n\n"
    caption += f"{msgRep.BIO}:\n<code>{user_bio}</code>\n\n"
    if user_self:
        caption += f"{msgRep.COMMON_SELF}"
    else:
        caption += f"{msgRep.COMMON}: {common_chat}"
    return caption


for cmd in ("id", "info", "kickme", "stats"):
    register_cmd_usage(
        cmd,
        usageRep.USER_USAGE.get(cmd, {}).get("args"),
        usageRep.USER_USAGE.get(cmd, {}).get("usage")
    )

register_module_desc(descRep.USER_DESC)
register_module_info(
    name="User",
    authors="nunopenim, prototype74",
    version=VERSION
)
