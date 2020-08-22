from tg_userbot import UBOT_LANG
from importlib import import_module

# Temp because pyCharm needs for autocompletion and I am being a Lazy S.O.B. again
import tg_userbot.translations.en as text

# Language selector logic

try:
    text = import_module("tg_userbot.translations." + UBOT_LANG)
except:
    print("There was a problem loading the language file. Make sure it exists! Should have the same name as the UBOT_LANG variable in config.py. Attempting to load default language")
    try:
        text = import_module("tg_userbot.translations.en")
    except:
        print("English language file not found, bot quitting!")
        exit(1)

# Language processor!

class AdminText(object): # Admin module
    NOT_ADMIN = text.AdminText.NOT_ADMIN
    BANNING_USER = text.AdminText.BANNING_USER
    NO_PERMS = text.AdminText.NO_PERMS
    NO_MSG_DEL_PERMS = text.AdminText.NO_MSG_DEL_PERMS
    BANNED_SUCCESSFULLY = text.AdminText.BANNED_SUCCESSFULLY
    UNBANNING_USER = text.AdminText.UNBANNING_USER
    UNBANNED_SUCCESSFULLY = text.AdminText.UNBANNED_SUCCESSFULLY
    USERID_INVALID = text.AdminText.USERID_INVALID
    FAILED_FETCH_USER = text.AdminText.FAILED_FETCH_USER
    KICKING_USER = text.AdminText.KICKING_USER
    KICKED_SUCCESSFULLY = text.AdminText.KICKED_SUCCESSFULLY
    ONLY_CHAN_GROUPS = text.AdminText.ONLY_CHAN_GROUPS
    NOT_USER = text.AdminText.NOT_USER
    PROMT_SELF = text.AdminText.PROMT_SELF
    ADM_ALRD = text.AdminText.ADM_ALRD
    PROMTING_USER = text.AdminText.PROMTING_USER
    NO_ADD_ADM_RIGHT = text.AdminText.NO_ADD_ADM_RIGHT
    PRMT_SUCCESS = text.AdminText.PRMT_SUCCESS
    TOO_MANY_ADM = text.AdminText.TOO_MANY_ADM
    ALREADY_NOT_ADM = text.AdminText.ALREADY_NOT_ADM
    DMT_MYSELF = text.AdminText.DMT_MYSELF
    DMTING_USER = text.AdminText.DMTING_USER
    DMTED_SUCCESSFULLY = text.AdminText.DMTED_SUCCESSFULLY
    NO_DEl_USERS = text.AdminText.NO_DEl_USERS
    SEARCHING_DEL_USERS = text.AdminText.SEARCHING_DEL_USERS
    FOUND_DEL_ACCS = text.AdminText.FOUND_DEL_ACCS
    DELETING_ACCS = text.AdminText.DELETING_ACCS
    NO_BAN_PERMS = text.AdminText.NO_BAN_PERMS
    DEL_ALL_SUCCESFULLY = text.AdminText.DEL_ALL_SUCCESFULLY
    DEL_SOME_SUCCESSFULLY = text.AdminText.DEL_SOME_SUCCESSFULLY
    BANLOG = text.AdminText.BANLOG
    UNBANLOG = text.AdminText.UNBANLOG
    KICKLOG = text.AdminText.KICKLOG
    CLEAN_DELACC_LOG = text.AdminText.CLEAN_DELACC_LOG
    PROMT_LOG = text.AdminText.PROMT_LOG
    DMT_LOG = text.AdminText.DMT_LOG
    MUTING_USR = text.AdminText.MUTING_USR
    USER_MUTED = text.AdminText.USER_MUTED
    UNMUTING_USR = text.AdminText.UNMUTING_USR
    USER_UNMUTED = text.AdminText.USER_UNMUTED
    MUTE_LOG = text.AdminText.MUTE_LOG
    UNMUTE_LOG = text.AdminText.UNMUTE_LOG
    MSG_NOT_FOUND_PIN = text.AdminText.MSG_NOT_FOUND_PIN
    PINNED_SUCCESSFULLY = text.AdminText.PINNED_SUCCESSFULLY

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

class DeletionsText(object):
    PURGE_COMPLETE = text.DeletionsText.PURGE_COMPLETE
    DEL_FAILED = text.DeletionsText.DEL_FAILED
    PURGE_LOG = text.DeletionsText.PURGE_LOG

class ChatInfoText(object):
    CHAT_ANALYSIS = text.ChatInfoText.CHAT_ANALYSIS
    EXCEPTION = text.ChatInfoText.EXCEPTION
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
    SCAN_CHANNEL_FAIL = text.MemberInfoText.SCAN_CHANNEL_FAIL
    FAIL_GET_MEMBER_CHAT = text.MemberInfoText.FAIL_GET_MEMBER_CHAT
    FAIL_GET_MEMBER_ARGS = text.MemberInfoText.FAIL_GET_MEMBER_ARGS
    INVALID_USER_ID = text.MemberInfoText.INVALID_USER_ID
    FAIL_GET_MEMBER_DIV = text.MemberInfoText.FAIL_GET_MEMBER_DIV
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

class UserText(object):
    LEAVING = text.UserText.LEAVING
    KICKME_LOG = text.UserText.KICKME_LOG
    STATS_PROCESSING = text.UserText.STATS_PROCESSING
    STATS_USERS = text.UserText.STATS_USERS
    STATS_GROUPS = text.UserText.STATS_GROUPS
    STATS_SUPER_GROUPS = text.UserText.STATS_SUPER_GROUPS
    STATS_CHANNELS = text.UserText.STATS_CHANNELS
    STATS_BOTS = text.UserText.STATS_BOTS
    FETCH_INFO = text.UserText.FETCH_INFO
    NO_PROF_PIC = text.UserText.NO_PROF_PIC
    UNKNOWN = text.UserText.UNKNOWN
    USR_NO_BIO = text.UserText.USR_NO_BIO
    USR_INFO = text.UserText.USR_INFO
    FIRST_NAME = text.UserText.FIRST_NAME
    LAST_NAME = text.UserText.LAST_NAME
    USERNAME = text.UserText.USERNAME
    DCID = text.UserText.DCID
    PROF_PIC_COUNT = text.UserText.PROF_PIC_COUNT
    PROF_LINK = text.UserText.PROF_LINK
    ISBOT = text.UserText.ISBOT
    ISRESTRICTED = text.UserText.ISRESTRICTED
    ISVERIFIED = text.UserText.ISVERIFIED
    USR_ID = text.UserText.USR_ID
    BIO = text.UserText.BIO
    COMMON = text.UserText.COMMON

class GeneralMessages(object):
    ERROR = text.GeneralMessages.ERROR
    GET_USER_FROM_EVENT_FAIL = text.GeneralMessages.GET_USER_FROM_EVENT_FAIL

class HelpText(object):
    INVALID_NAME = text.HelpText.INVALID_NAME
    DEFAULT = text.HelpText.DEFAULT

class WebToolsText(object):
    PING_SPEED = text.WebToolsText.PING_SPEED
    DCMESSAGE = text.WebToolsText.DCMESSAGE
    BAD_ARGS = text.WebToolsText.BAD_ARGS
    INVALID_HOST = text.WebToolsText.INVALID_HOST
    PINGER_VAL = text.WebToolsText.PINGER_VAL

class HelpDesignations(object):
    ADMIN_HELP = text.HelpDesignations.ADMIN_HELP
    CHATINFO_HELP = text.HelpDesignations.CHATINFO_HELP
    DELETIONS_HELP = text.HelpDesignations.DELETIONS_HELP
    MEMBERINFO_HELP = text.HelpDesignations.MEMBERINFO_HELP
    SYSTOOLS_HELP = text.HelpDesignations.SYSTOOLS_HELP
    USER_HELP = text.HelpDesignations.USER_HELP
