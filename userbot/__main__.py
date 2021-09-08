# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import (tgclient, log, __hyper_logger__, _services,
                     _getprop, _setprop, PROJECT, SAFEMODE)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.registration import (update_all_modules,
                                           update_load_modules,
                                           update_user_modules,
                                           getAllModules)
from userbot.sysutils.sys_funcs import botVerAsTuple, isWindows, verAsTuple
from userbot.version import VERSION
from telethon.errors.rpcerrorlist import (ApiIdInvalidError,
                                          PhoneNumberBannedError,
                                          PhoneNumberInvalidError)
from logging import shutdown
from importlib import import_module
from glob import glob
from os.path import dirname, basename, isfile, join
import asyncio


class _Modules:
    def __init__(self):
        self.__imported_module = None
        self.__load_modules_count = 0
        self.__not_load_modules = getConfig("NOT_LOAD_MODULES", [])

    def __load_modules(self) -> tuple:
        all_modules = []
        sys_modules = []
        user_modules = []
        sys_module_paths = sorted(
            glob(join(dirname(__file__), "modules", "*.py")))
        user_module_paths = sorted(
            glob(join(dirname(__file__), "modules_user", "*.py")))
        for module in sys_module_paths:
            if isfile(module) and not basename(module).startswith("__") and \
               module.endswith(".py"):
                filename = basename(module)[:-3]
                all_modules.append(filename)
                try:
                    if filename not in self.__not_load_modules:
                        sys_modules.append(filename)
                except:
                    sys_modules.append(filename)
        for module in user_module_paths:
            if isfile(module) and not basename(module).startswith("__") and \
               module.endswith(".py"):
                filename = basename(module)[:-3]
                all_modules.append(filename)
                if filename not in sys_modules:
                    user_modules.append(filename)
                elif not SAFEMODE:
                    log.warning(f"Module '{filename}' not loaded as "
                                "present as built-in module already")
        return (all_modules, sys_modules, user_modules)

    def import_load_modules(self):
        def tryImportModule(path, module) -> bool:
            try:
                self.__imported_module = import_module(path + module)
                return True
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (BaseException, Exception):
                log.error(f"Unable to start module '{module}' due "
                          "to an unhandled exception",
                          exc_info=True)
            return False
        try:
            all_modules, sys_modules, user_modules = self.__load_modules()
            for module in sorted(all_modules):
                update_all_modules(module)
            for module in sys_modules:
                if tryImportModule("userbot.modules.", module):
                    update_load_modules(module, True)
                    self.__load_modules_count += 1
                else:
                    update_load_modules(module, False)
            for module in user_modules:
                if not SAFEMODE:
                    if module not in self.__not_load_modules:
                        if tryImportModule("userbot.modules_user.", module):
                            update_load_modules(module, True)
                            self.__load_modules_count += 1
                        else:
                            update_load_modules(module, False)
                update_user_modules(module)
        except:
            raise
        return

    def loaded_modules(self) -> int:
        return self.__load_modules_count


def start_modules():
    if SAFEMODE:
        log.info("Starting built-in modules only")
    else:
        log.info("Starting modules")
    modules = _Modules()
    try:
        modules.import_load_modules()
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except (BaseException, Exception) as e:
        log.critical(f"Failed to start modules: {e}", exc_info=True)
        options = ["Start Recovery",
                   "Contact support",
                   "Keep HyperUBot running",
                   "Quit HyperUBot"]
        contact_text = ("That all modules are failing to start shouldn't "
                        "happen. Feel free to contact us at Telegram "
                        "'https://t.me/HyperUBotSupport' and keep your "
                        "hyper.log file ready!")
        if isWindows():
            options[0] += " (python recovery.py)"
            options[1] = contact_text
            options.pop()
            options.pop()
            _services._suggest_options(options)
            while True:
                try:
                    inp = input("Keep HyperUBot running? (y/n): ")
                except KeyboardInterrupt:
                    print()
                    raise KeyboardInterrupt
                if inp.lower() in ("y", "yes"):
                    break
                elif inp.lower() in ("n", "no"):
                    raise KeyboardInterrupt
                else:
                    log.warning("Invalid input. Try again...")
        else:
            try:
                option = _services._suggest_options(options)
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if option == 1:
                vices._reboot_recovery(False)
            elif option == 2:
                log.info(contact_text)
                raise KeyboardInterrupt
            elif option == 4:
                raise KeyboardInterrupt
    load_modules_count = modules.loaded_modules()
    sum_modules = len(getAllModules())
    if not load_modules_count:
        log.warning("No modules started!")
    elif load_modules_count > 0:
        log.info(f"Modules ({load_modules_count}/{sum_modules}) "
                 "started and ready!")
    return


async def check_last_reboot(client):
    if _getprop("reboot"):
        chat_id = _getprop("rebootchatid")
        msg_id = _getprop("rebootmsgid")
        msg = _getprop("rebootmsg")
        if _getprop("updateversion"):
            if not botVerAsTuple() == verAsTuple(_getprop("updateversion")):
                msg = _getprop("updatefailedmsg")
            _setprop("updateversion", 0)
            _setprop("updatefailedmsg", 0)
        if chat_id and msg_id and msg:
            try:
                await client.edit_message(chat_id, msg_id, msg)
            except:
                log.warning("Failed to edit (reboot) message")
        # reset props
        _setprop("reboot", False)
        _setprop("rebootchatid", 0)
        _setprop("rebootmsgid", 0)
        _setprop("rebootmsg", 0)
    return


async def send_welcome_msg(client, ownerID: int):
    from userbot.include.language_processor import WelcomeText as msg
    log.info("Welcome to HyperUBot! You made it to run HyperUBot on your "
             "machine. What's next? Get surprised by running the following "
             "commands in any chat: .status, .help or .modules. Need help "
             "with your new userbot? Check out our wiki "
             "'https://github.com/prototype74/HyperUBot/wiki' or chat with "
             "us in our support group 'https://t.me/HyperUBotSupport'. "
             "Have fun!")
    robo_face = u"\U0001F916"
    pager_emoji = u"\U0001F4DF"
    page_emoji = u"\U0001F4C4"
    disk_emoji = u"\U0001F4BE"
    pkg_emoji = u"\U0001F4E6"
    text = f"**{msg.WELCOME_TO_HYPERUBOT}** {robo_face}\n\n"
    text += (f"{msg.INFO}:\n\n")
    text += (f"{pager_emoji} `.status` - __{msg.INFO_STATUS}__\n\n")
    text += (f"{page_emoji} `.listcmds` (__{msg.INFO_OR}__ `.help`) - "
             f"__{msg.INFO_HELP.format('`.help status`')}__\n\n")
    text += (f"{disk_emoji} `.modules` - __{msg.INFO_MODULES}__\n\n")
    text += (f"{pkg_emoji} `.pkg` - __{msg.INFO_PKG}__\n\n")
    supp_link = f"[{msg.INFO_SUPPORT_LINK}](https://t.me/HyperUBotSupport)"
    wiki_link = (f"[{msg.INFO_SUPPORT_WIKI}]"
                 f"(https://github.com/prototype74/HyperUBot/wiki)")
    text += (f"{msg.INFO_SUPPORT.format(wiki_link, supp_link)}\n\n")
    text += msg.INFO_FUN
    try:
        await client.send_message(ownerID, text, link_preview=False)
        try:
            from telethon.tl.functions.messages import MarkDialogUnreadRequest
            await client(MarkDialogUnreadRequest(ownerID, True))
        except:
            pass
    except:
        log.warning("Failed to send welcome message")
    return


def run_client():
    try:
        log.info("Starting Telegram client")
        with tgclient:
            me = tgclient.loop.run_until_complete(tgclient.get_me())
            log.info(f"You're running {PROJECT} v{VERSION} as "
                     f"{me.first_name} (ID: {me.id})")
            if not _getprop("setupcompleted"):
                asyncio.get_event_loop().run_until_complete(
                    send_welcome_msg(tgclient, me.id))
                _setprop("setupcompleted", True)
            asyncio.get_event_loop().run_until_complete(
                check_last_reboot(tgclient))
            tgclient.run_until_disconnected()
    except ApiIdInvalidError as ae:
        log.critical(f"API Key and/or API Hash is/are invalid: {ae}",
                     exc_info=True)
        log.warning("It may be possible that there is/are a typo in "
                    "your API Key and/or API Hash. If so, just start "
                    "'Secure-Config-Updater' and update them with your "
                    "correct keys")
        options = ["Start Secure-Config-Updater",
                   "Quit HyperUBot"]
        if isWindows():
            options[0] += " (python update_secure_cfg.py)"
            options.pop()
            _services._suggest_options(options)
            raise KeyboardInterrupt
        else:
            try:
                option = _services._suggest_options(options)
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if option == 1:
                _services._start_scfg_updater()
            elif option == 2:
                KeyboardInterrupt
    except PhoneNumberInvalidError:
        log.critical("Phone number is not valid", exc_info=True)
        options = ["Start String Session Generator",
                   "Quit HyperUBot"]
        if isWindows():
            options[0] += " (python generate_session.py)"
            options.pop()
            _services._suggest_options(options)
            raise KeyboardInterrupt
        else:
            try:
                option = _services._suggest_options(options)
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if option == 1:
                _services._start_session_gen()
            if option == 2:
                raise KeyboardInterrupt
    except PhoneNumberBannedError as pbe:
        log.critical(f"Phone number banned: {pbe}", exc_info=True)
        log.warning("The phone number is banned, something HyperUBot can't "
                    "fix. Please contact the Telegram Support")
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except (BaseException, Exception) as e:
        log.critical(f"Client has stopped: {e}", exc_info=True)
        options = ["Start Recovery",
                   "Contact support",
                   "Quit HyperUBot"]
        contact_text = ("If you facing issues with HyperUBot contact us at "
                        "Telegram 'https://t.me/HyperUBotSupport' and keep "
                        "your hyper.log file ready!")
        if isWindows():
            options[0] += " (python recovery.py)"
            options[1] = contact_text
            options.pop()
            _services._suggest_options(options)
            raise KeyboardInterrupt
        else:
            try:
                option = _services._suggest_options(options)
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if option == 1:
                _services._reboot_recovery(False)
            elif option == 2:
                log.info(contact_text)
                raise KeyboardInterrupt
            elif option == 3:
                raise KeyboardInterrupt
    return


def shutdown_logging():
    try:
        __hyper_logger__._stop_logging()
        shutdown()
    except:
        pass
    return


def check_reboot():
    perf_reboot = getConfig("REBOOT", False)
    start_recovery = getConfig("START_RECOVERY", False)
    try:
        if perf_reboot or start_recovery:
            if perf_reboot:  # preferred if True
                if getConfig("REBOOT_SAFEMODE"):
                    _services._reboot(True)
                else:
                    _services._reboot()
            elif start_recovery:
                commit_id = getConfig("UPDATE_COMMIT_ID")
                if commit_id:
                    _services._reboot_recovery(True, commit_id)
                else:
                    _services._reboot_recovery(False)
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except (BaseException, Exception) as e:
        if start_recovery:
            log.critical(f"Failed to reboot HyperUBot into recovery: {e}",
                         exc_info=True)
        else:
            log.critical(f"Failed to reboot HyperUBot: {e}",
                         exc_info=True)
    return


def main():
    start_modules()
    log.info("HyperUBot is going online")
    run_client()
    log.info("HyperUBot is offline")
    check_reboot()
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.info("Exiting...")
    except (BaseException, Exception) as e:
        log.critical(f"HyperUBot has stopped: {e}", exc_info=True)
        quit(1)
    finally:
        shutdown_logging()
    quit()
