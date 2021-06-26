# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.configuration import addConfig, getConfig
from userbot.sysutils.colors import Color, setColorText
from userbot.sysutils.log_formatter import LogFileFormatter, LogColorFormatter
from userbot.sysutils.sys_funcs import os_name, verAsTuple
from userbot.version import VERSION as hubot_version
from telethon import TelegramClient, version
from telethon.errors.rpcerrorlist import (ApiIdInvalidError,
                                          PhoneNumberInvalidError)
from telethon.sessions import StringSession
from dotenv import load_dotenv
from getpass import getpass
from logging import FileHandler, StreamHandler, basicConfig, INFO, getLogger
from os import path, execle, environ, listdir, mkdir, remove
from platform import platform, machine, processor
from pyAesCrypt import decryptFile
from sys import argv, executable, version_info

# Terminal logging
LOGFILE = "hyper.log"
try:
    if path.exists(LOGFILE):
        remove(LOGFILE)
except:
    pass
log = getLogger(__name__)
_fhandler = FileHandler(LOGFILE)
_fhandler.setFormatter(LogFileFormatter())
_shandler = StreamHandler()
_shandler.setFormatter(LogColorFormatter())
basicConfig(handlers=[_fhandler, _shandler], level=INFO)

PROJECT = "HyperUBot"
OS = os_name()  # Current Operating System [DEPRECATED]
SAFEMODE = False

# Check safe mode from command line
if len(argv) >= 2:
    if argv[1].lower() == "-safemode":
        SAFEMODE = True

try:
    if path.exists(LOGFILE):
        _sys_string = "======= SYS INFO\n\n"
        _sys_string += "Project: {}\n".format(PROJECT)
        _sys_string += "Version: {}\n".format(hubot_version)
        _sys_string += "Safe mode: {}\n".format("On" if SAFEMODE else "Off")
        _sys_string += "Operating System: {}\n".format(os_name())
        _sys_string += "Platform: {}\n".format(platform())
        _sys_string += "Machine: {}\n".format(machine())
        _sys_string += "Processor: {}\n".format(processor())
        _sys_string += "Python: v{}.{}.{}\n".format(version_info.major,
                                                    version_info.minor,
                                                    version_info.micro)
        _sys_string += "Telethon: v{}\n\n".format(version.__version__)
        _sys_string += "======= TERMINAL LOGGING\n\n"
        _file = open(LOGFILE, "w")
        _file.write(_sys_string)
        _file.close()
except Exception as e:
    log.warning("Unable to write system information into log: {}".format(e))

# Check Python version
if (version_info.major, version_info.minor) < (3, 8):
    log.error("Python v3.8+ is required! "
              "Please update Python to v3.8 or newer "
              "(current version: {}.{}.{}).".format(version_info.major,
                                                    version_info.minor,
                                                    version_info.micro))
    quit(1)

# Check Telethon version
if verAsTuple(version.__version__) < (1, 21, 1):
    log.error("Telethon version 1.21.1+ is required! "
              "Please update Telethon to v1.21.1 or newer "
              f"(current version: {version.__version__}).")
    quit(1)

if SAFEMODE:
    log.info(setColorText("Booting in SAFE MODE", Color.GREEN))
    log.info("Loading required configurations")
else:
    log.info("Loading configurations")

if path.exists(path.join(".", "userbot", "config.env")):
    from userbot.include.aux_funcs import strlist_to_list, str_to_bool
    _len_before = len(environ.items())
    load_dotenv(path.join(".", "userbot", "config.env"))
    loaded_env = {key: value
                  for key, value in list(environ.items())[_len_before:]}
    if not SAFEMODE:
        for key, value in loaded_env.items():
            if key not in ("API_KEY", "API_HASH", "STRING_SESSION"):
                if value.startswith("[") and value.endswith("]"):
                    addConfig(key, strlist_to_list(value))
                elif value in ("True", "true", "False", "false"):
                    addConfig(key, str_to_bool(value))
                else:  # default case
                    addConfig(key, int(value) if value.isnumeric() else value)
    if getConfig("SAMPLE_CONFIG", None):
        log.error("Please remove SAMPLE_CONFIG from config.env!")
        quit(1)
    if SAFEMODE:
        addConfig("UBOT_LANG", loaded_env.get("UBOT_LANG", "en"))
    environ["API_KEY"] = "0"
    environ["API_HASH"] = "None"
    environ["STRING_SESSION"] = "None"
    del loaded_env
elif path.exists(path.join(".", "userbot", "config.py")):
    _cfg_loadable = False
    try:
        import userbot.config as cfg
        _cfg_loadable = True
    except (IndentationError, NameError,
            TypeError, ValueError, SyntaxError):  # totally F
        log.warning("config.py file isn't well-formed. Please make sure "
                    "your config file matches expected python script "
                    "formation", exc_info=True)
    except Exception as e:
        log.warning(f"Unable to load configs: {e}", exc_info=True)
    try:
        if not SAFEMODE:
            from inspect import getmembers, isclass, isfunction
    except Exception as e:
        log.warning(f"Couldn't import config components: {e}", exc_info=True)
        if _cfg_loadable:
            _cfg_loadable = False
    if not SAFEMODE and _cfg_loadable:
        for name, cfgclass in getmembers(cfg, isclass):
            for attr_name in vars(cfgclass):
                attr_val = getattr(cfgclass, attr_name)
                if not attr_name.startswith("__") and \
                   not isfunction(attr_val):
                    if attr_name not in ("API_KEY", "API_HASH",
                                         "STRING_SESSION"):
                        addConfig(attr_name, attr_val)
    if SAFEMODE and _cfg_loadable:
        addConfig("UBOT_LANG",
                  (cfg.ConfigClass.UBOT_LANG
                   if hasattr(cfg.ConfigClass, "UBOT_LANG") else "en"))
    del _cfg_loadable
    try:
        del cfg
    except:
        pass
elif not path.exists(path.join(".", "userbot", "secure_config")):
    try:
        log.warning("Couldn't find config file(s) in \"userbot\" directory. "
                    "Starting Setup Assistant...")
        _PY_EXEC = (executable
                    if " " not in executable else '"' + executable + '"')
        _tcmd = [_PY_EXEC, "setup.py"]
        execle(_PY_EXEC, *_tcmd, environ)
    except Exception as e:
        log.warning(f"Failed to start Setup Assistant: {e}", exc_info=True)
        log.error("Couldn't find config file(s) in \"userbot\" directory. "
                  "Please run the Setup Assistant to setup your config "
                  "file(s) or create them manually: "
                  "Environment and Python scripts are supported")
    quit()

if path.exists(path.join(".", "userbot", "secure_config")):
    _password = ""
    _pwd_confm = False
    _attempts = 0
    while True:
        try:
            decryptFile(infile=path.join(".", "userbot", "secure_config"),
                        outfile=path.join(".", "userbot", "_temp.py"),
                        passw=_password,
                        bufferSize=(64 * 1024))
            break
        except ValueError as e:
            if "wrong password" in str(e).lower() and \
               _attempts < 5:
                if not _pwd_confm:
                    log.info("Password required for secure config")
                else:
                    log.warning("Invalid password. Try again...")
                try:
                    while True:
                        _password = getpass("Please enter your password: ")
                        if not _pwd_confm:
                            _pwd_confm = True
                        break
                except KeyboardInterrupt:
                    quit()
                _attempts += 1
            else:
                log.error("Unable to read secure config")
                quit(1)
        except Exception:
            log.error("Unable to read secure config")
            quit(1)

    try:
        import userbot._temp as _s_cfg
        API_KEY = _s_cfg.API_KEY
        API_HASH = _s_cfg.API_HASH
        STRING_SESSION = _s_cfg.STRING_SESSION
    except Exception:
        log.error("Unable to read secure config")
        quit(1)
    finally:
        if path.exists(path.join(".", "userbot", "_temp.py")):
            remove(path.join(".", "userbot", "_temp.py"))
        if path.exists(path.join(".", "userbot", "__pycache__")) and \
           path.isdir(path.join(".", "userbot", "__pycache__")):
            for name in listdir(path.join(".", "userbot", "__pycache__")):
                if name.startswith("_temp.cpython-") and \
                   name.endswith(".pyc"):
                    remove(path.join(".", "userbot", "__pycache__", name))
                    break
        del _password
        del _pwd_confm
        del _attempts
    del _s_cfg

if SAFEMODE and not getConfig("UBOT_LANG"):
    addConfig("UBOT_LANG", "en")

if not getConfig("TEMP_DL_DIR"):
    addConfig("TEMP_DL_DIR", path.join(".", "downloads"))

log.info("Configurations loaded")

try:
    if getConfig("USERDATA") and not path.exists(getConfig("USERDATA")):
        mkdir(getConfig("USERDATA"))
except Exception:
    log.error("Failed to initialize user data directory")

try:
    if not path.exists(getConfig("TEMP_DL_DIR")):
        mkdir(getConfig("TEMP_DL_DIR"))
except Exception:
    log.error("Failed to initialize download directory")

if "API_KEY" not in globals() or ("API_KEY" in globals() and not API_KEY):
    log.error("API Key is empty or doesn't exist")
    log.error("API Key is required in order to use HyperUBot properly")
    log.error("Please obtain your API Key from 'https://my.telegram.org' "
              "or if not present create/update your secure config")
    quit(1)

if "API_HASH" not in globals() or ("API_HASH" in globals() and not API_HASH):
    log.error("API Hash is empty or doesn't exist")
    log.error("API Hash is required in order to use HyperUBot properly")
    log.error("Please obtain your API Hash from 'https://my.telegram.org' "
              "or if not present create/update your secure config")
    quit(1)

if "STRING_SESSION" not in globals() or \
   ("STRING_SESSION" in globals() and not STRING_SESSION):
    log.error("String session is empty or doesn't exist")
    log.error("string session is required in order to use HyperUBot "
              "properly")
    log.error("Please run 'generate_session.py' to get a new string "
              "session, or if present already, then update your secure "
              "config using 'update_secure_cfg.py' in HyperUBot's "
              "root directory")
    quit(1)

try:
    tgclient = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
    del API_KEY
    del API_HASH
    del STRING_SESSION
except ApiIdInvalidError as ae:
    log.critical(f"API Key and/or API Hash is/are invalid: {ae}",
                 exc_info=True)
    quit(1)
except PhoneNumberInvalidError as pe:
    log.critical(f"Phone number is not valid: {pe}", exc_info=True)
    quit(1)
except Exception as e:
    log.critical(f"Failed to create Telegram Client: {e}", exc_info=True)
    quit(1)
