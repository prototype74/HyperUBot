# My stuff
from tg_userbot import tgclient
import tg_userbot.include.git_api as git

# Telethon stuff
from telethon.events import NewMessage

UNIVERSE_URL = "nunopenim/module-universe"

# Maybe add just a single command, but multiple arguments?
@tgclient.on(NewMessage(pattern=r"^\.universe$", outgoing=True))
async def universe_checker(msg):
    files = ""
    assets = git.getAssets(git.getReleaseData(git.getData(UNIVERSE_URL), 0))
    for asset in assets:
        assetName = git.getReleaseFileName(asset)
        assetURL = git.getReleaseFileURL(asset)
        files += "[{}]({})".format(assetName, assetURL)
    await msg.edit(files, parse_mode='md')
    return
