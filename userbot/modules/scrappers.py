# Copyright 2020-2022 nunopenim @github
# Copyright 2020-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.language_processor import (getBotLangCode,
                                                ScrappersText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon.errors import ChatSendMediaForbiddenError, MessageTooLongError
from telethon.tl.types import (Document, DocumentAttributeAudio,
                               DocumentAttributeFilename)
from datetime import datetime
from currency_converter import CurrencyConverter
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from gtts.tts import gTTSError
from logging import getLogger
from pydub import AudioSegment
from os import remove, rename
from os.path import exists, getmtime, join, dirname
from speech_recognition import (AudioFile, Recognizer, UnknownValueError,
                                RequestError)
from urllib.request import urlopen
from zipfile import BadZipFile, ZipFile
from certifi import where as ca_where

log = getLogger(__name__)
ehandler = EventHandler(log)
TEMP_DL_DIR = getConfig("TEMP_DL_DIR")
CC_CSV_PATH = join(getConfig("USERDATA"), "currency.csv")
DEST_LANG = getBotLangCode()


def build_supported_langs():
    ret_val = ""
    for i in LANGUAGES:
        ret_val += "`{}`: {}\n".format(i, LANGUAGES[i])
    return ret_val


@ehandler.on(command="scrlang", outgoing=True)
async def lang_check(event):
    await event.edit(msgRep.SCRLANG.format(LANGUAGES[DEST_LANG]))
    return


@ehandler.on(command="setlang", hasArgs=True, outgoing=True)
async def set_lang(event):
    global DEST_LANG
    args = event.pattern_match.group(1).split()
    if len(args) != 1:
        await event.edit(msgRep.MULT_ARGS)
        return
    args = args[0]
    if args not in LANGUAGES:
        await event.edit(msgRep.INV_CT_CODE.format(build_supported_langs()))
        return
    DEST_LANG = args
    await event.edit(msgRep.SUCCESS_LANG_CHANGE.format(LANGUAGES[args]))
    return


@ehandler.on(command="trt", hasArgs=True, outgoing=True)
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
        result = translator.translate(text=msg, dest=DEST_LANG, src="auto")
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


@ehandler.on(command="tts", hasArgs=True, outgoing=True)
async def text_to_speech(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        msg = msg.message
    else:
        msg = event.pattern_match.group(1)

    chat = await event.get_chat()

    try:
        tts = gTTS(text=msg, lang=DEST_LANG)
        file_loc = join(TEMP_DL_DIR, "tts.mp3")
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


@ehandler.on(command="stt", outgoing=True)
async def speech_to_text(event):
    """ Note: telethon may borrow a different DC id to download audio """
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
    else:
        await event.edit(msgRep.REPLY_TO_VM)
        return

    filename, file_format = (None,)*2
    voice_note = False

    if msg.media and hasattr(msg.media, "document") and \
       isinstance(msg.media.document, Document) and \
       msg.media.document.mime_type.startswith("audio"):
        for attribute in msg.media.document.attributes:
            if isinstance(attribute, DocumentAttributeAudio):
                if not voice_note:  # set only if not True already
                    voice_note = attribute.voice
            if isinstance(attribute, DocumentAttributeFilename):
                if not file_format:  # set only if none
                    string = attribute.file_name.split(".")
                    file_format = string[-1]
        if not voice_note:
            await event.edit(msgRep.WORKS_WITH_VM_ONLY)
            return
        if not file_format:  # alternative way
            file_format = msg.media.document.mime_type.split("/")[1]
        filename = join(TEMP_DL_DIR, "audio." + file_format)
        await event.edit(msgRep.CONVERT_STT)
        try:
            await msg.download_media(file=filename)
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.FAILED_LOAD_AUDIO)
            return
    else:
        await event.edit(msgRep.REPLY_TO_VM)
        return

    try:
        audio_file = AudioSegment.from_file(filename, file_format)
        audio_wav = join(TEMP_DL_DIR, "audio.wav")
        audio_file.export(audio_wav, "wav")

        r = Recognizer()
        with AudioFile(audio_wav) as source:
            audio = r.record(source)
        result = r.recognize_google(audio)
        text = f"**{msgRep.STT}**\n\n"
        text += f"{msgRep.STT_TEXT}:\n"
        text += f"__{result}__"
        await event.edit(text)
    except UnknownValueError:
        await event.edit(msgRep.STT_NOT_RECOGNIZED)
    except RequestError:
        await event.edit(msgRep.STT_REQ_FAILED)
    except MessageTooLongError:
        await event.edit(msgRep.STT_OUTPUT_TOO_LONG)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRep.UNABLE_TO_STT)

    try:
        remove(filename)
        remove(audio_wav)
    except Exception as e:
        log.warning(f"Unable to delete audio(s): {e}")
    return


def update_currency_data():
    if exists(CC_CSV_PATH):
        file_date = datetime.fromtimestamp(getmtime(CC_CSV_PATH))
        duration = datetime.today() - file_date
        if not duration.days >= 1:  # don't update if file is not a day old
            return

    userdata_dir = getConfig("USERDATA")
    if not userdata_dir:
        log.warning("Userdata directory not available")
        return
    try:
        zipfile = join(userdata_dir, "currency.zip")
        # get latest data from the European Central Bank
        z = urlopen("https://www.ecb.int/stats/eurofxref/eurofxref-hist.zip",
                    cafile=ca_where(), capath=dirname(ca_where()))
        with open(zipfile, "wb") as cur_zip:
            cur_zip.write(z.read())
        cur_zip.close()
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
                    zipObject.extract(filename, userdata_dir)
                    break
            zipObject.close()
        try:
            if exists(CC_CSV_PATH):
                remove(CC_CSV_PATH)
        except Exception as e:
            log.warning(f"Unable to delete old csv file: {e}")
            return
        try:
            rename(join(userdata_dir, csv_filename), CC_CSV_PATH)
            log.info("[CURRENCY] data history successfully updated")
        except Exception as e:
            log.warning(f"Unable to rename csv file: {e}")
    except BadZipFile as bze:
        log.warning(f"Bad zip archive: {bze}")
    except Exception as e:
        log.warning(f"Failed to extract data history: {e}")

    try:
        remove(zipfile)
    except Exception as e:
        log.warning(f"Couldn't remove zip file: {e}")
    return


@ehandler.on(command="currency", hasArgs=True, outgoing=True)
async def cc(event):
    args_from_event = event.pattern_match.group(1).split(" ", 2)
    if len(args_from_event) == 3:
        amount, c_from_iso, c_to_iso = args_from_event
    elif len(args_from_event) == 2:
        amount, c_from_iso = args_from_event
        c_to_iso = "USD"  # default
    else:
        await event.edit(msgRep.NOT_EGH_ARGS)
        return

    try:
        amount = "{:.2f}".format(float(amount.replace(",", ".")))
    except Exception:
        await event.edit(msgRep.INVALID_AMOUNT_FORMAT)
        return

    c_from_iso = c_from_iso.upper()
    c_to_iso = c_to_iso.upper()

    try:
        try:
            update_currency_data()
            c = CurrencyConverter(currency_file=CC_CSV_PATH)
        except Exception as e:
            log.warning(f"Unable to read updated data history: {e}. "
                        "Falling back to default currency data.")
            c = CurrencyConverter()
        if c_from_iso not in c.currencies:
            await event.edit(msgRep.CC_ISO_UNSUPPORTED.format(c_from_iso))
            return
        if c_to_iso not in c.currencies:
            await event.edit(msgRep.CC_ISO_UNSUPPORTED.format(c_to_iso))
            return
        date = c.bounds[c_from_iso]
        result = "{:.2f}".format(c.convert(amount=amount,
                                           currency=c_from_iso,
                                           new_currency=c_to_iso))
        strings = f"**{msgRep.CC_HEADER}**\n\n"
        strings += msgRep.CFROM_CTO.format(c_from_iso, c_to_iso) + "\n"
        strings += f"{amount} {c_from_iso} = {result} {c_to_iso}\n\n"
        strings += f"__{msgRep.CC_LAST_UPDATE}: {date.last_date}__"
        await event.edit(strings)
    except ValueError as ve:
        await event.edit(f"`{msgRep.INVALID_INPUT}: {ve}`")
    except Exception as e:
        log.warning(f"Failed to convert currency: {e}")
        await event.edit(msgRep.UNABLE_TO_CC)
    return


for cmd in ("trt", "tts", "stt", "scrlang", "setlang", "currency"):
    register_cmd_usage(
        cmd,
        usageRep.SCRAPPERS_USAGE.get(cmd, {}).get("args"),
        usageRep.SCRAPPERS_USAGE.get(cmd, {}).get("usage")
    )

register_module_desc(descRep.SCRAPPERS_DESC)
register_module_info(
    name="Scrappers",
    authors="nunopenim, prototype74",
    version=VERSION
)
