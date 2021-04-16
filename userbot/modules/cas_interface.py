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
from userbot.include.language_processor import CasIntText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.version import VERSION
from telethon.errors import ChatAdminRequiredError, MessageTooLongError, ChatSendMediaForbiddenError
from telethon.tl.types import User, Chat, Channel, PeerUser, PeerChannel
from datetime import datetime
from logging import getLogger
from os import path, remove
from os.path import exists, getmtime
from requests import get, ConnectionError, Timeout
from time import sleep

log = getLogger(__name__)
ehandler = EventHandler(log)
CAS_CSV = path.join(getConfig("TEMP_DL_DIR"), "export.csv")
CAS_USER_IDS = []

def updateCASList() -> bool:
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

def createCASFile(input_text: str, filename: str) -> tuple:
    try:
        with open(filename, "w") as cas_file:
            cas_file.write(input_text)
        cas_file.close()
        return (filename, True)
    except IOError as io:
        log.warning(io)
    except Exception as e:
        log.warning(e)
    return (filename, False)

async def casSendAsFile(event, input_text: str):
    await event.edit(msgRep.TOO_MANY_CAS)
    try:
        filename, success = createCASFile(input_text, path.join(getConfig("TEMP_DL_DIR"), "caslist.txt"))
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

def isCSVoutdated() -> bool:
    if not exists(CAS_CSV):
        return False
    file_date = datetime.fromtimestamp(getmtime(CAS_CSV))
    duration = datetime.today() - file_date
    return True if duration.days >= 1 else False

async def casupdater(event, showinfo: bool, tries: int = 0):
    try:
        request = get("https://api.cas.chat/export.csv", timeout=10)
        if showinfo:
            await event.edit(msgRep.UPDATER_DOWNLOADING)
        with open(CAS_CSV, "wb") as file:
            file.write(request.content)
        file.close()
        if not updateCASList():
            await event.edit(msgRep.FAIL_APPEND_CAS)
            return
        if showinfo:
            await event.edit(msgRep.UPDATE_SUCCESS)
        log.info("Updated to latest CAS CSV data")
    except ConnectionError as c:
        log.warning(c)
        await event.edit(msgRep.NO_CONNECTION)
    except Timeout as t:
        if tries <= 5:
            log.info(f"Reconnecting to CAS server...({tries})")
            await event.edit(msgRep.RETRY_CONNECTION.format(tries))
            sleep(0.5)
            tries += 1
            await casupdater(event, showinfo, tries)
        else:
            log.warning(t)
            await event.edit(msgRep.TIMEOUT)
    except Exception as e:
        log.error(e)
        await event.edit(msgRep.UPDATE_FAILED)

    return

@ehandler.on(command="casupdate", outgoing=True)
async def casupdate(event):
    log.info("Manual CAS CSV data update started")
    await event.edit(msgRep.UPDATER_CONNECTING)
    await casupdater(event, showinfo=True)
    return

@ehandler.on(command="cascheck", hasArgs=True, outgoing=True)
async def cascheck(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        if isinstance(msg.from_id, PeerUser):
            entity_id = msg.from_id.user_id
        elif isinstance(msg.from_id, PeerChannel):  # check the channel instead
            entity_id = msg.from_id.channel_id
        else:
            entity_id = None
    else:
        entity_id = event.pattern_match.group(1)
        try:
            entity_id = int(entity_id)
        except:
            pass

    if not entity_id:
        entity_id = event.chat_id

    cas_data = None

    try:
        try:
            entity = await event.client.get_entity(entity_id)
        except Exception as e:
            log.warning(e)
            entity = None
        is_chat = True if isinstance(entity, (Chat, Channel)) else False
        if not is_chat:
            try:
                cas_data = cas_api.get_user_data(user_id=entity.id if entity else int(entity_id))
            except:
                pass
        offenses = cas_api.offenses(cas_data)
        time_banned = cas_api.timeadded(cas_data)
    except Exception as e:
        log.warning(e)

    if not cas_data and not entity:
        await event.edit(msgRep.GIVEN_ENT_INVALID)
        return

    global CAS_USER_IDS
    if exists(CAS_CSV):
        if isCSVoutdated():
            await event.edit(msgRep.AUTO_UPDATE)
            log.info("Auto update CAS CSV data started")
            await casupdater(event, showinfo=False)
        if not CAS_USER_IDS and not updateCASList():
            await event.edit(msgRep.CAS_CHECK_FAIL_ND)
            log.warning("Export CSV format from cas.chat is not valid")
            return
    else:
        log.info("CAS CSV data not available")
        if not cas_data and is_chat:
            await event.edit(msgRep.CAS_CHECK_ND)
            return

    cas_count = 0

    try:
        if isinstance(entity, User):
            firstname = entity.first_name if not entity.deleted else msgRep.DELETED_ACCOUNT
            lastname = entity.last_name  # can be None
            username = entity.username  # can be None
            await event.edit(msgRep.CHECK_USER_ID.format(firstname))
            is_banned = f"[{msgRep.BANNED}](https://api.cas.chat/check?user_id={entity.id})" if cas_api.isbanned(cas_data) else msgRep.NOT_BANNED
            text = f"**{msgRep.USER_HEADER}**\n\n"
            text += f"{msgRep.USER_ID}: `{entity.id}`\n"
            text += f"{msgRep.FIRST_NAME}: {firstname}\n"
            if lastname:
                text += f"{msgRep.LAST_NAME}: {lastname}\n"
            text += f"{msgRep.USERNAME}: @{username}\n\n" if username else "\n"
            text += f"**{msgRep.CAS_DATA}**\n\n"
            text += f"{msgRep.RESULT}: {is_banned}\n"
            if offenses:
                text +=  f"{msgRep.OFFENSES}: `{offenses}`\n"
            if time_banned:
                text +=  f"{msgRep.BANNED_SINCE}: `{time_banned.strftime('%b %d, %Y')} - {time_banned.time()} {time_banned.tzname()}`"
        elif isinstance(entity, (Chat, Channel)):
            await event.edit(msgRep.CHECK_CHAT)
            title = entity.title
            text_users = ""
            async for user in event.client.iter_participants(entity.id):
                if user.id in CAS_USER_IDS:
                    cas_count += 1
                    if user.deleted:
                        text_users += f"\n{cas_count}. {msgRep.DELETED_ACCOUNT} - `{user.id}`"
                    else:
                        if user.username:
                            text_users += f"\n{cas_count}. @{user.username} - `{user.id}`"
                        else:
                            text_users += f"\n{cas_count}. [{user.first_name}](tg://user?id={user.id}) - `{user.id}`"
            if cas_count == 1:
                text = msgRep.USER_DETECTED.format(cas_count, title) + ":\n"
            else:
                text = msgRep.USERS_DETECTED.format(cas_count, title) + ":\n"
            text += text_users
            if not cas_count:
                text = msgRep.NO_USERS.format(title)
        elif not entity and cas_data:
            await event.edit(msgRep.CHECK_USER_ID.format(entity_id))
            is_banned = f"[{msgRep.BANNED}](https://api.cas.chat/check?user_id={entity_id})" if cas_api.isbanned(cas_data) else msgRep.NOT_BANNED
            text = f"**{msgRep.USER_HEADER}**\n\n"
            text += f"{msgRep.USER_ID}: `{entity_id}`\n\n"
            text += f"**{msgRep.CAS_DATA}**\n\n"
            text += f"{msgRep.RESULT}: {is_banned}\n"
            if offenses:
                text +=  f"{msgRep.OFFENSES}: `{offenses}`\n"
            if time_banned:
                text +=  f"{msgRep.BANNED_SINCE}: `{time_banned.strftime('%b %d, %Y')} - {time_banned.time()} {time_banned.tzname()}`"
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
        return
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.CAS_CHECK_FAIL)
        return

    try:
        if cas_count > 35:  # limit list up to 35 users
            await casSendAsFile(event, text)
        else:
            await event.edit(text)
    except MessageTooLongError:
        await casSendAsFile(event, text)

    return

for cmd in ("casupdate", "cascheck"):
    register_cmd_usage(cmd, usageRep.CAS_INTERFACE_USAGE.get(cmd, {}).get("args"), usageRep.CAS_INTERFACE_USAGE.get(cmd, {}).get("usage"))

register_module_desc(descRep.CAS_INTERFACE_DESC)
register_module_info(
    name="CAS Interface",
    authors="nunopenim, prototype74",
    version=VERSION
)
