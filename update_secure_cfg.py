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
from sys import platform  # noqa: E402
import os  # noqa: E402

IS_WINDOWS = (True if system().lower() == "windows" or
              os.name == "nt" or platform.startswith("win") else False)
WIN_COLOR_ENABLED = False
SECURE_CONFIG = os.path.join(".", "userbot", "secure_config")

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
    return f"{color}{text}{Colors.END}"


try:
    import pyAesCrypt
except:
    print(setColorText("pyAesCrypt is not installed!", Colors.RED))
    quit(1)


def _getAPIsAndSession() -> tuple:
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
                                   "32 characters", Colors.YELLOW))
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        while True:
            string_session = input("Please enter your String Session: ")
            if string_session:
                break
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))
        return (api_key, api_hash, string_session)
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        pass
    return (None, None, None)


def main():
    print("Secure-Config-Updater creates a new secured config file "
          "with your API Key, Hash and String Session stored "
          "to protect these sensitive data from unauthorized access")
    print()

    while True:
        inp = input("Continue? (y/n): ")
        if inp.lower() in ("y", "yes"):
            break
        elif inp.lower() in ("n", "no"):
            raise KeyboardInterrupt
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    api_key, api_hash, string_session = _getAPIsAndSession()

    if not api_key or not api_hash or not string_session:
        print(setColorText("Input values not valid", Colors.RED))
        return

    print()
    print("You have the option to setup a password to your secure config "
          "to increase the security of your sensitive data. This is "
          "optional and not mandatory but extra protection doesn't hurt.")
    print(setColorText("If you forgot your password, you have to create "
                       "a new secure config!", Colors.YELLOW))
    print()

    set_pwd = False

    while True:
        inp = input("Set password? (y/n): ")
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
              "Maximum length is 1024 characters")
        while True:
            password = getpass("Your password: ")
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
            retype_pwd = getpass("Retype your password: ")
            if password == retype_pwd:
                break
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

    print()
    try:
        print("Securing configs...")
        if os.path.exists(SECURE_CONFIG):
            os.remove(SECURE_CONFIG)
        if os.path.exists("_temp.py"):
            os.remove("_temp.py")
        secure_configs = (f'API_KEY = "{api_key}"\n'
                          f'API_HASH = "{api_hash}"\n'
                          f'STRING_SESSION = "{string_session}"')
        with open("_temp.py", "w") as cfg_file:
            cfg_file.write(secure_configs)
        cfg_file.close()
        pyAesCrypt.encryptFile(infile="_temp.py",
                               outfile=SECURE_CONFIG,
                               passw=password,
                               bufferSize=(64 * 1024))
        os.remove("_temp.py")
        if os.path.exists(SECURE_CONFIG):
            print(setColorText("Configs secured", Colors.GREEN))
        else:
            print(setColorText("Failed to secure configs", Colors.RED))
    except Exception as e:
        print(setColorText(f"Failed to secure configs: {e}", Colors.RED))
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
    except (BaseException, Exception) as e:
        print(setColorText(f"Secure config updater stopped: {e}",
                           Colors.RED_BG))
        quit(1)
    quit()
