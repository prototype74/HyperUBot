# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# tguserbot stuff
from userbot import tgclient, MODULE_DESC, MODULE_DICT, TEMP_DL_DIR, UBOT_LANG
from userbot.include.language_processor import (ScrappersText as msgRep, ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)

# Telethon stuff
from telethon.errors import ChatSendMediaForbiddenError, MessageTooLongError
from telethon.events import NewMessage

# Misc
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from gtts.tts import gTTSError
from logging import getLogger
from os import remove
from os.path import basename


log = getLogger(__name__)


@tgclient.on(NewMessage(pattern=r"^\.trt(?: |$)(.*)", outgoing=True))
async def translate(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        msg = msg.message
    else:
        msg = event.pattern_match.group(1)

    if not msg:
        await event.edit(msgRep.NO_TEXT_OR_MSG)
        return

    await event.edit(msgRep.TRANSLATING)

    try:
        translator = Translator()
        result = translator.translate(text=msg, dest=UBOT_LANG, src="auto")
        if result.src == result.dest:
            await event.edit(msgRep.SAME_SRC_TARGET_LANG)
            return
        src_lang = LANGUAGES.get(result.src, "Unknown")
        target_lang = LANGUAGES.get(result.dest, "Unknown")

        text = f"{msgRep.DETECTED_LANG}: <b>{src_lang.title()}</b>\n"
        text += f"{msgRep.TARGET_LANG}: <b>{target_lang.title()}</b>\n\n"
        if not event.reply_to_msg_id:
            text += f"<b>{msgRep.ORG_TEXT}:</b>\n"
            text += msg + "\n\n"
        text += f"<b>{msgRep.TRANS_TEXT}:</b>\n"
        text += result.text
        await event.edit(text, parse_mode="html")
    except MessageTooLongError:
        await event.edit(msgRep.MSG_TOO_LONG)
    except Exception as e:
        log.warning(e)
        if event.reply_to_msg_id:
            await event.edit(msgRep.FAIL_TRANS_MSG)
        else:
            await event.edit(msgRep.FAIL_TRANS_TEXT)

    return


@tgclient.on(NewMessage(pattern=r"^\.tts(?: |$)(.*)", outgoing=True))
async def text_to_speech(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        msg = msg.message
    else:
        msg = event.pattern_match.group(1)

    chat = await event.get_chat()

    try:
        tts = gTTS(text=msg, lang=UBOT_LANG)
        file_loc = TEMP_DL_DIR + "tts.mp3"
        tts.save(file_loc)
        await event.client.send_file(chat.id, file=file_loc, voice_note=True)
        await event.delete()
        remove(file_loc)
    except ChatSendMediaForbiddenError:
        await event.edit(msgRep.MEDIA_FORBIDDEN)
    except AssertionError as ae:
        log.warning(ae)
        if not msg:
            await event.edit(msgRep.NO_TEXT_TTS)
        else:
            await event.edit(msgRep.FAIL_TTS)
    except gTTSError as ge:
        log.error(ge)
        await event.edit(msgRep.FAIL_API_REQ)
    except ValueError as ve:
        log.warning(ve)
        await event.edit(msgRep.INVALID_LANG_CODE)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.FAIL_TTS)

    return


MODULE_DESC.update({basename(__file__)[:-3]: descRep.SCRAPPERS_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.SCRAPPERS_USAGE})
