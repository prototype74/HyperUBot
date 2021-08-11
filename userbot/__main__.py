# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, log, _hyper_logger, PROJECT, SAFEMODE
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.registration import (update_all_modules,
                                           update_load_modules,
                                           update_user_modules,
                                           getAllModules)
from userbot.version import VERSION
from logging import shutdown
from importlib import import_module
from glob import glob
from os import execle, environ
from os.path import dirname, basename, isfile, join
from sys import executable


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
                                "present in sys already")
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
        log.info("Starting system modules only")
    else:
        log.info("Starting modules")
    modules = _Modules()
    try:
        modules.import_load_modules()
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except (BaseException, Exception) as e:
        log.critical(f"Failed to start modules: {e}", exc_info=True)
    load_modules_count = modules.loaded_modules()
    sum_modules = len(getAllModules())
    if not load_modules_count:
        log.warning("No modules started!")
    elif load_modules_count > 0:
        log.info(f"Modules ({load_modules_count}/{sum_modules}) "
                 "started and ready!")
    return


def run_client():
    try:
        log.info("Starting Telegram client")
        with tgclient:
            me = tgclient.loop.run_until_complete(tgclient.get_me())
            log.info(f"You're running {PROJECT} v{VERSION} as "
                     f"{me.first_name} (ID: {me.id})")
            tgclient.run_until_disconnected()
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except (BaseException, Exception) as e:
        log.critical(f"Client has stopped: {e}", exc_info=True)
    return


def shutdown_logging():
    try:
        _hyper_logger._stop_logging()
        shutdown()
    except:
        pass
    return


def check_reboot():
    perf_reboot = getConfig("REBOOT", False)
    start_recovery = getConfig("START_RECOVERY", False)
    try:
        if perf_reboot or start_recovery:
            py_exec = (executable
                       if " " not in executable else '"' + executable + '"')
            if perf_reboot:  # preferred if True
                if getConfig("REBOOT_SAFEMODE"):
                    log.info("Rebooting into safe mode...")
                    tcmd = [py_exec, "-m", "userbot", "-safemode"]
                else:
                    log.info("Performing normal reboot...")
                    tcmd = [py_exec, "-m", "userbot"]
            elif start_recovery:
                commit_id = getConfig("UPDATE_COMMIT_ID")
                if commit_id:
                    log.info("Starting auto update in recovery...")
                    tcmd = [py_exec, "recovery.py", "-autoupdate", commit_id]
                else:
                    log.info("Rebooting into recovery...")
                    tcmd = [py_exec, "recovery.py"]
            shutdown_logging()
            execle(py_exec, *tcmd, environ)
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
        log.info("Keyboard interruption. Exiting...")
    except (BaseException, Exception) as e:
        log.critical(f"HyperUBot has stopped: {e}", exc_info=True)
        quit(1)
    finally:
        shutdown_logging()
    quit()
