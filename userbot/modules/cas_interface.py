# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License
#
# This module is powered by Combot Anti-Spam (CAS) system (https://cas.chat)

import userbot.include.cas_api as cas_api
from userbot.include.language_processor import (CasIntText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon.errors import (ChatAdminRequiredError, MessageTooLongError,
                             ChatSendMediaForbiddenError)
from telethon.tl.types import Chat, Channel, PeerUser, PeerChannel
from logging import getLogger
from os import path, remove
from os.path import exists
from requests import get, ConnectionError, Timeout

log = getLogger(__name__)
ehandler = EventHandler(log)
CAS_CSV = path.join(getConfig("USERDATA"), "export.csv")
CAS_USER_IDS = []


def _updateCASList() -> bool:
    global CAS_USER_IDS
    try:
        if CAS_USER_IDS:
            CAS_USER_IDS = []  # reset before appending again
        with open(CAS_CSV, "r") as data:
            for cas_id in data:
                try:
                    CAS_USER_IDS.append(int(cas_id))
                except:
                    pass
        data.close()
        if CAS_USER_IDS:
            return True
    except Exception as e:
        log.error(e)
    return False


def _createCASFile(title: str, cas_list: dict, filename: str) -> tuple:
    try:
        input_text = f"{title}\n\n"
        with open(filename, "w") as cas_file:
            for i, (key, val) in enumerate(cas_list.items(), start=1):
                input_text += f"{i}. {val} - {key}\n"  # val (name), key (id)
            cas_file.write(input_text)
        cas_file.close()
        return (filename, True)
    except IOError as io:
        log.warning(io)
    except Exception as e:
        log.warning(e)
    return (filename, False)


async def _casSendAsFile(event, title: str, cas_list: dict):
    await event.edit(msgRep.TOO_MANY_CAS)
    try:
        filename, success = _createCASFile(title, cas_list,
                                           path.join(getConfig("TEMP_DL_DIR"),
                                                     "caslist.txt"))
        if success:
            await event.client.send_file(event.chat_id, filename)
        else:
            await event.edit(msgRep.FAIL_UPLOAD_LIST)
    except ChatSendMediaForbiddenError:
        await event.edit(msgRep.SEND_MEDIA_FORBIDDEN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.FAIL_UPLOAD_LIST)
    if success:
        remove(filename)
    return


async def _getCASUser(event, entity, entity_id):
    user_id = entity.id if entity else entity_id
    if entity:
        firstname = entity.first_name if not entity.deleted \
                    else msgRep.DELETED_ACCOUNT
        lastname = entity.last_name  # can be None
        username = entity.username  # can be None
        await event.edit(msgRep.CHECK_USER.format(firstname))
    else:
        await event.edit(msgRep.CHECK_USER_ID.format(user_id))

    try:
        cas_data = cas_api.get_user_data(user_id)
    except:
        log.info("CAS user data not available")
        await event.edit(msgRep.CAS_CHECK_FAIL)
        return

    try:
        offenses = cas_api.offenses(cas_data)
    except Exception as e:
        log.warning(e)
        offenses = None

    try:
        time_banned = cas_api.timeadded(cas_data)
    except Exception as e:
        log.warning(e)
        time_banned = None

    is_banned = (f"[{msgRep.BANNED}]"
                 f"(https://api.cas.chat/check?user_id={user_id})"
                 if cas_api.isbanned(cas_data) else msgRep.NOT_BANNED)

    text = f"**{msgRep.USER_HEADER}**\n\n"
    text += f"{msgRep.USER_ID}: `{user_id}`\n"
    if entity:
        text += f"{msgRep.FIRST_NAME}: {firstname}\n"
        if lastname:
            text += f"{msgRep.LAST_NAME}: {lastname}\n"
        if username:
            text += f"{msgRep.USERNAME}: @{username}\n"
    text += f"\n**{msgRep.CAS_DATA}**\n\n"
    text += f"{msgRep.RESULT}: {is_banned}\n"
    if offenses:
        text += f"{msgRep.OFFENSES}: `{offenses}`\n"
    if time_banned:
        text += f"{msgRep.BANNED_SINCE}: "\
                f"`{time_banned.strftime('%b %d, %Y')} - "\
                f"{time_banned.time()} {time_banned.tzname()}`"
    await event.edit(text)
    return


async def _getCASChat(event, entity):
    global CAS_USER_IDS
    await event.edit(msgRep.CHECK_CHAT)
    if exists(CAS_CSV):
        if not CAS_USER_IDS and not _updateCASList():
            log.warning("Export CSV format from cas.chat is not valid")
            await event.edit(msgRep.CAS_CHECK_FAIL_ND)
            return
    else:
        log.info("CAS CSV data not available")
        await event.edit(msgRep.CAS_CHECK_ND)
        return
    title = entity.title
    text_users = ""
    cas_list = {}
    cas_count = 0
    async for user in event.client.iter_participants(entity.id):
        if user.id in CAS_USER_IDS:
            cas_count += 1
            if user.deleted:
                text_users += f"\n{cas_count}. {msgRep.DELETED_ACCOUNT} - "\
                              f"`{user.id}`"
                cas_list[user.id] = msgRep.DELETED_ACCOUNT
            elif user.username:
                text_users += f"\n{cas_count}. @{user.username} - "\
                                  f"`{user.id}`"
                cas_list[user.id] = f"@{user.username}"
            else:
                text_users += f"\n{cas_count}. "\
                              f"[{user.first_name}](tg://user?id={user.id}) "\
                              f"- `{user.id}`"
                cas_list[user.id] = user.first_name
    if cas_count == 1:
        text = msgRep.USER_DETECTED.format(cas_count, title) + ":\n"
    else:
        text = msgRep.USERS_DETECTED.format(cas_count, title) + ":\n"
    text += text_users
    if not cas_count:
        text = msgRep.NO_USERS.format(title)
    try:
        if cas_count > 30:  # limit list up to 30 users
            await _casSendAsFile(event, title, cas_list)
        else:
            await event.edit(text)
    except MessageTooLongError:
        await _casSendAsFile(event, text)
    return


@ehandler.on(command="casupdate", outgoing=True)
async def casupdate(event):
    log.info("Start to update CAS CSV data")
    await event.edit(msgRep.UPDATER_CONNECTING)
    try:
        request = get("https://api.cas.chat/export.csv", timeout=10)
        await event.edit(msgRep.UPDATER_DOWNLOADING)
        with open(CAS_CSV, "wb") as file:
            file.write(request.content)
        file.close()
        if not _updateCASList():
            await event.edit(msgRep.FAIL_APPEND_CAS)
            return
        log.info("Updated to latest CAS CSV data")
        await event.edit(msgRep.UPDATE_SUCCESS)
    except ConnectionError as c:
        log.warning(c)
        await event.edit(msgRep.NO_CONNECTION)
    except Timeout as t:
        log.warning(t)
        await event.edit(msgRep.TIMEOUT)
    except Exception as e:
        log.error(e)
        await event.edit(msgRep.UPDATE_FAILED)
    return


@ehandler.on(command="cascheck", hasArgs=True, outgoing=True)
async def cascheck(event):
    entity_id = None
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        if isinstance(msg.from_id, PeerUser):
            entity_id = msg.from_id.user_id
        elif isinstance(msg.from_id, PeerChannel):  # check the channel instead
            entity_id = msg.from_id.channel_id
    else:
        entity_id = event.pattern_match.group(1)
        try:
            entity_id = int(entity_id)
        except:
            pass

    if not entity_id:
        entity_id = event.chat_id

    try:
        entity = await event.client.get_entity(entity_id)
    except Exception as e:
        log.warning(e)
        entity = None

    if not entity and not isinstance(entity_id, int):
        await event.edit(msgRep.GIVEN_ENT_INVALID)
        return

    try:
        is_chat = True if isinstance(entity, (Chat, Channel)) else False
        if is_chat:
            await _getCASChat(event, entity)
        else:
            await _getCASUser(event, entity, entity_id)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.error(e)
        await event.edit(msgRep.CAS_CHECK_FAIL)
    return


register_cmd_usage("casupdate",
                   usageRep.CAS_INTERFACE_USAGE.get(
                       "casupdate", {}).get("args"),
                   usageRep.CAS_INTERFACE_USAGE.get(
                       "casupdate", {}).get("usage"))
register_cmd_usage("cascheck",
                   usageRep.CAS_INTERFACE_USAGE.get(
                       "cascheck", {}).get("args"),
                   usageRep.CAS_INTERFACE_USAGE.get(
                       "cascheck", {}).get("usage"))

register_module_desc(descRep.CAS_INTERFACE_DESC)
register_module_info(
    name="CAS Interface",
    authors="nunopenim, prototype74",
    version=VERSION
)
