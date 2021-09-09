# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from sys import version_info

if (version_info.major, version_info.minor) < (3, 8):
    print("Python v3.8+ is required to start Secure-Config-Updater! Please "
          "update Python to v3.8 or newer "
          "(current version: {}.{}.{}).".format(
              version_info.major, version_info.minor, version_info.micro))
    quit(1)

from platform import system  # noqa: E402
from sys import executable, platform  # noqa: E402
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
    CYAN = "\033[96m"
    RED_BG = "\033[101m"
    END = "\033[0m"


def setColorText(text: str, color: Colors) -> str:
    if IS_WINDOWS and not WIN_COLOR_ENABLED:
        return text  # don't use ANSI codes
    return f"{color}{text}{Colors.END}"


try:
    from cffi import __version__
except:
    print(setColorText("cffi is not installed!", Colors.RED))
    if IS_WINDOWS:
        print(setColorText("Please install cffi package by "
                           "executing 'pip install cffi'",
                           Colors.YELLOW))
    else:
        print(setColorText("Please install cffi package by "
                           "executing 'python3 -m pip install cffi'",
                           Colors.YELLOW))
    quit(1)

try:
    # just to ensure proper version is installed (required by pyAesCrypt)
    cffi_ver = tuple(map(int, __version__.split(".")))
    if cffi_ver < (1, 14, 6):
        print(setColorText("cffi version 1.14.6 is required. "
                           f"Current version is {__version__}", Colors.RED))
        if IS_WINDOWS:
            print(setColorText("Please upgrade cffi package by "
                               "executing 'pip install --upgrade cffi'",
                               Colors.YELLOW))
        else:
            print(setColorText("Please install cffi package by "
                               "executing 'python3 -m pip install --upgrade "
                               "cffi'", Colors.YELLOW))
        quit()
except Exception as e:
    print(setColorText("Unable to check cffi version: {e}", Colors.RED))
    quit(1)

try:
    import pyAesCrypt
except:
    print(setColorText("pyAesCrypt is not installed!", Colors.RED))
    if IS_WINDOWS:
        print(setColorText("Please install pyAesCrypt package by "
                           "executing 'pip install pyAesCrypt'",
                           Colors.YELLOW))
    else:
        print(setColorText("Please install pyAesCrypt package by "
                           "executing 'python3 -m pip install pyAesCrypt'",
                           Colors.YELLOW))
    quit(1)


def _getAPIsAndSession() -> tuple:
    try:
        while True:
            try:
                api_key = input("Please enter your App api_id (API Key): ")
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
                api_hash = input("Please enter your App api_hash (API Hash): ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
            if len(api_hash) == 32:
                break
            elif len(api_hash) > 0:
                print(setColorText("Invalid input. API Hash should have a "
                                   "length of 32 characters!", Colors.YELLOW))
            else:
                print(setColorText("Invalid input. Try again...",
                                   Colors.YELLOW))

        while True:
            try:
                string_session = input("Please enter your valid "
                                       "String Session: ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
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


def _start_userbot():
    py_exec = executable if " " not in executable else '"' + executable + '"'
    try:
        tcmd = [py_exec, "-m", "userbot"]
        os.execle(py_exec, *tcmd, os.environ)
    except Exception as e:
        print(setColorText(f"Failed to start HyperUBot: {e}",
                           Colors.RED))
    return


def main():
    print(setColorText("Secure-Config-Updater", Colors.CYAN) +
          " creates a new secured config file with your App api_id (API Key), "
          "App api_hash (API Hash) and String Session stored to protect these "
          "sensitive data from unauthorized access")
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
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    api_key, api_hash, string_session = _getAPIsAndSession()

    if not api_key or not api_hash or not string_session:
        print(setColorText("Input values are not valid", Colors.RED))
        return

    print()
    print("There is an option to setup a password to your secure config "
          "to increase the security of your sensitive data. This is "
          "optional and not mandatory but extra protection doesn't hurt.")
    print(setColorText("If you forgot your password, you have to create "
                       "a new secure config!", Colors.YELLOW))
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
              "Maximum length is 1024 characters. \nNote: Your password is "
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
    cfg_secured = False
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
            cfg_secured = True
        else:
            print(setColorText("Failed to secure configs", Colors.RED))
    except Exception as e:
        print(setColorText(f"Failed to secure configs: {e}", Colors.RED))

    if cfg_secured:
        print("Do you wish to start HyperUBot?")
        print()
        if IS_WINDOWS:
            print("Run the following command to start HyperUBot: " +
                  setColorText("python -m userbot", Colors.CYAN))
        else:
            while True:
                try:
                    inp = input("Start HyperUBot? (y/n): ")
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
    except (BaseException, Exception) as e:
        print(setColorText(f"Secure-Config-Updater stopped: {e}",
                           Colors.RED_BG))
        quit(1)
    quit()
