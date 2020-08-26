# My stuff
from tg_userbot import tgclient
from tg_userbot.include.language_processor import StickersText as msgRep

# Telethon stuff
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.events import NewMessage
from telethon.tl.types import DocumentAttributeSticker, InputStickerSetID

@tgclient.on(NewMessage(pattern=r"^\.stkrinfo$", outgoing=True))
async def get_pack_info(event):
    if not event.is_reply:
        await event.edit(msgRep.FAIL_FETCH_INFO)
        return
    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        await event.edit(msgRep.NOT_STICKER)
        return
    try:
        stickerset_attr = rep_msg.document.attributes[1]
        await event.edit(msgRep.FETCHING_STICKER_DETAILS)
    except BaseException:
        await event.edit(msgRep.NOT_STICKER)
        return
    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        await event.edit(msgRep.NOT_STICKER)
        return
    get_stickerset = await tgclient(GetStickerSetRequest(InputStickerSetID(id=stickerset_attr.stickerset.id, access_hash=stickerset_attr.stickerset.access_hash)))
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)
    await event.edit(msgRep.STICKER_INFO_OUTPUT.format(get_stickerset.set.title, get_stickerset.set.short_name, get_stickerset.set.official, get_stickerset.set.archived, len(get_stickerset.packs), ' '.join(pack_emojis)))

