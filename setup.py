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
from subprocess import check_call, check_output, DEVNULL  # noqa: E402
from sys import executable, platform  # noqa: E402
import json  # noqa: E402
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
    CYAN = "\033[96m"
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


def _check_setup_req() -> bool:
    setup_req = {}
    try:
        out = check_output([PY_EXEC, "-m", "pip", "list", "--format", "json"])
        out_json = json.loads(out)
        for elem in out_json:
            name = elem.get("name")
            ver = elem.get("version")
            if elem.get("name") == "Telethon" or \
               elem.get("name") == "pyAesCrypt":
                setup_req[name] = ver
    except:
        return False

    try:
        print()
        print("Checking for required packages...")
        print()
        if not setup_req.get("Telethon"):
            try:
                check_call(
                    [PY_EXEC, "-m", "pip", "install", "Telethon"],
                    stdout=DEVNULL,
                    stderr=DEVNULL)
            except Exception as e:
                print(
                    setColorText(
                        f"Failed to install Telethon package: {e}",
                        Colors.RED))
                return False
        else:
            telethon_version = tuple(
                map(int, setup_req.get("Telethon").split(".")))
            if telethon_version < (1, 23, 0):
                try:
                    check_call(
                        [PY_EXEC, "-m", "pip", "install", "--upgrade",
                         "Telethon"],
                        stdout=DEVNULL,
                        stderr=DEVNULL)
                except Exception as e:
                    print(
                        setColorText(
                            f"Failed to upgrade Telethon package: {e}",
                            Colors.RED))
                    return False
        if not setup_req.get("pyAesCrypt"):
            try:
                check_call(
                    [PY_EXEC, "-m", "pip", "install", "pyAesCrypt"],
                    stdout=DEVNULL,
                    stderr=DEVNULL)
            except Exception as e:
                print(
                    setColorText(
                        f"Failed to install pyAesCrypt package: {e}",
                        Colors.RED))
                return False
        else:
            pyAesCrypt_vesion = tuple(
                map(int, setup_req.get("pyAesCrypt").split(".")))
            if pyAesCrypt_vesion < (6, 0, 0):
                try:
                    check_call(
                        [PY_EXEC, "-m", "pip", "install", "--upgrade",
                         "pyAesCrypt"],
                        stdout=DEVNULL,
                        stderr=DEVNULL)
                except Exception as e:
                    print(
                        setColorText(
                            f"Failed to upgrade pyAesCrypt package: {e}",
                            Colors.RED))
                    return False
    except:
        return False
    return True


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
            try:
                api_key = input("Please enter your API Key: ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            try:
                api_key = int(api_key)
                break
            except:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        while True:
            try:
                api_hash = input("Please enter your API Hash: ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
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
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        pass
    return (None, None)


def _generateStringSession() -> tuple:
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    from telethon.errors.rpcerrorlist import (ApiIdInvalidError,
                                              PhoneNumberBannedError,
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
                "The phone number is not valid. Try again...", Colors.YELLOW))
        except PhoneNumberBannedError:
            print(setColorText(
                "The phone number is banned, probably forever. "
                "At this point there is nothing HyperUBot can do to fix it. "
                "The only possible way is to contact the Telegram Support",
                Colors.YELLOW))
            raise KeyboardInterrupt
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as e:
            print(setColorText(
                f"Unable to obtain a new string session: {e}", Colors.RED))
            break
    return (None, None, None)


def _run_userbot():
    try:
        tcmd = [PY_EXEC, "-m", "userbot"]
        os.execle(PY_EXEC, *tcmd, os.environ)
    except Exception as e:
        print(setColorText(f"Failed to start HyperUBot: {e}", Colors.RED))
    return


def main():
    print(setColorText("Welcome to HyperUBot's Setup Assistant!", Colors.CYAN))
    print("The Setup Assistant will guide you through all required "
          "processes to run HyperUBot on your device properly")
    print()

    while True:
        try:
            con = input("Continue? (y/n): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
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
        return

    secure_config = os.path.join(".", "userbot", "secure_config")

    if os.path.exists(secure_config) and os.path.isfile(secure_config):
        print(setColorText("Seems like the setup is completed already "
                           "or done manually", Colors.GREEN))
        while True:
            try:
                inp = input("Continue Setup Assistant? (y/n): ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if inp.lower() in ("y", "yes"):
                break
            elif inp.lower() in ("n", "no"):
                print("Alright, exiting Setup Assistant...")
                return
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

    if not _check_setup_req():
        print(setColorText("All or some packages required for Setup Assistant "
                           "are not present. Setup Assistant requires "
                           "'Telethon>=1.23.0' and 'pyAesCrypt>=6.0.0'. "
                           "Make sure these packages are installed in order "
                           "to continue. Exiting Setup Assistant...",
                           Colors.RED))
        return

    from pyAesCrypt import encryptFile

    print("HyperUBot requires, like all other Telegram userbots, "
          "an API Key, an API Hash and a String Session in order "
          "to run HyperUBot as an user client.\n"
          "If not done yet, please go to 'https://my.telegram.org' and\n"
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
    print()

    while True:
        try:
            inp = input("Ready? (y/n): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if inp.lower() in ("y", "yes"):
            break
        elif inp.lower() in ("n", "no"):
            print("Alright, exiting Setup Assistant...")
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
        print(
            setColorText("Feel free to contact us at Telegram "
                         "'https://t.me/HyperUBotSupport' if you need help "
                         "to handle this issue. Please keep a copy of the "
                         "error above ready or take a screenshot of it",
                         Colors.YELLOW))
        return

    print()
    print("As the API Key, API Hash and String Session are vaild, it's "
          "important to store them into a secured configuration file "
          "to avoid unauthorized access to these values. There is also an "
          "option to setup a password to your secured configuration "
          "to increase the security of your sensitive data. This is "
          "optional and not needed. This cannot be setup later.")
    print(setColorText("If you forgot your password, you have to create "
                       "a new secure configuration!",
                       Colors.YELLOW))
    print()

    set_pwd = False
    while True:
        try:
            inp = input("Set password? (y/n): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if inp.lower() in ("y", "yes"):
            set_pwd = True
            break
        elif inp.lower() in ("n", "no"):
            break
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    password = ""
    if set_pwd:
        print()
        from getpass import getpass
        print("Your password must have at least a length of 4 characters. "
              "Maximum length is 1024 characters \nNote: Your password is "
              "hidden while typing.")
        print()
        while True:
            try:
                password = getpass("Your password: ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if len(password) >= 4 and len(password) <= 1024:
                break
            elif len(password) < 4:
                print(setColorText("Password too short.", Colors.YELLOW))
            elif len(password) > 1024:
                print(setColorText("Password too long.", Colors.YELLOW))
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))
        while True:
            try:
                retype_pwd = getpass("Retype your password: ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if password == retype_pwd:
                break
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

    print()
    print("HyperUBot supports additional configurations such as logging, "
          "download path for temporary downloads etc.\n"
          "There are 3 types: Environment (config.env), configuration file "
          "(config.ini) and Python script (config.py).\n"
          "Which type of configuration file you wish to have?\n")
    print("[1] Environment (config.env)\n"
          "[2] Configuration file (config.ini)\n"
          "[3] Python script (config.py)\n")

    config_file = None

    while True:
        try:
            inp = input("Your input [1-3] (or 'X' to exit setup): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if inp == "1":
            config_file = os.path.join(".", "userbot", "config.env")
            break
        elif inp == "2":
            config_file = os.path.join(".", "userbot", "config.ini")
            break
        elif inp == "3":
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
        try:
            inp = input("Your input "
                        f"[{first_key_from_langs}-{last_key_from_langs}] "
                        "(or 'X' to exit setup): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
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

    print(f"Writing configuration files...")
    try:
        if os.path.exists("_temp.py"):
            os.remove("_temp.py")
        if os.path.exists(secure_config) and os.path.isfile(secure_config):
            os.remove(secure_config)
        secure_configs = (f'API_KEY = "{api_key}"\n'
                          f'API_HASH = "{api_hash}"\n'
                          f'STRING_SESSION = "{string_session}"')
        with open("_temp.py", "w") as temp_file:
            temp_file.write(secure_configs)
        temp_file.close()
        print(f"Securing API configurations...")
        encryptFile(infile="_temp.py",
                    outfile=secure_config,
                    passw=password,
                    bufferSize=(64 * 1024))
        os.remove("_temp.py")
        if not os.path.exists(secure_config):
            print(setColorText("Failed to secure configurations", Colors.RED))
            return
    except Exception as e:
        print(
            setColorText(f"Failed to secure configurations: {e}",
                         Colors.RED))
        return

    try:
        dl_path = os.path.join(".", "downloads")  # default path
        if config_file.endswith(".env"):
            configs = (f'UBOT_LANG = "{lang_code}"\n'
                       'LOGGING = False\n'
                       'LOGGING_CHATID = 0\n'
                       f'TEMP_DL_DIR = "{dl_path}"\n'
                       'NOT_LOAD_MODULES = []\n'
                       'COMMUNITY_REPOS = []\n'
                       'ALLOW_SIDELOAD = False\n')
        elif config_file.endswith(".ini"):
            configs = ('[CONFIGS]\n'
                       f'UBOT_LANG = {lang_code}\n'
                       'LOGGING = no\n'
                       'LOGGING_CHATID = 0\n'
                       f'TEMP_DL_DIR = {dl_path}\n'
                       'NOT_LOAD_MODULES = []\n'
                       'COMMUNITY_REPOS = []\n'
                       'ALLOW_SIDELOAD = no\n')
        else:  # py script
            configs = ('class ConfigClass(object):\n'
                       f'{"":4}UBOT_LANG = "{lang_code}"\n'
                       f'{"":4}LOGGING = False\n'
                       f'{"":4}LOGGING_CHATID = 0\n'
                       f'{"":4}TEMP_DL_DIR = "{dl_path}"\n'
                       f'{"":4}NOT_LOAD_MODULES = []\n'
                       f'{"":4}COMMUNITY_REPOS = []\n'
                       f'{"":4}ALLOW_SIDELOAD = False\n')
        with open(config_file, "w") as cfg_file:
            print(f"Writing optional configuration file in {config_file}")
            cfg_file.write(configs)
        cfg_file.close()
    except Exception as e:
        print(
            setColorText(f"Failed to write optional configuration file: {e}",
                         Colors.RED))
        return

    print("Installing required pip packages...")
    _install_requirements()

    print()
    print(setColorText("Yaaaay! Setup completed! :P", Colors.GREEN))
    print()
    start_bot_text = ("Do you wish to start HyperUBot now? You can always "
                      "start it by executing 'python3 -m userbot' in "
                      "HyperUBot's directory later.")

    if IS_WINDOWS:
        start_bot_text = start_bot_text.replace("python3", "python")

    print(start_bot_text)

    while True:
        try:
            inp = input("Start HyperUBot now? (y/n): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if inp.lower() in ("y", "yes"):
            _run_userbot()
            break
        elif inp.lower() in ("n", "no"):
            break
        else:
            print(setColorText("Invalid input. Try again...",
                               Colors.YELLOW))
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
    except (BaseException, Exception) as e:
        print(setColorText(f"Setup Assistant stopped: {e}",
                           Colors.RED_BG))
        quit(1)
    quit()
