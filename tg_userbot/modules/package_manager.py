# My stuff
from tg_userbot import tgclient, USER_MODULES, COMMUNITY_REPOS, LOGGING
import tg_userbot.include.git_api as git
from tg_userbot.include.aux_funcs import event_log
from tg_userbot.include.language_processor import PackageManagerText as msgRep

# Telethon stuff
from telethon.events import NewMessage

# Misc stuff
import requests
import os
import time
import sys

UNIVERSE_URL = "nunopenim/module-universe"
UNIVERSE_NAME = "modules-universe"
USER_MODULES_DIR = "./tg_userbot/modules_user/"
MODULE_LIST = None # the thing that should get updated if you do .pkg update
REPOS_NAMES = []

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
        if repoName not in REPOS_NAMES:
            REPOS_NAMES.append(repoName)
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
        repos = UNIVERSE_NAME
        for repo in REPOS_NAMES:
            repos += ", " + repo
        await msg.edit(msgRep.UPDATE_COMPLETE.format(repos))
        return
    elif cmd_args[0] == "list":
        files = ""
        count = 1
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            files += msgRep.EMPTY_LIST
        else:
            oldName = ""
            for m in MODULE_LIST:
                if not (m["repo"] == oldName):
                    files += msgRep.FILES_IN.format(m["repo"])
                    oldName = m["repo"]
                    count = 1
                files += msgRep.FILE_DSC.format(count, m["name"], m["url"], m["size"])
                count += 1
        await msg.edit(files, parse_mode='md')
        return
    elif cmd_args[0] == "install":
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            await msg.edit(msgRep.EMPTY_LIST)
            return
        if len(cmd_args) == 1:
            await msg.edit(msgRep.NO_PKG)
            return
        del(cmd_args[0])
        fileURLs = []
        modules_installed = []
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
                await msg.edit(msgRep.MOD_NOT_FOUND_INSTALL.format(i))
                return

        for i in fileURLs:
            request = requests.get(i['link'], allow_redirects=True)
            open(USER_MODULES_DIR + i['filename'], 'wb').write(request.content)
            modules_installed.append(i['filename'].strip(".py"))
        md_installed_string = ""
        for md in modules_installed:
            if md_installed_string == "":
                md_installed_string += md
            else:
                md_installed_string += ", " + md
        await msg.edit(msgRep.DONE_RBT)
        time.sleep(1)  # just so we can actually see a message
        if LOGGING:
            await event_log(msg, "MODULE INSTALL", custom_text=msgRep.INSTALL_LOG.format(md_installed_string))
        await msg.edit(msgRep.REBOOT_DONE_INS.format(md_installed_string))
        args = [sys.executable, "-m", "tg_userbot"]
        os.execle(sys.executable, *args, os.environ)
        await msg.client.disconnect()
        return
    elif cmd_args[0] == "uninstall":
        if len(USER_MODULES) == 0:
            await msg.edit(msgRep.NO_UNINSTALL_MODULES)
            return
        if len(cmd_args) == 1:
            await msg.edit(msgRep.NO_UN_NAME)
            return
        if len(cmd_args) > 2:
            await msg.edit(msgRep.MULTIPLE_NAMES)
            return
        modName = cmd_args[1].lower()
        if modName not in USER_MODULES:
            await msg.edit(msgRep.NOT_IN_USERSPACE.format(modName))
            return
        await msg.edit(msgRep.UNINSTALLING.format(modName))
        os.remove(USER_MODULES_DIR + modName + ".py")
        await msg.edit(msgRep.DONE_RBT)
        time.sleep(1)  # just so we can actually see a message
        if LOGGING:
            await event_log(msg, "MODULE UNINSTALL", custom_text=msgRep.UNINSTALL_LOG.format(modName))
        await msg.edit(msgRep.REBOOT_DONE_UNINS)
        args = [sys.executable, "-m", "tg_userbot"]
        os.execle(sys.executable, *args, os.environ)
        await msg.client.disconnect()
        return
    else:
        await msg.edit(msgRep.INVALID_ARG)
        return
