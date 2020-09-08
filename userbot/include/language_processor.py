# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import UBOT_LANG
from importlib import import_module
from logging import getLogger

# Temp because pyCharm needs for autocompletion and I am being a Lazy S.O.B. again
import userbot.translations.en as text

log = getLogger(__name__)

# Language selector logic

try:
    text = import_module("userbot.translations." + UBOT_LANG)
except:
    log.warning("There was a problem loading the language file. Make sure it exists! Should have the same name as the UBOT_LANG variable in config.py. Attempting to load default language")
    try:
        text = import_module("userbot.translations.en")
    except:
        log.error("English language file not found, bot quitting!")
        exit(1)

# Language processor!

class AdminText(object): # Admin module
    FAIL_CHAT = text.AdminText.FAIL_CHAT
    NO_GROUP_CHAN = text.AdminText.NO_GROUP_CHAN
    NO_GROUP_CHAN_ARGS = text.AdminText.NO_GROUP_CHAN_ARGS
    NO_ADMIN = text.AdminText.NO_ADMIN
    NO_BAN_PRIV = text.AdminText.NO_BAN_PRIV
    DELETED_ACCOUNT = text.AdminText.DELETED_ACCOUNT
    CANNOT_BAN_SELF = text.AdminText.CANNOT_BAN_SELF
    CANNOT_BAN_ADMIN = text.AdminText.CANNOT_BAN_ADMIN
    BAN_SUCCESS_REMOTE = text.AdminText.BAN_SUCCESS_REMOTE
    BAN_SUCCESS = text.AdminText.BAN_SUCCESS
    BAN_FAILED = text.AdminText.BAN_FAILED
    CANNOT_UNBAN_SELF = text.AdminText.CANNOT_UNBAN_SELF
    UNBAN_SUCCESS_REMOTE = text.AdminText.UNBAN_SUCCESS_REMOTE
    UNBAN_SUCCESS = text.AdminText.UNBAN_SUCCESS
    UNBAN_FAILED = text.AdminText.UNBAN_FAILED
    CANNOT_KICK_SELF = text.AdminText.CANNOT_KICK_SELF
    KICK_SUCCESS_REMOTE = text.AdminText.KICK_SUCCESS_REMOTE
    KICK_SUCCESS = text.AdminText.KICK_SUCCESS
    KICK_FAILED = text.AdminText.KICK_FAILED
    NOONE_TO_PROMOTE = text.AdminText.NOONE_TO_PROMOTE
    NOT_USER = text.AdminText.NOT_USER
    CANNOT_PROMOTE_SELF = text.AdminText.CANNOT_PROMOTE_SELF
    ADMIN_ALREADY_SELF = text.AdminText.ADMIN_ALREADY_SELF
    ADMIN_ALREADY = text.AdminText.ADMIN_ALREADY
    ADMIN_NOT_ENOUGH_PERMS = text.AdminText.ADMIN_NOT_ENOUGH_PERMS
    ADD_ADMINS_REQUIRED = text.AdminText.ADD_ADMINS_REQUIRED
    PROMOTE_SUCCESS = text.AdminText.PROMOTE_SUCCESS
    TOO_MANY_ADMINS = text.AdminText.TOO_MANY_ADMINS
    EMOJI_NOT_ALLOWED = text.AdminText.EMOJI_NOT_ALLOWED
    GET_ENTITY_FAILED = text.AdminText.GET_ENTITY_FAILED
    PROMOTE_FAILED = text.AdminText.PROMOTE_FAILED
    NOONE_TO_DEMOTE = text.AdminText.NOONE_TO_DEMOTE
    CANNOT_DEMOTE_SELF = text.AdminText.CANNOT_DEMOTE_SELF
    DEMOTED_ALREADY = text.AdminText.DEMOTED_ALREADY
    DEMOTE_SUCCESS = text.AdminText.DEMOTE_SUCCESS
    CANNOT_DEMOTE_ADMIN = text.AdminText.CANNOT_DEMOTE_ADMIN
    DEMOTE_FAILED = text.AdminText.DEMOTE_FAILED
    NO_GROUP_ARGS = text.AdminText.NO_GROUP_ARGS
    NOT_MUTE_SUB_CHAN = text.AdminText.NOT_MUTE_SUB_CHAN
    CANNOT_MUTE_SELF = text.AdminText.CANNOT_MUTE_SELF
    MUTE_SUCCESS_REMOTE = text.AdminText.MUTE_SUCCESS_REMOTE
    MUTE_SUCCESS = text.AdminText.MUTE_SUCCESS
    MUTE_FAILED = text.AdminText.MUTE_FAILED
    NOT_UNMUTE_SUB_CHAN = text.AdminText.NOT_UNMUTE_SUB_CHAN
    CANNOT_UNMUTE_SELF = text.AdminText.CANNOT_UNMUTE_SELF
    UNMUTE_SUCCESS_REMOTE = text.AdminText.UNMUTE_SUCCESS_REMOTE
    UNMUTE_SUCCESS = text.AdminText.UNMUTE_SUCCESS
    UNMUTE_FAILED = text.AdminText.UNMUTE_FAILED
    TRY_DEL_ACCOUNTS = text.AdminText.TRY_DEL_ACCOUNTS
    DEL_ACCS_COUNT = text.AdminText.DEL_ACCS_COUNT
    REM_DEL_ACCS_COUNT = text.AdminText.REM_DEL_ACCS_COUNT
    NO_DEL_ACCOUNTS = text.AdminText.NO_DEL_ACCOUNTS
    REPLY_TO_MSG = text.AdminText.REPLY_TO_MSG
    PIN_SUCCESS = text.AdminText.PIN_SUCCESS
    PINNED_ALREADY = text.AdminText.PINNED_ALREADY
    PIN_FAILED = text.AdminText.PIN_FAILED
    LOG_PIN_MSG_ID = text.AdminText.LOG_PIN_MSG_ID

class StatusText(object):
    UBOT = text.StatusText.UBOT
    SYSTEM_STATUS = text.StatusText.SYSTEM_STATUS
    ONLINE = text.StatusText.ONLINE
    VER_TEXT = text.StatusText.VER_TEXT
    USR_TEXT = text.StatusText.USR_TEXT
    RTT = text.StatusText.RTT
    TELETON_VER = text.StatusText.TELETON_VER
    PYTHON_VER = text.StatusText.PYTHON_VER
    GITAPI_VER = text.StatusText.GITAPI_VER
    CASAPI_VER = text.StatusText.CASAPI_VER
    COMMIT_NUM = text.StatusText.COMMIT_NUM
    ERROR = text.StatusText.ERROR
    DAYS = text.StatusText.DAYS
    BOT_UPTIMETXT = text.StatusText.BOT_UPTIMETXT
    MAC_UPTIMETXT = text.StatusText.MAC_UPTIMETXT
    SHUTDOWN = text.StatusText.SHUTDOWN
    SHUTDOWN_LOG = text.StatusText.SHUTDOWN_LOG
    SYSD_NEOFETCH_REQ = text.StatusText.SYSD_NEOFETCH_REQ
    RESTART = text.StatusText.RESTART
    RESTART_LOG = text.StatusText.RESTART_LOG
    RESTARTED = text.StatusText.RESTARTED

class DeletionsText(object):
    CANNOT_DEL_MSG = text.DeletionsText.CANNOT_DEL_MSG
    UNABLE_DEL_MSG = text.DeletionsText.UNABLE_DEL_MSG
    DEL_MSG_FAILED = text.DeletionsText.DEL_MSG_FAILED
    REPLY_DEL_MSG = text.DeletionsText.REPLY_DEL_MSG
    NO_ADMIN_PURGE = text.DeletionsText.NO_ADMIN_PURGE
    NO_DEL_PRIV = text.DeletionsText.NO_DEL_PRIV
    PURGE_MSG_FAILED = text.DeletionsText.PURGE_MSG_FAILED
    PURGE_COMPLETE = text.DeletionsText.PURGE_COMPLETE
    LOG_PURGE = text.DeletionsText.LOG_PURGE
    REPLY_PURGE_MSG = text.DeletionsText.REPLY_PURGE_MSG

class ChatInfoText(object):
    CHAT_ANALYSIS = text.ChatInfoText.CHAT_ANALYSIS
    EXCEPTION = text.ChatInfoText.EXCEPTION
    CANNOT_GET_CHATINFO = text.ChatInfoText.CANNOT_GET_CHATINFO
    YES_BOLD = text.ChatInfoText.YES_BOLD
    NO_BOLD = text.ChatInfoText.NO_BOLD
    YES = text.ChatInfoText.YES
    NO = text.ChatInfoText.NO
    CHATINFO = text.ChatInfoText.CHATINFO
    CHAT_ID = text.ChatInfoText.CHAT_ID
    CHATTYPE = text.ChatInfoText.CHATTYPE
    CHAT_NAME = text.ChatInfoText.CHAT_NAME
    FORMER_NAME = text.ChatInfoText.FORMER_NAME
    CHAT_TYPE_PUBLIC = text.ChatInfoText.CHAT_TYPE_PUBLIC
    CHAT_TYPE_PRIVATE = text.ChatInfoText.CHAT_TYPE_PRIVATE
    CREATOR = text.ChatInfoText.CREATOR
    CREATOR_WITH_URL = text.ChatInfoText.CREATOR_WITH_URL
    CREATED_NOT_NULL = text.ChatInfoText.CREATED_NOT_NULL
    CREATED_NULL = text.ChatInfoText.CREATED_NULL
    DCID = text.ChatInfoText.DCID
    CHAT_LEVEL = text.ChatInfoText.CHAT_LEVEL
    VIEWABLE_MSG = text.ChatInfoText.VIEWABLE_MSG
    DELETED_MSG = text.ChatInfoText.DELETED_MSG
    SENT_MSG = text.ChatInfoText.SENT_MSG
    SENT_MSG_PRED = text.ChatInfoText.SENT_MSG_PRED
    MEMBERS = text.ChatInfoText.MEMBERS
    ADMINS = text.ChatInfoText.ADMINS
    BOT_COUNT = text.ChatInfoText.BOT_COUNT
    ONLINE_MEM = text.ChatInfoText.ONLINE_MEM
    RESTRICTED_COUNT = text.ChatInfoText.RESTRICTED_COUNT
    BANNEDCOUNT = text.ChatInfoText.BANNEDCOUNT
    GRUP_STICKERS = text.ChatInfoText.GRUP_STICKERS
    LINKED_CHAT = text.ChatInfoText.LINKED_CHAT
    LINKED_CHAT_TITLE = text.ChatInfoText.LINKED_CHAT_TITLE
    SLW_MODE = text.ChatInfoText.SLW_MODE
    SLW_MODE_TIME = text.ChatInfoText.SLW_MODE_TIME
    SPER_GRP = text.ChatInfoText.SPER_GRP
    RESTR = text.ChatInfoText.RESTR
    PFORM = text.ChatInfoText.PFORM
    REASON = text.ChatInfoText.REASON
    TEXT = text.ChatInfoText.TEXT
    SCAM = text.ChatInfoText.SCAM
    VERFIED = text.ChatInfoText.VERFIED
    DESCRIPTION = text.ChatInfoText.DESCRIPTION
    UNKNOWN = text.ChatInfoText.UNKNOWN
    INVALID_CH_GRP = text.ChatInfoText.INVALID_CH_GRP
    PRV_BAN = text.ChatInfoText.PRV_BAN
    NOT_EXISTS = text.ChatInfoText.NOT_EXISTS

class MemberInfoText(object):
    SCAN = text.MemberInfoText.SCAN
    FAIL_GET_MEMBER_CHAT = text.MemberInfoText.FAIL_GET_MEMBER_CHAT
    FAIL_GET_MEMBER = text.MemberInfoText.FAIL_GET_MEMBER
    NOT_SUPERGROUP = text.MemberInfoText.NOT_SUPERGROUP
    INVALID_CHAT_ID = text.MemberInfoText.INVALID_CHAT_ID
    ME_NOT_PART = text.MemberInfoText.ME_NOT_PART
    USER_NOT_PART = text.MemberInfoText.USER_NOT_PART
    FAIL_GET_PART = text.MemberInfoText.FAIL_GET_PART
    DELETED_ACCOUNT = text.MemberInfoText.DELETED_ACCOUNT
    TIME_FOREVER = text.MemberInfoText.TIME_FOREVER
    ME_NOT_MEMBER = text.MemberInfoText.ME_NOT_MEMBER
    USER_NOT_MEMBER = text.MemberInfoText.USER_NOT_MEMBER
    MEMBERINFO = text.MemberInfoText.MEMBERINFO
    GENERAL = text.MemberInfoText.GENERAL
    MINFO_ID = text.MemberInfoText.MINFO_ID
    FIRST_NAME = text.MemberInfoText.FIRST_NAME
    USERNAME = text.MemberInfoText.USERNAME
    GROUP = text.MemberInfoText.GROUP
    GROUP_NAME = text.MemberInfoText.GROUP_NAME
    STATUS = text.MemberInfoText.STATUS
    STATUS_OWNER = text.MemberInfoText.STATUS_OWNER
    STATUS_ADMIN = text.MemberInfoText.STATUS_ADMIN
    STATUS_MEMBER = text.MemberInfoText.STATUS_MEMBER
    STATUS_BANNED = text.MemberInfoText.STATUS_BANNED
    STATUS_MUTED = text.MemberInfoText.STATUS_MUTED
    STATUS_RESTRICTED = text.MemberInfoText.STATUS_RESTRICTED
    STATUS_MUTED_NOT_MEMBER = text.MemberInfoText.STATUS_MUTED_NOT_MEMBER
    STATUS_RESTRICTED_NOT_MEMBER = text.MemberInfoText.STATUS_RESTRICTED_NOT_MEMBER
    STATUS_BANNED_UNTIL = text.MemberInfoText.STATUS_BANNED_UNTIL
    STATUS_MUTED_UNTIL = text.MemberInfoText.STATUS_MUTED_UNTIL
    STATUS_RESTRICTED_UNTIL = text.MemberInfoText.STATUS_RESTRICTED_UNTIL
    STATUS_BANNED_BY = text.MemberInfoText.STATUS_BANNED_BY
    STATUS_MUTED_BY = text.MemberInfoText.STATUS_MUTED_BY
    STATUS_RESTRICTED_BY = text.MemberInfoText.STATUS_RESTRICTED_BY
    ADMIN_TITLE = text.MemberInfoText.ADMIN_TITLE
    PERMISSIONS = text.MemberInfoText.PERMISSIONS
    CHANGE_GROUP_INFO = text.MemberInfoText.CHANGE_GROUP_INFO
    DELETE_MESSAGES = text.MemberInfoText.DELETE_MESSAGES
    BAN_USERS = text.MemberInfoText.BAN_USERS
    INVITE_USERS = text.MemberInfoText.INVITE_USERS
    PIN_MESSAGES = text.MemberInfoText.PIN_MESSAGES
    ADD_ADMINS = text.MemberInfoText.ADD_ADMINS
    ROOT_RIGHTS = text.MemberInfoText.ROOT_RIGHTS
    SEND_MESSAGES = text.MemberInfoText.SEND_MESSAGES
    SEND_MEDIA = text.MemberInfoText.SEND_MEDIA
    SEND_GIFS_STICKERS = text.MemberInfoText.SEND_GIFS_STICKERS
    SEND_POLLS = text.MemberInfoText.SEND_POLLS
    EMBED_LINKS = text.MemberInfoText.EMBED_LINKS
    WARN_ADMIN_PRIV = text.MemberInfoText.WARN_ADMIN_PRIV
    PROMOTED_BY = text.MemberInfoText.PROMOTED_BY
    ADDED_BY = text.MemberInfoText.ADDED_BY
    JOIN_DATE = text.MemberInfoText.JOIN_DATE

class ScrappersText(object):
    NO_TEXT_OR_MSG = text.ScrappersText.NO_TEXT_OR_MSG
    TRANSLATING = text.ScrappersText.TRANSLATING
    SAME_SRC_TARGET_LANG = text.ScrappersText.SAME_SRC_TARGET_LANG
    DETECTED_LANG = text.ScrappersText.DETECTED_LANG
    TARGET_LANG = text.ScrappersText.TARGET_LANG
    ORG_TEXT = text.ScrappersText.ORG_TEXT
    TRANS_TEXT = text.ScrappersText.TRANS_TEXT
    MSG_TOO_LONG = text.ScrappersText.MSG_TOO_LONG
    FAIL_TRANS_MSG = text.ScrappersText.FAIL_TRANS_MSG
    FAIL_TRANS_TEXT = text.ScrappersText.FAIL_TRANS_TEXT
    MEDIA_FORBIDDEN = text.ScrappersText.MEDIA_FORBIDDEN
    NO_TEXT_TTS = text.ScrappersText.NO_TEXT_TTS
    FAIL_TTS = text.ScrappersText.FAIL_TTS
    FAIL_API_REQ = text.ScrappersText.FAIL_API_REQ
    INVALID_LANG_CODE = text.ScrappersText.INVALID_LANG_CODE

class UserText(object):
    LEAVING = text.UserText.LEAVING
    STATS_PROCESSING = text.UserText.STATS_PROCESSING
    STATS_HEADER = text.UserText.STATS_HEADER
    STATS_USERS = text.UserText.STATS_USERS
    STATS_BLOCKED = text.UserText.STATS_BLOCKED
    STATS_BOTS = text.UserText.STATS_BOTS
    STATS_BLOCKED_TOTAL = text.UserText.STATS_BLOCKED_TOTAL
    STATS_GROUPS = text.UserText.STATS_GROUPS
    STATS_SGC_OWNER = text.UserText.STATS_SGC_OWNER
    STATS_GROUPS_ADMIN = text.UserText.STATS_GROUPS_ADMIN
    STATS_SUPER_GROUPS = text.UserText.STATS_SUPER_GROUPS
    STATS_SG_ADMIN = text.UserText.STATS_SG_ADMIN
    STATS_CHANNELS = text.UserText.STATS_CHANNELS
    STATS_CHAN_ADMIN = text.UserText.STATS_CHAN_ADMIN
    STATS_UNKNOWN = text.UserText.STATS_UNKNOWN
    STATS_TOTAL = text.UserText.STATS_TOTAL
    FETCH_INFO = text.UserText.FETCH_INFO
    FAILED_FETCH_INFO = text.UserText.FAILED_FETCH_INFO
    UNKNOWN = text.UserText.UNKNOWN
    DELETED_ACCOUNT = text.UserText.DELETED_ACCOUNT
    YES = text.UserText.YES
    NO = text.UserText.NO
    USR_NO_BIO = text.UserText.USR_NO_BIO
    USR_INFO = text.UserText.USR_INFO
    FIRST_NAME = text.UserText.FIRST_NAME
    LAST_NAME = text.UserText.LAST_NAME
    USERNAME = text.UserText.USERNAME
    DCID = text.UserText.DCID
    PROF_PIC_COUNT = text.UserText.PROF_PIC_COUNT
    PROF_LINK = text.UserText.PROF_LINK
    ISBOT = text.UserText.ISBOT
    SCAMMER = text.UserText.SCAMMER
    ISRESTRICTED = text.UserText.ISRESTRICTED
    ISVERIFIED = text.UserText.ISVERIFIED
    USR_ID = text.UserText.USR_ID
    BIO = text.UserText.BIO
    COMMON_SELF = text.UserText.COMMON_SELF
    COMMON = text.UserText.COMMON

class GeneralMessages(object):
    ERROR = text.GeneralMessages.ERROR
    CHAT_NOT_USER = text.GeneralMessages.CHAT_NOT_USER
    FAIL_FETCH_USER = text.GeneralMessages.FAIL_FETCH_USER
    ENTITY_NOT_USER = text.GeneralMessages.ENTITY_NOT_USER
    CALL_UREQ_FAIL = text.GeneralMessages.CALL_UREQ_FAIL
    LOG_USER = text.GeneralMessages.LOG_USER
    LOG_USERNAME = text.GeneralMessages.LOG_USERNAME
    LOG_USER_ID = text.GeneralMessages.LOG_USER_ID
    LOG_CHAT_TITLE = text.GeneralMessages.LOG_CHAT_TITLE
    LOG_CHAT_LINK = text.GeneralMessages.LOG_CHAT_LINK
    LOG_CHAT_ID = text.GeneralMessages.LOG_CHAT_ID

class HelpText(object):
    INVALID_ARG = text.HelpText.INVALID_ARG
    USAGE = text.HelpText.USAGE
    NAME_OF_MODULE = text.HelpText.NAME_OF_MODULE
    AVAILABLE_MODULES = text.HelpText.AVAILABLE_MODULES
    DISABLED_MODULES = text.HelpText.DISABLED_MODULES
    NAME_MODULE = text.HelpText.NAME_MODULE
    MISSING_NAME_MODULE = text.HelpText.MISSING_NAME_MODULE
    MODULE_NOT_FOUND = text.HelpText.MODULE_NOT_FOUND
    MODULE_NO_DESC = text.HelpText.MODULE_NO_DESC
    MODULE_NO_USAGE = text.HelpText.MODULE_NO_USAGE
    ASTERISK = text.HelpText.ASTERISK

class WebToolsText(object):
    PING_SPEED = text.WebToolsText.PING_SPEED
    DCMESSAGE = text.WebToolsText.DCMESSAGE
    BAD_ARGS = text.WebToolsText.BAD_ARGS
    INVALID_HOST = text.WebToolsText.INVALID_HOST
    PINGER_VAL = text.WebToolsText.PINGER_VAL
    SPD_START = text.WebToolsText.SPD_START
    SPD_FAILED = text.WebToolsText.SPD_FAILED
    SPD_NO_RESULT = text.WebToolsText.SPD_NO_RESULT
    SPD_NO_MEMORY = text.WebToolsText.SPD_NO_MEMORY
    SPD_FAIL_SEND_RESULT = text.WebToolsText.SPD_FAIL_SEND_RESULT
    SPD_MEGABITS = text.WebToolsText.SPD_MEGABITS
    SPD_MEGABYTES = text.WebToolsText.SPD_MEGABYTES
    SPD_TIME = text.WebToolsText.SPD_TIME
    SPD_DOWNLOAD = text.WebToolsText.SPD_DOWNLOAD
    SPD_UPLOAD = text.WebToolsText.SPD_UPLOAD
    SPD_PING = text.WebToolsText.SPD_PING
    SPD_ISP = text.WebToolsText.SPD_ISP
    SPD_HOSTED_BY = text.WebToolsText.SPD_HOSTED_BY

class CasIntText(object):
    FAIL = text.CasIntText.FAIL
    USER_HEADER = text.CasIntText.USER_HEADER
    USER_ID = text.CasIntText.USER_ID
    FIRST_NAME = text.CasIntText.FIRST_NAME
    LAST_NAME = text.CasIntText.LAST_NAME
    USERNAME = text.CasIntText.USERNAME
    CAS_DATA = text.CasIntText.CAS_DATA
    RESULT = text.CasIntText.RESULT
    OFFENSES = text.CasIntText.OFFENSES
    DAY_ADDED = text.CasIntText.DAY_ADDED
    TIME_ADDED = text.CasIntText.TIME_ADDED
    UTC_INFO = text.CasIntText.UTC_INFO
    USERS_DETECTED = text.CasIntText.USERS_DETECTED
    NO_USRS = text.CasIntText.NO_USRS
    NO_ADM = text.CasIntText.NO_ADM
    CAS_CHECK_FAIL = text.CasIntText.CAS_CHECK_FAIL

class GitHubText(object):
    INVALID_URL = text.GitHubText.INVALID_URL
    NO_RELEASE = text.GitHubText.NO_RELEASE
    AUTHOR_STR = text.GitHubText.AUTHOR_STR
    RELEASE_NAME = text.GitHubText.RELEASE_NAME
    ASSET = text.GitHubText.ASSET
    SIZE = text.GitHubText.SIZE
    DL_COUNT = text.GitHubText.DL_COUNT
    INVALID_ARGS = text.GitHubText.INVALID_ARGS

class StickersText(object):
    FAIL_FETCH_INFO = text.StickersText.FAIL_FETCH_INFO
    NOT_STICKER = text.StickersText.NOT_STICKER
    FETCHING_STICKER_DETAILS = text.StickersText.FETCHING_STICKER_DETAILS
    STICKER_INFO_OUTPUT = text.StickersText.STICKER_INFO_OUTPUT

class TerminalText(object):
    BASH_ERROR = text.TerminalText.BASH_ERROR
    PYTHON_INSTRUCTION = text.TerminalText.PYTHON_INSTRUCTION
    PYTHON_RESULT = text.TerminalText.PYTHON_RESULT

class MiscText(object):
    COIN_LANDED_VAL = text.MiscText.COIN_LANDED_VAL
    THRWING_COIN = text.MiscText.THRWING_COIN
    HEADS = text.MiscText.HEADS
    TAILS = text.MiscText.TAILS
    RAND_INVLD_ARGS = text.MiscText.RAND_INVLD_ARGS
    FRST_LIMIT_INVALID = text.MiscText.FRST_LIMIT_INVALID
    SCND_LIMIT_INVALID = text.MiscText.SCND_LIMIT_INVALID
    RAND_NUM_GEN = text.MiscText.RAND_NUM_GEN

class PackageManagerText(object):
    INVALID_ARG = text.PackageManagerText.INVALID_ARG
    UPDATE_COMPLETE = text.PackageManagerText.UPDATE_COMPLETE
    EMPTY_LIST = text.PackageManagerText.EMPTY_LIST
    FILES_IN = text.PackageManagerText.FILES_IN
    FILE_DSC = text.PackageManagerText.FILE_DSC
    NO_PKG = text.PackageManagerText.NO_PKG
    MOD_NOT_FOUND_INSTALL = text.PackageManagerText.MOD_NOT_FOUND_INSTALL
    DONE_RBT = text.PackageManagerText.DONE_RBT
    NO_UNINSTALL_MODULES = text.PackageManagerText.NO_UNINSTALL_MODULES
    NO_UN_NAME = text.PackageManagerText.NO_UN_NAME
    MULTIPLE_NAMES = text.PackageManagerText.MULTIPLE_NAMES
    NOT_IN_USERSPACE = text.PackageManagerText.NOT_IN_USERSPACE
    UNINSTALLING = text.PackageManagerText.UNINSTALLING
    REBOOT_DONE_INS = text.PackageManagerText.REBOOT_DONE_INS
    REBOOT_DONE_UNINS = text.PackageManagerText.REBOOT_DONE_UNINS
    INSTALL_LOG = text.PackageManagerText.INSTALL_LOG
    UNINSTALL_LOG = text.PackageManagerText.UNINSTALL_LOG

class ModuleDescriptions(object):
    ADMIN_DESC = text.ModuleDescriptions.ADMIN_DESC
    CHATINFO_DESC = text.ModuleDescriptions.CHATINFO_DESC
    DELETIONS_DESC = text.ModuleDescriptions.DELETIONS_DESC
    MEMBERINFO_DESC = text.ModuleDescriptions.MEMBERINFO_DESC
    SCRAPPERS_DESC = text.ModuleDescriptions.SCRAPPERS_DESC
    SYSTOOLS_DESC = text.ModuleDescriptions.SYSTOOLS_DESC
    USER_DESC = text.ModuleDescriptions.USER_DESC
    WEBTOOLS_DESC = text.ModuleDescriptions.WEBTOOLS_DESC
    CAS_INTERFACE_DESC = text.ModuleDescriptions.CAS_INTERFACE_DESC
    GITHUB_DESC = text.ModuleDescriptions.GITHUB_DESC
    TERMINAL_DESC = text.ModuleDescriptions.TERMINAL_DESC
    MISC_DESC = text.ModuleDescriptions.MISC_DESC
    PACKAGE_MANAGER_DESC = text.ModuleDescriptions.PACKAGE_MANAGER_DESC

class ModuleUsages(object):
    ADMIN_USAGE = text.ModuleUsages.ADMIN_USAGE
    CHATINFO_USAGE = text.ModuleUsages.CHATINFO_USAGE
    DELETIONS_USAGE = text.ModuleUsages.DELETIONS_USAGE
    MEMBERINFO_USAGE = text.ModuleUsages.MEMBERINFO_USAGE
    SCRAPPERS_USAGE = text.ModuleUsages.SCRAPPERS_USAGE
    SYSTOOLS_USAGE = text.ModuleUsages.SYSTOOLS_USAGE
    USER_USAGE = text.ModuleUsages.USER_USAGE
    WEBTOOLS_USAGE = text.ModuleUsages.WEBTOOLS_USAGE
    CAS_INTERFACE_USAGE = text.ModuleUsages.CAS_INTERFACE_USAGE
    GITHUB_USAGE = text.ModuleUsages.GITHUB_USAGE
    TERMINAL_USAGE = text.ModuleUsages.TERMINAL_USAGE
    MISC_USAGE = text.ModuleUsages.MISC_USAGE
    PACKAGE_MANAGER_USAGE = text.ModuleUsages.PACKAGE_MANAGER_USAGE
