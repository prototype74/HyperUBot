# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO, VERSION
from userbot.include.aux_funcs import fetch_user, isRemoteCMD, module_info
from userbot.include.language_processor import MessagesText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from telethon.errors import ChatAdminRequiredError, InputUserDeactivatedError, SearchQueryEmptyError
from telethon.events import NewMessage
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty, ChannelParticipantsAdmins, Chat, Channel
from logging import getLogger
from os.path import basename

log = getLogger(__name__)

@tgclient.on(NewMessage(pattern=r"^\.msgs(?: |$)(.*)", outgoing=True))
async def countmessages(event):
    user, chat = await fetch_user(event, get_chat=True)

    if not user:
        return

    if not chat:
        await event.edit(msgRep.FAIL_CHAT)
        return

    remote = isRemoteCMD(event, chat.id)

    try:
        msg_info = await event.client(SearchRequest(peer=chat.id, q="",  # search for any message
                                                    filter=InputMessagesFilterEmpty(),
                                                    min_date=None, max_date=None,
                                                    add_offset=0, offset_id=0,
                                                    limit=0, max_id=0, min_id=0,
                                                    hash=0, from_id=user.id))
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
        return
    except InputUserDeactivatedError:
        await event.edit(msgRep.CANNOT_COUNT_DEL)
        return
    except SearchQueryEmptyError as sqee:
        log.warning(sqee)
        await event.edit(msgRep.CANNOT_COUNT_FWD)
        return
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.FAIL_COUNT_MSG)
        return

    user_link = "@" + user.username if user.username else f"[{user.first_name}](tg://user?id={user.id})"

    if hasattr(msg_info, "count"):
        if remote:
            await event.edit(msgRep.USER_HAS_SENT_REMOTE.format(user_link, msg_info.count, chat.title))
        else:
            await event.edit(msgRep.USER_HAS_SENT.format(user_link, msg_info.count))
    else:
        if remote:
            await event.edit(msgRep.CANNOT_COUNT_MSG_REMOTE.format(chat.title))
        else:
            await event.edit(msgRep.CANNOT_COUNT_MSG)
    return

@tgclient.on(NewMessage(pattern=r"^\.topusers(?: |$)(.*)", outgoing=True))
async def topusers(event):
    arg = event.pattern_match.group(1)

    try:
        arg = int(arg)
    except:
        pass

    if not arg:
        arg = event.chat_id

    try:
        chat = await event.client.get_entity(arg)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.FAIL_CHAT)
        return

    if not isinstance(chat, (Chat, Channel)):
        await event.edit(msgRep.NO_GROUP_CHAN)
        return

    users = {}
    count = 0
    # if this feature is being used in channels, then filter by admins only
    channel = True if hasattr(chat, "broadcast") and chat.broadcast else False

    try:
        await event.edit(msgRep.PICKING_MEMBERS)
        async for user in event.client.iter_participants(chat.id, filter=ChannelParticipantsAdmins() if channel else None):
            # counting messages from deleted users would trigger InputUserDeactivatedError exception,
            # so skip them.
            if not user.deleted:
                user_link  = "@" + user.username if user.username else f"[{user.first_name}](tg://user?id={user.id})"
                if not user_link in users.keys():
                    msg_info = await event.client(SearchRequest(peer=chat.id,
                                                                q="",  # search for any message
                                                                filter=InputMessagesFilterEmpty(),
                                                                min_date=None, max_date=None,
                                                                add_offset=0, offset_id=0,
                                                                limit=0, max_id=0, min_id=0,
                                                                hash=0, from_id=user.id))
                    users[user_link] = msg_info.count  # add new key
        count = len(users.keys()) if len(users.keys()) < 10 else 10
        # sort the dictionary by highest value and limit it to 10 keys or lower
        users = {key: value for key, value in sorted(users.items(), key=lambda item: item[1], reverse=True)[:count]}
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
        return
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.FAILED_TO_PICK)
        return

    text = msgRep.TOP_USERS_TEXT.format(count, chat.title) + ":\n\n"
    count = 1
    for key, value in users.items():
        text += "{}. {}: `{}` {}\n".format(count, key, value, msgRep.TOP_USERS_MSGS)
        count += 1
    await event.edit(text)
    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.MESSAGES_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.MESSAGES_USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Messages", version=VERSION)})
