# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.colors import Color, setColorText
from sys import argv, version_info

# Check Python version
if (version_info.major, version_info.minor) < (3, 8):
    print(setColorText("HyperUBot requires at least Python v3.8! "
                       "Please update Python to v3.8 or newer "
                       "(current version is {}.{}.{})".format(
                           version_info.major, version_info.minor,
                           version_info.micro), Color.RED))
    quit(1)

PROJECT = "HyperUBot"
SAFEMODE = False

# Check safe mode from command line
if len(argv) >= 2:
    if argv[1].lower() == "-safemode":
        SAFEMODE = True

from telethon import TelegramClient, version  # noqa: E402
from userbot.sysutils.sys_funcs import os_name, verAsTuple  # noqa: E402

OS = os_name()  # Current Operating System [DEPRECATED]

# Check Telethon version
if verAsTuple(version.__version__) < (1, 23, 0):
    print(setColorText("HyperUBot requires at least Telethon version 1.23.0! "
                       "Please update Telethon to v1.23.0 or newer "
                       f"(current version is {version.__version__})",
                       Color.RED))
    quit(1)

from userbot.sysutils.config_loader import (check_secure_config,
                                            load_configs,
                                            get_secure_config)  # noqa: E402
from userbot.sysutils.configuration import addConfig, getConfig  # noqa: E402
from userbot.sysutils.logger import _UserbotLogger  # noqa: E402
from telethon.errors.rpcerrorlist import (ApiIdInvalidError,
                                          PhoneNumberInvalidError)  # noqa: E402
from telethon.sessions import StringSession  # noqa: E402
from logging import getLogger  # noqa: E402
from os import path, mkdir  # noqa: E402

# Start file and terminal logging
log = getLogger(__name__)
_hyper_logger = _UserbotLogger(log)
_hyper_logger._setup_logger()
_hyper_logger._initialize_logfile(PROJECT, SAFEMODE, version_info, version)

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
