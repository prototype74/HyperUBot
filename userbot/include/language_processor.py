# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.configuration import getConfig
from importlib import import_module
from logging import getLogger
from sys import _getframe

log = getLogger(__name__)

# Language selector logic


def getBotLangCode() -> str:
    """
    Get the current bot language code from bot configuration.
    Default is 'en' if config doesn't exist

    Example:
        from userbot.include.language_processor import getBotLangCode

        print(f"Current bot language code is {getBotLangCode()}")

    Returns:
        the bot language code e.g. 'en'
    """
    ubot_lang = getConfig("UBOT_LANG", "en")
    if not ubot_lang or not isinstance(ubot_lang, str):
        ubot_lang = "en"
    return ubot_lang

__botlangcode__ = getBotLangCode()
__botlangname__ = "Unknown"

try:
    lang = import_module("userbot.translations." + __botlangcode__)
except ModuleNotFoundError:  # Language file not found
    if not __botlangcode__ == "en":
        log.warning(f"'{__botlangcode__}' language file not found. Make sure "
                    "it exists! Should have the same name as the UBOT_LANG "
                    "config in your config file. Attempting to load default "
                    "language...")
        try:
            lang = import_module("userbot.translations.en")
        except ModuleNotFoundError:
            log.error("Default language file not found, bot quitting!")
            quit(1)
        except Exception:
            log.error("Unable to load default language file, bot quitting!",
                      exc_info=True)
            quit(1)
    else:
        log.error("Default language file not found, bot quitting!")
        quit(1)
except Exception:  # Unhandled exception in language file
    if not __botlangcode__ == "en":
        log.warning(f"There was a problem loading the '{__botlangcode__}' "
                    "language file. Attempting to load default "
                    "language...", exc_info=True)
        try:
            lang = import_module("userbot.translations.en")
        except ModuleNotFoundError:
            log.error("Default language file not found, bot quitting!")
            quit(1)
        except Exception:
            log.error("Unable to load default language file, bot quitting!",
                      exc_info=True)
            quit(1)
    else:
        log.error("Unable to load default language file, bot quitting!",
                  exc_info=True)
        quit(1)

if hasattr(lang, "NAME"):
    __botlangname__ = lang.NAME
log.info(f"Loading {__botlangname__} language")

try:
    if lang.__name__ == "userbot.translations.en":
        dlang = lang
    else:
        dlang = import_module("userbot.translations.en")
except ModuleNotFoundError:
    log.error("Default language file not found, bot quitting!")
    quit(1)
except Exception:
    log.error("Unable to load default language file, bot quitting!",
              exc_info=True)
    quit(1)

# Language processor!


def getLangString(obj: object, name_of_class: str, attribute: str) -> str:
    # as 'lang' is the same object as 'dlang', use 'lang' only
    if lang is dlang:
        try:
            try:
                class_name = getattr(obj, name_of_class)
            except AttributeError:
                log.error(f"Class '{name_of_class}' not found in default "
                          "language resource", exc_info=True)
                quit(1)
            return getattr(class_name, attribute)
        except AttributeError:
            log.error(f"Attribute '{attribute}' not found in class "
                      f"'{name_of_class}' of default language resource",
                      exc_info=True)
            quit(1)
        except Exception as e:
            log.error(f"Unable to load language string: {e}", exc_info=True)
            quit(1)
    else:
        try:
            class_name = getattr(obj, name_of_class)
            return getattr(class_name, attribute)
        except AttributeError:
            try:
                class_name = getattr(dlang, name_of_class)
            except Exception:
                log.error(f"Class '{name_of_class}' not found in "
                          f"{__botlangname__} and default language resources",
                          exc_info=True)
                quit(1)
            try:
                def_attr = getattr(class_name, attribute)
                log.warning(f"Attribute '{attribute}' not found in class "
                            f"'{name_of_class}' of {__botlangname__} language "
                            "resource or class doesn't exist. Using default "
                            "attribute")
                return def_attr
            except AttributeError:
                log.error(f"Attribute '{attribute}' not found in classes "
                          f"'{name_of_class}' of {__botlangname__} and "
                          "default language resources", exc_info=True)
                quit(1)
        except Exception as e:
            log.error("Unable to load language string: {e}", exc_info=True)
            quit(1)


class AdminText(object):
    ADMINS_IN_CHAT = getLangString(
        lang, _getframe().f_code.co_name, "ADMINS_IN_CHAT")
    UNABLE_GET_ADMINS = getLangString(
        lang, _getframe().f_code.co_name, "UNABLE_GET_ADMINS")
    FAIL_CHAT = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_CHAT")
    NO_GROUP_CHAN = getLangString(
        lang, _getframe().f_code.co_name, "NO_GROUP_CHAN")
    NO_GROUP_CHAN_ARGS = getLangString(
        lang, _getframe().f_code.co_name, "NO_GROUP_CHAN_ARGS")
    NO_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "NO_ADMIN")
    NO_BAN_PRIV = getLangString(
        lang, _getframe().f_code.co_name, "NO_BAN_PRIV")
    DELETED_ACCOUNT = getLangString(
        lang, _getframe().f_code.co_name, "DELETED_ACCOUNT")
    CANNOT_BAN_SELF = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_BAN_SELF")
    CANNOT_BAN_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_BAN_ADMIN")
    BAN_SUCCESS_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "BAN_SUCCESS_REMOTE")
    BAN_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "BAN_SUCCESS")
    BAN_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "BAN_FAILED")
    CANNOT_UNBAN_SELF = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_UNBAN_SELF")
    UNBAN_SUCCESS_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "UNBAN_SUCCESS_REMOTE")
    UNBAN_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "UNBAN_SUCCESS")
    UNBAN_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "UNBAN_FAILED")
    CANNOT_KICK_SELF = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_KICK_SELF")
    KICK_SUCCESS_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "KICK_SUCCESS_REMOTE")
    KICK_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "KICK_SUCCESS")
    KICK_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "KICK_FAILED")
    PERSON_ANONYMOUS = getLangString(
        lang, _getframe().f_code.co_name, "PERSON_ANONYMOUS")
    CANNOT_PROMOTE_CHANNEL = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_PROMOTE_CHANNEL")
    NO_ONE_TO_PROMOTE = getLangString(
        lang, _getframe().f_code.co_name, "NO_ONE_TO_PROMOTE")
    NOT_USER = getLangString(
        lang, _getframe().f_code.co_name, "NOT_USER")
    CANNOT_PROMOTE_SELF = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_PROMOTE_SELF")
    ADMIN_ALREADY_SELF = getLangString(
        lang, _getframe().f_code.co_name, "ADMIN_ALREADY_SELF")
    ADMIN_ALREADY = getLangString(
        lang, _getframe().f_code.co_name, "ADMIN_ALREADY")
    ADMIN_NOT_ENOUGH_PERMS = getLangString(
        lang, _getframe().f_code.co_name, "ADMIN_NOT_ENOUGH_PERMS")
    ADD_ADMINS_REQUIRED = getLangString(
        lang, _getframe().f_code.co_name, "ADD_ADMINS_REQUIRED")
    PROMOTE_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "PROMOTE_SUCCESS")
    TOO_MANY_ADMINS = getLangString(
        lang, _getframe().f_code.co_name, "TOO_MANY_ADMINS")
    EMOJI_NOT_ALLOWED = getLangString(
        lang, _getframe().f_code.co_name, "EMOJI_NOT_ALLOWED")
    GET_ENTITY_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "GET_ENTITY_FAILED")
    PROMOTE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "PROMOTE_FAILED")
    CANNOT_DEMOTE_CHANNEL = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_DEMOTE_CHANNEL")
    NO_ONE_TO_DEMOTE = getLangString(
        lang, _getframe().f_code.co_name, "NO_ONE_TO_DEMOTE")
    CANNOT_DEMOTE_SELF = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_DEMOTE_SELF")
    DEMOTED_ALREADY = getLangString(
        lang, _getframe().f_code.co_name, "DEMOTED_ALREADY")
    DEMOTE_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "DEMOTE_SUCCESS")
    CANNOT_DEMOTE_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_DEMOTE_ADMIN")
    DEMOTE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "DEMOTE_FAILED")
    NO_GROUP_ARGS = getLangString(
        lang, _getframe().f_code.co_name, "NO_GROUP_ARGS")
    NOT_MUTE_SUB_CHAN = getLangString(
        lang, _getframe().f_code.co_name, "NOT_MUTE_SUB_CHAN")
    CANNOT_MUTE_SELF = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_MUTE_SELF")
    MUTE_SUCCESS_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "MUTE_SUCCESS_REMOTE")
    MUTE_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "MUTE_SUCCESS")
    MUTE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "MUTE_FAILED")
    NOT_UNMUTE_SUB_CHAN = getLangString(
        lang, _getframe().f_code.co_name, "NOT_UNMUTE_SUB_CHAN")
    CANNOT_UNMUTE_SELF = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_UNMUTE_SELF")
    UNMUTE_SUCCESS_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "UNMUTE_SUCCESS_REMOTE")
    UNMUTE_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "UNMUTE_SUCCESS")
    UNMUTE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "UNMUTE_FAILED")
    INVALID_ID = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_ID")
    INVALID_USERNAME = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_USERNAME")
    TRY_DEL_ACCOUNTS = getLangString(
        lang, _getframe().f_code.co_name, "TRY_DEL_ACCOUNTS")
    DEL_ACCS_COUNT = getLangString(
        lang, _getframe().f_code.co_name, "DEL_ACCS_COUNT")
    DEL_ACCS_COUNT_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "DEL_ACCS_COUNT_REMOTE")
    REM_DEL_ACCS_COUNT = getLangString(
        lang, _getframe().f_code.co_name, "REM_DEL_ACCS_COUNT")
    REM_DEL_ACCS_COUNT_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "REM_DEL_ACCS_COUNT_REMOTE")
    REM_DEL_ACCS_COUNT_EXCP = getLangString(
        lang, _getframe().f_code.co_name, "REM_DEL_ACCS_COUNT_EXCP")
    NO_DEL_ACCOUNTS = getLangString(
        lang, _getframe().f_code.co_name, "NO_DEL_ACCOUNTS")
    NO_DEL_ACCOUNTS_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "NO_DEL_ACCOUNTS_REMOTE")


class SystemToolsText(object):
    UBOT = getLangString(
        lang, _getframe().f_code.co_name, "UBOT")
    SYSTEM_STATUS = getLangString(
        lang, _getframe().f_code.co_name, "SYSTEM_STATUS")
    VER_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "VER_TEXT")
    USR_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "USR_TEXT")
    SAFEMODE = getLangString(
        lang, _getframe().f_code.co_name, "SAFEMODE")
    ON = getLangString(
        lang, _getframe().f_code.co_name, "ON")
    OFF = getLangString(
        lang, _getframe().f_code.co_name, "OFF")
    LANG = getLangString(
        lang, _getframe().f_code.co_name, "LANG")
    RTT = getLangString(
        lang, _getframe().f_code.co_name, "RTT")
    TELETON_VER = getLangString(
        lang, _getframe().f_code.co_name, "TELETON_VER")
    PYTHON_VER = getLangString(
        lang, _getframe().f_code.co_name, "PYTHON_VER")
    GITAPI_VER = getLangString(
        lang, _getframe().f_code.co_name, "GITAPI_VER")
    COMMIT_NUM = getLangString(
        lang, _getframe().f_code.co_name, "COMMIT_NUM")
    ERROR = getLangString(
        lang, _getframe().f_code.co_name, "ERROR")
    DAYS = getLangString(
        lang, _getframe().f_code.co_name, "DAYS")
    BOT_UPTIMETXT = getLangString(
        lang, _getframe().f_code.co_name, "BOT_UPTIMETXT")
    MAC_UPTIMETXT = getLangString(
        lang, _getframe().f_code.co_name, "MAC_UPTIMETXT")
    SHUTDOWN = getLangString(
        lang, _getframe().f_code.co_name, "SHUTDOWN")
    SHUTDOWN_LOG = getLangString(
        lang, _getframe().f_code.co_name, "SHUTDOWN_LOG")
    SYSD_GATHER_INFO = getLangString(
        lang, _getframe().f_code.co_name, "SYSD_GATHER_INFO")
    SYSD_NEOFETCH_REQ = getLangString(
        lang, _getframe().f_code.co_name, "SYSD_NEOFETCH_REQ")
    RESTART = getLangString(
        lang, _getframe().f_code.co_name, "RESTART")
    RESTART_UNSUPPORTED = getLangString(
        lang, _getframe().f_code.co_name, "RESTART_UNSUPPORTED")
    RESTART_LOG = getLangString(
        lang, _getframe().f_code.co_name, "RESTART_LOG")
    RESTARTED = getLangString(
        lang, _getframe().f_code.co_name, "RESTARTED")
    GENERAL = getLangString(
        lang, _getframe().f_code.co_name, "GENERAL")
    STORAGE = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE")
    STORAGE_TOTAL = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_TOTAL")
    STORAGE_USED = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_USED")
    STORAGE_FREE = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_FREE")
    USED_BY_HYPERUBOT = getLangString(
        lang, _getframe().f_code.co_name, "USED_BY_HYPERUBOT")
    STORAGE_SYSTEM = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_SYSTEM")
    STORAGE_USER = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_USER")
    STORAGE_USERDATA = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_USERDATA")
    STORAGE_TEMP_DL = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_TEMP_DL")
    STORAGE_HDD = getLangString(
        lang, _getframe().f_code.co_name, "STORAGE_HDD")
    UPLD_LOG = getLangString(
        lang, _getframe().f_code.co_name, "UPLD_LOG")
    SUCCESS_UPLD_LOG = getLangString(
        lang, _getframe().f_code.co_name, "SUCCESS_UPLD_LOG")
    FAILED_UPLD_LOG = getLangString(
        lang, _getframe().f_code.co_name, "FAILED_UPLD_LOG")


class DeletionsText(object):
    CANNOT_DEL_MSG = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_DEL_MSG")
    DEL_MSG_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "DEL_MSG_FAILED")
    REPLY_DEL_MSG = getLangString(
        lang, _getframe().f_code.co_name, "REPLY_DEL_MSG")
    NO_ADMIN_PURGE = getLangString(
        lang, _getframe().f_code.co_name, "NO_ADMIN_PURGE")
    NO_DEL_PRIV = getLangString(
        lang, _getframe().f_code.co_name, "NO_DEL_PRIV")
    PURGE_MSG_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "PURGE_MSG_FAILED")
    PURGE_COMPLETE = getLangString(
        lang, _getframe().f_code.co_name, "PURGE_COMPLETE")
    LOG_PURGE = getLangString(
        lang, _getframe().f_code.co_name, "LOG_PURGE")
    REPLY_PURGE_MSG = getLangString(
        lang, _getframe().f_code.co_name, "REPLY_PURGE_MSG")


class ChatInfoText(object):
    CHAT_ANALYSIS = getLangString(
        lang, _getframe().f_code.co_name, "CHAT_ANALYSIS")
    EXCEPTION = getLangString(
        lang, _getframe().f_code.co_name, "EXCEPTION")
    REPLY_NOT_CHANNEL = getLangString(
        lang, _getframe().f_code.co_name, "REPLY_NOT_CHANNEL")
    CANNOT_GET_CHATINFO = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_GET_CHATINFO")
    YES_BOLD = getLangString(
        lang, _getframe().f_code.co_name, "YES_BOLD")
    NO_BOLD = getLangString(
        lang, _getframe().f_code.co_name, "NO_BOLD")
    YES = getLangString(
        lang, _getframe().f_code.co_name, "YES")
    NO = getLangString(
        lang, _getframe().f_code.co_name, "NO")
    DELETED_ACCOUNT = getLangString(
        lang, _getframe().f_code.co_name, "DELETED_ACCOUNT")
    CHATINFO = getLangString(
        lang, _getframe().f_code.co_name, "CHATINFO")
    CHAT_ID = getLangString(
        lang, _getframe().f_code.co_name, "CHAT_ID")
    CHANNEL = getLangString(
        lang, _getframe().f_code.co_name, "CHANNEL")
    GROUP = getLangString(
        lang, _getframe().f_code.co_name, "GROUP")
    CHAT_TYPE = getLangString(
        lang, _getframe().f_code.co_name, "CHAT_TYPE")
    CHAT_NAME = getLangString(
        lang, _getframe().f_code.co_name, "CHAT_NAME")
    FORMER_NAME = getLangString(
        lang, _getframe().f_code.co_name, "FORMER_NAME")
    CHAT_PUBLIC = getLangString(
        lang, _getframe().f_code.co_name, "CHAT_PUBLIC")
    CHAT_PRIVATE = getLangString(
        lang, _getframe().f_code.co_name, "CHAT_PRIVATE")
    GROUP_TYPE = getLangString(
        lang, _getframe().f_code.co_name, "GROUP_TYPE")
    GROUP_TYPE_GIGAGROUP = getLangString(
        lang, _getframe().f_code.co_name, "GROUP_TYPE_GIGAGROUP")
    GROUP_TYPE_SUPERGROUP = getLangString(
        lang, _getframe().f_code.co_name, "GROUP_TYPE_SUPERGROUP")
    GROUP_TYPE_NORMAL = getLangString(
        lang, _getframe().f_code.co_name, "GROUP_TYPE_NORMAL")
    OWNER = getLangString(
        lang, _getframe().f_code.co_name, "OWNER")
    OWNER_WITH_URL = getLangString(
        lang, _getframe().f_code.co_name, "OWNER_WITH_URL")
    CREATED_NOT_NULL = getLangString(
        lang, _getframe().f_code.co_name, "CREATED_NOT_NULL")
    CREATED_NULL = getLangString(
        lang, _getframe().f_code.co_name, "CREATED_NULL")
    DCID = getLangString(
        lang, _getframe().f_code.co_name, "DCID")
    VIEWABLE_MSG = getLangString(
        lang, _getframe().f_code.co_name, "VIEWABLE_MSG")
    DELETED_MSG = getLangString(
        lang, _getframe().f_code.co_name, "DELETED_MSG")
    SENT_MSG = getLangString(
        lang, _getframe().f_code.co_name, "SENT_MSG")
    SENT_MSG_PRED = getLangString(
        lang, _getframe().f_code.co_name, "SENT_MSG_PRED")
    MEMBERS = getLangString(
        lang, _getframe().f_code.co_name, "MEMBERS")
    ADMINS = getLangString(
        lang, _getframe().f_code.co_name, "ADMINS")
    BOT_COUNT = getLangString(
        lang, _getframe().f_code.co_name, "BOT_COUNT")
    ONLINE_MEM = getLangString(
        lang, _getframe().f_code.co_name, "ONLINE_MEM")
    RESTRICTED_COUNT = getLangString(
        lang, _getframe().f_code.co_name, "RESTRICTED_COUNT")
    BANNEDCOUNT = getLangString(
        lang, _getframe().f_code.co_name, "BANNEDCOUNT")
    GRUP_STICKERS = getLangString(
        lang, _getframe().f_code.co_name, "GRUP_STICKERS")
    LINKED_CHAT = getLangString(
        lang, _getframe().f_code.co_name, "LINKED_CHAT")
    LINKED_CHAT_TITLE = getLangString(
        lang, _getframe().f_code.co_name, "LINKED_CHAT_TITLE")
    SLW_MODE = getLangString(
        lang, _getframe().f_code.co_name, "SLW_MODE")
    SLW_MODE_TIME = getLangString(
        lang, _getframe().f_code.co_name, "SLW_MODE_TIME")
    RESTR = getLangString(
        lang, _getframe().f_code.co_name, "RESTR")
    PFORM = getLangString(
        lang, _getframe().f_code.co_name, "PFORM")
    REASON = getLangString(
        lang, _getframe().f_code.co_name, "REASON")
    TEXT = getLangString(
        lang, _getframe().f_code.co_name, "TEXT")
    SCAM = getLangString(
        lang, _getframe().f_code.co_name, "SCAM")
    VERFIED = getLangString(
        lang, _getframe().f_code.co_name, "VERFIED")
    DESCRIPTION = getLangString(
        lang, _getframe().f_code.co_name, "DESCRIPTION")
    UNKNOWN = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN")
    INVALID_CH_GRP = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_CH_GRP")
    PRV_BAN = getLangString(
        lang, _getframe().f_code.co_name, "PRV_BAN")
    NOT_EXISTS = getLangString(
        lang, _getframe().f_code.co_name, "NOT_EXISTS")
    CID_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "CID_TEXT")
    CID_NO_GROUP = getLangString(
        lang, _getframe().f_code.co_name, "CID_NO_GROUP")
    LINK_INVALID_ID = getLangString(
        lang, _getframe().f_code.co_name, "LINK_INVALID_ID")
    LINK_INVALID_ID_GROUP = getLangString(
        lang, _getframe().f_code.co_name, "LINK_INVALID_ID_GROUP")
    LINK_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "LINK_TEXT")
    NO_LINK = getLangString(
        lang, _getframe().f_code.co_name, "NO_LINK")
    NO_ADMIN_PERM = getLangString(
        lang, _getframe().f_code.co_name, "NO_ADMIN_PERM")
    NO_INVITE_PERM = getLangString(
        lang, _getframe().f_code.co_name, "NO_INVITE_PERM")
    UNABLE_GET_LINK = getLangString(
        lang, _getframe().f_code.co_name, "UNABLE_GET_LINK")


class MemberInfoText(object):
    SCAN = getLangString(
        lang, _getframe().f_code.co_name, "SCAN")
    FAIL_GET_MEMBER_CHAT = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_GET_MEMBER_CHAT")
    FAIL_GET_MEMBER = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_GET_MEMBER")
    NOT_SUPERGROUP = getLangString(
        lang, _getframe().f_code.co_name, "NOT_SUPERGROUP")
    INVALID_CHAT_ID = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_CHAT_ID")
    ME_NOT_PART = getLangString(
        lang, _getframe().f_code.co_name, "ME_NOT_PART")
    USER_NOT_PART = getLangString(
        lang, _getframe().f_code.co_name, "USER_NOT_PART")
    FAIL_GET_PART = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_GET_PART")
    DELETED_ACCOUNT = getLangString(
        lang, _getframe().f_code.co_name, "DELETED_ACCOUNT")
    TIME_FOREVER = getLangString(
        lang, _getframe().f_code.co_name, "TIME_FOREVER")
    ME_NOT_MEMBER = getLangString(
        lang, _getframe().f_code.co_name, "ME_NOT_MEMBER")
    USER_NOT_MEMBER = getLangString(
        lang, _getframe().f_code.co_name, "USER_NOT_MEMBER")
    MEMBERINFO = getLangString(
        lang, _getframe().f_code.co_name, "MEMBERINFO")
    GENERAL = getLangString(
        lang, _getframe().f_code.co_name, "GENERAL")
    MINFO_ID = getLangString(
        lang, _getframe().f_code.co_name, "MINFO_ID")
    FIRST_NAME = getLangString(
        lang, _getframe().f_code.co_name, "FIRST_NAME")
    USERNAME = getLangString(
        lang, _getframe().f_code.co_name, "USERNAME")
    GROUP = getLangString(
        lang, _getframe().f_code.co_name, "GROUP")
    GROUP_NAME = getLangString(
        lang, _getframe().f_code.co_name, "GROUP_NAME")
    STATUS = getLangString(
        lang, _getframe().f_code.co_name, "STATUS")
    STATUS_OWNER = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_OWNER")
    STATUS_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_ADMIN")
    STATUS_MEMBER = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_MEMBER")
    STATUS_BANNED = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_BANNED")
    STATUS_MUTED = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_MUTED")
    STATUS_RESTRICTED = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_RESTRICTED")
    STATUS_MUTED_NOT_MEMBER = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_MUTED_NOT_MEMBER")
    STATUS_RESTRICTED_NOT_MEMBER = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_RESTRICTED_NOT_MEMBER")
    STATUS_BANNED_UNTIL = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_BANNED_UNTIL")
    STATUS_MUTED_UNTIL = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_MUTED_UNTIL")
    STATUS_RESTRICTED_UNTIL = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_RESTRICTED_UNTIL")
    STATUS_BANNED_BY = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_BANNED_BY")
    STATUS_MUTED_BY = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_MUTED_BY")
    STATUS_RESTRICTED_BY = getLangString(
        lang, _getframe().f_code.co_name, "STATUS_RESTRICTED_BY")
    ADMIN_TITLE = getLangString(
        lang, _getframe().f_code.co_name, "ADMIN_TITLE")
    PERMISSIONS = getLangString(
        lang, _getframe().f_code.co_name, "PERMISSIONS")
    CHANGE_GROUP_INFO = getLangString(
        lang, _getframe().f_code.co_name, "CHANGE_GROUP_INFO")
    DELETE_MESSAGES = getLangString(
        lang, _getframe().f_code.co_name, "DELETE_MESSAGES")
    BAN_USERS = getLangString(
        lang, _getframe().f_code.co_name, "BAN_USERS")
    INVITE_USERS = getLangString(
        lang, _getframe().f_code.co_name, "INVITE_USERS")
    PIN_MESSAGES = getLangString(
        lang, _getframe().f_code.co_name, "PIN_MESSAGES")
    ADD_ADMINS = getLangString(
        lang, _getframe().f_code.co_name, "ADD_ADMINS")
    MANAGE_CALLS = getLangString(
        lang, _getframe().f_code.co_name, "MANAGE_CALLS")
    ANONYMOUS = getLangString(
        lang, _getframe().f_code.co_name, "ANONYMOUS")
    ROOT_RIGHTS = getLangString(
        lang, _getframe().f_code.co_name, "ROOT_RIGHTS")
    SEND_MESSAGES = getLangString(
        lang, _getframe().f_code.co_name, "SEND_MESSAGES")
    SEND_MEDIA = getLangString(
        lang, _getframe().f_code.co_name, "SEND_MEDIA")
    SEND_GIFS_STICKERS = getLangString(
        lang, _getframe().f_code.co_name, "SEND_GIFS_STICKERS")
    SEND_POLLS = getLangString(
        lang, _getframe().f_code.co_name, "SEND_POLLS")
    EMBED_LINKS = getLangString(
        lang, _getframe().f_code.co_name, "EMBED_LINKS")
    WARN_ADMIN_PRIV = getLangString(
        lang, _getframe().f_code.co_name, "WARN_ADMIN_PRIV")
    PROMOTED_BY = getLangString(
        lang, _getframe().f_code.co_name, "PROMOTED_BY")
    ADDED_BY = getLangString(
        lang, _getframe().f_code.co_name, "ADDED_BY")
    JOIN_DATE = getLangString(
        lang, _getframe().f_code.co_name, "JOIN_DATE")


class MessagesText(object):
    NO_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "NO_ADMIN")
    FAIL_CHAT = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_CHAT")
    CANNOT_COUNT_DEL = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_COUNT_DEL")
    CANNOT_QUERY_FWD = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_QUERY_FWD")
    FAIL_COUNT_MSG = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_COUNT_MSG")
    USER_HAS_SENT = getLangString(
        lang, _getframe().f_code.co_name, "USER_HAS_SENT")
    USER_HAS_SENT_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "USER_HAS_SENT_REMOTE")
    CANNOT_COUNT_MSG = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_COUNT_MSG")
    CANNOT_COUNT_MSG_REMOTE = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_COUNT_MSG_REMOTE")
    PIN_REPLY_TO_MSG = getLangString(
        lang, _getframe().f_code.co_name, "PIN_REPLY_TO_MSG")
    PIN_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "PIN_SUCCESS")
    PIN_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "PIN_FAILED")
    LOG_PIN_MSG_ID = getLangString(
        lang, _getframe().f_code.co_name, "LOG_PIN_MSG_ID")
    UNPIN_REPLY_TO_MSG = getLangString(
        lang, _getframe().f_code.co_name, "UNPIN_REPLY_TO_MSG")
    UNPIN_ALL_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "UNPIN_ALL_SUCCESS")
    UNPIN_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "UNPIN_SUCCESS")
    UNPIN_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "UNPIN_FAILED")
    LOG_UNPIN_ALL_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "LOG_UNPIN_ALL_TEXT")


class ScrappersText(object):
    NO_TEXT_OR_MSG = getLangString(
        lang, _getframe().f_code.co_name, "NO_TEXT_OR_MSG")
    TRANSLATING = getLangString(
        lang, _getframe().f_code.co_name, "TRANSLATING")
    SAME_SRC_TARGET_LANG = getLangString(
        lang, _getframe().f_code.co_name, "SAME_SRC_TARGET_LANG")
    DETECTED_LANG = getLangString(
        lang, _getframe().f_code.co_name, "DETECTED_LANG")
    TARGET_LANG = getLangString(
        lang, _getframe().f_code.co_name, "TARGET_LANG")
    ORG_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "ORG_TEXT")
    TRANS_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "TRANS_TEXT")
    MSG_TOO_LONG = getLangString(
        lang, _getframe().f_code.co_name, "MSG_TOO_LONG")
    FAIL_TRANS_MSG = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_TRANS_MSG")
    FAIL_TRANS_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_TRANS_TEXT")
    MEDIA_FORBIDDEN = getLangString(
        lang, _getframe().f_code.co_name, "MEDIA_FORBIDDEN")
    NO_TEXT_TTS = getLangString(
        lang, _getframe().f_code.co_name, "NO_TEXT_TTS")
    FAIL_TTS = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_TTS")
    FAIL_API_REQ = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_API_REQ")
    INVALID_LANG_CODE = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_LANG_CODE")
    NOT_EGH_ARGS = getLangString(
        lang, _getframe().f_code.co_name, "NOT_EGH_ARGS")
    INVALID_AMOUNT_FORMAT = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_AMOUNT_FORMAT")
    CC_ISO_UNSUPPORTED = getLangString(
        lang, _getframe().f_code.co_name, "CC_ISO_UNSUPPORTED")
    CC_HEADER = getLangString(
        lang, _getframe().f_code.co_name, "CC_HEADER")
    CFROM_CTO = getLangString(
        lang, _getframe().f_code.co_name, "CFROM_CTO")
    INVALID_INPUT = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_INPUT")
    UNABLE_TO_CC = getLangString(
        lang, _getframe().f_code.co_name, "UNABLE_TO_CC")
    CC_LAST_UPDATE = getLangString(
        lang, _getframe().f_code.co_name, "CC_LAST_UPDATE")
    REPLY_TO_VM = getLangString(
        lang, _getframe().f_code.co_name, "REPLY_TO_VM")
    WORKS_WITH_VM_ONLY = getLangString(
        lang, _getframe().f_code.co_name, "WORKS_WITH_VM_ONLY")
    CONVERT_STT = getLangString(
        lang, _getframe().f_code.co_name, "CONVERT_STT")
    FAILED_LOAD_AUDIO = getLangString(
        lang, _getframe().f_code.co_name, "FAILED_LOAD_AUDIO")
    STT = getLangString(
        lang, _getframe().f_code.co_name, "STT")
    STT_TEXT = getLangString(
        lang, _getframe().f_code.co_name, "STT_TEXT")
    STT_NOT_RECOGNIZED = getLangString(
        lang, _getframe().f_code.co_name, "STT_NOT_RECOGNIZED")
    STT_REQ_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "STT_REQ_FAILED")
    STT_OUTPUT_TOO_LONG = getLangString(
        lang, _getframe().f_code.co_name, "STT_OUTPUT_TOO_LONG")
    UNABLE_TO_STT = getLangString(
        lang, _getframe().f_code.co_name, "UNABLE_TO_STT")
    SCRLANG = getLangString(
        lang, _getframe().f_code.co_name, "SCRLANG")
    MULT_ARGS = getLangString(
        lang, _getframe().f_code.co_name, "MULT_ARGS")
    INV_CT_CODE = getLangString(
        lang, _getframe().f_code.co_name, "INV_CT_CODE")
    SUCCESS_LANG_CHANGE = getLangString(
        lang, _getframe().f_code.co_name, "SUCCESS_LANG_CHANGE")


class UserText(object):
    CANNOT_LEAVE = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_LEAVE")
    LEAVING = getLangString(
        lang, _getframe().f_code.co_name, "LEAVING")
    STATS_PROCESSING = getLangString(
        lang, _getframe().f_code.co_name, "STATS_PROCESSING")
    STATS_HEADER = getLangString(
        lang, _getframe().f_code.co_name, "STATS_HEADER")
    STATS_USERS = getLangString(
        lang, _getframe().f_code.co_name, "STATS_USERS")
    STATS_BLOCKED = getLangString(
        lang, _getframe().f_code.co_name, "STATS_BLOCKED")
    STATS_BOTS = getLangString(
        lang, _getframe().f_code.co_name, "STATS_BOTS")
    STATS_BLOCKED_TOTAL = getLangString(
        lang, _getframe().f_code.co_name, "STATS_BLOCKED_TOTAL")
    STATS_GROUPS = getLangString(
        lang, _getframe().f_code.co_name, "STATS_GROUPS")
    STATS_SGC_OWNER = getLangString(
        lang, _getframe().f_code.co_name, "STATS_SGC_OWNER")
    STATS_GROUPS_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "STATS_GROUPS_ADMIN")
    STATS_SUPER_GROUPS = getLangString(
        lang, _getframe().f_code.co_name, "STATS_SUPER_GROUPS")
    STATS_SG_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "STATS_SG_ADMIN")
    STATS_CHANNELS = getLangString(
        lang, _getframe().f_code.co_name, "STATS_CHANNELS")
    STATS_CHAN_ADMIN = getLangString(
        lang, _getframe().f_code.co_name, "STATS_CHAN_ADMIN")
    STATS_UNKNOWN = getLangString(
        lang, _getframe().f_code.co_name, "STATS_UNKNOWN")
    STATS_TOTAL = getLangString(
        lang, _getframe().f_code.co_name, "STATS_TOTAL")
    FETCH_INFO = getLangString(
        lang, _getframe().f_code.co_name, "FETCH_INFO")
    FAILED_FETCH_INFO = getLangString(
        lang, _getframe().f_code.co_name, "FAILED_FETCH_INFO")
    UNKNOWN = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN")
    DELETED_ACCOUNT = getLangString(
        lang, _getframe().f_code.co_name, "DELETED_ACCOUNT")
    YES = getLangString(
        lang, _getframe().f_code.co_name, "YES")
    NO = getLangString(
        lang, _getframe().f_code.co_name, "NO")
    USR_NO_BIO = getLangString(
        lang, _getframe().f_code.co_name, "USR_NO_BIO")
    USR_INFO = getLangString(
        lang, _getframe().f_code.co_name, "USR_INFO")
    FIRST_NAME = getLangString(
        lang, _getframe().f_code.co_name, "FIRST_NAME")
    LAST_NAME = getLangString(
        lang, _getframe().f_code.co_name, "LAST_NAME")
    USERNAME = getLangString(
        lang, _getframe().f_code.co_name, "USERNAME")
    DCID = getLangString(
        lang, _getframe().f_code.co_name, "DCID")
    PROF_PIC_COUNT = getLangString(
        lang, _getframe().f_code.co_name, "PROF_PIC_COUNT")
    PROF_LINK = getLangString(
        lang, _getframe().f_code.co_name, "PROF_LINK")
    ISBOT = getLangString(
        lang, _getframe().f_code.co_name, "ISBOT")
    SCAMMER = getLangString(
        lang, _getframe().f_code.co_name, "SCAMMER")
    ISRESTRICTED = getLangString(
        lang, _getframe().f_code.co_name, "ISRESTRICTED")
    ISVERIFIED = getLangString(
        lang, _getframe().f_code.co_name, "ISVERIFIED")
    USR_ID = getLangString(
        lang, _getframe().f_code.co_name, "USR_ID")
    BIO = getLangString(
        lang, _getframe().f_code.co_name, "BIO")
    COMMON_SELF = getLangString(
        lang, _getframe().f_code.co_name, "COMMON_SELF")
    COMMON = getLangString(
        lang, _getframe().f_code.co_name, "COMMON")
    UNABLE_GET_IDS = getLangString(
        lang, _getframe().f_code.co_name, "UNABLE_GET_IDS")
    ORIGINAL_AUTHOR = getLangString(
        lang, _getframe().f_code.co_name, "ORIGINAL_AUTHOR")
    FORWARDER = getLangString(
        lang, _getframe().f_code.co_name, "FORWARDER")
    DUAL_HAS_ID_OF = getLangString(
        lang, _getframe().f_code.co_name, "DUAL_HAS_ID_OF")
    MY_ID = getLangString(
        lang, _getframe().f_code.co_name, "MY_ID")
    DEL_HAS_ID_OF = getLangString(
        lang, _getframe().f_code.co_name, "DEL_HAS_ID_OF")
    ID_NOT_ACCESSIBLE = getLangString(
        lang, _getframe().f_code.co_name, "ID_NOT_ACCESSIBLE")
    ORG_HAS_ID_OF = getLangString(
        lang, _getframe().f_code.co_name, "ORG_HAS_ID_OF")


class SystemUtilitiesText(object):
    CMD_STOPPED = getLangString(
        lang, _getframe().f_code.co_name, "CMD_STOPPED")


class GeneralMessages(object):
    ERROR = getLangString(
        lang, _getframe().f_code.co_name, "ERROR")
    CHAT_NOT_USER = getLangString(
        lang, _getframe().f_code.co_name, "CHAT_NOT_USER")
    FAIL_FETCH_ENTITY = getLangString(
        lang, _getframe().f_code.co_name, "FAIL_FETCH_ENTITY")
    UNSUPPORTED_ENTITY = getLangString(
        lang, _getframe().f_code.co_name, "UNSUPPORTED_ENTITY")
    PERSON_ANONYMOUS = getLangString(
        lang, _getframe().f_code.co_name, "PERSON_ANONYMOUS")
    CANT_FETCH_REQ = getLangString(
        lang, _getframe().f_code.co_name, "CANT_FETCH_REQ")
    LOG_USER = getLangString(
        lang, _getframe().f_code.co_name, "LOG_USER")
    LOG_USERNAME = getLangString(
        lang, _getframe().f_code.co_name, "LOG_USERNAME")
    LOG_USER_ID = getLangString(
        lang, _getframe().f_code.co_name, "LOG_USER_ID")
    LOG_CHAT_TITLE = getLangString(
        lang, _getframe().f_code.co_name, "LOG_CHAT_TITLE")
    LOG_CHAT_LINK = getLangString(
        lang, _getframe().f_code.co_name, "LOG_CHAT_LINK")
    LOG_CHAT_ID = getLangString(
        lang, _getframe().f_code.co_name, "LOG_CHAT_ID")
    UNKNOWN = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN")


class ModulesUtilsText(object):
    INVALID_ARG = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_ARG")
    USAGE = getLangString(
        lang, _getframe().f_code.co_name, "USAGE")
    AVAILABLE_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "AVAILABLE_MODULES")
    DISABLED_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "DISABLED_MODULES")
    NAME_MODULE = getLangString(
        lang, _getframe().f_code.co_name, "NAME_MODULE")
    MISSING_NUMBER_MODULE = getLangString(
        lang, _getframe().f_code.co_name, "MISSING_NUMBER_MODULE")
    MODULE_NOT_AVAILABLE = getLangString(
        lang, _getframe().f_code.co_name, "MODULE_NOT_AVAILABLE")
    MODULE_NO_DESC = getLangString(
        lang, _getframe().f_code.co_name, "MODULE_NO_DESC")
    MODULE_NO_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "MODULE_NO_USAGE")
    ASTERISK = getLangString(
        lang, _getframe().f_code.co_name, "ASTERISK")
    NOT_RUNNING_INFO = getLangString(
        lang, _getframe().f_code.co_name, "NOT_RUNNING_INFO")
    UNKNOWN = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN")
    SYSTEM = getLangString(
        lang, _getframe().f_code.co_name, "SYSTEM")
    SYSTEM_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "SYSTEM_MODULES")
    USER = getLangString(
        lang, _getframe().f_code.co_name, "USER")
    USER_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "USER_MODULES")
    PKG_NAME = getLangString(
        lang, _getframe().f_code.co_name, "PKG_NAME")
    MODULE_TYPE = getLangString(
        lang, _getframe().f_code.co_name, "MODULE_TYPE")
    AUTHORS = getLangString(
        lang, _getframe().f_code.co_name, "AUTHORS")
    VERSION = getLangString(
        lang, _getframe().f_code.co_name, "VERSION")
    SIZE = getLangString(
        lang, _getframe().f_code.co_name, "SIZE")
    INSTALL_DATE = getLangString(
        lang, _getframe().f_code.co_name, "INSTALL_DATE")
    LISTCMDS_TITLE = getLangString(
        lang, _getframe().f_code.co_name, "LISTCMDS_TITLE")
    LISTCMDS_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "LISTCMDS_USAGE")
    ARGS_NOT_REQ = getLangString(
        lang, _getframe().f_code.co_name, "ARGS_NOT_REQ")
    ARGS_NOT_AVAILABLE = getLangString(
        lang, _getframe().f_code.co_name, "ARGS_NOT_AVAILABLE")
    CMD_NOT_FOUND = getLangString(
        lang, _getframe().f_code.co_name, "CMD_NOT_FOUND")
    MOD_HELP = getLangString(
        lang, _getframe().f_code.co_name, "MOD_HELP")
    MOD_UTILS = getLangString(
        lang, _getframe().f_code.co_name, "MOD_UTILS")


class WebToolsText(object):
    PING_SPEED = getLangString(
        lang, _getframe().f_code.co_name, "PING_SPEED")
    DCMESSAGE = getLangString(
        lang, _getframe().f_code.co_name, "DCMESSAGE")
    BAD_ARGS = getLangString(
        lang, _getframe().f_code.co_name, "BAD_ARGS")
    INVALID_HOST = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_HOST")
    PINGER_VAL = getLangString(
        lang, _getframe().f_code.co_name, "PINGER_VAL")
    SPD_TEST_SELECT_SERVER = getLangString(
        lang, _getframe().f_code.co_name, "SPD_TEST_SELECT_SERVER")
    SPD_TEST_DOWNLOAD = getLangString(
        lang, _getframe().f_code.co_name, "SPD_TEST_DOWNLOAD")
    SPD_TEST_UPLOAD = getLangString(
        lang, _getframe().f_code.co_name, "SPD_TEST_UPLOAD")
    SPD_PROCESSING = getLangString(
        lang, _getframe().f_code.co_name, "SPD_PROCESSING")
    SPD_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "SPD_FAILED")
    SPD_NO_RESULT = getLangString(
        lang, _getframe().f_code.co_name, "SPD_NO_RESULT")
    SPD_NO_MEMORY = getLangString(
        lang, _getframe().f_code.co_name, "SPD_NO_MEMORY")
    SPD_FAIL_SEND_RESULT = getLangString(
        lang, _getframe().f_code.co_name, "SPD_FAIL_SEND_RESULT")
    SPD_MEGABITS = getLangString(
        lang, _getframe().f_code.co_name, "SPD_MEGABITS")
    SPD_MEGABYTES = getLangString(
        lang, _getframe().f_code.co_name, "SPD_MEGABYTES")
    SPD_TIME = getLangString(
        lang, _getframe().f_code.co_name, "SPD_TIME")
    SPD_DOWNLOAD = getLangString(
        lang, _getframe().f_code.co_name, "SPD_DOWNLOAD")
    SPD_UPLOAD = getLangString(
        lang, _getframe().f_code.co_name, "SPD_UPLOAD")
    SPD_PING = getLangString(
        lang, _getframe().f_code.co_name, "SPD_PING")
    SPD_ISP = getLangString(
        lang, _getframe().f_code.co_name, "SPD_ISP")
    SPD_HOSTED_BY = getLangString(
        lang, _getframe().f_code.co_name, "SPD_HOSTED_BY")


class GitHubText(object):
    INVALID_URL = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_URL")
    NO_RELEASE = getLangString(
        lang, _getframe().f_code.co_name, "NO_RELEASE")
    AUTHOR_STR = getLangString(
        lang, _getframe().f_code.co_name, "AUTHOR_STR")
    RELEASE_NAME = getLangString(
        lang, _getframe().f_code.co_name, "RELEASE_NAME")
    ASSET = getLangString(
        lang, _getframe().f_code.co_name, "ASSET")
    SIZE = getLangString(
        lang, _getframe().f_code.co_name, "SIZE")
    DL_COUNT = getLangString(
        lang, _getframe().f_code.co_name, "DL_COUNT")
    INVALID_ARGS = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_ARGS")


class TerminalText(object):
    BASH_ERROR = getLangString(
        lang, _getframe().f_code.co_name, "BASH_ERROR")
    BASH_CRT_FILE_FAILED_RO = getLangString(
        lang, _getframe().f_code.co_name, "BASH_CRT_FILE_FAILED_RO")
    BASH_CRT_FILE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "BASH_CRT_FILE_FAILED")
    BASH_SEND_FILE_MTLO = getLangString(
        lang, _getframe().f_code.co_name, "BASH_SEND_FILE_MTLO")
    BASH_SEND_FILE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "BASH_SEND_FILE_FAILED")


class MiscText(object):
    COIN_LANDED_VAL = getLangString(
        lang, _getframe().f_code.co_name, "COIN_LANDED_VAL")
    THRWING_COIN = getLangString(
        lang, _getframe().f_code.co_name, "THRWING_COIN")
    HEADS = getLangString(
        lang, _getframe().f_code.co_name, "HEADS")
    TAILS = getLangString(
        lang, _getframe().f_code.co_name, "TAILS")
    RAND_INVLD_ARGS = getLangString(
        lang, _getframe().f_code.co_name, "RAND_INVLD_ARGS")
    FRST_LIMIT_INVALID = getLangString(
        lang, _getframe().f_code.co_name, "FRST_LIMIT_INVALID")
    SCND_LIMIT_INVALID = getLangString(
        lang, _getframe().f_code.co_name, "SCND_LIMIT_INVALID")
    RAND_NUM_GEN = getLangString(
        lang, _getframe().f_code.co_name, "RAND_NUM_GEN")


class PackageManagerText(object):
    REPO_LIST_EMPTY = getLangString(
        lang, _getframe().f_code.co_name, "REPO_LIST_EMPTY")
    PACKAGES_UPDATER = getLangString(
        lang, _getframe().f_code.co_name, "PACKAGES_UPDATER")
    INVALID_REPO_URL = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_REPO_URL")
    UPDATING = getLangString(
        lang, _getframe().f_code.co_name, "UPDATING")
    UPDATE_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_SUCCESS")
    UPDATE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_FAILED")
    UPDATER_FINISHED = getLangString(
        lang, _getframe().f_code.co_name, "UPDATER_FINISHED")
    LIST_OF_PACKAGES = getLangString(
        lang, _getframe().f_code.co_name, "LIST_OF_PACKAGES")
    INSTALLED_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "INSTALLED_MODULES")
    NO_MODULES_INSTALLED = getLangString(
        lang, _getframe().f_code.co_name, "NO_MODULES_INSTALLED")
    MODULES_IN = getLangString(
        lang, _getframe().f_code.co_name, "MODULES_IN")
    AUTHOR = getLangString(
        lang, _getframe().f_code.co_name, "AUTHOR")
    VERSION = getLangString(
        lang, _getframe().f_code.co_name, "VERSION")
    REPO_NO_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "REPO_NO_MODULES")
    REPOS_NO_DATA = getLangString(
        lang, _getframe().f_code.co_name, "REPOS_NO_DATA")
    INSTALLED = getLangString(
        lang, _getframe().f_code.co_name, "INSTALLED")
    INSTALLED_NOTLOADED = getLangString(
        lang, _getframe().f_code.co_name, "INSTALLED_NOTLOADED")
    UPGRADEABLE = getLangString(
        lang, _getframe().f_code.co_name, "UPGRADEABLE")
    START_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "START_FAILED")
    DISABLED = getLangString(
        lang, _getframe().f_code.co_name, "DISABLED")
    EQUAL_NAME = getLangString(
        lang, _getframe().f_code.co_name, "EQUAL_NAME")
    NEVER = getLangString(
        lang, _getframe().f_code.co_name, "NEVER")
    LAST_UPDATED = getLangString(
        lang, _getframe().f_code.co_name, "LAST_UPDATED")
    INSTALL_EMPTY = getLangString(
        lang, _getframe().f_code.co_name, "INSTALL_EMPTY")
    PACKAGE_INSTALLER = getLangString(
        lang, _getframe().f_code.co_name, "PACKAGE_INSTALLER")
    NO_REPO_URL = getLangString(
        lang, _getframe().f_code.co_name, "NO_REPO_URL")
    INSTALL_EMPTY_REPO = getLangString(
        lang, _getframe().f_code.co_name, "INSTALL_EMPTY_REPO")
    UNKNOWN_REPO_URL = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN_REPO_URL")
    UNKNOWN_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN_MODULES")
    DOWNLOADING = getLangString(
        lang, _getframe().f_code.co_name, "DOWNLOADING")
    DOWN_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "DOWN_FAILED")
    INSTALL_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "INSTALL_FAILED")
    INSTALL_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "INSTALL_SUCCESS")
    UPDATE_DATA_FAIL = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_DATA_FAIL")
    NO_INSTALL_QUEUED = getLangString(
        lang, _getframe().f_code.co_name, "NO_INSTALL_QUEUED")
    INSTALLER_FINISHED = getLangString(
        lang, _getframe().f_code.co_name, "INSTALLER_FINISHED")
    UNINSTALL_EMPTY = getLangString(
        lang, _getframe().f_code.co_name, "UNINSTALL_EMPTY")
    PACKAGE_UNINSTALLER = getLangString(
        lang, _getframe().f_code.co_name, "PACKAGE_UNINSTALLER")
    UNINSTALL_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "UNINSTALL_FAILED")
    UNINSTALL_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "UNINSTALL_SUCCESS")
    UNINSTALL_DATA = getLangString(
        lang, _getframe().f_code.co_name, "UNINSTALL_DATA")
    UPDATE_DATA_FAIL = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_DATA_FAIL")
    MODULE_NOT_INSTALL = getLangString(
        lang, _getframe().f_code.co_name, "MODULE_NOT_INSTALL")
    UNINSTALLER_FINISHED = getLangString(
        lang, _getframe().f_code.co_name, "UNINSTALLER_FINISHED")
    NO_REPO_NAMES = getLangString(
        lang, _getframe().f_code.co_name, "NO_REPO_NAMES")
    NO_REPO_REMOVE = getLangString(
        lang, _getframe().f_code.co_name, "NO_REPO_REMOVE")
    REPO_REMOVER = getLangString(
        lang, _getframe().f_code.co_name, "REPO_REMOVER")
    CANNOT_REMOVE_REPO = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_REMOVE_REPO")
    REMOVING = getLangString(
        lang, _getframe().f_code.co_name, "REMOVING")
    REMOVE_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "REMOVE_SUCCESS")
    REMOVE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "REMOVE_FAILED")
    UNKNOWN_REPO = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN_REPO")
    REMOVER_FINISHED = getLangString(
        lang, _getframe().f_code.co_name, "REMOVER_FINISHED")
    LOAD_PGKS = getLangString(
        lang, _getframe().f_code.co_name, "LOAD_PGKS")
    CANNOT_INSTALL_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "CANNOT_INSTALL_MODULES")
    PACKAGE_MANAGER = getLangString(
        lang, _getframe().f_code.co_name, "PACKAGE_MANAGER")
    UNKNOWN_OPTION = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN_OPTION")
    NO_OPTION = getLangString(
        lang, _getframe().f_code.co_name, "NO_OPTION")
    PKG_HELP = getLangString(
        lang, _getframe().f_code.co_name, "PKG_HELP")
    TEXT_TOO_LONG = getLangString(
        lang, _getframe().f_code.co_name, "TEXT_TOO_LONG")


class UpdaterText(object):
    CHECKING_UPDATES = getLangString(
        lang, _getframe().f_code.co_name, "CHECKING_UPDATES")
    GIT_REPO = getLangString(
        lang, _getframe().f_code.co_name, "GIT_REPO")
    DOWNLOADING_RELEASE = getLangString(
        lang, _getframe().f_code.co_name, "DOWNLOADING_RELEASE")
    UPDATE_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_FAILED")
    UPDATE_INTERNAL_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_INTERNAL_FAILED")
    START_RECOVERY_FAILED = getLangString(
        lang, _getframe().f_code.co_name, "START_RECOVERY_FAILED")
    ALREADY_UP_TO_DATE = getLangString(
        lang, _getframe().f_code.co_name, "ALREADY_UP_TO_DATE")
    LATEST = getLangString(
        lang, _getframe().f_code.co_name, "LATEST")
    CURRENT = getLangString(
        lang, _getframe().f_code.co_name, "CURRENT")
    UPDATE_AVAILABLE = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_AVAILABLE")
    RELEASE_DATE = getLangString(
        lang, _getframe().f_code.co_name, "RELEASE_DATE")
    CHANGELOG_AT = getLangString(
        lang, _getframe().f_code.co_name, "CHANGELOG_AT")
    DOWNLOAD_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "DOWNLOAD_SUCCESS")
    DOWNLOAD_SUCCESS_WIN = getLangString(
        lang, _getframe().f_code.co_name, "DOWNLOAD_SUCCESS_WIN")
    UPDATE_QUEUED = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_QUEUED")
    UPDATE_SUCESS = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_SUCESS")
    UPDATE_FAIL = getLangString(
        lang, _getframe().f_code.co_name, "UPDATE_FAIL")


class SideloaderText(object):
    NOT_PY_FILE = getLangString(
        lang, _getframe().f_code.co_name, "NOT_PY_FILE")
    DLOADING = getLangString(
        lang, _getframe().f_code.co_name, "DLOADING")
    MODULE_EXISTS = getLangString(
        lang, _getframe().f_code.co_name, "MODULE_EXISTS")
    SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "SUCCESS")
    LOG = getLangString(
        lang, _getframe().f_code.co_name, "LOG")
    REBOOT_INFO = getLangString(
        lang, _getframe().f_code.co_name, "REBOOT_INFO")
    INVALID_FILE = getLangString(
        lang, _getframe().f_code.co_name, "INVALID_FILE")


class FeatureMgrText(object):
    DISABLE_FTR = getLangString(
        lang, _getframe().f_code.co_name, "DISABLE_FTR")
    DISABLE_FTR_FAIL = getLangString(
        lang, _getframe().f_code.co_name, "DISABLE_FTR_FAIL")
    DISABLE_FTR_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "DISABLE_FTR_SUCCESS")
    DISABLED_FTRS = getLangString(
        lang, _getframe().f_code.co_name, "DISABLED_FTRS")
    NO_DISABLED_FTRS = getLangString(
        lang, _getframe().f_code.co_name, "NO_DISABLED_FTRS")
    ENABLE_FTR = getLangString(
        lang, _getframe().f_code.co_name, "ENABLE_FTR")
    ENABLE_FTR_FAIL = getLangString(
        lang, _getframe().f_code.co_name, "ENABLE_FTR_FAIL")
    ENABLE_FTR_SUCCESS = getLangString(
        lang, _getframe().f_code.co_name, "ENABLE_FTR_SUCCESS")


class WelcomeText(object):
    WELCOME_TO_HYPERUBOT = getLangString(
        lang, _getframe().f_code.co_name, "WELCOME_TO_HYPERUBOT")
    INFO = getLangString(
        lang, _getframe().f_code.co_name, "INFO")
    INFO_STATUS = getLangString(
        lang, _getframe().f_code.co_name, "INFO_STATUS")
    INFO_OR = getLangString(
        lang, _getframe().f_code.co_name, "INFO_OR")
    INFO_HELP = getLangString(
        lang, _getframe().f_code.co_name, "INFO_HELP")
    INFO_MODULES = getLangString(
        lang, _getframe().f_code.co_name, "INFO_MODULES")
    INFO_PKG = getLangString(
        lang, _getframe().f_code.co_name, "INFO_PKG")
    INFO_SUPPORT = getLangString(
        lang, _getframe().f_code.co_name, "INFO_SUPPORT")
    INFO_SUPPORT_LINK = getLangString(
        lang, _getframe().f_code.co_name, "INFO_SUPPORT_LINK")
    INFO_SUPPORT_WIKI = getLangString(
        lang, _getframe().f_code.co_name, "INFO_SUPPORT_WIKI")
    INFO_FUN = getLangString(
        lang, _getframe().f_code.co_name, "INFO_FUN")


class ModuleDescriptions(object):
    ADMIN_DESC = getLangString(
        lang, _getframe().f_code.co_name, "ADMIN_DESC")
    CHATINFO_DESC = getLangString(
        lang, _getframe().f_code.co_name, "CHATINFO_DESC")
    DELETIONS_DESC = getLangString(
        lang, _getframe().f_code.co_name, "DELETIONS_DESC")
    MEMBERINFO_DESC = getLangString(
        lang, _getframe().f_code.co_name, "MEMBERINFO_DESC")
    MESSAGES_DESC = getLangString(
        lang, _getframe().f_code.co_name, "MESSAGES_DESC")
    SCRAPPERS_DESC = getLangString(
        lang, _getframe().f_code.co_name, "SCRAPPERS_DESC")
    SYSTOOLS_DESC = getLangString(
        lang, _getframe().f_code.co_name, "SYSTOOLS_DESC")
    USER_DESC = getLangString(
        lang, _getframe().f_code.co_name, "USER_DESC")
    WEBTOOLS_DESC = getLangString(
        lang, _getframe().f_code.co_name, "WEBTOOLS_DESC")
    GITHUB_DESC = getLangString(
        lang, _getframe().f_code.co_name, "GITHUB_DESC")
    TERMINAL_DESC = getLangString(
        lang, _getframe().f_code.co_name, "TERMINAL_DESC")
    MISC_DESC = getLangString(
        lang, _getframe().f_code.co_name, "MISC_DESC")
    PACKAGE_MANAGER_DESC = getLangString(
        lang, _getframe().f_code.co_name, "PACKAGE_MANAGER_DESC")
    UPDATER_DESC = getLangString(
        lang, _getframe().f_code.co_name, "UPDATER_DESC")
    SIDELOADER_DESC = getLangString(
        lang, _getframe().f_code.co_name, "SIDELOADER_DESC")
    FEATURE_MGR_DESC = getLangString(
        lang, _getframe().f_code.co_name, "FEATURE_MGR_DESC")


class ModuleUsages(object):
    ADMIN_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "ADMIN_USAGE")
    CHATINFO_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "CHATINFO_USAGE")
    DELETIONS_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "DELETIONS_USAGE")
    MEMBERINFO_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "MEMBERINFO_USAGE")
    MESSAGES_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "MESSAGES_USAGE")
    SCRAPPERS_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "SCRAPPERS_USAGE")
    SYSTOOLS_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "SYSTOOLS_USAGE")
    USER_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "USER_USAGE")
    WEBTOOLS_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "WEBTOOLS_USAGE")
    GITHUB_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "GITHUB_USAGE")
    TERMINAL_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "TERMINAL_USAGE")
    MISC_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "MISC_USAGE")
    PACKAGE_MANAGER_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "PACKAGE_MANAGER_USAGE")
    UPDATER_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "UPDATER_USAGE")
    SIDELOADER_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "SIDELOADER_USAGE")
    MODULES_UTILS_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "MODULES_UTILS_USAGE")
    FEATURE_MGR_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "FEATURE_MGR_USAGE")


def getBotLang() -> str:
    """
    Get the current bot language name

    Example:
        from userbot.include.language_processor import getBotLang

        print(f"Current bot language is '{getBotLang()}'")

    Returns:
        the bot language e.g. 'English' else 'Unknown'
    """
    language_name = __botlangname__
    if language_name == "Unknown":
        language_name = GeneralMessages.UNKNOWN
    return language_name

del lang, dlang  # clean up
log.info("{} language loaded successfully".format(
    getBotLang().replace(GeneralMessages.UNKNOWN, "Unknown")))
