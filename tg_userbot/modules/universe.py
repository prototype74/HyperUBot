# My stuff
from tg_userbot import tgclient
import tg_userbot.include.git_api as git

# Telethon stuff
from telethon.events import NewMessage

UNIVERSE_URL = "nunopenim/module-universe"
UNIVERSE_NAME = "modules-universe"
MODULE_LIST = None # the thing that should get updated if you do .pkg update

def list_updater():
    global MODULE_LIST
    MODULE_LIST = {}
    assets = git.getAssets(git.getReleaseData(git.getData(UNIVERSE_URL), 0))
    for asset in assets:
        assetName = git.getReleaseFileName(asset)
        assetURL = git.getReleaseFileURL(asset)
        assetSize = git.getSize(asset)
        MODULE_LIST.update({'name': assetName, 'url': assetURL, 'size': assetSize})
    return MODULE_LIST

# Maybe add just a single command, but multiple arguments?
@tgclient.on(NewMessage(pattern=r"^\.pkg(?: |$)(.*)", outgoing=True))
async def universe_checker(msg):
    cmd_args = msg.pattern_match.group(1).split(" ", 1)
    if cmd_args[0] == "update":
        list_updater()
        await msg.edit("Modules list has been updated from the universe **{}**".format(UNIVERSE_NAME))
        return
    elif cmd_args[0] == "list":
        files = "Files in **{}**:\n\n".format(UNIVERSE_NAME)
        count = 1
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            files += "`There are no modules in the package list!`"
        else:
            for m in MODULE_LIST:
                files += "{}. [{}]({}) - {} Bytes\n".format(count, m['name'], m['url'], m['size'])
                count += 1
        await msg.edit(files, parse_mode='md')
        return
    else:
        await msg.edit("Invalid argument! Make sure it is either **update** or **list**!")
        return
