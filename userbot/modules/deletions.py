# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import event_log
from userbot.include.language_processor import (DeletionsText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon.tl.types import Chat, Channel, User
from asyncio import sleep
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")


async def del_msgs(event, chat_id, messages: list) -> int:
    msgs_count = 0
    try:
        # delete_messages() revokes messages by default (revoke=True)
        affected_msgs = await event.client.delete_messages(
            entity=chat_id, message_ids=messages)
        for am in affected_msgs:
            msgs_count += am.pts_count
    except Exception as e:
        raise Exception(e)
    return msgs_count


@ehandler.on(command="del", outgoing=True)
async def delete(event):
    if event.reply_to_msg_id:
        try:
            msgs_count = await del_msgs(event,
                                        chat_id=event.chat_id,
                                        messages=[event.reply_to_msg_id])
            # del_msgs should return 1 if target message has been deleted
            if not msgs_count:
                await event.edit(msgRep.CANNOT_DEL_MSG)
                return
            await event.delete()
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.DEL_MSG_FAILED)
    else:
        await event.edit(msgRep.REPLY_DEL_MSG)
    return


@ehandler.on(command="purge", outgoing=True)
async def purge(event):
    """ Please don't abuse this feature to delete someone's else
        whole group history, for real, just don't.
    """
    if event.reply_to_msg_id:
        chat = await event.get_chat()
        channel_obj = True if isinstance(chat, Channel) else False
        chat_obj = True if isinstance(chat, Chat) else False

        if channel_obj or chat_obj:
            if not chat.creator and not chat.admin_rights:
                await event.edit(msgRep.NO_ADMIN_PURGE)
                return
            if chat.admin_rights and not chat.admin_rights.delete_messages:
                await event.edit(msgRep.NO_DEL_PRIV)
                return

        message_ids = []
        if chat_obj or isinstance(chat, User):
            # For normal groups and PMs
            async for message in (
                event.client.iter_messages(entity=chat.id,
                                           min_id=event.reply_to_msg_id)):
                if not message.id == event.message.id:
                    message_ids.append(message.id)
            message_ids.append(event.reply_to_msg_id)
        else:
            # For channel objects (Channels and Super groups)
            # Instead of using iter_messages we just create a range of IDs
            # between the replied msg' ID and this event's ID (e.g. 24
            # (replied msg) to 48 (.'purge' msg)) regardless if there are
            # gaps (due to deletions) between the min and max ID. This method
            # works for channels and super groups only as channel objects have
            # their own message IDs. Using this method in PMs or normal
            # groups may accidentally cause deletions in different
            # PM conversations or normal chats
            for i in range(event.reply_to_msg_id, event.message.id):
                if not i == event.message.id:
                    message_ids.append(i)
            message_ids.reverse()

        nested_msgs = []

        # As Telegram only allows to delete up to 100 messages at once,
        # nest every 100th ID into a new list
        for i in range(0, len(message_ids), 100):
            nested_msgs.append(message_ids[i:i+100])

        msgs_count = 0
        try:
            for msgs_list in nested_msgs:
                msgs_count += await del_msgs(event, chat_id=chat.id,
                                             messages=msgs_list)
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.PURGE_MSG_FAILED)
            return

        try:
            await event.edit(msgRep.PURGE_COMPLETE.format(msgs_count))
            await sleep(2)
            await event.delete()
            if LOGGING:
                await event_log(event, "PURGE", chat_title=chat.title
                                if hasattr(chat, "title") else None,
                                chat_link=chat.username
                                if hasattr(chat, "username") else None,
                                chat_id=event.chat_id,
                                custom_text=msgRep.LOG_PURGE.format(
                                    msgs_count))
        except Exception as e:
            log.error(e)
    else:
        await event.edit(msgRep.REPLY_PURGE_MSG)
    return


for cmd in ("del", "purge"):
    register_cmd_usage(
        cmd,
        usageRep.DELETIONS_USAGE.get(cmd, {}).get("args"),
        usageRep.DELETIONS_USAGE.get(cmd, {}).get("usage")
    )

register_module_desc(descRep.DELETIONS_DESC)
register_module_info(
    name="Deletions",
    authors="nunopenim, prototype74",
    version=VERSION
)
