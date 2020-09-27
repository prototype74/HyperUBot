# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, USER_MODULES, COMMUNITY_REPOS, LOGGING, MODULE_DESC, MODULE_DICT, OS
import userbot.include.git_api as git
from userbot.include.aux_funcs import event_log, sizeStrMaker
from userbot.include.language_processor import PackageManagerText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
from telethon.events import NewMessage
import requests
import os
import time
import sys
from logging import getLogger
from os.path import basename

log = getLogger(__name__)

if OS and OS.startswith("win"):
    USER_MODULES_DIR = ".\\userbot\\modules_user\\"
else:
    USER_MODULES_DIR = "./userbot/modules_user/"

if " " not in sys.executable:
    EXECUTABLE = sys.executable
else:
    EXECUTABLE = '"' + sys.executable + '"'

PACKAGELIST = "./userbot/package_lists.hbot"
UNIVERSE_URL = "nunopenim/module-universe"
UNIVERSE_NAME = "modules-universe"

def write_list():
    global MODULE_LIST
    if os.path.exists(PACKAGELIST):
        os.remove(PACKAGELIST)
    file = open(PACKAGELIST, "w+")
    for mod in MODULE_LIST:
        str_to_write = mod["repo"] + "|" + mod["name"] + "|" + mod["url"] + "|" + str(mod["size"]) + "\n"
        file.write(str_to_write)
    file.close()

def read_list():
    global MODULE_LIST
    MODULE_LIST = []
    if os.path.exists(PACKAGELIST):
        file = open(PACKAGELIST, "r")
        lines = file.readlines()
        for line in lines:
            params = line.split("|")
            MODULE_LIST.append({"repo": params[0], "name": params[1], "url": params[2], "size": int(params[3])})
    return MODULE_LIST

MODULE_LIST = read_list()
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
        repoName = git.getReleaseTag(git.getReleaseData(git.getData(repoURL), 0))
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

@tgclient.on(NewMessage(pattern=r"^\.pkg(?: |$)(.*)", outgoing=True))
async def universe_checker(msg):
    cmd_args = msg.pattern_match.group(1).split(" ", 1)
    if cmd_args[0].lower() == "update":
        list_updater()
        write_list()
        repos = UNIVERSE_NAME
        for repo in REPOS_NAMES:
            repos += ", " + repo
        await msg.edit(msgRep.UPDATE_COMPLETE.format(repos))
        return
    elif cmd_args[0].lower() == "list":
        files = msgRep.INSTALLED
        count = 1
        for item in USER_MODULES:
            files += str(count) + ". " + item + "\n"
            count += 1
        if len(USER_MODULES) == 0:
            files += "__No modules installed in userspace__\n"
        count = 1
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            files += msgRep.EMPTY_LIST
        else:
            mdInstalled = False
            oldName = ""
            for m in MODULE_LIST:
                if not (m["repo"] == oldName):
                    files += msgRep.FILES_IN.format(m["repo"])
                    oldName = m["repo"]
                    count = 1
                size = sizeStrMaker(int(m["size"]))
                mdName = m["name"].split(".py")[0]
                if mdName in USER_MODULES:
                    mdName += "*"
                    mdInstalled = True
                files += msgRep.FILE_DSC.format(count, mdName, m["url"], size)
                count += 1
            if mdInstalled:
                files += msgRep.ALREADY_PRESENT
        await msg.edit(files, parse_mode='md')
        return
    elif cmd_args[0].lower() == "install":
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            await msg.edit(msgRep.EMPTY_LIST)
            return
        if len(cmd_args) == 1:
            await msg.edit(msgRep.NO_PKG)
            return
        del(cmd_args[0])
        fileURLs = []
        modules_installed = []
        cmd_args = cmd_args[0].split(" ")
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
            if os.path.exists(USER_MODULES_DIR + i['filename']): # We remove first, in case exists for updates
                os.remove(USER_MODULES_DIR + i['filename'])
            open(USER_MODULES_DIR + i['filename'], 'wb').write(request.content)
            modules_installed.append(i['filename'])
            log.info(f"Module '{i['filename'][:-3]}' has been installed to userspace")
        md_installed_string = ""
        for md in modules_installed:
            if md_installed_string == "":
                md_installed_string += md
            else:
                md_installed_string += ", " + md
        log.info("Rebooting userbot...")
        await msg.edit(msgRep.DONE_RBT)
        time.sleep(1)  # just so we can actually see a message
        if LOGGING:
            await event_log(msg, "MODULE INSTALL", custom_text=msgRep.INSTALL_LOG.format(md_installed_string))
        await msg.edit(msgRep.REBOOT_DONE_INS.format(md_installed_string))
        args = [EXECUTABLE, "-m", "userbot"]
        os.execle(sys.executable, *args, os.environ)
        await msg.client.disconnect()
        return
    elif cmd_args[0].lower() == "uninstall":
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
        log.info(f"Module '{modName}' has been uninstalled from userspace")
        log.info("Rebooting userbot...")
        await msg.edit(msgRep.DONE_RBT)
        time.sleep(1)  # just so we can actually see a message
        if LOGGING:
            await event_log(msg, "MODULE UNINSTALL", custom_text=msgRep.UNINSTALL_LOG.format(modName))
        await msg.edit(msgRep.REBOOT_DONE_UNINS.format(modName))
        args = [EXECUTABLE, "-m", "userbot"]
        os.execle(sys.executable, *args, os.environ)
        await msg.client.disconnect()
        return
    else:
        await msg.edit(msgRep.INVALID_ARG)
        return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.PACKAGE_MANAGER_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.PACKAGE_MANAGER_USAGE})
