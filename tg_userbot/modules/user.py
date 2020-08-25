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
    if event.fwd_from:
        return
    await event.edit(msgRep.FETCH_INFO)
    replied_user = await fetch_user(event, full_user=True)
    caption = await fetch_info(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(event.chat_id, caption=caption, link_preview=False, force_document=False, reply_to=message_id_to_reply, parse_mode="html")
        await event.delete()
    except TypeError:
        await event.edit(caption, parse_mode="html")

async def fetch_info(replied_user, event):
    replied_user_profile_photos = await event.client(GetUserPhotosRequest(user_id=replied_user.user.id, offset=42, max_id=0, limit=80))
    replied_user_profile_photos_count = msgRep.NO_PROF_PIC
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError as e:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
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
    first_name = first_name.replace("\u2060", "") if first_name else ("(N/A)")
    last_name = last_name.replace("\u2060", "") if last_name else ("(N/A)")
    username = "@{}".format(username) if username else ("(N/A)")
    user_bio = msgRep.USR_NO_BIO if not user_bio else user_bio
    caption = msgRep.USR_INFO
    caption += msgRep.FIRST_NAME.format(first_name)
    caption += msgRep.LAST_NAME.format(last_name)
    caption += msgRep.USERNAME.format(username)
    caption += msgRep.DCID.format(dc_id)
    caption += msgRep.PROF_PIC_COUNT.format(replied_user_profile_photos_count)
    caption += msgRep.PROF_LINK
    caption += f"<a href=\"tg://user?id={user_id}\">{first_name}</a>\n"
    caption += msgRep.ISBOT.format(is_bot)
    caption += msgRep.ISRESTRICTED.format(restricted)
    caption += msgRep.ISVERIFIED.format(verified)
    caption += msgRep.USR_ID.format(user_id)
    caption += msgRep.BIO.format(user_bio)
    caption += msgRep.COMMON.format(common_chat)
    return caption

HELP_DICT.update({"user":helpRep.USER_HELP})
