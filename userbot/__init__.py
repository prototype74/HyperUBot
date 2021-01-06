# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.configuration import addConfig, getConfig
from userbot.sysutils.log_formatter import LogFileFormatter, LogColorFormatter
from telethon import TelegramClient, version
from telethon.sessions import StringSession
from dotenv import load_dotenv
from json import loads
from logging import FileHandler, StreamHandler, basicConfig, INFO, getLogger
from os import path, environ, mkdir, remove
from platform import platform, python_compiler, system, machine, processor
from sys import version_info

# Terminal logging
LOGFILE = "hyper.log"
if path.exists(LOGFILE):
    remove(LOGFILE)
log = getLogger(__name__)
fhandler = FileHandler(LOGFILE)
fhandler.setFormatter(LogFileFormatter())
shandler = StreamHandler()
shandler.setFormatter(LogColorFormatter())
basicConfig(handlers=[fhandler, shandler], level=INFO)

PROJECT = "HyperUBot"
VERSION = "3.0.3"
OS = system()  # Current Operating System

try:
    if path.exists(LOGFILE):
        sys_string = "======= SYS INFO\n\n"
        sys_string += "Project: {}\n".format(PROJECT)
        sys_string += "Version: {}\n".format(VERSION)
        sys_string += "Operating System: {}\n".format(OS)
        sys_string += "Platform: {}\n".format(platform())
        sys_string += "Machine: {}\n".format(machine())
        sys_string += "Processor: {}\n".format(processor())
        sys_string += "Python: v{}.{}.{}\n".format(version_info.major, version_info.minor, version_info.micro)
        sys_string += "Python compiler: {}\n".format(python_compiler())
        sys_string += "Telethon: v{}\n\n".format(version.__version__)
        sys_string += "======= TERMINAL LOGGING\n\n"
        file = open(LOGFILE, "w")
        file.write(sys_string)
        file.close()
except Exception as e:
    log.warning("Unable to write system information into log: {}".format(e))

# Check Python version
if (version_info.major, version_info.minor) < (3, 8):
    log.error("Python v3.8+ is required! Please update Python to v3.8 or newer " +
              "(current version: {}.{}.{}).".format(version_info.major, version_info.minor, version_info.micro))
    quit(1)

# Check Telethon version
telethon_version = tuple(map(int, version.__version__.split(".")))
if telethon_version < (1, 18, 2):
    log.error("Telethon version 1.18.2+ is required! " +
              f"Please update Telethon to v1.18.2 or newer (current version: {version.__version__}).")
    quit(1)

CURR_PATH = path.dirname(__file__)

if OS and OS.lower().startswith("win"):
    CURR_PATH += "\\"  # Windows backslash path
else:
    CURR_PATH += "/"  # Other Linux systems or macOS

def strlist_to_list(strlist: str) -> list:
    try:
        list_obj = loads(strlist)
    except:
        list_obj = []
    return list_obj

def str_to_bool(strbool: str) -> bool:
    if strbool in ("True", "true"):
        return True
    elif strbool in ("False", "false"):
        return False
    raise ValueError(f"{strbool} is not a bool")

log.info("Loading configurations")

if path.exists(CURR_PATH + "config.env"):
    len_before = len(environ.items())
    load_dotenv(CURR_PATH + "config.env")
    loaded_env =  {key: value for key, value in list(environ.items())[len_before:]}
    for key, value in loaded_env.items():
        if not key in ("API_KEY", "API_HASH", "STRING_SESSION"):
            if key == "TEMP_DL_DIR":
                if OS and OS.lower().startswith("win"):
                    value += "\\"
                else:
                    value += "/"
            if value.startswith("[") and value.endswith("]"):
                addConfig(key, strlist_to_list(value))
            elif value in ("True", "true", "False", "false"):
                addConfig(key, str_to_bool(value))
            else:  # default case
                addConfig(key, int(value) if value.isnumeric() else value)
    if getConfig("SAMPLE_CONFIG", None):
        log.error("Please remove SAMPLE_CONFIG from config.env!")
        quit(1)
    API_KEY = environ.get("API_KEY", None)
    API_HASH = environ.get("API_HASH", None)
    STRING_SESSION = environ.get("STRING_SESSION", None)
    environ["API_KEY"] = "0"
    environ["API_HASH"] = "None"
    environ["STRING_SESSION"] = "None"
    del loaded_env
elif path.exists(CURR_PATH + "config.py"):
    try:
        import userbot.config
        from inspect import getmembers, isclass, isfunction
    except ImportError as ie:
        log.error(f"Couldn't import configurations: {ie}", exc_info=True)
        quit(1)
    for name, cfgclass in getmembers(userbot.config, isclass):
        for attr_name in vars(cfgclass):
            attr_val = getattr(cfgclass, attr_name)
            if not attr_name.startswith("__") and \
               not isfunction(attr_val):
                if not attr_name in ("API_KEY", "API_HASH", "STRING_SESSION"):
                    if attr_name == "TEMP_DL_DIR":
                        if OS and OS.lower().startswith("win"):
                            new_val = attr_val + "\\"
                        else:
                            new_val = attr_val + "/"
                        addConfig(attr_name, new_val)
                    else:
                        addConfig(attr_name, attr_val)
    API_KEY = userbot.config.ConfigClass.API_KEY if hasattr(userbot.config.ConfigClass, "API_KEY") else None
    API_HASH = userbot.config.ConfigClass.API_HASH if hasattr(userbot.config.ConfigClass, "API_HASH") else None
    STRING_SESSION = userbot.config.ConfigClass.STRING_SESSION if hasattr(userbot.config.ConfigClass, "STRING_SESSION") else None
    del userbot.config
else:
    log.error("No Config file found! Make sure it's located in \"userbot\" directory or setup your config file first if you didn't. " +
    "Environment and py scripts are supported.")
    quit(1)

if not getConfig("TEMP_DL_DIR"):
    addConfig("TEMP_DL_DIR", ".\\downloads\\" if OS and OS.lower().startswith("win") else "./downloads/")

log.info("Configurations loaded")

try:
    if not path.exists(getConfig("TEMP_DL_DIR")):
        mkdir(getConfig("TEMP_DL_DIR"))
except OSError:
    log.error("Failed to initialize download directory.")

if not API_KEY:
    log.error("API_KEY is empty! Obtain your API KEY from https://my.telegram.org if you don't have one.")
    quit(1)

if not API_HASH:
    log.error("API_HASH is empty! Obtain your API HASH from https://my.telegram.org if you don't have one.")
    quit(1)

try:
    if STRING_SESSION:
        tgclient = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
        # delete vars after tgclient
        del API_KEY
        del API_HASH
        del STRING_SESSION
    else:
        log.error("STRING SESSION is empty!")
        log.error("Please run 'generate_session.py' to get a new string session or if present, set your string session to STRING_SESSION in your config.* file")
        log.error("Terminating...")
        quit(1)
except Exception as e:
    log.critical(f"Failed to create Telegram Client: {e}", exc_info=True)
    quit(1)

# SYSVARS
ALL_MODULES = []  # [sys + user] name of modules
LOAD_MODULES = {}  # {Module name: isRunning}
USER_MODULES = []  # [Name of user module]
MODULE_DESC = {}  # {Module name: MODULE_DESC}
MODULE_DICT = {}  # {Module name: MODULE_USAGE}
MODULE_INFO = {}  # {Module name: MODULE_INFO}
