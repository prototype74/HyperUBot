# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License
#
# This module is powered by Combot Anti-Spam (CAS) system (https://cas.chat)

from userbot import tgclient, MODULE_DESC, MODULE_DICT, TEMP_DL_DIR
import userbot.include.cas_api as cas_api
from userbot.include.language_processor import CasIntText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from telethon.events import NewMessage
from telethon.errors import ChatAdminRequiredError, MessageTooLongError, ChatSendMediaForbiddenError
from telethon.tl.types import User, Chat, Channel
from datetime import datetime
from logging import getLogger
from os import remove
from os.path import basename, exists, getmtime
from requests import get, ConnectionError, Timeout

log = getLogger(__name__)
CAS_CSV = TEMP_DL_DIR + "export.csv"
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
        filename, success = createCASFile(input_text, TEMP_DL_DIR + "caslist.txt")
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
    if duration.days >= 1:
        return True
    else:
        return False

async def casupdater(event, showinfo: bool):
    if showinfo:
        await event.edit(msgRep.UPDATER_CONNECTING)

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
        log.warning(t)
        await event.edit(msgRep.TIMEOUT)
    except Exception as e:
        log.error(e)
        await event.edit(msgRep.UPDATE_FAILED)

    return

@tgclient.on(NewMessage(pattern=r"^\.casupdate$", outgoing=True))
async def casupdate(event):
    log.info("Manual CAS CSV data update started")
    await casupdater(event, showinfo=True)
    return

@tgclient.on(NewMessage(pattern=r"^\.cascheck(?: |$)(.*)", outgoing=True))
async def cascheck(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        entity_id = msg.from_id
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
        await event.edit(msgRep.CAS_CHECK_ND)
        log.info("CAS CSV data not available")
        return

    cas_count = 0
    await event.edit(msgRep.PROCESSING)

    try:
        if isinstance(entity, User):
            firstname = entity.first_name if not entity.deleted else msgRep.DELETED_ACCOUNT
            lastname = entity.last_name  # can be None
            username = entity.username  # can be None
            text = f"**{msgRep.USER_HEADER}**\n\n"
            text += f"{msgRep.USER_ID}: `{entity.id}`\n"
            text += f"{msgRep.FIRST_NAME}: {firstname}\n"
            if lastname:
                text += f"{msgRep.LAST_NAME}: {lastname}\n"
            text += f"{msgRep.USERNAME}: @{username}\n\n" if username else "\n"
            text += f"**{msgRep.CAS_DATA}**\n\n"
            text += f"{msgRep.RESULT}: {cas_api.isbanned(cas_data)}\n"
            if offenses:
                text +=  f"{msgRep.OFFENSES}: `{offenses}`\n"
            if time_banned:
                text +=  f"{msgRep.BANNED_SINCE}: `{time_banned.strftime('%b %d, %Y')} - {time_banned.time()} {time_banned.tzname()}`"
        elif isinstance(entity, (Chat, Channel)):
            title = entity.title if entity.title else "this chat"
            text_users = ""
            async for user in event.client.iter_participants(entity.id):
                if user.id in CAS_USER_IDS:
                    cas_count += 1
                    if user.deleted:
                        text_users += f"\n{cas_count}. Deleted Account - `{user.id}`"
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
            text = f"**{msgRep.USER_HEADER}**\n\n"
            text += f"{msgRep.USER_ID}: `{entity_id}`\n\n"
            text += f"**{msgRep.CAS_DATA}**\n\n"
            text += f"{msgRep.RESULT}: {cas_api.isbanned(cas_data)}\n"
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

MODULE_DESC.update({basename(__file__)[:-3]: descRep.CAS_INTERFACE_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.CAS_INTERFACE_USAGE})
