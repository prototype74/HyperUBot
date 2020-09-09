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
from datetime import datetime
from currency_converter import CurrencyConverter
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from gtts.tts import gTTSError
from logging import getLogger
from os import remove, rename
from os.path import basename, exists, getmtime
from urllib.request import urlretrieve
from zipfile import ZipFile


log = getLogger(__name__)
CC_CSV_PATH = TEMP_DL_DIR + "currency.csv"


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


def update_currency_data():
    if exists(CC_CSV_PATH):
        file_date = datetime.fromtimestamp(getmtime(CC_CSV_PATH))
        duration = datetime.today() - file_date
        if not duration.days >= 1:  # don't update if file is not a day old
            return

    try:
        zipfile = TEMP_DL_DIR + "currency.zip"
        # get latest data from the European Central Bank
        data_history = urlretrieve("http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip", zipfile)
    except Exception as e:
        log.warning(f"Unable to download updated data history: {e}")
        return

    try:
        csv_filename = None
        with ZipFile(zipfile, "r") as zipObject:
            contents = zipObject.namelist()
            for filename in contents:
                if filename.endswith(".csv"):
                    csv_filename = filename
                    zipObject.extract(filename, TEMP_DL_DIR)
                    break
        try:
            rename(TEMP_DL_DIR + filename, CC_CSV_PATH)
            log.info("[CURRENCY] data history successfully updated")
        except Exception as e:
            log.warning(f"Unable to rename csv file: {e}")
    except Exception as e:
        log.warning(f"Failed to extract data history: {e}")

    try:
        remove(zipfile)
    except Exception as e:
        log.warning(f"Couldn't remove zip file: {e}")

    return


@tgclient.on(NewMessage(pattern=r"^\.currency(?: |$)(.*)", outgoing=True))
async def cc(event):
    args_from_event = event.pattern_match.group(1).split(" ", 2)
    if len(args_from_event) == 3:
        amount, c_from_iso, c_to_iso = args_from_event
    elif len(args_from_event) == 2:
        amount, c_from_iso = args_from_event
        c_to_iso = "USD"  # default
    else:
        await event.edit("Not enough arguments given.")
        return

    try:
        amount = round(float(amount.replace(",", ".")), 2)
    except:
        await event.edit("`Invalid amount format`")
        return

    c_from_iso = c_from_iso.upper()
    c_to_iso = c_to_iso.upper()

    try:
        try:
            update_currency_data()
            c = CurrencyConverter(currency_file=CC_CSV_PATH)
        except Exception as e:
            log.warning(f"Unable to read updated data history: {e}. Falling back to default currency data.")
            c = CurrencyConverter()
        if not c_from_iso in c.currencies:
            await event.edit(f"`'{c_from_iso}' unsupported country ISO currency`")
            return
        if not c_to_iso in c.currencies:
            await event.edit(f"`'{c_to_iso}' unsupported country ISO currency`")
            return
        result = round(c.convert(amount=amount, currency=c_from_iso, new_currency=c_to_iso), 2)
        strings = "**Currency converter**\n\n"
        strings += f"**{c_from_iso}** to **{c_to_iso}**\n"
        strings += f"{amount} {c_from_iso} = {result} {c_to_iso}"
        await event.edit(strings)
    except ValueError as e:
        await event.edit(f"`Invalid input: {e}`")

    return


MODULE_DESC.update({basename(__file__)[:-3]: descRep.SCRAPPERS_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.SCRAPPERS_USAGE})
