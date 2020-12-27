# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, log, fhandler, PROJECT, OS, ALL_MODULES, LOAD_MODULES, VERSION, USER_MODULES
from userbot.sysutils.configuration import getConfig
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from logging import shutdown
from importlib import import_module
from glob import glob
from os.path import dirname, basename, isfile

class _Modules:
    def __init__(self):
        self.__imported_module = None
        self.__load_modules_count = 0
        self.__not_load_modules = getConfig("NOT_LOAD_MODULES", [])

    def __load_modules(self) -> tuple:
        all_modules = []
        sys_modules = []
        user_modules = []
        if OS and OS.startswith("win"):
            sys_module_paths = sorted(glob(dirname(__file__) + "\\modules\\*.py"))
            user_module_paths = sorted(glob(dirname(__file__) + "\\modules_user\\*.py"))
        else:
            sys_module_paths = sorted(glob(dirname(__file__) + "/modules/*.py"))
            user_module_paths = sorted(glob(dirname(__file__) + "/modules_user/*.py"))
        for module in sys_module_paths:
            if isfile(module) and module.endswith(".py"):
                filename = basename(module)[:-3]
                all_modules.append(filename)
                try:
                    if not filename in self.__not_load_modules:
                        sys_modules.append(filename)
                except:
                    sys_modules.append(filename)
        for module in user_module_paths:
            if isfile(module) and module.endswith(".py"):
                filename = basename(module)[:-3]
                all_modules.append(filename)
                if not filename in sys_modules:
                    user_modules.append(filename)
                else:
                    log.warning(f"Module '{filename}' not loaded as present in sys already")
        return (all_modules, sys_modules, user_modules)

    def import_load_modules(self) -> bool:
        def tryImportModule(path, module) -> bool:
            try:
                self.__imported_module = import_module(path + module)
                return True
            except ModuleNotFoundError as mnfe:
                raise ModuleNotFoundError(mnfe)
            except Exception:
                log.error(f"Unable to start module '{module}' due to an unhandled exception", exc_info=True)
            return False

        all_modules, sys_modules, user_modules = self.__load_modules()
        try:
            for module in sorted(all_modules):
                ALL_MODULES.append(module)
            for module in sys_modules:
                if tryImportModule("userbot.modules.", module):
                    LOAD_MODULES[module] = True
                    self.__load_modules_count += 1
                else:
                    LOAD_MODULES[module] = False
            for module in user_modules:
                if not module in self.__not_load_modules:
                    if tryImportModule("userbot.modules_user.", module):
                        LOAD_MODULES[module] = True
                        self.__load_modules_count += 1
                    else:
                        LOAD_MODULES[module] = False
                USER_MODULES.append(module)
            return True
        except ModuleNotFoundError as mnfe:
            log.error(f"Unable to load module: {mnfe}", exc_info=True)
        return False

    def loaded_modules(self) -> int:
        return self.__load_modules_count

if __name__ == "__main__":
    try:
        log.info("Loading resources and modules")
        modules = _Modules()
        if not modules.import_load_modules():
            quit(1)
        load_modules_count = modules.loaded_modules()
        sum_modules = len(ALL_MODULES)
        if not load_modules_count:
            log.warning("No module(s) loaded!")
        elif load_modules_count > 0:
            log.info(f"Modules ({load_modules_count}/{sum_modules}) loaded and ready")
        log.info("Starting Telegram client")
        with tgclient:
            me = tgclient.loop.run_until_complete(tgclient.get_me())
            log.info("You're running %s v%s as %s (ID: %s)", PROJECT, VERSION, me.first_name, me.id)
            tgclient.run_until_disconnected()
    except KeyboardInterrupt:
        log.info("Keyboard interruption. Terminating...")
    except PhoneNumberInvalidError:
        log.error("Invalid phone number!")
    except Exception as e:
        log.critical(f"Unable to start userbot: {e}", exc_info=True)

    try:
        if fhandler:
            fhandler.close()
        shutdown()  # shutdown logging
    except:
        pass
