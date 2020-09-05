# My stuff
from tg_userbot import tgclient
import tg_userbot.include.git_api as git

# Telethon stuff
from telethon.events import NewMessage

UNIVERSE_URL = "nunopenim/module-universe"
UNIVERSE_NAME = "modules-universe"

# Maybe add just a single command, but multiple arguments?
@tgclient.on(NewMessage(pattern=r"^\.universe$", outgoing=True))
async def universe_checker(msg):
    files = "Files in **{}**:\n\n".format(UNIVERSE_NAME)
    count = 1
    assets = git.getAssets(git.getReleaseData(git.getData(UNIVERSE_URL), 0))
    for asset in assets:
        assetName = git.getReleaseFileName(asset)
        assetURL = git.getReleaseFileURL(asset)
        assetSize = git.getSize(asset)
        files += "{}. [{}]({}) - {} MB\n".format(count, assetName, assetURL, assetSize)
        count += 1
    await msg.edit(files, parse_mode='md')
    return
