# Copyright 2020-2022 nunopenim @github
# Copyright 2020-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import (_tgclient, log, __hyper_logger__, _services,
                     _getprop, _setprop, PROJECT, SAFEMODE)
from userbot._core.module_loader import import_module, start_language_processor
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.registration import (getAllModules, getLoadModules,
                                           getRegisteredCMDs)
from userbot.sysutils.sys_funcs import isWindows, verAsTuple
from userbot.version import VERSION, VERSION_TUPLE
from telethon.errors.rpcerrorlist import (ApiIdInvalidError,
                                          PhoneNumberBannedError,
                                          PhoneNumberInvalidError)
from logging import shutdown
from glob import glob
import os


def init_load_modules():
    built_in_modules_path = sorted(
        glob(os.path.join(os.path.dirname(__file__), "modules", "*.py")))
    user_modules_path = sorted(
        glob(os.path.join(os.path.dirname(__file__), "modules_user", "*.py")))
    for module in built_in_modules_path:
        if os.path.isfile(module) and \
           not os.path.basename(module).startswith("__") and \
           module.endswith(".py"):
            filename = os.path.basename(module)[:-3]
            import_module(filename, False, False)
    for module in user_modules_path:
        if os.path.isfile(module) and \
           not os.path.basename(module).startswith("__") and \
           module.endswith(".py"):
            filename = os.path.basename(module)[:-3]
            import_module(filename, True, False)
    return


def start_modules():
    if SAFEMODE:
        log.info("Starting built-in modules only...")
    else:
        log.info("Starting modules...")
    try:
        init_load_modules()
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
                _services._reboot_recovery(False)
            elif option == 2:
                log.info(contact_text)
                raise KeyboardInterrupt
            elif option == 4:
                raise KeyboardInterrupt
    load_modules_count = 0
    for is_running in getLoadModules().values():
        if is_running:
            load_modules_count += 1
    sum_modules = len(getAllModules())
    reg_features = len(getRegisteredCMDs())
    if load_modules_count > 0:
        log.info(f"Modules ({load_modules_count}/{sum_modules}) "
                 "started and ready!")
    else:
        log.warning("No modules started!")
    if reg_features > 0:
        log.info(f"A total of {reg_features} features were registered")
    else:
        log.info(f"No features were registered")
    return


async def check_last_reboot(client):
    if _getprop("reboot"):
        chat_id = _getprop("rebootchatid")
        msg_id = _getprop("rebootmsgid")
        msg = _getprop("rebootmsg")
        if _getprop("updateversion"):
            if not VERSION_TUPLE == verAsTuple(_getprop("updateversion")):
                msg = _getprop("updatefailedmsg")
            _setprop("updateversion", 0)
            _setprop("updatefailedmsg", 0)
        if chat_id and msg_id and msg:
            try:
                await client.edit_message(chat_id, msg_id, msg)
            except Exception as e:
                log.warning(f"Failed to edit (reboot) message: {e}")
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
             "commands in any chat: .status, .help or .mods. Need help with "
             "your new userbot? Check out our wiki "
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
    text += (f"{page_emoji} `.lcmds` (__{msg.INFO_OR}__ `.help`) - "
             f"__{msg.INFO_HELP.format('`.help status`')}__\n\n")
    text += (f"{disk_emoji} `.mods` - __{msg.INFO_MODULES}__\n\n")
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
        except Exception as e:
            log.warning(f"Failed to set saved messages as unread: {e}")
    except Exception as e:
        log.warning(f"Failed to send welcome message: {e}")
    return


def run_client():
    try:
        log.info("Starting Telegram client")
        with _tgclient:
            me = _tgclient.loop.run_until_complete(_tgclient.get_me())
            log.info(f"You're running {PROJECT} v{VERSION} as "
                     f"{me.first_name} (ID: {me.id})")
            if not _getprop("setupcompleted"):
                _tgclient.loop.run_until_complete(
                    send_welcome_msg(_tgclient, me.id))
                _setprop("setupcompleted", True)
            _tgclient.loop.run_until_complete(
                check_last_reboot(_tgclient))
            _tgclient.run_until_disconnected()
    except ApiIdInvalidError as ae:
        log.critical(f"App api_id and/or App api_hash is/are invalid: {ae}",
                     exc_info=True)
        log.warning("It may be possible that there is/are a typo in "
                    "your App api_id and/or App api_hash. If so, just start "
                    "'Secure-Config-Updater' and update them with your "
                    "correct keys")
        options = ["Start Secure-Config-Updater",
                   "Quit HyperUBot"]
        if isWindows():
            options[0] += " (python update_secure_cfg.py)"
            options.pop()
            _services._suggest_options(options)
            raise KeyboardInterrupt
        try:
            option = _services._suggest_options(options)
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if option == 1:
            _services._start_scfg_updater()
        elif option == 2:
            raise KeyboardInterrupt
    except PhoneNumberInvalidError:
        log.critical("Phone number is not valid", exc_info=True)
        options = ["Start String Session Generator",
                   "Quit HyperUBot"]
        if isWindows():
            options[0] += " (python generate_session.py)"
            options.pop()
            _services._suggest_options(options)
            raise KeyboardInterrupt
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
    except ConnectionError:
        log.error("Connection to Telegram servers failed!",
                  exc_info=True)
        log.warning("Please check your network connection and try it again. "
                    "If, however, your network connection works fine, it "
                    "may be possible that the Telegram servers are down "
                    "temporary")
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
    except Exception:
        print("Exception: Failed to close logger")
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
    try:
        start_language_processor()
    except SystemExit:
        log.error("Language processor stopped the process")
        return
    except (ModuleNotFoundError, BaseException, Exception):
        return
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
