# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
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

from os import environ, execle, name  # noqa: E402
from platform import system  # noqa: E402
from sys import executable, platform  # noqa: E402
from telethon import version  # noqa: E402
from telethon.sync import TelegramClient  # noqa: E402
from telethon.sessions import StringSession  # noqa: E402

IS_WINDOWS = (True if system().lower() == "windows" or
              name == "nt" or platform.startswith("win") else False)
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
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    END = "\033[0m"


def setColorText(text: str, color: Colors) -> str:
    if IS_WINDOWS and not WIN_COLOR_ENABLED:
        return text  # don't use ANSI codes
    return f"{color}{text}{Colors.END}"

telethon_version = tuple(map(int, version.__version__.split(".")))
if telethon_version < (1, 23, 0):
    print(setColorText(
        "Telethon version 1.23.0+ is required! Please update "
        "Telethon to v1.23.0 or newer "
        f"(current version: {version.__version__}).", Colors.RED))
    quit(1)

print("Welcome to HyperUBot's String Session generator!\n"
      "Get a new String Session from your Telegram account with the help of "
      "this script.\n\n"
      "Important: If not done yet, please go to https://my.telegram.org and\n"
      "1. log in into your account\n"
      "2. create a new application\n"
      "3. get your API Key and Hash (do NOT share these IDs with "
      "anyone else!)\n\n"
      "Please keep the following requirements ready to obtain a new "
      "String Session:\n"
      "- Your Telegram application's API Key and Hash (to access your "
      "application)\n"
      "- Your Phone Number (required to log in into your account)\n"
      "- Your Account's password (Two-Step Verification; if enabled)\n")

try:
    while True:
        con = input("Continue? (y/n): ")
        if con.lower() in ("y", "yes"):
            break
        elif con.lower() in ("n", "no"):
            raise KeyboardInterrupt
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    while True:
        API_KEY = input("Please enter your API Key: ")
        try:
            API_KEY = int(API_KEY)
            break
        except:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    while True:
        API_HASH = input("Please enter your API Hash: ")
        if len(API_HASH) == 32:
            break
        elif len(API_HASH) > 0:
            print(setColorText("Invalid input. API Hash has a length of "
                               "32 characters", Colors.YELLOW))
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))
except KeyboardInterrupt:
    print("Exiting...")
    quit()

start_scfg_updater = False

try:
    client = TelegramClient(StringSession(), API_KEY, API_HASH)
    with client:
        print("This long string below is your new String Session:\n\n")
        print(setColorText(client.session.save(), Colors.GREEN))
        print("\n\nPlease keep this string to a safe place and " +
              setColorText("DON'T SHARE IT WITH ANYONE!!", Colors.RED))
        print("Next step is to start Secure-Config-Updater to store your new "
              "string session safe in a secured config file\n")
        while True:
            inp = input("Start Secure-Config-Updater? (y/n): ")
            if inp.lower() in ("y", "yes"):
                start_scfg_updater = True
                break
            elif inp.lower() in ("n", "no"):
                raise KeyboardInterrupt
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))
except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(setColorText(f"Unable to obtain a new string session: {e}",
                       Colors.RED))
    quit(1)

if start_scfg_updater:
    try:
        tcmd = [PY_EXEC, "update_secure_cfg.py"]
        execle(PY_EXEC, *tcmd, environ)
    except Exception as e:
        print(setColorText(f"Failed to start Secure-Config-Updater: {e}",
                           Colors.RED))
quit()
