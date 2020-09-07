# My stuff
from tg_userbot import tgclient
import tg_userbot.include.git_api as git

# Telethon stuff
from telethon.events import NewMessage

# Misc stuff
import requests

UNIVERSE_URL = "nunopenim/module-universe"
UNIVERSE_NAME = "modules-universe"
MODULE_LIST = None # the thing that should get updated if you do .pkg update

def list_updater():
    global MODULE_LIST
    MODULE_LIST = []
    assets = git.getAssets(git.getReleaseData(git.getData(UNIVERSE_URL), 0))
    for asset in assets:
        assetName = git.getReleaseFileName(asset)
        assetURL = git.getReleaseFileURL(asset)
        assetSize = git.getSize(asset)
        MODULE_LIST.append({"name": assetName, "url": assetURL, "size": assetSize})
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
                files += "{}. [{}]({}) - {} Bytes\n".format(count, m["name"], m["url"], m["size"])
                count += 1
        await msg.edit(files, parse_mode='md')
        return
    elif cmd_args[0] == "install":
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            await msg.edit("The modules list is empty! Please run `.pkg update` first!")
            return
        if len(cmd_args) == 1:
            await msg.edit("`No specified package to install! Command halted!`")
            return
        del(cmd_args[0])
        fileURLs = []
        for i in cmd_args:
            if not i.endswith(".py"):
                i += ".py"
            for j in MODULE_LIST:
                if j['name'] == i:
                    fileURLs.append({'filename': i, 'link': j['url']})
                else:
                    await msg.edit("No module named `{}` was found in the release repo! Aborting!".format(i))
                    return
        # print(fileURLs)
        for i in fileURLs:
            request = requests.get(i['link'], allow_redirects=True)
            open('tg_userbot/modules/' + i['filename'], 'wb').write(request.content)
        await msg.edit("Done! Reboot userbot!")
        return
    else:
        await msg.edit("Invalid argument! Make sure it is **update**, **list** or **install**!")
        return
