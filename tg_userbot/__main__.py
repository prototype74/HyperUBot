# tguserbot Stuff
from tg_userbot import (tgclient, log, fhandler, PROJECT, OS, ALL_MODULES,
                        LOAD_MODULES, NOT_LOAD_MODULES, VERSION, USER_MODULES)

# Telethon Stuff
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

# Misc
from logging import shutdown
from importlib import import_module
from glob import glob
from os.path import dirname, basename, isfile


class _Modules:
    def __init__(self):
        self.__imported_module = None
        self.__load_modules_count = 0
        self.__not_load_modules_count = 0

    def __load_modules(self) -> list:
        if OS and OS.startswith("win"):
            module_paths = glob(dirname(__file__) + "\\modules\\*.py")
            user_paths = glob(dirname(__file__) + "\\modules_user\\*.py")
        else:
            module_paths = glob(dirname(__file__) + "/modules/*.py")
            user_paths = glob(dirname(__file__) + "/modules_user/*.py")
        for module in sorted(module_paths + user_paths):
            if isfile(module) and module.endswith(".py"):
                filename = basename(module)[:-3]
                ALL_MODULES.append(filename)
                try:
                    if not filename in NOT_LOAD_MODULES:
                        LOAD_MODULES.append(filename)
                except:
                    LOAD_MODULES.append(filename)
            if module in user_paths:
                USER_MODULES.append(filename)
        return LOAD_MODULES

    def import_load_modules(self) -> bool:
        load_modules = self.__load_modules()
        try:
            for module in load_modules:
                if module in USER_MODULES:
                    self.__imported_module = import_module("tg_userbot.modules_user." + module)
                else:
                    self.__imported_module = import_module("tg_userbot.modules." + module)
                self.__load_modules_count += 1
            if NOT_LOAD_MODULES:
                for module in NOT_LOAD_MODULES:
                    if module in ALL_MODULES:
                        self.__not_load_modules_count += 1
            return True
        except ModuleNotFoundError as mnfe:
            log.error(f"Unable to load module: {mnfe}")
        except ImportError as ie:
            log.error(f"Unable to import module: {ie}")
        return False

    def loaded_modules(self) -> int:
        return self.__load_modules_count

    def not_loaded_modules(self) -> int:
        return self.__not_load_modules_count

if __name__ == "__main__":
    try:
        modules = _Modules()
        if not modules.import_load_modules():
            quit(1)
        load_modules_count = modules.loaded_modules()
        not_load_modules_count = modules.not_loaded_modules()
        sum_modules = load_modules_count + not_load_modules_count
        with tgclient:
            tgclient.start()
            if not load_modules_count:
                log.warning("No module(s) available!")
            elif load_modules_count > 0:
                log.info(f"{load_modules_count} of {sum_modules} module(s) loaded!")
            log.info("%s %s: operational!", PROJECT, VERSION)
            me = tgclient.loop.run_until_complete(tgclient.get_me())
            log.info("You're logged in as: %s - ID: %s", me.first_name, me.id)
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
        shutdown()
    except:
        pass
