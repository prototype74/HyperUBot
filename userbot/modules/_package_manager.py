# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import _setprop, SAFEMODE
from userbot._core.module_loader import import_module, unimport_module
from userbot.include.git_api import getLatestData
from userbot.include.aux_funcs import sizeStrMaker
from userbot.include.language_processor import (PackageManagerText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.package_manager import _PackageManagerJSON
from userbot.sysutils.registration import (getUserModules,
                                           getLoadModules,
                                           register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.sysutils.sys_funcs import isWindows
from userbot.version import VERSION
from telethon.errors import MessageTooLongError
from datetime import datetime, timedelta
from glob import glob
from logging import getLogger
from urllib.request import urlretrieve
import os

log = getLogger(__name__)
ehandler = EventHandler(log)
_pkg_manager = _PackageManagerJSON()
_pkg_manager._init_json()
_pkg_list = _pkg_manager._read_json()
_pkg_list = _pkg_manager._check_packages(_pkg_list)
_attempts = 0


def _get_release(repo_url: str) -> dict:
    repo_data = {}
    try:
        release_data = getLatestData(repo_url)
        repo_data["author"] = release_data["html_url"].split(
            "https://github.com/")[1].split("/")[0]
        repo_data["name"] = release_data["html_url"].split(
            "https://github.com/")[1].split("/")[1]
        repo_data["version"] = release_data["tag_name"]
        assets = []
        repo_assets = release_data.get("assets", [])
        if repo_assets:
            for asset in repo_assets:
                if not repo_data.get("link", None):
                    repo_data["link"] = os.path.dirname(
                        asset.get("browser_download_url")) + "/"
                if asset.get("name", "").endswith(".py"):
                    assets.append({"name": asset.get("name"),
                                   "size":  asset.get("size")})
        repo_data["assets"] = assets
        return repo_data
    except Exception as e:
        log.error(f"Failed to get release from {repo_url}: {e}")
    return {}


def filerList(list_to_filer: list) -> list:
    filtered_list = list(dict.fromkeys(list_to_filer))
    if "" in filtered_list:
        filtered_list.remove("")
    return filtered_list


async def _update_pkg_list(event, repo_names=None):
    global _pkg_list
    pkg_repos = _pkg_list.get("repos", [])
    list_modified = False
    if repo_names:
        # update specific repo(s) only
        # or add a new repo
        repos = filerList(repo_names.split(" "))
    else:  # update all repos
        repos = ["nunopenim/module-universe"]
        community_repos = getConfig("COMMUNITY_REPOS", [])
        if isinstance(community_repos, (list, tuple)):
            for c_repo in community_repos:
                try:
                    _1, _2 = c_repo.split("/")
                    if c_repo not in repos:
                        repos.append(c_repo)
                except:
                    pass  # just ignore
        for repo in pkg_repos:
            repo_author = repo.get("author", "Unknown")
            repo_name = repo.get("name", "Unknown")
            repo_url = f"{repo_author}/{repo_name}"
            if repo_url not in repos:
                repos.append(repo_url)
        pkg_repos = []  # reset
        list_modified = True

    if not repos:
        # this is a "99.99% impossible" case but well
        # better safe than sorry
        if event:
            await event.edit(msgRep.REPO_LIST_EMPTY)
        return

    text = f"**{msgRep.PACKAGES_UPDATER}**\n\n"
    red_cross = u"\u274C"  # red cross mark emoji
    check_mark = u"\u2705"  # check mark emoji
    down = u"\u2B07"  # down emoji
    warning = u"\u26A0"  # warning emoji

    for r in repos:
        try:
            r_author, r_name = r.split("/")
        except:
            log.warning(f"[UPDATE] Invalid repo URL format: {r}")
            text += f"{warning} {msgRep.INVALID_REPO_URL}: {r}\n"
            if event:
                await event.edit(text)
            continue
        text += f"{down} {msgRep.UPDATING.format(r_name)}\n"
        if event:
            await event.edit(text)
        for i, repo in enumerate(pkg_repos):
            if r_author == repo.get("author", "Unknown") and \
               r_name == repo.get("name", "Unknown"):
                new_data = _get_release(f"{r_author}/{r_name}")
                if new_data:
                    pkg_repos[i] = new_data
                    text = text.replace(
                        f"{down} {msgRep.UPDATING.format(r_name)}",
                        f"{check_mark} {msgRep.UPDATE_SUCCESS.format(r_name)}")
                    if not list_modified:
                        list_modified = True
                else:
                    log.error("[UPDATE] Failed to get release "
                              f"data from {r_name}")
                    text = text.replace(
                        f"{down} {msgRep.UPDATING.format(r_name)}",
                        f"{red_cross} {msgRep.UPDATE_FAILED.format(r_name)}")
                break
        else:
            new_data = _get_release(f"{r_author}/{r_name}")
            if new_data:
                pkg_repos.append(new_data)
                text = text.replace(
                    f"{down} {msgRep.UPDATING.format(r_name)}",
                    f"{check_mark} {msgRep.UPDATE_SUCCESS.format(r_name)}")
                if not list_modified:
                    list_modified = True
            else:
                log.error(f"[UPDATE] Failed to get release data from {r_name}")
                text = text.replace(
                    f"{down} {msgRep.UPDATING.format(r_name)}",
                    f"{red_cross} {msgRep.UPDATE_FAILED.format(r_name)}")
        if event:
            await event.edit(text)
    if list_modified:
        _pkg_list["last_updated"] = str(datetime.now())
        _pkg_list["repos"] = pkg_repos
        _pkg_manager._save_json(_pkg_list)
        log.info("[UPDATE] Repo data updated")
    text += "\n"
    text += msgRep.UPDATER_FINISHED
    if event:
        await event.edit(text)
    return


def _update_needed() -> bool:
    global _pkg_list
    try:
        date_diff = datetime.now() - datetime.fromisoformat(
            _pkg_list.get("last_updated"))
        return date_diff > timedelta(hours=1)
    except:
        pass
    return False


def _get_all_user_modules() -> list:
    user_module_list = []
    user_module_path = sorted(
        glob(os.path.join(".", "userbot", "modules_user", "*.py")))
    for module in user_module_path:
        if os.path.isfile(module) and \
           not os.path.basename(module).startswith("__") and \
           module.endswith(".py"):
            filename = os.path.basename(module)[:-3]
            user_module_list.append(filename)
    return user_module_list


async def _list_pkgs(command: str) -> str:
    installed_only = False
    repos_only = False
    if command:
        if command.lower() == "-installed":
            installed_only = True
        elif command.lower() == "-repos":
            repos_only = True
    user_module_list = _get_all_user_modules()
    if getConfig("PKG_ENABLE_AUTO_UPDATE"):
        if _update_needed():
            log.info("Auto updating repo data")
            await _update_pkg_list(None)
    text = f"**{msgRep.LIST_OF_PACKAGES}**\n\n"
    no_entry = u"\u26D4"  # no_entry emoji
    negative_cross = u"\u274E"  # green negative cross mark emoji
    warning = u"\u26A0"  # warning emoji
    disabled_module = False
    installed_not_loaded = False
    mod_not_running = False
    if not repos_only:
        not_load_modules = getConfig("NOT_LOAD_MODULES", [])
        user_modules = getUserModules()
        loaded_modules = getLoadModules()
        text += f"**{msgRep.INSTALLED_MODULES} ({len(user_module_list)}):**\n"
        if user_module_list:
            for module in user_module_list:
                info = ""
                if module in not_load_modules:
                    info += f" {no_entry}"
                    if not disabled_module:
                        disabled_module = True
                elif module not in user_modules:
                    info += f" {negative_cross}"
                    if not installed_not_loaded:
                        installed_not_loaded = True
                else:
                    for mod, isrun in loaded_modules.items():
                        if module == mod and not isrun:
                            info += f" {warning}"
                            if not mod_not_running:
                                mod_not_running = True
                            break
                text += f"- {module}{info}\n"
        else:
            text += f"__{msgRep.NO_MODULES_INSTALLED}__\n"
        text += "\n"
    global _pkg_list
    pkg_repos = _pkg_list.get("repos", [])
    installed_already = False
    upgradeable = False
    equal_module = False
    check_mark = u"\u2705"  # check mark emoji
    ccw_emoji = u"\U0001F504"  # counterclockwise emoji
    info_emoji = u"\u2139"  # information emoji
    if not installed_only and pkg_repos:
        module_sources = _pkg_list.get("module_sources", [])
        for repo in pkg_repos:
            repo_author = repo.get("author", "Unknown")
            repo_name = repo.get("name", "Unknown")
            repo_version = repo.get("version", "Unknown")
            assets = repo.get("assets", [])
            assets_size = len(assets)
            text += (f"**{msgRep.MODULES_IN.format(repo_name)} "
                     f"({assets_size}):**\n")
            text += f"{msgRep.AUTHOR}: **{repo_author}**\n"
            text += f"{msgRep.VERSION}: **{repo_version}**\n"
            if assets:
                for asset in assets:
                    module_name = asset.get("name")[:-3]
                    module_size = sizeStrMaker(asset.get("size", 0))
                    info = ""
                    if module_name in user_module_list:
                        for mod_src in module_sources:
                            # check if installed module is from known
                            # package lists
                            mod_src_name = mod_src.get("name", "")
                            mod_src_author = mod_src.get("author", "Unknown")
                            mod_src_repo = mod_src.get("repo", "Unknown")
                            mod_src_version = mod_src.get("version", "Unknown")
                            mod_src_size = mod_src.get("size", 0)
                            if module_name == mod_src_name:
                                if mod_src_author == repo_author and \
                                   mod_src_repo == repo_name:
                                    info += f" {check_mark}"
                                    if not installed_already:
                                        installed_already = True
                                    if not mod_src_version == repo_version and\
                                       not mod_src_size == module_size:
                                        # assume the module were updated
                                        info += f" {ccw_emoji}"
                                        if not upgradeable:
                                            upgradeable = True
                                    break
                    if len(pkg_repos) >= 2:  # more known repos
                        # check if current module's name exist
                        # in a different repo too
                        for repo2 in pkg_repos:
                            if not repo == repo2:
                                assets2 = repo2.get("assets", [])
                                if assets2:
                                    for asset2 in assets2:
                                        module_name2 = asset2.get("name")[:-3]
                                        if module_name == module_name2:
                                            info += f" {info_emoji}"
                                            if not equal_module:
                                                equal_module = True
                                            break
                    text += f"- {module_name} ({module_size}){info}\n"
            else:
                text += f"__{msgRep.REPO_NO_MODULES}__\n"
            text += "\n"
    elif not installed_only:
        text += f"__{msgRep.REPOS_NO_DATA.format('`.pkg update`')}__\n"
        text += "\n"

    if installed_already:
        text += f"{check_mark} __{msgRep.INSTALLED}__\n"
    if installed_not_loaded:
        text += f"{negative_cross} __{msgRep.INSTALLED_NOTLOADED}__\n"
    if upgradeable:
        text += f"{ccw_emoji} __{msgRep.UPGRADEABLE}__\n"
    if mod_not_running:
        text += f"{warning} __{msgRep.START_FAILED}__\n"
    if disabled_module:
        text += f"{no_entry} __{msgRep.DISABLED}__\n"
    if equal_module:
        text += f"{info_emoji} __{msgRep.EQUAL_NAME}__\n"
    if any(x for x in (installed_already, installed_not_loaded,
                       mod_not_running, disabled_module, equal_module)):
        text += "\n"
    time = _pkg_list.get("last_updated", None)
    try:
        time = datetime.fromisoformat(time)
        time = time.strftime("%Y-%m-%d %H:%M:%S")
    except:
        time = msgRep.NEVER
    text += f"__{msgRep.LAST_UPDATED}: {time}__"
    return text


def ctrl_modules(modules: list, remove: bool):
    for module in modules:
        if remove:
            unimport_module(module)
        else:
            import_module(module, True)
    return


def _validate_code(name) -> bool:
    try:
        if os.path.exists(name) and os.path.isfile(name):
            with open(name, "rb") as script_file:
                compile(script_file.read(),
                        filename=os.path.basename(name),
                        mode="exec")
            script_file.close()
        return True
    except Exception as e:
        log.error(f"Validation for '{os.path.basename(name)}' failed",
                  exc_info=True)
    return False


async def _install_pkgs(event, command: str):
    if not command:
        await event.edit(msgRep.INSTALL_EMPTY)
        return
    commands = command.split(" ", 1)
    if len(commands) >= 2:
        first_arg, sec_arg = commands
    else:
        first_arg, sec_arg = commands[0], None

    if not first_arg:
        await event.edit(msgRep.INSTALL_EMPTY)
        return

    queued_mod_to_install = []
    global _pkg_list
    _pkg_list = _pkg_manager._read_json()
    pkg_repos = _pkg_list.get("repos", [])

    if not pkg_repos:
        await event.edit(msgRep.REPOS_NO_DATA.format("`.pkg update`"))
        return

    unknown_modules = []
    text = f"**{msgRep.PACKAGE_INSTALLER}**\n\n"
    red_cross = u"\u274C"  # red cross mark emoji
    check_mark = u"\u2705"  # check mark emoji
    down = u"\u2B07"  # down emoji
    warning = u"\u26A0"  # warning emoji

    if first_arg.lower() == "-repo":  # check specific repo
        if not sec_arg:
            text += f"{warning} {msgRep.NO_REPO_URL}\n"
            await event.edit(text)
            return
        sec_arg = sec_arg.split(" ", 1)
        if len(sec_arg) >= 2:
            repo_url, mods = sec_arg
        else:
            repo_url, mods = sec_arg[0], None
        try:
            r_author, r_name = repo_url.split("/")
        except:
            text += ("f{warning} {msgRep.INVALID_REPO_URL}: {repo_url}\n")
            await event.edit(text)
            return
        if not mods:
            text += (f"{warning} {msgRep.INSTALL_EMPTY_REPO}\n")
            await event.edit(text)
            return
        mods = filerList(mods.split(" "))
        for repo in pkg_repos:
            repo_author = repo.get("author", "Unknown")
            repo_name = repo.get("name", "Unknown")
            repo_version = repo.get("version", "Unknown")
            if r_author == repo_author and r_name == repo_name:
                assets = repo.get("assets", [])
                list_of_mods = {}
                if assets:
                    for mod in mods:
                        for asset in assets:
                            module_name = asset.get("name", "")
                            module_size = asset.get("size", 0)
                            if mod == module_name[:-3]:
                                list_of_mods[module_name] = module_size
                                break
                        else:
                            if mod not in unknown_modules:
                                unknown_modules.append(mod)
                if list_of_mods:
                    queued_mod_to_install.append(
                        {"repo_author": repo_author,
                         "repo_name": repo_name,
                         "repo_version": repo_version,
                         "repo_link": repo.get("link"),
                         "modules": list_of_mods})
                break
        else:
            text += f"{warning} {msgRep.UNKNOWN_REPO_URL}\n"
            await event.edit(text)
            return
    else:  # check all repos
        mods = []
        mods.append(first_arg)
        if sec_arg:
            mods_from_sec_arg = sec_arg.split(" ")
            for mod_from_sec_arg in mods_from_sec_arg:
                mods.append(mod_from_sec_arg)
        mods = filerList(mods)
        known_modules_found = []
        for repo in pkg_repos:
            list_of_mods = {}
            repo_author = repo.get("author", "Unknown")
            repo_name = repo.get("name", "Unknown")
            repo_version = repo.get("version", "Unknown")
            assets = repo.get("assets", [])
            if assets:
                for mod in mods:
                    for asset in assets:
                        module_name = asset.get("name", "")
                        module_size = asset.get("size", 0)
                        if mod == module_name[:-3]:
                            if mod not in known_modules_found:
                                # it may be possbile that there are modules
                                # with same name from different repos, so
                                # pick the first match only
                                list_of_mods[module_name] = module_size
                                known_modules_found.append(mod)
                            if mod in unknown_modules:
                                # module found in an another repo
                                unknown_modules.remove(mod)
                            break
                    else:
                        # module not found in current repo
                        if mod not in unknown_modules and \
                           mod not in known_modules_found:
                            unknown_modules.append(mod)
            if list_of_mods:
                queued_mod_to_install.append({"repo_author": repo_author,
                                              "repo_name": repo_name,
                                              "repo_version": repo_version,
                                              "repo_link": repo.get("link"),
                                              "modules": list_of_mods})
    if unknown_modules:
        text += (f"{warning} {msgRep.UNKNOWN_MODULES}: "
                 f"{', '.join(unknown_modules)}\n")
        text += "\n"
        text += msgRep.INSTALLER_FINISHED
        await event.edit(text)
        return
    if not queued_mod_to_install:
        text += f"{warning} {msgRep.NO_INSTALL_QUEUED}\n"
        text += "\n"
        text += msgRep.INSTALLER_FINISHED
        await event.edit(text)
        return
    pkg_mod_sources = _pkg_list.get("module_sources", [])
    do_update_mod_list = False
    installed_modules = []
    for queue in queued_mod_to_install:
        repo_author = queue.get("repo_author")
        repo_name = queue.get("repo_name")
        repo_version = queue.get("repo_version")
        repo_link = queue.get("repo_link")
        list_of_mods = queue.get("modules")
        for module, size in list_of_mods.items():
            curr_module = module[:-3]  # without .py
            text += f"{down} {msgRep.DOWNLOADING.format(curr_module)}\n"
            await event.edit(text)
            module_path = os.path.join(".", "userbot", "modules_user", module)
            try:
                log.info(f"[INSTALL] Downloading module '{module}'...")
                dw_url = f"{repo_link}{module}"
                urlretrieve(dw_url, module_path)
            except Exception as e:
                log.error("[INSTALL] Unable to download "
                          f"module '{module}': {e}",
                          exc_info=True)
                text = text.replace(
                    f"{down} {msgRep.DOWNLOADING.format(curr_module)}",
                    f"{red_cross} {msgRep.DOWN_FAILED.format(curr_module)}")
                await event.edit(text)
                continue
            if not _validate_code(module_path):
                text = text.replace(
                    f"{down} {msgRep.DOWNLOADING.format(curr_module)}",
                    f"{red_cross} {msgRep.INSTALL_FAILED.format(curr_module)}")
                await event.edit(text)
                try:
                    os.remove(module_path)
                except:
                    pass
                continue
            if curr_module not in installed_modules:
                installed_modules.append(curr_module)
            try:
                # download was successful so update module source list
                new_data = {"name": curr_module,
                            "author": repo_author,
                            "repo": repo_name,
                            "version": repo_version,
                            "size": size}
                for i, mod_source in enumerate(pkg_mod_sources):
                    # check if module is already on source list
                    # update it's data if true
                    mod_name = mod_source.get("name", "")
                    if mod_name == curr_module:
                        pkg_mod_sources[i] = new_data
                        break
                else:
                    pkg_mod_sources.append(new_data)
                if not do_update_mod_list:
                    do_update_mod_list = True
                text = text.replace(
                    f"{down} {msgRep.DOWNLOADING.format(curr_module)}",
                    f"{check_mark} "
                    f"{msgRep.INSTALL_SUCCESS.format(curr_module)}")
            except Exception as e:
                log.warning("[INSTALL] Failed to update source data "
                            f"for module '{module}'",
                            exc_info=True)
                down_text = msgRep.DOWNLOADING.format(curr_module)
                fail_text = msgRep.UPDATE_DATA_FAIL.format(curr_module)
                text = text.replace(f"{down} {down_text}",
                                    f"{warning} {fail_text}")
            await event.edit(text)
    if do_update_mod_list:
        _pkg_list["module_sources"] = pkg_mod_sources
        _pkg_manager._save_json(_pkg_list)
    text += "\n"
    text += msgRep.INSTALLER_FINISHED
    await event.edit(text)
    if installed_modules:
        ctrl_modules(installed_modules, False)
    return


async def _uninstall_pkgs(event, module_names: str):
    if not module_names:
        await event.edit(msgRep.UNINSTALL_EMPTY)
        return
    modules_from_arg = filerList(module_names.split(" "))
    user_modules = _get_all_user_modules()
    if not user_modules:
        await event.edit(msgRep.NO_MODULES_INSTALLED)
        return
    global _pkg_list
    _pkg_list = _pkg_manager._read_json()
    pkg_mod_sources = _pkg_list.get("module_sources", [])
    do_update_mod_list = False
    text = f"**{msgRep.PACKAGE_UNINSTALLER}**\n\n"
    red_cross = u"\u274C"  # red cross mark emoji
    check_mark = u"\u2705"  # check mark emoji
    warning = u"\u26A0"  # warning emoji
    unkwn = u"\u2754"  # grey question mark emoji
    uninstalled_modules = []
    for module in modules_from_arg:
        if module in user_modules:
            try:
                os.remove(os.path.join(".", "userbot", "modules_user",
                                       f"{module}.py"))
            except:
                log.error("[UNINSTALL] Failed to uninstall "
                          f"module '{module}'",
                          exc_info=True)
                text += (f"{red_cross} "
                         f"{msgRep.UNINSTALL_FAILED.format(module)}\n")
                await event.edit(text)
                continue
            if module not in uninstalled_modules:
                uninstalled_modules.append(module)
            try:
                # remove deleted module from module source list
                for i, mod_source in enumerate(pkg_mod_sources):
                    mod_name = mod_source.get("name", "")
                    if mod_name == module:
                        pkg_mod_sources.pop(i)
                        break
                if not do_update_mod_list:
                    do_update_mod_list = True
                log.info("[UNINSTALL] Uninstalled module "
                         f"'{module}' successfully")
                text += (f"{check_mark} "
                         f"{msgRep.UNINSTALL_SUCCESS.format(module)}\n")
            except Exception as e:
                log.error("[UNINSTALL] Failed to remove source data "
                          f"for module '{module}'",
                          exc_info=True)
                text += (f"{warning} "
                         f"{msgRep.UNINSTALL_DATA.format(module)}\n")
        else:
            log.info(f"[UNINSTALL] Module '{module}' not installed")
            text += f"{unkwn} {msgRep.MODULE_NOT_INSTALL.format(module)}\n"
        await event.edit(text)
    if do_update_mod_list:
        _pkg_list["module_sources"] = pkg_mod_sources
        _pkg_manager._save_json(_pkg_list)
    text += "\n"
    text += msgRep.UNINSTALLER_FINISHED
    await event.edit(text)
    if uninstalled_modules:
        ctrl_modules(uninstalled_modules, True)
    return


async def _rm_repo(event, repo_names=None):
    if repo_names:
        repos = filerList(repo_names.split(" "))
    else:
        await event.edit(msgRep.NO_REPO_NAMES)
        return

    global _pkg_list
    pkg_repos = _pkg_list.get("repos", [])

    if not pkg_repos:
        await event.edit(msgRep.NO_REPO_REMOVE)
        return

    list_modified = False
    text = f"**{msgRep.REPO_REMOVER}**\n\n"
    red_cross = u"\u274C"  # red cross mark emoji
    check_mark = u"\u2705"  # check mark emoji
    recycle = u"\u267B"  # recycling emoji
    warning = u"\u26A0"  # warning emoji
    unkwn = u"\u2754"  # grey question mark emoji

    protected_repos = ["nunopenim/module-universe"]
    community_repos = getConfig("COMMUNITY_REPOS", [])

    if isinstance(community_repos, (list, tuple)):
        for c_repo in community_repos:
            try:
                _1, _2 = c_repo.split("/")
                if c_repo not in protected_repos:
                    protected_repos.append(c_repo)
            except:
                pass  # just ignore

    for r in repos:
        try:
            r_author, r_name = r.split("/")
        except:
            log.warning(f"[RMREPO] Invalid repo URL format: {r}")
            text += f"{warning} {msgRep.INVALID_REPO_URL}: {r}\n"
            await event.edit(text)
            continue
        if r in protected_repos:
            text += f"{warning} {msgRep.CANNOT_REMOVE_REPO.format(r_name)}\n"
            await event.edit(text)
            continue
        text += f"{recycle} {msgRep.REMOVING.format(r_name)}\n"
        await event.edit(text)
        for i, repo in enumerate(pkg_repos):
            if r_author == repo.get("author", "Unknown") and \
               r_name == repo.get("name", "Unknown"):
                try:
                    pkg_repos.pop(i)
                    text = text.replace(
                        f"{recycle} {msgRep.REMOVING.format(r_name)}",
                        f"{check_mark} {msgRep.REMOVE_SUCCESS.format(r_name)}")
                    if not list_modified:
                        list_modified = True
                except:
                    log.error(f"[RMREPO] Failed to remove {r_name} from list")
                    text = text.replace(
                        f"{recycle} {msgRep.REMOVING.format(r_name)}",
                        f"{red_cross} {msgRep.REMOVE_FAILED.format(r_name)}")
                break
        else:
            text = text.replace(f"{recycle} {msgRep.REMOVING.format(r_name)}",
                                f"{unkwn} {msgRep.UNKNOWN_REPO}: {r}")
        await event.edit(text)
    if list_modified:
        _pkg_list["repos"] = pkg_repos
        _pkg_manager._save_json(_pkg_list)
    text += "\n"
    text += msgRep.REMOVER_FINISHED
    await event.edit(text)
    return


@ehandler.on(command="pkg", hasArgs=True, outgoing=True)
async def package_manager(event):
    args_from_event = event.pattern_match.group(1).split(" ", 1)
    if len(args_from_event) >= 2:
        first_arg, sec_arg = args_from_event
    else:
        first_arg, sec_arg = args_from_event[0], None

    global _attempts

    if first_arg.lower() == "update":
        await _update_pkg_list(event, sec_arg)
    elif first_arg.lower() == "list":
        await event.edit(msgRep.LOAD_PGKS)
        text = await _list_pkgs(sec_arg)
        try:
            await event.edit(text)
        except MessageTooLongError:
            text = text.replace("*", "")
            text = text.replace("__", "")
            text = text.replace(u"\u26D4", "(-)")
            text = text.replace(u"\u274E", "(x)")
            text = text.replace(u"\u26A0", "/!\\")
            text = text.replace(u"\u2705", "(+)")
            text = text.replace(u"\U0001F504", "(UP)")
            text = text.replace(u"\u2139", "(i)")
            print(text)
            text_alt = f"**{msgRep.LIST_OF_PACKAGES}**\n\n"
            text_alt += f"__{msgRep.TEXT_TOO_LONG}__"
            await event.edit(text_alt)
    elif first_arg.lower() == "install":
        if SAFEMODE:
            await event.edit(msgRep.CANNOT_INSTALL_MODULES)
            return
        await _install_pkgs(event, sec_arg)
    elif (first_arg.lower() == "uninstall" or
          first_arg.lower() == "remove"):
        await _uninstall_pkgs(event, sec_arg)
    elif first_arg.lower() == "rmrepo":
        await _rm_repo(event, sec_arg)
    else:
        text = text = f"**{msgRep.PACKAGE_MANAGER}**\n\n"
        if first_arg:
            text += f"`{msgRep.UNKNOWN_OPTION.format(first_arg)}`\n"
            if _attempts >= 2:
                text += f"\n{msgRep.PKG_HELP.format('`.help pkg`')}\n"
            else:
                _attempts += 1
            await event.edit(text)
            return
        else:
            text += (f"{msgRep.NO_OPTION}. "
                     f"{msgRep.PKG_HELP.format('`.help pkg`')}\n")
        await event.edit(text)
    if _attempts:
        _attempts = 0
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
