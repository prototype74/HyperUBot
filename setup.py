# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from sys import version_info

if (version_info.major, version_info.minor) < (3, 8):
    print("Python v3.8+ is required! Please update "
          "Python to v3.8 or newer "
          "(current version: {}.{}.{}).".format(
              version_info.major, version_info.minor, version_info.micro))
    quit(1)

from platform import system  # noqa: E402
from subprocess import check_call  # noqa: E402
from sys import executable, platform  # noqa: E402
import os  # noqa: E402

IS_WINDOWS = (True if system().lower() == "windows" or
              os.name == "nt" or platform.startswith("win") else False)
PY_EXEC = executable if " " not in executable else '"' + executable + '"'
WIN_COLOR_ENABLED = False

try:
    if IS_WINDOWS:
        import colorama
        colorama.init()
        WIN_COLOR_ENABLED = True
except:
    pass


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED_BG = "\033[101m"
    END = "\033[0m"


def setColorText(text: str, color: Colors) -> str:
    if IS_WINDOWS and not WIN_COLOR_ENABLED:
        return text  # don't use ANSI codes
    return color + text + Colors.END


def _userbot_installed() -> bool:
    if not os.path.exists(os.path.join(".", "userbot")) or \
       not os.path.exists(os.path.join(".", "userbot", "__init__.py")) or \
       not os.path.exists(os.path.join(".", "userbot", "__main__.py")):
        return False
    return True


def _installTelethon(upgrade: bool = False) -> bool:
    try:
        if upgrade:
            check_call(
                [PY_EXEC, "-m", "pip", "install", "--upgrade", "Telethon"])
        else:
            check_call(
                [PY_EXEC, "-m", "pip", "install", "Telethon"])
        return True
    except Exception as e:
        if upgrade:
            print(setColorText(
                f"Failed to upgrade Telethon package: {e}", Colors.RED))
        else:
            print(setColorText(
                f"Failed to install Telethon package: {e}", Colors.RED))
    return False


def _install_requirements():
    try:
        check_call(
            [PY_EXEC, "-m", "pip", "install", "-r", "requirements.txt"])
    except Exception as e:
        print(setColorText(
            f"Failed to install pip requirements: {e}", Colors.RED))
    return


def _getAPIs() -> tuple:
    api_key, api_hash = (None,)*2
    try:
        while True:
            api_key = input("Please enter your API Key: ")
            try:
                api_key = int(api_key)
                break
            except:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        while True:
            api_hash = input("Please enter your API Hash: ")
            if len(api_hash) == 32:
                break
            elif len(api_hash) > 0:
                print(setColorText("Invalid input. API Hash has a length of "
                                   "32 characters",
                                   Colors.YELLOW))
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))
        return (api_key, api_hash)
    except:
        pass
    return (None, None)


def _generateStringSession() -> tuple:
    from telethon.errors.rpcerrorlist import (ApiIdInvalidError,
                                              PhoneNumberInvalidError)
    while True:
        try:
            api_key, api_hash = _getAPIs()
            if not api_key:
                break
            if not api_hash:
                break
            client = TelegramClient(StringSession(), api_key, api_hash)
            with client:
                string_session = client.session.save()
            return (api_key, api_hash, string_session)
        except ApiIdInvalidError:
            print(setColorText(
                "API Key and/or API Hash incorrect. Try again...",
                Colors.YELLOW))
        except PhoneNumberInvalidError:
            print(setColorText(
                "Phone number is not valid. Try again...", Colors.YELLOW))
        except Exception as e:
            print(setColorText(
                f"Unable to obtain new string session: {e}", Colors.RED))
            break
    return (None, None, None)


def _run_userbot():
    try:
        tcmd = [PY_EXEC, "-m", "userbot"]
        os.execle(PY_EXEC, *tcmd, os.environ)
    except Exception as e:
        print(setColorText(f"Failed to run HyperUBot: {e}", Colors.RED))
    return


if __name__ == "__main__":
    try:
        print("Welcome to HyperUBot's Setup Assistant!")
        print("This setup will guide you through required processes to run "
              "HyperUBot on your Machine")

        while True:
            con = input("Continue? (y/n): ")
            if con.lower() in ("y", "yes"):
                break
            elif con.lower() in ("n", "no"):
                # not actually a keyboard interruption but same result
                # as in KeyboardInterrupt exception block
                raise KeyboardInterrupt
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        if not _userbot_installed():
            print(setColorText("HyperUBot not installed", Colors.RED_BG))
            quit(1)

        if os.path.exists(os.path.join(".", "userbot", "config.env")) or \
           os.path.exists(os.path.join(".", "userbot", "config.py")):
            print(setColorText("Seems like the setup is completed already "
                               "or done manually", Colors.GREEN))
            quit()

        install_telethon_started = False

        while True:
            try:
                from telethon import version
                from telethon.sync import TelegramClient
                from telethon.sessions import StringSession
                break
            except:
                if not install_telethon_started:
                    print("Telethon package not installed. Installing...")
                    install_telethon_started = True
                    _installTelethon()
                else:
                    print(setColorText("Unable to import Telethon. "
                                       "Setup Assistant was not able to "
                                       "install the Telethon package",
                                       Colors.RED))
                    quit(1)

        telethon_version = tuple(map(int, version.__version__.split(".")))
        if telethon_version < (1, 21, 1):
            print("Upgrading Telethon first...\n", Colors.YELLOW)
            if not _installTelethon(True):
                quit(1)

        print("\nHyperUBot requires, like all other Telegram userbots, "
              "an API Key, an API Hash and a String Session in order "
              "to run HyperUBot as an user client.\n"
              "If not done yet, please go to https://my.telegram.org and\n"
              "1. log in into your Telegram account\n"
              "2. create a new application (or use an existing one)\n"
              "3. get your API Key and Hash (do NOT share these values with "
              "anyone else!)\n\n"
              "Please keep the following requirements ready to obtain a "
              "new String Session:\n"
              "- Your Telegram application's API Key and Hash (from your "
              "(existing) application (you created before))\n"
              "- Your Phone Number which you use for your Telegram account "
              "(required to log in into your account)\n"
              "- Your Account's password (Two-Step Verification; "
              "if enabled)\n")

        while True:
            inp = input("Ready? (y/n): ")
            if inp.lower() in ("y", "yes"):
                break
            elif inp.lower() in ("n", "no"):
                print("Alright, cancelling Setup Assistant")
                raise KeyboardInterrupt
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        api_key, api_hash, string_session = _generateStringSession()

        if not api_key or not api_hash or not string_session:
            print(
                setColorText("Setup Assistant failed to get a new "
                             "string session from your API Key/Hash",
                             Colors.RED))
            quit(1)

        print("\nAs the API Key, API Hash and String Session are vaild, it's "
              "important to store them into a configuration file to avoid "
              "being asked for these values everytime you run HyperUBot. "
              "HyperUBot supports 2 types: Environment (config.env) and "
              "Python script (config.py).\n"
              "Which type of configuration file you wish to have?\n")
        print("[1] Environment (config.env)\n"
              "[2] Python script (config.py)\n")

        config_file = None

        while True:
            inp = input("Your input [1-2] (or 'X' to cancel setup): ")
            if inp == "1":
                config_file = os.path.join(".", "userbot", "config.env")
                break
            elif inp == "2":
                config_file = os.path.join(".", "userbot", "config.py")
                break
            elif inp.lower() == "x":
                raise KeyboardInterrupt
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        langs = {"1": {"text": "English/English", "code": "en"},
                 "2": {"text": "German/Deutsch", "code": "de"},
                 "3": {"text": "Portuguese/Português", "code": "pt"}}

        lang_text = ("\nHyperUBot knows some different languages, not much "
                     "but still it does.\n"
                     "Please select your preferred language:\n\n")

        first_key_from_langs, last_key_from_langs = (0,)*2

        for key, value in langs.items():
            if not first_key_from_langs:
                first_key_from_langs = key
            language = value.get("text")
            language_code = value.get("code", "").upper()
            lang_text += f"[{key}] {language} ({language_code})\n"
            last_key_from_langs = key

        print(lang_text)
        lang_code = "en"  # default language

        while True:
            inp = input("Your input "
                        f"[{first_key_from_langs}-{last_key_from_langs}] "
                        "(or 'X' to cancel setup): ")
            if inp in langs.keys():
                for key, value in langs.items():
                    if inp == key:
                        lang_code = value.get("code")
                        break
                break
            elif inp.lower() == "x":
                raise KeyboardInterrupt
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        try:
            dl_path = os.path.join(".", "downloads")  # default path
            if config_file.endswith(".env"):
                configs = (f'API_KEY = "{api_key}"\n'
                           f'API_HASH = "{api_hash}"\n'
                           f'STRING_SESSION = "{string_session}"\n'
                           f'UBOT_LANG = "{lang_code}"\n'
                           'LOGGING = False\n'
                           'LOGGING_CHATID = 0\n'
                           f'TEMP_DL_DIR = "{dl_path}"\n'
                           'NOT_LOAD_MODULES = []\n'
                           'COMMUNITY_REPOS = []\n')
            else:  # py script
                configs = ('class ConfigClass(object):\n'
                           f'{"":4}API_KEY = "{api_key}"\n'
                           f'{"":4}API_HASH = "{api_hash}"\n'
                           f'{"":4}STRING_SESSION = "{string_session}"\n'
                           f'{"":4}UBOT_LANG = "{lang_code}"\n'
                           f'{"":4}LOGGING = False\n'
                           f'{"":4}LOGGING_CHATID = 0\n'
                           f'{"":4}TEMP_DL_DIR = "{dl_path}"\n'
                           f'{"":4}NOT_LOAD_MODULES = []\n'
                           f'{"":4}COMMUNITY_REPOS = []\n')
            with open(config_file, "w") as cfg_file:
                print(f"Writing configuration file in {config_file}")
                cfg_file.write(configs)
            cfg_file.close()
        except Exception as e:
            print(
                setColorText(f"Failed to write configuration file: {e}",
                             Colors.RED))
            quit(1)

        print("Installing required pip packages...")
        _install_requirements()

        print(setColorText("\nYaaaay! Setup completed! :P\n", Colors.GREEN))
        start_bot_text = ("Do you wish to run HyperUBot now? You can always "
                          "run it by executing 'python3 -m userbot' in "
                          "HyperUBot's directory later.")

        if IS_WINDOWS:
            start_bot_text = start_bot_text.replace("python3", "python")

        print(start_bot_text)

        while True:
            inp = input("Run HyperUBot now? (y/n): ")
            if inp.lower() in ("y", "yes"):
                _run_userbot()
                break
            elif inp.lower() in ("n", "no"):
                break
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(setColorText(f"Setup Assistant crashed: {e}", Colors.RED_BG))
        quit(1)
    quit()
