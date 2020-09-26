# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.log_formatter import LogFileFormatter, LogColorFormatter
from telethon import TelegramClient, version
from telethon.sessions import StringSession
from dotenv import load_dotenv
from json import loads
from logging import FileHandler, StreamHandler, basicConfig, INFO, getLogger
from os import path, environ, mkdir, remove
from platform import platform, python_compiler, system, machine, processor
from sys import version_info  # check python version

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
VERSION = "1.0.1"
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

if (version_info.major, version_info.minor) < (3, 8):
    log.error("Required Python 3.8!")
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

if path.exists(CURR_PATH + "config.env"):
    load_dotenv(CURR_PATH + "config.env")
    SAMPLE_CONFIG = environ.get("SAMPLE_CONFIG", None)
    if SAMPLE_CONFIG:
        log.error("Please remove SAMPLE_CONFIG from config.env!")
        quit(1)
    API_KEY = environ.get("API_KEY", None)
    API_HASH = environ.get("API_HASH", None)
    LOGGING = environ.get("LOGGING", False)
    LOGGING_CHATID = int(environ.get("LOGGING_CHATID", "0"))
    STRING_SESSION = environ.get("STRING_SESSION", None)
    TEMP_DL_DIR = environ.get("TEMP_DL_DIR", "./downloads")
    UBOT_LANG = environ.get("UBOT_LANG", "en")
    NOT_LOAD_MODULES = strlist_to_list(environ.get("NOT_LOAD_MODULES", "[]"))
    COMMUNITY_REPOS = strlist_to_list(environ.get("COMMUNITY_REPOS", "[]"))
elif path.exists(CURR_PATH + "config.py"):
    try:
        from userbot.config import ConfigClass  # Import here, otherwise error
    except ImportError as ie:
        log.error(f"Couldn't import ConfigClass: {ie}")
        quit(1)
    API_KEY = ConfigClass.API_KEY if hasattr(ConfigClass, "API_KEY") else None
    API_HASH = ConfigClass.API_HASH if hasattr(ConfigClass, "API_HASH") else None
    LOGGING = ConfigClass.LOGGING if hasattr(ConfigClass, "LOGGING") else False
    LOGGING_CHATID = ConfigClass.LOGGING_CHATID if hasattr(ConfigClass, "LOGGING_CHATID") else 0
    STRING_SESSION = ConfigClass.STRING_SESSION if hasattr(ConfigClass, "STRING_SESSION") else None
    TEMP_DL_DIR = ConfigClass.TEMP_DL_DIR if hasattr(ConfigClass, "TEMP_DL_DIR") else "./downloads"
    UBOT_LANG = ConfigClass.UBOT_LANG if hasattr(ConfigClass, "UBOT_LANG") else "en"
    NOT_LOAD_MODULES = ConfigClass.NOT_LOAD_MODULES if hasattr(ConfigClass, "NOT_LOAD_MODULES") else []
    COMMUNITY_REPOS = ConfigClass.COMMUNITY_REPOS if hasattr(ConfigClass, "COMMUNITY_REPOS") else []
else:
    log.error("No Config file found! Make sure it's located in ./userbot/config.* or setup your config file first if you didn't. " +
    "Environment and py scripts are supported.")
    quit(1)

if OS and OS.lower().startswith("win"):
    TEMP_DL_DIR += "\\"
else:
    TEMP_DL_DIR += "/"

try:
    if not path.exists(TEMP_DL_DIR):
        mkdir(TEMP_DL_DIR)
except OSError:
    log.error("Failed to initialize download directory.")

if not API_KEY:
    log.error("API KEY is empty! Obtain your API KEY from https://my.telegram.org if you don't have one.")
    quit(1)

if not API_HASH:
    log.error("API HASH is empty! Obtain your API HASH from https://my.telegram.org if you don't have one.")
    quit(1)

try:
    if STRING_SESSION:
        tgclient = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
    else:
        log.error("STRING SESSION is empty!")
        log.error("Please run 'generate_session.py' to get a new string session or if present, set your string session to STRING_SESSION in your config.* file")
        log.error("Terminating...")
        quit(1)
except Exception as e:
    log.critical(f"Failed to create Telegram Client: {e}", exc_info=True)
    quit(1)

# SYSVARS
ALL_MODULES = []
LOAD_MODULES = []
MODULE_DESC = {}
MODULE_DICT = {}
USER_MODULES = []
