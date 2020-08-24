# tguserbot Stuff
from tg_userbot import bot, LOGS, PROJECT, NOT_LOAD_MODULES, VERSION
from tg_userbot.modules import ALL_MODULES

# Telethon Stuff
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

# Misc
from importlib import import_module


class Modules:
    def __init__(self):
        self.__imported_module = None
        self.__modules_count = 0
        self.__not_load_modules_count = 0

    def load_modules(self) -> bool:
        try:
            for module in ALL_MODULES:
                self.__imported_module = import_module("tg_userbot.modules." + module)
                self.__modules_count += 1
            for module in NOT_LOAD_MODULES:
                self.__not_load_modules_count += 1
            return True
        except ModuleNotFoundError as mnfe:
            LOGS.error(f"Unable to load module: {mnfe}")
        except ImportError as ie:
            LOGS.error(f"Unable to import module: {ie}")
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
        with bot:
            bot.start()
            if not modules_count:
                LOGS.warning("No module(s) available!")
            elif modules_count > 0:
                LOGS.info(f"{modules_count} of {sum_modules} module(s) loaded!")
            LOGS.info("%s %s: operational!", PROJECT, VERSION)
            me = bot.loop.run_until_complete(bot.get_me())
            LOGS.info("You're logged in as: %s - ID: %s", me.first_name, me.id)
            bot.run_until_disconnected()
    except KeyboardInterrupt:
        LOGS.info("Keyboard interruption. Terminating...")
    except PhoneNumberInvalidError:
        LOGS.error("Invalid phone number!")
    except Exception as e:
        LOGS.error(f"Unable to start userbot: {e}")

