# tguserbot Stuff
from tg_userbot import (tgclient, log, fhandler, PROJECT, OS, ALL_MODULES,
                        NOT_LOAD_MODULES, VERSION)

# Telethon Stuff
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

# Misc
from logging import shutdown
from importlib import import_module
from glob import glob
from os.path import dirname, basename, isfile


class Modules:
    def __init__(self):
        self.__imported_module = None
        self.__modules_count = 0
        self.__not_load_modules_count = 0

    def __all_modules(self) -> list:
        modules = []
        if OS and OS.startswith("win"):
            module_paths = glob(dirname(__file__) + "\\modules\\*.py")
        else:
            module_paths = glob(dirname(__file__) + "/modules/*.py")
        for module in module_paths:
            if isfile(module) and module.endswith(".py") and \
               not module.endswith("__init__.py"):
                filename = basename(module)[:-3]
                try:
                    if not filename in NOT_LOAD_MODULES:
                        modules.append(filename)
                except:
                    modules.append(filename)
        return sorted(modules)

    def load_modules(self) -> bool:
        ALL_MODULES = self.__all_modules()
        try:
            for module in ALL_MODULES:
                self.__imported_module = import_module("tg_userbot.modules." + module)
                self.__modules_count += 1
            for module in NOT_LOAD_MODULES:
                self.__not_load_modules_count += 1
            return True
        except ModuleNotFoundError as mnfe:
            log.error(f"Unable to load module: {mnfe}")
        except ImportError as ie:
            log.error(f"Unable to import module: {ie}")
        return False

    def loaded_modules(self) -> int:
        return self.__modules_count

    def not_loaded_modules(self) -> int:
        return self.__not_load_modules_count

if __name__ == "__main__":
    try:
        modules = Modules()
        if not modules.load_modules():
            quit(1)
        modules_count = modules.loaded_modules()
        not_load_modules_count = modules.not_loaded_modules()
        sum_modules = modules_count + not_load_modules_count
        with tgclient:
            tgclient.start()
            if not modules_count:
                log.warning("No module(s) available!")
            elif modules_count > 0:
                log.info(f"{modules_count} of {sum_modules} module(s) loaded!")
            log.info("%s %s: operational!", PROJECT, VERSION)
            me = tgclient.loop.run_until_complete(tgclient.get_me())
            log.info("You're logged in as: %s - ID: %s", me.first_name, me.id)
            tgclient.run_until_disconnected()
    except KeyboardInterrupt:
        log.info("Keyboard interruption. Terminating...")
    except PhoneNumberInvalidError:
        log.error("Invalid phone number!")
    except Exception as e:
        log.error(f"Unable to start userbot: {e}")

    try:
        if fhandler:
            fhandler.close()
        shutdown()
    except:
        pass
