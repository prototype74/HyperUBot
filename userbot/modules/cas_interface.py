# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient, MODULE_DESC, MODULE_DICT
import userbot.include.cas_api as cas_api
from userbot.include.language_processor import (CasIntText as msgRep, ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.include.aux_funcs import fetch_user as get_user

# Telethon stuff
from telethon.events import NewMessage
from telethon.errors import ChatAdminRequiredError

# Misc
from logging import getLogger
from os.path import basename

log = getLogger(__name__)

@tgclient.on(NewMessage(pattern=r"^\.cascheck(?: |$)(.*)", outgoing=True))
async def caschecker(event):
    if event.fwd_from:
        return
    user_analysis = await get_user(event)
    if user_analysis is None:
        text = msgRep.FAIL
        await event.edit(text, parse_mode="html")
        return
    text = msgRep.USER_HEADER
    text += msgRep.USER_ID + str(user_analysis.id) + "\n"
    if user_analysis.first_name:
        text += msgRep.FIRST_NAME + str(user_analysis.first_name) + "\n"
    if user_analysis.last_name:
        text += msgRep.LAST_NAME + str(user_analysis.last_name) + "\n"
    if user_analysis.username:
        text += msgRep.USERNAME + str(user_analysis.username) + "\n"
    text += msgRep.CAS_DATA
    result = cas_api.banchecker(user_analysis.id)
    text += msgRep.RESULT + str(result) + "\n"
    if result:
        parsing = cas_api.offenses(user_analysis.id)
        if parsing:
            text += msgRep.OFFENSES
            text += str(parsing)
            text += "\n"
        parsing = cas_api.timeadded(user_analysis.id)
        if parsing:
            parseArray = str(parsing).split(", ")
            text += msgRep.DAY_ADDED
            text += str(parseArray[1])
            text += msgRep.TIME_ADDED
            text += str(parseArray[0])
            text += msgRep.UTC_INFO
    await event.edit(text, parse_mode="html")
    return

@tgclient.on(NewMessage(pattern=r"^\.groupcheck$", outgoing=True))
async def groupchecker(cas):
    text = ""
    chat = cas.chat_id
    try:
        info = await cas.client.get_entity(chat)
    except (TypeError, ValueError) as err:
        await cas.edit(str(err))
        return
    try:
        cas_count, members_count = (0,) * 2
        banned_users = ""
        async for user in cas.client.iter_participants(info.id):
            if cas_api.banchecker(user.id):
                cas_count += 1
                if not user.deleted:
                    banned_users += f"{user.first_name} {user.id}\n"
                else:
                    banned_users += f"Deleted Account {user.id}\n"
            members_count += 1
        text = msgRep.USERS_DETECTED.format(cas_count, members_count)
        text += banned_users
        if not cas_count:
            text = msgRep.NO_USRS
    except ChatAdminRequiredError:
        await cas.edit(msgRep.NO_ADM)
        return
    except BaseException as be:
        log.warning(be)
        await cas.edit(msgRep.CAS_CHECK_FAIL)
        return
    await cas.edit(text)
    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.CAS_INTERFACE_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.CAS_INTERFACE_USAGE})
