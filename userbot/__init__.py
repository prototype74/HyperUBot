# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.config_loader import (check_secure_config,
                                            load_configs,
                                            get_secure_config)
from userbot.sysutils.configuration import addConfig, getConfig
from userbot.sysutils.colors import Color, setColorText
from userbot.sysutils.log_formatter import LogFileFormatter, LogColorFormatter
from userbot.sysutils.sys_funcs import os_name, verAsTuple
from userbot.version import VERSION as hubot_version
from telethon import TelegramClient, version
from telethon.errors.rpcerrorlist import (ApiIdInvalidError,
                                          PhoneNumberInvalidError)
from telethon.sessions import StringSession
from logging import FileHandler, StreamHandler, basicConfig, INFO, getLogger
from os import path, mkdir, remove
from platform import platform, machine, processor
from sys import argv, version_info

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
if verAsTuple(version.__version__) < (1, 23, 0):
    log.error("Telethon version 1.23.0+ is required! "
              "Please update Telethon to v1.23.0 or newer "
              f"(current version: {version.__version__}).")
    quit(1)

if SAFEMODE:
    log.info(setColorText("Booting in SAFE MODE", Color.GREEN))
    log.info("Loading required configurations")
else:
    log.info("Loading configurations")

API_KEY, API_HASH, STRING_SESSION = get_secure_config()

if not API_KEY and not API_HASH and not STRING_SESSION:
    if not check_secure_config():
        log.error("Cannot continue to start HyperUBot. "
                  "You may need to create a (new) secure config first.")
    quit(1)

try:
    load_configs(SAFEMODE)  # optional configs
except KeyboardInterrupt:
    log.info("Exiting...")
    quit()
except Exception:
    log.error("Unable to load optional configurations", exc_info=True)

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
