# Copyright 2021-2022 nunopenim @github
# Copyright 2021-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from sys import version_info

if (version_info.major, version_info.minor) < (3, 8):
    print("Python v3.8+ is required to start Setup Assistant! Please update "
          "Python to v3.8 or newer "
          "(current version: {}.{}.{}).".format(
              version_info.major, version_info.minor, version_info.micro))
    quit(1)

from platform import system  # noqa: E402
from subprocess import check_call, check_output, DEVNULL  # noqa: E402
from sys import argv, executable, platform, stdin  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402

IS_WINDOWS = (True if system().lower() == "windows" or
              os.name == "nt" or platform.startswith("win") else False)
PY_EXEC = executable if " " not in executable else '"' + executable + '"'
SECURE_CONFIG = os.path.join(".", "userbot", "secure_config")
NOPIP = False

if len(argv) >= 2:
    if argv[1].lower() == "-nopip":
        NOPIP = True

if IS_WINDOWS:
    try:
        import colorama
        colorama.init()
        WIN_COLOR_ENABLED = True
    except (ImportError, ModuleNotFoundError):
        WIN_COLOR_ENABLED = False
    except Exception as e:
        WIN_COLOR_ENABLED = False
        print(f"Exception: {e}")

if IS_WINDOWS:
    import msvcrt
else:
    import termios
    import tty


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


def _install_package(name: str, upgrade: bool = False) -> bool:
    try:
        if upgrade:
            print(f"Upgrading {name} package...")
            command = [PY_EXEC, "-m", "pip", "install", "--upgrade", name]
        else:
            print(f"Installing {name} package...")
            command = [PY_EXEC, "-m", "pip", "install", name]
        check_call(command, stdout=DEVNULL, stderr=DEVNULL)
        print(f"{name} package installed")
        return True
    except Exception as e:
        if upgrade:
            print(setColorText(f"Failed to upgrade {name} package: {e}",
                               Colors.RED))
        else:
            print(setColorText(f"Failed to install {name} package: {e}",
                               Colors.RED))
    return False


def _get_pip_packages() -> dict:
    setup_req = {}
    req_pip_names = ("Telethon", "pyAesCrypt", "cffi")
    try:
        out = check_output([PY_EXEC, "-m", "pip", "list", "--format", "json"],
                           stderr=DEVNULL)
        out_json = json.loads(out)
        for elem in out_json:
            name = elem.get("name")
            ver = elem.get("version")
            if ((name in req_pip_names) and len(setup_req) < 3):
                setup_req[name] = ver
    except Exception as e:
        print(setColorText(f"Unable to get installed packages: {e}",
                           Colors.RED))
        return {}
    return setup_req


def _check_setup_req() -> bool:
    print("Checking for required packages...")
    setup_req = _get_pip_packages()
    if not setup_req:
        return False

    req_pip_names = {
        "Telethon": (1, 24, 0),
        "pyAesCrypt": (6, 0, 0),
        "cffi": (1, 15, 0)
    }
    try:
        for name, ver in req_pip_names.items():
            if not setup_req.get(name):
                if not _install_package(name):
                    return False
            else:
                pkg_version = tuple(map(int, setup_req.get(name).split(".")))
                if pkg_version < ver:
                    if not _install_package(name, True):
                        return False
    except Exception as e:
        print(setColorText(f"Failed to check requirements: {e}",
                           Colors.RED))
        return False
    return True


def _install_requirements():
    try:
        check_call(
            [PY_EXEC, "-m", "pip", "install", "-r", "requirements.txt"],
            stderr=DEVNULL)
    except Exception as e:
        print(setColorText(
            f"Failed to install pip requirements: {e}", Colors.RED))
    return


def _getAPIs() -> tuple:
    while True:
        try:
            api_key = input("Please enter your App api_id: ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        try:
            api_key = int(api_key)
            break
        except ValueError:
            print(setColorText("Invalid input. Try again...",
                               Colors.YELLOW))

    while True:
        try:
            api_hash = input("Please enter your App api_hash: ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if len(api_hash) == 32:
            break
        elif len(api_hash) > 0:
            print(setColorText("Invalid input. API Hash should have a "
                               "length of 32 characters!",
                               Colors.YELLOW))
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))
    return (api_key, api_hash)


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
                "App api_id and/or App api_hash incorrect. Try again...",
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
            print()
            raise KeyboardInterrupt
        except Exception as e:
            print(setColorText(
                f"Unable to obtain a new string session: {e}", Colors.RED))
            break
    return (None, None, None)


# from userbot/sysutils/getpass.py
def _GetwchPOSIX():
    if IS_WINDOWS:
        return ""
    # based on: https://docs.python.org/3/library/termios.html#example
    fd = stdin.fileno()
    prev_attr = termios.tcgetattr(fd)
    try:
        tty.setraw(fd, termios.TCSAFLUSH)
        char = stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, prev_attr)
    return char


_getwch = msvcrt.getwch if IS_WINDOWS else _GetwchPOSIX


def _getpass(prompt):
    print(prompt, end="", flush=True)
    password_chars = []
    while True:
        char = _getwch()
        if ord(char) in (10, 13):
            break
        elif ord(char) in (8, 127):
            if len(password_chars) > 0:
                password_chars.pop()
                print("\b \b", end="", flush=True)
        elif ord(char) in (3,):
            raise KeyboardInterrupt
        else:
            password_chars.append(char)
            print("*", end="", flush=True)
    print()
    password = "".join(password_chars)
    return password


def _start_userbot():
    try:
        tcmd = [PY_EXEC, "-m", "userbot"]
        os.execle(PY_EXEC, *tcmd, os.environ)
    except Exception as e:
        print(setColorText(f"Failed to start HyperUBot: {e}", Colors.RED))
    return


def _greetings():
    print(setColorText("Welcome to HyperUBot's Setup Assistant!", Colors.CYAN))
    print("The Setup Assistant will guide you through all required "
          "processes to run HyperUBot on your device properly. It may "
          "be possible that the Setup Assistant will install some pip "
          "packages first which are required for the configurations "
          "of HyperUBot during the setup. All other pip packages "
          "which are required only while the bot is running will be "
          "installed at the end of the setup.")
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
            raise KeyboardInterrupt
        else:
            print(setColorText("Invalid input. Try again...",
                               Colors.YELLOW))
    return


def _check_setup_completed_already():
    if os.path.exists(SECURE_CONFIG) and os.path.isfile(SECURE_CONFIG):
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
                raise KeyboardInterrupt
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))
    return


def _pre_procedure():
    print("HyperUBot requires, like all other Telegram userbots, "
          "an App api_id (API Key), an App api_hash (API Hash) and a "
          "valid String Session in order to allow HyperUBot to login "
          "into your account to interact as 'user'bot. Please follow the "
          "steps below to obtain your API Key, API Hash and to finally "
          "get a String Session:")
    print()
    print("1. Login to My Telegram: https://my.telegram.org")
    print("2. Go to 'API development tools' and fill out the form")
    print("3. Get your App api_id and App api_hash. You will need them "
          "for the next step")
    print()
    print(setColorText("Note: Always remember not to share your "
                       "App api_id and App api_hash!", Colors.YELLOW))
    print()

    while True:
        try:
            inp = input("Continue? (y/n): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if inp.lower() in ("y", "yes"):
            break
        elif inp.lower() in ("n", "no"):
            raise KeyboardInterrupt
        else:
            print(setColorText("Invalid input. Try again...",
                               Colors.YELLOW))
    print()
    print("As we want to interact as user, the Telegram client will ask for "
          "your phone number, don't worry it's only required for "
          "user authorization and will not be send to anyone else. If "
          "Two-factor authentication (2FA) is enabled it will also ask for "
          "the account's password!")
    print()

    while True:
        try:
            inp = input("Ready? (y/n): ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if inp.lower() in ("y", "yes"):
            print()
            break
        elif inp.lower() in ("n", "no"):
            raise KeyboardInterrupt
        else:
            print(setColorText("Invalid input. Try again...",
                               Colors.YELLOW))
    return


def _post_procedure() -> bool:
    print("As the App api_id, App api_hash and String Session are valid, it's "
          "important to store them into a secured configuration file "
          "to avoid unauthorized access to these values. There is also an "
          "option to setup a password to your secured configuration "
          "to increase the security of your sensitive data. This is "
          "optional and not needed. This cannot be setup later.")
    print(setColorText("If you forgot your password, you have to create "
                       "a new secure configuration!",
                       Colors.YELLOW))
    print()

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
            set_pwd = False
            break
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))
    return set_pwd


def _setup_password() -> str:
    print("Your password must have at least a length of 4 characters. "
          "Maximum length is 1024 characters. You can anytime skip this by "
          "typing \"S\" as single character password.")
    print()
    while True:
        try:
            password = _getpass("Your new password: ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if len(password) >= 4 and len(password) <= 1024:
            break
        elif password.lower() == "s":
            print(setColorText("Continuing without password...",
                               Colors.YELLOW))
            return ""
        elif len(password) < 4:
            print(setColorText("Password too short.", Colors.YELLOW))
        elif len(password) > 1024:
            print(setColorText("Password too long.", Colors.YELLOW))
        else:
            print(setColorText("Invalid input. Try again...",
                               Colors.YELLOW))
    while True:
        try:
            retype_pwd = _getpass("Retype your password: ")
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        if password == retype_pwd:
            break
        elif retype_pwd.lower() == "s":
            print(setColorText("Continuing without password...",
                               Colors.YELLOW))
            return ""
        else:
            print(setColorText("Passwords did not match. Try again...",
                               Colors.YELLOW))
    return password


def _select_config_type() -> str:
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
    return config_file


def _select_language() -> str:
    langs = {"1": {"text": "English/English", "code": "en"},
             "2": {"text": "German/Deutsch", "code": "de"},
             "3": {"text": "Portuguese/Português", "code": "pt"}}

    lang_text = ("HyperUBot knows some different languages, not much "
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
    return lang_code


def _secure_configs(api_key: int, api_hash: str,
                    string_session: str, password: str) -> bool:
    from pyAesCrypt import encryptFile
    try:
        if os.path.exists("_temp.py"):
            os.remove("_temp.py")
        if os.path.exists(SECURE_CONFIG) and os.path.isfile(SECURE_CONFIG):
            os.remove(SECURE_CONFIG)
        secure_configs = (f'API_KEY = "{api_key}"\n'
                          f'API_HASH = "{api_hash}"\n'
                          f'STRING_SESSION = "{string_session}"')
        with open("_temp.py", "w") as temp_file:
            temp_file.write(secure_configs)
        temp_file.close()
        print(f"Securing API configurations...")
        encryptFile(infile="_temp.py",
                    outfile=SECURE_CONFIG,
                    passw=password,
                    bufferSize=(64 * 1024))
        os.remove("_temp.py")
        if not os.path.exists(SECURE_CONFIG):
            print(setColorText("Failed to secure configurations", Colors.RED))
            return False
    except Exception as e:
        print(
            setColorText(f"Failed to secure configurations: {e}",
                         Colors.RED))
        return False
    return True


def _optional_configs(config_file: str, lang_code: str) -> bool:
    try:
        dl_path = os.path.join(".", "downloads")  # default path
        if config_file.endswith(".env"):
            configs = (f'UBOT_LANG = "{lang_code}"\n'
                       'LOGGING = False\n'
                       'LOGGING_CHATID = 0\n'
                       f'TEMP_DL_DIR = "{dl_path}"\n'
                       'NOT_LOAD_MODULES = []\n'
                       'COMMUNITY_REPOS = []\n'
                       'ALLOW_SIDELOAD = False\n'
                       'PKG_ENABLE_AUTO_UPDATE = False\n'
                       'CLIENT_CONNECT_RETRIES = 5\n'
                       'CLIENT_RETRY_DELAY = 1\n'
                       'SIDELOAD_NO_REBOOT = False\n'
                       'TERMINAL_USE_BIN_BASH = False\n'
                       'UPDATER_ENABLE_SCHEDULER = False\n')
        elif config_file.endswith(".ini"):
            configs = ('[CONFIGS]\n'
                       f'UBOT_LANG = {lang_code}\n'
                       'LOGGING = no\n'
                       'LOGGING_CHATID = 0\n'
                       f'TEMP_DL_DIR = {dl_path}\n'
                       'NOT_LOAD_MODULES = []\n'
                       'COMMUNITY_REPOS = []\n'
                       'ALLOW_SIDELOAD = no\n'
                       'PKG_ENABLE_AUTO_UPDATE = no\n'
                       'CLIENT_CONNECT_RETRIES = 5\n'
                       'CLIENT_RETRY_DELAY = 1\n'
                       'SIDELOAD_NO_REBOOT = no\n'
                       'TERMINAL_USE_BIN_BASH = no\n'
                       'UPDATER_ENABLE_SCHEDULER = no\n')
        else:  # py script
            configs = ('class ConfigClass(object):\n'
                       f'{"":4}UBOT_LANG = "{lang_code}"\n'
                       f'{"":4}LOGGING = False\n'
                       f'{"":4}LOGGING_CHATID = 0\n'
                       f'{"":4}TEMP_DL_DIR = "{dl_path}"\n'
                       f'{"":4}NOT_LOAD_MODULES = []\n'
                       f'{"":4}COMMUNITY_REPOS = []\n'
                       f'{"":4}ALLOW_SIDELOAD = False\n'
                       f'{"":4}PKG_ENABLE_AUTO_UPDATE = False\n'
                       f'{"":4}CLIENT_CONNECT_RETRIES = 5\n'
                       f'{"":4}CLIENT_RETRY_DELAY = 1\n'
                       f'{"":4}SIDELOAD_NO_REBOOT = False\n'
                       f'{"":4}TERMINAL_USE_BIN_BASH = False\n'
                       f'{"":4}UPDATER_ENABLE_SCHEDULER = False\n')
        with open(config_file, "w") as cfg_file:
            print(f"Writing optional configuration file in {config_file}")
            cfg_file.write(configs)
        cfg_file.close()
        return True
    except Exception as e:
        print(
            setColorText(f"Failed to write optional configuration file: {e}",
                         Colors.RED))
    return False


def _suggest_start_option():
    start_bot_text = ("Do you wish to start HyperUBot now? You can always "
                      "start it by executing 'python3 -m userbot' in "
                      "HyperUBot's directory.")

    if IS_WINDOWS:
        start_bot_text = start_bot_text.replace("python3", "python")

    print(start_bot_text)

    if not IS_WINDOWS:
        while True:
            try:
                inp = input("Start HyperUBot now? (y/n): ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if inp.lower() in ("y", "yes"):
                _start_userbot()
                break
            elif inp.lower() in ("n", "no"):
                break
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))
    return


def main():
    _greetings()
    _check_setup_completed_already()

    if not _userbot_installed():
        print(setColorText("HyperUBot is not installed", Colors.RED_BG))
        return

    print()
    print(setColorText("1. Checking for pre-requisites", Colors.CYAN))
    print(setColorText("##############################", Colors.CYAN))

    if not NOPIP:
        print()
        check_setup_req = _check_setup_req()
    else:
        check_setup_req = True
    print()

    if not check_setup_req:
        print(setColorText("All or some packages required for Setup Assistant "
                           "are not present. Setup Assistant requires "
                           "'Telethon>=1.24.0', 'pyAesCrypt>=6.0.0' and "
                           "'cffi>=1.15.0'. Make sure these packages are "
                           "installed in order to continue. "
                           "Exiting Setup Assistant...",
                           Colors.RED))
        return

    print(setColorText("2. Generate String Session", Colors.CYAN))
    print(setColorText("##########################", Colors.CYAN))
    print()
    _pre_procedure()

    api_key, api_hash, string_session = _generateStringSession()

    if not api_key or not api_hash or not string_session:
        print(
            setColorText("Setup Assistant failed to get a new "
                         "string session from your App app_id/app_hash",
                         Colors.RED))
        print(
            setColorText("Feel free to contact us at Telegram "
                         "'https://t.me/HyperUBotSupport' if you need help "
                         "to handle this issue. Please keep a copy of the "
                         "error above ready or take a screenshot of it",
                         Colors.YELLOW))
        return

    print()
    print(setColorText("3. Secure configurations", Colors.CYAN))
    print(setColorText("########################", Colors.CYAN))
    print()
    set_pwd = _post_procedure()

    password = ""
    if set_pwd:
        print()
        password = _setup_password()

    print()
    print(setColorText("4. Optional configurations", Colors.CYAN))
    print(setColorText("##########################", Colors.CYAN))
    print()
    config_file = _select_config_type()
    print()
    print(setColorText("5. Select preferred language", Colors.CYAN))
    print(setColorText("############################", Colors.CYAN))
    print()
    lang_code = _select_language()
    print()
    print(setColorText("6. Finishing Setup Assistant", Colors.CYAN))
    print(setColorText("############################", Colors.CYAN))
    print()

    print(f"Writing configuration files...")
    cfg_secured = _secure_configs(api_key, api_hash, string_session, password)
    if not cfg_secured:
        return

    opt_created = _optional_configs(config_file, lang_code)
    if not opt_created:
        return

    if not NOPIP:
        print("Installing required pip packages...")
        _install_requirements()

    print()
    print(setColorText("Yaaaay! Setup completed! :P", Colors.GREEN))
    print()
    _suggest_start_option()
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Alright, exiting Setup Assistant...")
    except (BaseException, Exception) as e:
        print(setColorText(f"Setup Assistant stopped: {e}",
                           Colors.RED_BG))
        quit(1)
    quit()
