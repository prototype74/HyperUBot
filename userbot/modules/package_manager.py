# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import _setprop, SAFEMODE
import userbot.include.git_api as git
from userbot.include.aux_funcs import event_log, sizeStrMaker
from userbot.include.language_processor import (PackageManagerText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig, setConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (getUserModules, register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.sysutils.sys_funcs import isWindows
from userbot.version import VERSION
import requests
import os
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")

USER_MODULES_DIR = os.path.join(".", "userbot", "modules_user")
PACKAGELIST = "./userbot/package_lists.hbot"
UNIVERSE_URL = "nunopenim/module-universe"
UNIVERSE_NAME = "modules-universe"


def write_list():
    global MODULE_LIST
    if os.path.exists(PACKAGELIST):
        os.remove(PACKAGELIST)
    file = open(PACKAGELIST, "w+")
    for mod in MODULE_LIST:
        str_to_write = (mod["repo"] + "|" + mod["name"] +
                        "|" + mod["url"] + "|" + str(mod["size"]) + "\n")
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
            MODULE_LIST.append({"repo": params[0], "name": params[1],
                                "url": params[2], "size": int(params[3])})
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
        MODULE_LIST.append({"repo": UNIVERSE_NAME, "name": assetName,
                            "url": assetURL, "size": assetSize})
    for repoURL in getConfig("COMMUNITY_REPOS", []):
        repoName = git.getReleaseTag(
            git.getReleaseData(git.getData(repoURL), 0))
        if repoName not in REPOS_NAMES:
            REPOS_NAMES.append(repoName)
        assets = git.getAssets(git.getReleaseData(git.getData(repoURL), 0))
        for asset in assets:
            assetName = git.getReleaseFileName(asset)
            assetURL = git.getReleaseFileURL(asset)
            assetSize = git.getSize(asset)
            if assetName in MODULE_LIST:
                MODULE_LIST.remove(MODULE_LIST["name"] == assetName)
            MODULE_LIST.append({"repo": repoName, "name": assetName,
                                "url": assetURL, "size": assetSize})
    return MODULE_LIST


@ehandler.on(command="pkg", hasArgs=True, outgoing=True)
async def universe_checker(msg):
    cmd_args = msg.pattern_match.group(1).split(" ", 1)
    user_modules = getUserModules()
    if cmd_args[0].lower() == "update":
        list_updater()
        write_list()
        repos = UNIVERSE_NAME
        for repo in REPOS_NAMES:
            repos += ", " + repo
        await msg.edit(msgRep.UPDATE_COMPLETE.format(repos))
    elif cmd_args[0].lower() == "list":
        files = msgRep.INSTALLED
        count = 1
        for item in user_modules:
            files += str(count) + ". " + item + "\n"
            count += 1
        if len(user_modules) == 0:
            files += msgRep.NO_MOD_IN_USERSPACE
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
                if mdName in user_modules:
                    mdName += "*"
                    mdInstalled = True
                files += msgRep.FILE_DSC.format(count, mdName, m["url"], size)
                count += 1
            if mdInstalled:
                files += msgRep.ALREADY_PRESENT
        if SAFEMODE:
            files += msgRep.BOT_IN_SAFEMODE
        await msg.edit(files, parse_mode='md')
    elif cmd_args[0].lower() == "install":
        if MODULE_LIST is None or len(MODULE_LIST) == 0:
            await msg.edit(msgRep.EMPTY_LIST)
            return
        if len(cmd_args) == 1:
            await msg.edit(msgRep.NO_PKG)
            return
        if SAFEMODE:
            await msg.edit(msgRep.INSTALL_DSBLD_SAFEMODE)
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
            # We remove first, in case exists for updates
            if os.path.exists(os.path.join(USER_MODULES_DIR, i['filename'])):
                os.remove(os.path.join(USER_MODULES_DIR, i['filename']))
            open(os.path.join(USER_MODULES_DIR,
                              i['filename']), 'wb').write(request.content)
            modules_installed.append(i['filename'])
            log.info(f"Module '{i['filename'][:-3]}' "
                     f"has been installed to userspace")
        md_installed_string = ""
        for md in modules_installed:
            if md_installed_string == "":
                md_installed_string += md
            else:
                md_installed_string += ", " + md
        if LOGGING:
            await event_log(msg, "MODULE INSTALL",
                            custom_text=msgRep.INSTALL_LOG.format(
                                md_installed_string))
        if isWindows():
            log.info("Manual reboot required to load installed module(s)")
            await msg.edit(msgRep.INSTALL_WIN.format(md_installed_string))
        else:
            await msg.edit(msgRep.DONE_RBT)
            _setprop("reboot", True)
            _setprop("rebootchatid", msg.chat_id)
            _setprop("rebootmsgid", msg.message.id)
            _setprop("rebootmsg", msgRep.REBOOT_DONE_INS.format(
                md_installed_string))
            setConfig("REBOOT", True)
            await msg.client.disconnect()
    elif cmd_args[0].lower() == "uninstall":
        if len(user_modules) == 0:
            await msg.edit(msgRep.NO_UNINSTALL_MODULES)
            return
        if len(cmd_args) == 1:
            await msg.edit(msgRep.NO_UN_NAME)
            return
        del(cmd_args[0])
        mods_uninstall = cmd_args[0].split()
        modNames = ""
        for i in mods_uninstall:
            if modNames == "":
                modNames += i
            else:
                modNames += ", " + i
        await msg.edit(msgRep.UNINSTALLING.format(modNames))
        for modName in mods_uninstall:
            if modName not in user_modules:
                await msg.edit(msgRep.NOT_IN_USERSPACE.format(modName))
                return
            os.remove(os.path.join(USER_MODULES_DIR, modName + ".py"))
        log.info(f"Module '{modNames}' has been uninstalled from userspace")
        if LOGGING:
            await event_log(msg, "MODULE UNINSTALL",
                            custom_text=msgRep.UNINSTALL_LOG.format(modNames))
        if isWindows():
            log.info("Manual reboot required to unload uninstalled module(s)")
            await msg.edit(msgRep.UNINSTALL_WIN.format(modNames))
        else:
            await msg.edit(msgRep.DONE_RBT)
            _setprop("reboot", True)
            _setprop("rebootchatid", msg.chat_id)
            _setprop("rebootmsgid", msg.message.id)
            _setprop("rebootmsg", msgRep.REBOOT_DONE_UNINS.format(modNames))
            if SAFEMODE:
                setConfig("REBOOT_SAFEMODE", True)
            setConfig("REBOOT", True)
            await msg.client.disconnect()
    else:
        await msg.edit(msgRep.INVALID_ARG)
    return


register_cmd_usage("pkg",
                   usageRep.PACKAGE_MANAGER_USAGE.get("pkg", {}).get("args"),
                   usageRep.PACKAGE_MANAGER_USAGE.get("pkg", {}).get("usage"))

register_module_desc(descRep.PACKAGE_MANAGER_DESC)
register_module_info(
    name="Package Manager",
    authors="nunopenim, prototype74",
    version=VERSION
)
