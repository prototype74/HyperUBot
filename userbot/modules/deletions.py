# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import MODULE_DESC, MODULE_DICT, MODULE_INFO, VERSION
from userbot.include.aux_funcs import event_log, module_info
from userbot.include.language_processor import DeletionsText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from telethon.errors import MessageDeleteForbiddenError
from telethon.tl.functions.channels import DeleteMessagesRequest
from telethon.tl.functions.messages import DeleteMessagesRequest as DeleteMessagesRequestGPM
from telethon.tl.types import Chat, Channel
from asyncio import sleep
from logging import getLogger
from os.path import basename

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")

@ehandler.on(pattern=r"^\.del$", outgoing=True)
async def delete(event):
    if event.reply_to_msg_id:
        chat = await event.get_chat()
        try:
            if isinstance(chat, Channel):  # channel or supergroup
                update = await event.client(DeleteMessagesRequest(chat.id, [event.reply_to_msg_id]))
            else:
                # chat id isn't required to delete messages in normal groups or in PMs
                update = await event.client(DeleteMessagesRequestGPM([event.reply_to_msg_id], revoke=True))
            if not update.pts_count:  # pts_count is set to 1 if target message has been deleted
                await event.edit(msgRep.CANNOT_DEL_MSG)
                return
            await event.delete()
        except MessageDeleteForbiddenError:
            await event.edit(msgRep.UNABLE_DEL_MSG)
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.DEL_MSG_FAILED)
    else:
        await event.edit(msgRep.REPLY_DEL_MSG)

    return

@ehandler.on(pattern=r"^\.purge$", outgoing=True)
async def purge(event):
    """ Please don't abuse this feature to delete someone's else whole group history, for real, just don't """
    if event.reply_to_msg_id:
        chat = await event.get_chat()
        channel_obj = True if isinstance(chat, Channel) else False  # Channel or supergroup
        chat_obj = True if isinstance(chat, Chat) else False  # Normal group

        if channel_obj or chat_obj:
            if not chat.creator and not chat.admin_rights:
                await event.edit(msgRep.NO_ADMIN_PURGE)
                return
            if chat.admin_rights and not chat.admin_rights.delete_messages:
                await event.edit(msgRep.NO_DEL_PRIV)
                return

        message_ids = []
        wait_time_sec = 2  # Prevent FloodWaitError
        async for message in event.client.iter_messages(entity=chat.id, min_id=event.reply_to_msg_id,
                                                        wait_time=wait_time_sec):
            message_ids.append(message.id)

        message_ids.append(event.reply_to_msg_id)  # last but not least add replied message
        msg_count = len(message_ids)

        try:
            if channel_obj:
                await event.client(DeleteMessagesRequest(chat.id, message_ids))
            else:
                await event.client(DeleteMessagesRequestGPM(message_ids, revoke=True))
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.PURGE_MSG_FAILED)
            return

        try:
            result = await event.client.send_message(chat.id, msgRep.PURGE_COMPLETE.format(msg_count))
            await sleep(2.5)
            await result.delete()
            if LOGGING:
                await event_log(event, "PURGE", chat_title=chat.title if hasattr(chat, "title") else None,
                                chat_link=chat.username if hasattr(chat, "username") else None,
                                chat_id=chat.id if hasattr(chat, "id") else None,
                                custom_text= msgRep.LOG_PURGE.format(msg_count))
        except Exception as e:
            log.error(e)
    else:
        await event.edit(msgRep.REPLY_PURGE_MSG)

    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.DELETIONS_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.DELETIONS_USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Deletions", version=VERSION)})
