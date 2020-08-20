# tguserbot Stuff
from tg_userbot import bot, LOGS, PROJECT, VERSION
from tg_userbot.modules import ALL_MODULES

# Telethon Stuff
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

# Misc
from importlib import import_module


class Modules:
    def __init__(self):
        self.__imported_module = None
        self.__modules_count = 0

    def load_modules(self) -> bool:
        try:
            for module in ALL_MODULES:
                self.__imported_module = import_module("tg_userbot.modules." + module)
                self.__modules_count += 1
            return True
        except ModuleNotFoundError as mnfe:
            LOGS.error(f"Unable to load module: {mnfe}")
        except ImportError as ie:
            LOGS.error(f"Unable to import module: {ie}")
        return False

    def loaded_module(self) -> int:
        return self.__modules_count

if __name__ == "__main__":
    try:
        modules = Modules()
        if not modules.load_modules():
            quit(1)
        modules_count = modules.loaded_module()
        with bot:
            bot.start()
            if not modules_count:
                LOGS.warning("No module(s) available!")
            elif modules_count > 0:
                LOGS.info(f"{modules_count} module(s) loaded!")
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

