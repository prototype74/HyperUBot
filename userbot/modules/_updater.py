# Copyright 2020-2022 nunopenim @github
# Copyright 2020-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import _setprop
from userbot._core.access_controller import _protectedAccess
from userbot.include.aux_funcs import getGitReview
from userbot.include.git_api import getLatestData
from userbot.include.language_processor import (UpdaterText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import setConfig, getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.sysutils.sys_funcs import isWindows, verAsTuple
from userbot.version import VERSION, VERSION_TUPLE
from logging import getLogger
from urllib.request import urlretrieve
from zipfile import BadZipFile, LargeZipFile, ZipFile
from dateutil.parser import parse
import os
import sys

log = getLogger(__name__)
ehandler = EventHandler(log)
_update_scheduler = getConfig("UPDATER_ENABLE_SCHEDULER", False)

if _update_scheduler:
    from userbot import _tgclient
    from telethon.tl.functions.messages import MarkDialogUnreadRequest
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    from datetime import datetime, timedelta
    from logging import WARNING
    from tzlocal import get_localzone
    _scheduler = AsyncIOScheduler(timezone=str(get_localzone()))
    getLogger("apscheduler").setLevel(WARNING)

RELEASE_DIR = os.path.join(".", "releases")
UPDATE_PACKAGE = os.path.join(RELEASE_DIR, "update.zip")
_LATEST_VER = {}


def _get_latest_release(updater_rules: str, release: str) -> bool:
    if not os.path.exists(RELEASE_DIR):
        try:
            os.mkdir(RELEASE_DIR)
        except Exception as e:
            log.error(f"Failed to create release directory: {e}")
            return False

    try:
        try:
            log.info("Downloading updater rules...")
            urlretrieve(updater_rules, os.path.join(RELEASE_DIR, "rules.py"))
        except Exception as e:
            log.error("Unable to download updater rules")
            raise Exception(e)
        log.info("Downloading update package...")
        urlretrieve(release, UPDATE_PACKAGE)
        log.info("Download successful")
        return True
    except Exception as e:
        log.error(f"Unable to download latest release: {e}")
    return False


def _get_commit_id():
    commit_id = None
    if not os.path.exists(UPDATE_PACKAGE):
        log.warning("Update package not found")
        return commit_id

    try:
        contents = None
        with ZipFile(UPDATE_PACKAGE, "r") as updateZIP:
            contents = updateZIP.namelist()
        updateZIP.close()
        if contents and len(contents) >= 1:
            commit_id = contents[0][:-1].split("-")[-1]
    except BadZipFile as bze:
        log.error(f"Bad zip archive: {bze}", exc_info=True)
    except LargeZipFile as lze:
        log.error(f"Zip archive too large (>64): {lze}", exc_info=True)
    except Exception as e:
        log.error(f"Failed to get commit id from update package: {e}",
                  exc_info=True)
    return commit_id


def _set_autoupdate(chat_id: int, msg_id: int,
                    new_version: str, commit_id: str) -> bool:
    try:
        _setprop("reboot", True)
        _setprop("rebootchatid", chat_id)
        _setprop("rebootmsgid", msg_id)
        _setprop("rebootmsg", msgRep.UPDATE_SUCESS.format(new_version))
        _setprop("updateversion", new_version)
        _setprop("updatefailedmsg", msgRep.UPDATE_FAIL.format(new_version))
        setConfig("UPDATE_COMMIT_ID", commit_id)
        setConfig("START_RECOVERY", True)
        return True
    except Exception as e:
        log.error(f"Unable to set reboot reason: {e}")
    return False


async def _is_git_repo() -> bool:
    return True if await getGitReview() else False


def _parse_datetime(date) -> str:
    try:
        dt = parse(date)
        date_format = f"`{dt.strftime('%b %d, %Y')}`"
        return date_format
    except Exception:
        log.warning("Failed to parse publish date")
    return date


def _print_instructions(commit_id: str):
    if isWindows():
        print()
        print("=== UPDATE INSTRUCTIONS ===")
        print(f"Commit ID: {commit_id}")
        print("- Start recovery (python recovery.py)")
        print("- Select 'Apply update'")
        print("- Enter commit id (see above)")
        print("- Wait for recovery to finish")
        print("- Exit recovery")
        print("- Start HyperUBot (python -m userbot)")
        print()
    return


@ehandler.on(command="update", hasArgs=True, outgoing=True)
async def updater(event):
    arg = event.pattern_match.group(1)
    git_repo = await _is_git_repo()
    warn_emoji = u"\u26A0"
    update_now = True if arg.lower() == "upgrade" else False
    global _LATEST_VER

    if not update_now or (update_now and not _LATEST_VER):
        await event.edit(msgRep.CHECKING_UPDATES)

    if update_now and _LATEST_VER:
        await event.edit(msgRep.DOWNLOADING_RELEASE)
        if not _get_latest_release(_LATEST_VER.get("rules"),
                                   _LATEST_VER.get("zip")):
            await event.edit(msgRep.UPDATE_FAILED)
            log.error("Failed to download latest release. Aborting process",
                      exc_info=True)
            _LATEST_VER.clear()
            return
        release_ver = _LATEST_VER.get("version")
        _LATEST_VER.clear()
        commit_id = _get_commit_id()
        if not commit_id:
            await event.edit(msgRep.UPDATE_FAILED)
            return
        if isWindows():
            _print_instructions(commit_id)
            await event.edit(msgRep.DOWNLOAD_SUCCESS_WIN)
        else:
            await event.edit(msgRep.DOWNLOAD_SUCCESS)
            if _set_autoupdate(event.chat_id, event.message.id,
                               release_ver, commit_id):
                await event.client.disconnect()
            else:
                await event.edit(msgRep.START_RECOVERY_FAILED)
        return

    try:
        release_data = getLatestData("prototype74/HyperUBot")
    except Exception:
        await event.edit(msgRep.UPDATE_FAILED)
        log.error("Failed to get latest release", exc_info=True)
        return

    try:
        tag_version = release_data["tag_name"][1:]
        release_version = verAsTuple(tag_version)
    except ValueError:
        await event.edit(msgRep.UPDATE_FAILED)
        log.error("Invalid tag version from release", exc_info=True)
        return
    except Exception:
        await event.edit(msgRep.UPDATE_FAILED)
        log.error("Failed to parse tag version from release", exc_info=True)
        return

    if VERSION_TUPLE > release_version:
        log.warning(f"Current version newer than on release server "
                    f"({VERSION} > {tag_version})")
        await event.edit(f"{msgRep.UPDATE_FAILED}: "
                         f"{msgRep.UPDATE_INTERNAL_FAILED}")
        if _LATEST_VER:
            _LATEST_VER.clear()
        return

    if VERSION_TUPLE == release_version:
        log.info(f"Already up-to-date")
        reply = f"**{msgRep.ALREADY_UP_TO_DATE}**\n\n"
        if git_repo:
            reply += f"{warn_emoji} __{msgRep.GIT_REPO}__\n\n"
        reply += f"{msgRep.LATEST}: {tag_version}\n"
        reply += f"{msgRep.CURRENT}: {VERSION}\n"
        if _LATEST_VER:
            _LATEST_VER.clear()
        await event.edit(reply)
        return

    if VERSION_TUPLE < release_version:
        _LATEST_VER["version"] = tag_version
        try:
            assets = release_data.get("assets", [])
            if assets:
                for asset in assets:
                    if asset.get("name", "") == "rules.py":
                        _LATEST_VER["rules"] = asset.get(
                                                   "browser_download_url")
                        break
        except Exception:
            await event.edit(msgRep.UPDATE_FAILED)
            log.error("Failed to get assets from release", exc_info=True)
            return
        _LATEST_VER["zip"] = release_data.get("zipball_url")
        release_url = release_data.get("html_url")
        publish_date = _parse_datetime(release_data["published_at"])
        log.info(f"An Update to {tag_version} is available")
        reply = f"**{msgRep.UPDATE_AVAILABLE}**\n\n"
        if git_repo:
            reply += f"{warn_emoji} __{msgRep.GIT_REPO}__\n\n"
        reply += f"**{msgRep.LATEST}: {tag_version}**\n"
        reply += f"{msgRep.CURRENT}: {VERSION}\n"
        reply += (f"{msgRep.RELEASE_DATE}: {publish_date}\n\n"
                  if publish_date else "\n")
        reply += msgRep.CHANGELOG_AT.format(f"[GitHub]({release_url})\n\n")
        if update_now:
            reply += msgRep.DOWNLOADING_RELEASE
            await event.edit(reply)
            if not _get_latest_release(_LATEST_VER.get("rules"),
                                       _LATEST_VER.get("zip")):
                await event.edit(reply.replace(msgRep.DOWNLOADING_RELEASE,
                                               msgRep.UPDATE_FAILED))
                log.error("Failed to download latest release. "
                          "Aborting process", exc_info=True)
                _LATEST_VER.clear()
                return
            _LATEST_VER.clear()
            commit_id = _get_commit_id()
            if not commit_id:
                await event.edit(reply.replace(msgRep.DOWNLOADING_RELEASE,
                                               msgRep.UPDATE_FAILED))
                return
            if isWindows():
                _print_instructions(commit_id)
                await event.edit(reply.replace(msgRep.DOWNLOADING_RELEASE,
                                               msgRep.DOWNLOAD_SUCCESS_WIN))
            else:
                await event.edit(reply.replace(msgRep.DOWNLOADING_RELEASE,
                                               msgRep.DOWNLOAD_SUCCESS))
                if _set_autoupdate(event.chat_id, event.message.id,
                                   tag_version, commit_id):
                    await event.client.disconnect()
                else:
                    await event.edit(
                        reply.replace(msgRep.DOWNLOAD_SUCCESS,
                                      msgRep.START_RECOVERY_FAILED))
        else:
            reply += msgRep.UPDATE_QUEUED
            await event.edit(reply)
    return


if _update_scheduler:
    @_scheduler.scheduled_job("interval",
                              days=1,
                              next_run_time=(datetime.now() +
                                             timedelta(minutes=10)),
                              id="updater_job_1")
    async def update_scheduler():
        try:
            release_data = getLatestData("prototype74/HyperUBot")
        except Exception:
            log.warning("[NOTIFIER] Failed to get latest release")
            return

        try:
            tag_version = release_data["tag_name"][1:]
            release_version = verAsTuple(tag_version)
        except ValueError:
            log.warning("[NOTIFIER] Invalid tag version from release")
            return
        except Exception:
            log.warning("[NOTIFIER] Failed to parse tag version from release")
            return

        if VERSION_TUPLE < release_version:
            log.info(f"[NOTIFIER] An Update to {tag_version} is available")
            text = (f"**{msgRep.NOTIFIER_HEADER}**\n\n"
                    f"__{msgRep.NOTIFIER_INFO.format(tag_version)}__")
            try:
                me = await _tgclient.get_me()
                await _tgclient.send_message(me.id, text)
                try:
                    await _tgclient(MarkDialogUnreadRequest(me.id, True))
                except Exception as e:
                    log.warning("[NOTIFIER] Failed to set saved messages as "
                                f"unread: {e}")
            except Exception as e:
                log.warning("[NOTIFIER] Failed to send notification "
                            f"message: {e}")
            _scheduler.remove_job("updater_job_1")
            _scheduler.shutdown()
        return

    try:
        _scheduler.start()
    except (BaseException, Exception):
        _scheduler.shutdown()


register_cmd_usage(
    "update",
    usageRep.UPDATER_USAGE.get("update", {}).get("args"),
    usageRep.UPDATER_USAGE.get("update", {}).get("usage")
)
register_module_desc(descRep.UPDATER_DESC)
register_module_info(
    name="Updater",
    authors="nunopenim, prototype74",
    version=VERSION
)


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=(["_setprop", "setConfig", "_set_autoupdate"] +
           (["_tgclient"] if _update_scheduler else [])),
    warn_msg=("Access to protected attribute from Updater denied"
              "(requested by {1}:{2})"),
    mlogger=log
)
