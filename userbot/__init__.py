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
from logging import FileHandler, StreamHandler, basicConfig, INFO, getLogger
from os import path, execle, environ, mkdir, remove
from platform import platform, machine, processor
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
    API_KEY = environ.get("API_KEY", 0)
    API_HASH = environ.get("API_HASH", None)
    STRING_SESSION = environ.get("STRING_SESSION", None)
    if SAFEMODE:
        addConfig("UBOT_LANG", loaded_env.get("UBOT_LANG", "en"))
    environ["API_KEY"] = "0"
    environ["API_HASH"] = "None"
    environ["STRING_SESSION"] = "None"
    del loaded_env
elif path.exists(path.join(".", "userbot", "config.py")):
    try:
        import userbot.config as cfg
    except (IndentationError, NameError,
            TypeError, ValueError, SyntaxError):  # totally F
        log.error("config.py file isn't well-formed. Please make sure "
                  "your config file matches expected python script "
                  "formation", exc_info=True)
        quit(1)
    except Exception as e:
        log.error(f"Unable to load configs: {e}", exc_info=True)
        quit(1)
    try:
        if not SAFEMODE:
            from inspect import getmembers, isclass, isfunction
    except Exception as e:
        log.error(f"Couldn't import config components: {e}", exc_info=True)
        quit(1)
    if not SAFEMODE:
        for name, cfgclass in getmembers(cfg, isclass):
            for attr_name in vars(cfgclass):
                attr_val = getattr(cfgclass, attr_name)
                if not attr_name.startswith("__") and \
                   not isfunction(attr_val):
                    if attr_name not in ("API_KEY", "API_HASH",
                                         "STRING_SESSION"):
                        addConfig(attr_name, attr_val)
    API_KEY = (cfg.ConfigClass.API_KEY
               if hasattr(cfg.ConfigClass, "API_KEY") else 0)
    API_HASH = (cfg.ConfigClass.API_HASH
                if hasattr(cfg.ConfigClass, "API_HASH") else None)
    STRING_SESSION = (cfg.ConfigClass.STRING_SESSION
                      if hasattr(cfg.ConfigClass, "STRING_SESSION") else None)
    if SAFEMODE:
        addConfig("UBOT_LANG",
                  (cfg.ConfigClass.UBOT_LANG
                   if hasattr(cfg.ConfigClass, "UBOT_LANG") else "en"))
    del cfg
else:
    try:
        log.warning("Couldn't find a config file in \"userbot\" directory. "
                    "Starting Setup Assistant...")
        _PY_EXEC = (executable
                    if " " not in executable else '"' + executable + '"')
        _tcmd = [_PY_EXEC, "setup.py"]
        execle(_PY_EXEC, *_tcmd, environ)
    except Exception as e:
        log.warning(f"Failed to start Setup Assistant: {e}", exc_info=True)
        log.error("Couldn't find a config file in \"userbot\" directory. "
                  "Please run the Setup Assistant to setup your config file "
                  "or generate a config file manually: "
                  "Environment and Python scripts are supported")
    quit()

if not getConfig("TEMP_DL_DIR"):
    addConfig("TEMP_DL_DIR", path.join(".", "downloads"))

log.info("Configurations loaded")

try:
    if not path.exists(getConfig("TEMP_DL_DIR")):
        mkdir(getConfig("TEMP_DL_DIR"))
except Exception:
    log.error("Failed to initialize download directory")

if not API_KEY:
    log.error("Configuration 'API_KEY' is empty or doesn't exist in "
              "your config file")
    log.error("API_KEY is required in order to use HyperUBot properly")
    log.error("Please obtain your API Key from 'https://my.telegram.org'")
    quit(1)

if not API_HASH:
    log.error("Configuration 'API_HASH' is empty or doesn't exist in your "
              "config file")
    log.error("API_HASH is required in order to use HyperUBot properly")
    log.error("Please obtain your API Hash from 'https://my.telegram.org'")
    quit(1)

try:
    if STRING_SESSION:
        tgclient = TelegramClient(StringSession(STRING_SESSION),
                                  API_KEY, API_HASH)
        # delete vars after tgclient
        del API_KEY
        del API_HASH
        del STRING_SESSION
    else:
        log.error("Configuration 'STRING_SESSION' is empty or doesn't "
                  "exist in your config file")
        log.error("STRING_SESSION is required in order to use HyperUBot "
                  "properly")
        log.error("Please run 'generate_session.py' to get a new string "
                  "session or if present, set your string session to "
                  "STRING_SESSION=\"YOUR STRING\" in your config.* file")
        log.error("Exiting...")
        quit(1)
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
