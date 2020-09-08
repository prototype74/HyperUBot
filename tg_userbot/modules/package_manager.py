# My stuff
from tg_userbot import tgclient, USER_MODULES, COMMUNITY_REPOS
import tg_userbot.include.git_api as git

# Telethon stuff
from telethon.events import NewMessage

# Misc stuff
import requests
import os

UNIVERSE_URL = "nunopenim/module-universe"
UNIVERSE_NAME = "modules-universe"
USER_MODULES_DIR = "./tg_userbot/modules_user/"
MODULE_LIST = None # the thing that should get updated if you do .pkg update

def list_updater():
    global MODULE_LIST
    MODULE_LIST = []
    assets = git.getAssets(git.getReleaseData(git.getData(UNIVERSE_URL), 0))
    for asset in assets:
        assetName = git.getReleaseFileName(asset)
        assetURL = git.getReleaseFileURL(asset)
        assetSize = git.getSize(asset)
        MODULE_LIST.append({"repo": UNIVERSE_NAME, "name": assetName, "url": assetURL, "size": assetSize})
    for repoURL in COMMUNITY_REPOS:
        repoName = git.getReleaseName(git.getReleaseData(git.getData(repoURL), 0))
        assets = git.getAssets(git.getReleaseData(git.getData(repoURL), 0))
        for asset in assets:
            assetName = git.getReleaseFileName(asset)
            assetURL = git.getReleaseFileURL(asset)
            assetSize = git.getSize(asset)
            if assetName in MODULE_LIST:
                MODULE_LIST.remove(MODULE_LIST["name"] == assetName)
            MODULE_LIST.append({"repo": repoName, "name": assetName, "url": assetURL, "size": assetSize})
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
        files = ""
        count = 1
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            files += "`There are no modules in the package list!`"
        else:
            oldName = ""
            for m in MODULE_LIST:
                if not (m["repo"] == oldName):
                    files += "\n\n Files in {}".format(m["repo"])
                    oldName = m["repo"]
                    count = 1
                files += "{}. [{}]({}) - {} Bytes\n".format(count, m["name"], m["url"], m["size"])
                count += 1
        await msg.edit(files, parse_mode='md')
        return
    elif cmd_args[0] == "install":
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            await msg.edit("The modules list is empty! Please run `.pkg update` first!")
            return
        if len(cmd_args) == 1:
            await msg.edit("`No specified package to install! Process halted!`")
            return
        del(cmd_args[0])
        fileURLs = []
        for i in cmd_args:
            found = False
            if not i.endswith(".py"):
                i += ".py"
            for j in MODULE_LIST:
                if j['name'] == i:
                    fileURLs.append({'filename': i, 'link': j['url']})
                    found = True
                    break
            if not found:
                await msg.edit("No module named `{}` was found in the release repo! Aborting!".format(i))
                return
        # print(fileURLs)
        for i in fileURLs:
            request = requests.get(i['link'], allow_redirects=True)
            open(USER_MODULES_DIR + i['filename'], 'wb').write(request.content)
        await msg.edit("Done! Reboot userbot!")
        return
    elif cmd_args[0] == "uninstall":
        if len(USER_MODULES) == 0:
            await msg.edit("No uninstallable modules present! Process halted!")
            return
        if len(cmd_args) == 1:
            await msg.edit("Please specify a module name, I cannot uninstall __nothing__!")
            return
        if len(cmd_args) > 2:
            await msg.edit("For safety reasons, you can only uninstall one module at a time, please give a single name!")
            return
        modName = cmd_args[1].lower()
        if modName not in USER_MODULES:
            await msg.edit("`{}` is not a valid Userspace module name! Process halted!")
            return
        await msg.edit("`Uninstalling {}...`".format(modName))
        os.remove(USER_MODULES_DIR + modName + ".py")
        await msg.edit("Done! Reboot userbot!")
        return
    else:
        await msg.edit("Invalid argument! Make sure it is **update**, **list**, **install** or **uninstall**!")
        return
