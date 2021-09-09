# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from sys import version_info

if (version_info.major, version_info.minor) < (3, 8):
    print("Python v3.8+ is required to start this service! Please update "
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
    CYAN = "\033[96m"
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

print(setColorText("Welcome to HyperUBot's String-Session-Generator!",
                   Colors.CYAN))

print("The String-Session-Generator generates a new String Session "
      "in combination with your App api_id (API Key) and App api_hash "
      "(API Hash) to allow HyperUBot to login into your account to "
      "interact as 'user'bot. Please follow the steps below to obtain "
      "your API Key and API Hash to finally generate a String Session:")
print()
print("1. Login to My Telegram: https://my.telegram.org")
print("2. Go to 'API development tools' and fill out the form")
print("3. Get your App api_id and App api_hash. You will need them for the "
      "next step")
print()
print(setColorText("Note: Always remember not to share your App api_id and "
                   "App api_hash!", Colors.YELLOW))
print()
try:
    while True:
        con = input("Continue? (y/n): ")
        if con.lower() in ("y", "yes"):
            break
        elif con.lower() in ("n", "no"):
            raise KeyboardInterrupt
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))
except KeyboardInterrupt:
    print()
    print("Exiting...")
    quit()
print()
print("As we want to interact as user, the Telegram client will ask for "
      "your phone number, don't worry it's only required for "
      "user authorization and will not be send to anyone else. If "
      "Two-Step Verification is enabled it will also ask for the password!")
print()

try:
    while True:
        con = input("Ready? (y/n): ")
        if con.lower() in ("y", "yes"):
            print()
            break
        elif con.lower() in ("n", "no"):
            raise KeyboardInterrupt
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    print(setColorText("==== TELEGRAM CLIENT ====", Colors.CYAN))
    while True:
        API_KEY = input("Please enter your App api_id: ")
        try:
            API_KEY = int(API_KEY)
            break
        except:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    while True:
        API_HASH = input("Please enter your App api_hash: ")
        if len(API_HASH) == 32:
            break
        elif len(API_HASH) > 0:
            print(setColorText("Invalid input. API Hash should have a "
                               "length of 32 characters!", Colors.YELLOW))
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))
except KeyboardInterrupt:
    print()
    print("Exiting...")
    quit()

try:
    client = TelegramClient(StringSession(), API_KEY, API_HASH)
    with client:
        print("Alright there we go! This long string below is your new "
              "String Session:\n\n")
        print(setColorText(client.session.save(), Colors.GREEN))
        print("\n\nPlease keep this string to a safe place and " +
              setColorText("DON'T SHARE IT WITH ANYONE!!", Colors.RED))
        print(setColorText("=========================", Colors.CYAN))
except KeyboardInterrupt:
    print()
    print("Exiting...")
    quit()
except Exception as e:
    print(setColorText(f"Unable to obtain a new string session: {e}",
                       Colors.RED))
    quit(1)

start_scfg_updater = False
print("Next step is to start Secure-Config-Updater to store your new "
      "String Session safe in a secured config file\n")
if IS_WINDOWS:
    print("Run the following command to start the "
          "Secure-Config-Updater: " +
          setColorText("python update_secure_cfg.py", Colors.CYAN))
else:
    try:
        while True:
            inp = input("Start Secure-Config-Updater? (y/n): ")
            if inp.lower() in ("y", "yes"):
                start_scfg_updater = True
                break
            elif inp.lower() in ("n", "no"):
                break
            else:
                print(setColorText("Invalid input. Try again...",
                                       Colors.YELLOW))
    except KeyboardInterrupt:
        print()
        print("Exiting...")

if start_scfg_updater:
    try:
        tcmd = [PY_EXEC, "update_secure_cfg.py"]
        execle(PY_EXEC, *tcmd, environ)
    except Exception as e:
        print(setColorText(f"Failed to start Secure-Config-Updater: {e}",
                           Colors.RED))
quit()
