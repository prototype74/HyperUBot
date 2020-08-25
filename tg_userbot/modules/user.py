# My Stuff
from tg_userbot.include.watcher import watcher
from tg_userbot import BOTLOG, BOTLOG_CHATID, bot, HELP_DICT
from tg_userbot.include.language_processor import UserText as msgRep, HelpDesignations as helpRep
from tg_userbot.include.aux_funcs import fetch_user

# Telethon stuff
from telethon.tl.types import User, Chat, Channel
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.utils import get_input_location

# Misc Imports
from asyncio import sleep

@watcher(outgoing=True, pattern=r"^\.kickme$")
async def kickme(leave):
    await leave.edit(msgRep.LEAVING)
    await sleep(0.1) #wait to avoid bad stuff
    await leave.client.kick_participant(leave.chat_id, 'me')
    if BOTLOG:
        await leave.client.send_message(BOTLOG_CHATID, msgRep.KICKME_LOG.format(leave.chat.title, leave.chat.id))
    return

@watcher(outgoing=True, pattern=r"^\.stats$")
async def stats(event):
    result = ""
    users = 0
    groups = 0
    super_groups = 0
    channels = 0
    bots = 0
    await event.edit(msgRep.STATS_PROCESSING)
    dialogs = await bot.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                bots += 1
            else:
                users += 1
        elif isinstance(currrent_entity, Chat):
            groups += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                channels += 1
            else:
                super_groups += 1
        else: # Should never reach this!
            print(d + ": Unrecognized chat type")
    result += msgRep.STATS_USERS.format(users)
    result += msgRep.STATS_BOTS.format(bots)
    result += msgRep.STATS_SUPER_GROUPS.format(super_groups)
    result += msgRep.STATS_GROUPS.format(groups)
    result += msgRep.STATS_CHANNELS.format(channels)
    await event.edit(result)
    return

@watcher(pattern=r"^\.info(?: |$)(.*)", outgoing=True)
async def info(event):  # .info command
    await event.edit(msgRep.FETCH_INFO)

    full_user_obj = await fetch_user(event=event, full_user=True)
    if not full_user_obj:  #  fetch_user() will return an error msg if something failed
        return

    caption = await fetch_info(full_user_obj, event)

    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.edit(f"`Failed to fetch user info: {e}`")

    return

async def fetch_info(replied_user, event):
    replied_user_profile_photos = await event.client(GetUserPhotosRequest(user_id=replied_user.user.id, offset=42, max_id=0, limit=80))
    replied_user_profile_photos_count = 0
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    user_deleted = replied_user.user.deleted
    first_name = replied_user.user.first_name if not user_deleted else "Deleted Account"
    last_name = replied_user.user.last_name if replied_user.user.last_name else None
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = msgRep.UNKNOWN
        location = str(e)
    common_chat = str(replied_user.common_chats_count)
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
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
    if dc_id:
        caption += f"{msgRep.DCID}: {dc_id}\n"
    if replied_user_profile_photos_count:
        caption += f"{msgRep.PROF_PIC_COUNT}: {replied_user_profile_photos_count}\n"
    if not user_deleted:
        caption += f"{msgRep.PROF_LINK}: {profile_link}\n"
    caption += f"{msgRep.ISBOT}: {is_bot}\n"
    caption += f"{msgRep.ISRESTRICTED}: {restricted}\n"
    caption += f"{msgRep.ISVERIFIED}: {verified}\n\n"
    caption += f"{msgRep.BIO}:\n<code>{user_bio}</code>\n\n"
    caption += f"{msgRep.COMMON}: {common_chat}"

    return caption

HELP_DICT.update({"user":helpRep.USER_HELP})
