# tguserbot stuff
from tg_userbot import HELP_DICT
from tg_userbot import UBOT_LANG
from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import ScrappersText as msgRep, HelpDesignations as helpRep

# Telethon stuff
from telethon.errors import MessageTooLongError

# Misc
from googletrans import Translator, LANGUAGES


@watcher(pattern=r"^\.trt(?: |$)(.*)", outgoing=True)
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
    except MessageTooLongError as mtle:
        print("MessageTooLongError:", mtle)
        await event.edit(msgRep.MSG_TOO_LONG)
    except Exception as e:
        print("Exception:", e)
        if event.reply_to_msg_id:
            await event.edit(msgRep.FAIL_TRANS_MSG)
        else:
            await event.edit(msgRep.FAIL_TRANS_TEXT)

    return


HELP_DICT.update({"scrappers": helpRep.SCRAPPERS_HELP})
