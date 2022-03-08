# Copyright 2020-2022 nunopenim @github
# Copyright 2020-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.colors import Color, setColorText
import sys

# Check Python version
if (sys.version_info.major, sys.version_info.minor) < (3, 8):
    print(setColorText("HyperUBot requires at least Python v3.8! "
                       "Please update Python to v3.8 or newer "
                       "(current version is {}.{}.{})".format(
                           sys.version_info.major, sys.version_info.minor,
                           sys.version_info.micro), Color.RED))
    quit(1)

PROJECT = "HyperUBot"
SAFEMODE = False
SAFEMODE2 = False
NO_MODS = False

# Check command line
if len(sys.argv) >= 2:
    if sys.argv[1].lower() == "-safemode":  # safe mode
        SAFEMODE = True
    elif sys.argv[1].lower() == "-safemode2":  # advanced safe mode
        SAFEMODE = True
        SAFEMODE2 = True
    elif sys.argv[1].lower() == "-nomods":  # core services only
        NO_MODS = True

from telethon import version as tl_version  # noqa: E402
from userbot.sysutils.sys_funcs import isWindows, verAsTuple  # noqa: E402

# Check Telethon version
if verAsTuple(tl_version.__version__) < (1, 24, 0):
    print(setColorText("HyperUBot requires at least Telethon version 1.24.0! "
                       "Please update Telethon to v1.24.0 or newer "
                       f"(current version is {tl_version.__version__})",
                       Color.RED))
    quit(1)

from userbot._core.access_controller import _protectedAccess  # noqa: E402
from userbot._core.client import HyperClient  # noqa: E402
from userbot.sysutils.config_loader import (_ConfigLoader,
                                            _SecureConfigLoader)  # noqa: E402
from userbot.sysutils.configuration import addConfig, getConfig  # noqa: E402
from userbot.sysutils.logger import _UserbotLogger  # noqa: E402
from userbot.sysutils.properties import _SysProperties  # noqa: E402
from userbot.sysutils._services import _SysServices  # noqa: E402
from telethon.sessions import StringSession  # noqa: E402
from logging import getLogger  # noqa: E402
from os import path, mkdir  # noqa: E402

# Start file and terminal logging
log = getLogger(__name__)
__hyper_logger__ = _UserbotLogger(log)
__hyper_logger__._initialize_logfile(PROJECT, SAFEMODE, SAFEMODE2, NO_MODS,
                                     sys.version_info, tl_version)
__hyper_logger__._setup_logger()

try:
    if not path.exists(path.join(".", "userbot", "userdata")):
        mkdir(path.join(".", "userbot", "userdata"))
except Exception:
    log.error("Failed to initialize user data directory", exc_info=True)

# Initialize system props
__sysprops__ = _SysProperties()
__sysprops__._init_props()
_setprop = __sysprops__._setprop
_getprop = __sysprops__._getprop

# Initialize services
_services = _SysServices(__hyper_logger__)

# Initialize configurations
__cfg_loader__ = _ConfigLoader()
__scfg_loader__ = _SecureConfigLoader()
__cfg_loader__._initialize_configs()

if NO_MODS:
    log.info(setColorText("Booting in CORE ONLY MODE", Color.MAGENTA))
elif SAFEMODE:
    if SAFEMODE2:
        log.info(setColorText("Booting in ADVANCED SAFE MODE", Color.GREEN))
    else:
        log.info(setColorText("Booting in SAFE MODE", Color.GREEN))
    log.info("Loading required configurations")
else:
    log.info("Loading configurations")

try:
    API_KEY, API_HASH, STRING_SESSION = __scfg_loader__._get_secure_config()
except KeyboardInterrupt:
    print()
    log.info("Exiting...")
    quit()

if __scfg_loader__._load_cfg_failed():
    log.warning("There is an issue to parse or read your secure config. "
                "Due to this HyperUBot can't continue. If your secure config "
                "file got corrupted, start 'Secure-Config-Updater' to create "
                "a new file. If it's not, try the next suggestions")
    try:
        options = ["Start Secure-Config-Updater",
                   "Update your pip packages",
                   "Contact suppport",
                   "Quit HyperUBot"]
        pip_text = ("Outdated pip packages could also cause this issue. "
                    "To check for outdated pip packages run "
                    "'{} -m pip list -o' in your terminal and check if the "
                    "following packages are listed: cffi, pyAesCrypt. "
                    "If so, update them.")
        contact_text = ("If none of the suggestions helped, contact us at "
                        "Telegram 'https://t.me/HyperUBotSupport' and keep "
                        "your hyper.log file ready!")
        if isWindows():
            options[0] += " (python update_secure_cfg.py)"
            options[1] = pip_text.format("python")
            options[2] = contact_text
            options.pop()
            _services._suggest_options(options)
        else:
            option = _services._suggest_options(options)
            if option == 1:
                _services._start_scfg_updater()
            elif option == 2:
                log.info(pip_text.format(f"python{sys.version_info.major}."
                                         f"{sys.version_info.minor}"))
            elif option == 3:
                log.info(contact_text)
    except KeyboardInterrupt:
        print()
        log.info("Exiting...")
    quit(1)

if __scfg_loader__._getTooManyAttempts():
    log.error("Too many failed attempts. Please try again later.")
    log.warning("Forgot your password? Start 'Secure-Config-Updater' to "
                "create a new secure config file instead.")
    try:
        options = ["Start Secure-Config-Updater",
                   "Quit HyperUBot"]
        if isWindows():
            options[0] += " (python update_secure_cfg.py)"
            options.pop()
            _services._suggest_options(options)
        else:
            option = _services._suggest_options(options)
            if option == 1:
                _services._start_scfg_updater()
    except KeyboardInterrupt:
        print()
        log.info("Exiting...")
    quit(1)

if not API_KEY and not API_HASH and not STRING_SESSION:
    if not __scfg_loader__._check_secure_config():
        log.error("Cannot continue to start HyperUBot as there is no secure "
                  "config. You may need to create a (new) secure config")
    else:
        log.error("All values from your secure config are empty!")
    log.warning("If it's your first time running HyperUBot or if you "
                "reinstalled it, you should start the 'Setup Assistant' "
                "For all other cases: if you don't have a string session yet "
                "or it was terminated, start 'String Session Generator'. "
                "Start 'Secure-Config-Updater' to create/update your secure "
                "config but only if you have a valid string session already!")
    try:
        options = ["Start Setup Assistant (recommended)",
                   "Start String Session Generator",
                   "Start Secure-Config-Updater",
                   "Quit HyperUBot"]
        if isWindows():
            options[0] += " (python setup.py)"
            options[1] += " (python generate_session.py)"
            options[2] += " (python update_secure_cfg.py)"
            options.pop()
            _services._suggest_options(options)
        else:
            option = _services._suggest_options(options)
            if option == 1:
                _services._start_setup_assistant()
            elif option == 2:
                _services._start_session_gen()
            elif option == 3:
                _services._start_scfg_updater()
    except KeyboardInterrupt:
        print()
        log.info("Exiting...")
    quit(1)

if not API_KEY:
    log.error("App api_id from your secure config is empty!")

if not API_HASH:
    log.error("App api_hash from your secure config is empty!")

if not STRING_SESSION:
    log.error("String session from your secure config is empty!")

if not API_KEY or not API_HASH or not STRING_SESSION:
    log.error("Make sure none of your keys in your secure config are empty as "
              "these keys (App api_id, App api_hash and/or string session) "
              "are required in order to use HyperUBot properly")
    log.warning("If you skipped or just forgot to add them "
                "start 'Secure-Config-Updater' to update your secure "
                "config. " +
                (("If you don't know what a string session even is, start "
                  "'String Session Generator'")
                 if not STRING_SESSION else ""))
    try:
        options = ["Start Secure-Config-Updater",
                   "Quit HyperUBot"]
        if not STRING_SESSION:
            options.insert(1, "Start String Session Generator")
        if isWindows():
            options[0] += " (python update_secure_cfg.py)"
            if not STRING_SESSION:
                options[1] += " (python generate_session.py)"
            options.pop()
            _services._suggest_options(options)
        else:
            option = _services._suggest_options(options)
            if option == 1:
                _services._start_scfg_updater()
            elif option == 2 and not STRING_SESSION:
                _services._start_session_gen()
    except KeyboardInterrupt:
        print()
        log.info("Exiting...")
    quit(1)

if not NO_MODS:
    try:
        __cfg_loader__._load_configs(SAFEMODE)  # optional configs
    except KeyboardInterrupt:
        log.info("Exiting...")
        quit()
    except Exception:
        log.error("Unable to load optional configurations", exc_info=True)

if (SAFEMODE or NO_MODS) and not getConfig("UBOT_LANG"):
    addConfig("UBOT_LANG", "en")

if not getConfig("TEMP_DL_DIR"):
    addConfig("TEMP_DL_DIR", path.join(".", "downloads"))

if not NO_MODS:
    log.info("Configurations loaded")

try:
    if not path.exists(getConfig("TEMP_DL_DIR")):
        mkdir(getConfig("TEMP_DL_DIR"))
except Exception:
    log.error("Failed to initialize download directory")

try:
    _connect_retries = getConfig("CLIENT_CONNECT_RETRIES", 5)
    if not isinstance(_connect_retries, int) or _connect_retries < -1:
        _connect_retries = 5
    _retry_delay = getConfig("CLIENT_RETRY_DELAY", 1)
    if not isinstance(_retry_delay, (int, float)) or _retry_delay < 0:
        _retry_delay = 1
    _tgclient = HyperClient(StringSession(STRING_SESSION), API_KEY, API_HASH,
                            connection_retries=_connect_retries,
                            retry_delay=_retry_delay)
    del API_KEY, API_HASH, STRING_SESSION, _connect_retries, _retry_delay
except Exception as e:
    log.critical(f"Failed to create Telegram Client: {e}", exc_info=True)
    try:
        options = ["Start Recovery",
                   "Contact support",
                   "Quit HyperUBot"]
        contact_text = ("If you facing issues to start the bot contact us at "
                        "Telegram 'https://t.me/HyperUBotSupport' and keep "
                        "your hyper.log file ready!")
        if isWindows():
            options[0] += " (python recovery.py)"
            options[1] = contact_text
            options.pop()
            _services._suggest_options(options)
        else:
            option = _services._suggest_options(options)
            if option == 1:
                _services._reboot_recovery(False)
            elif option == 2:
                log.info(contact_text)
    except KeyboardInterrupt:
        print()
        log.info("Exiting...")
    quit(1)


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=[
        "addConfig", "HyperClient", "_ConfigLoader", "_SecureConfigLoader",
        "_services", "_setprop", "_SysProperties", "_SysServices", "_tgclient",
        "_UserbotLogger", "__cfg_loader__", "__hyper_logger__",
        "__scfg_loader__"
    ],
    warn_msg="Illegal access to '{0}' blocked (requested by {1}:{2})",
    allowed=(path.join("userbot", "modules", "_systools.py"),
             path.join("userbot", "modules", "_updater.py")),
    mlogger=log
)
