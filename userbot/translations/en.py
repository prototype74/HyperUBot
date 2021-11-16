# English Language file
#
# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

NAME = "English"  # default language


class AdminText(object):
    ADMINS_IN_CHAT = "Admins in **{}**"
    UNABLE_GET_ADMINS = "`Unable to get admins from this chat`"
    FAIL_CHAT = "`Failed to fetch chat`"
    NO_GROUP_CHAN = "`This chat isn't a group or channel`"
    NO_GROUP_CHAN_ARGS = "`This chat or given chat isn't a group or channel`"
    NO_ADMIN = "`Admin privileges are required to perform this action`"
    NO_BAN_PRIV = "`Ban permission is required to perform this action`"
    DELETED_ACCOUNT = "Deleted Account"
    CANNOT_BAN_SELF = "`I can't ban myself`"
    CANNOT_BAN_ADMIN = "`I can't ban this admin`"
    # user name, chat tile
    BAN_SUCCESS_REMOTE = "{} has been banned from **{}**"
    BAN_SUCCESS = "{} has been banned!"  # user name
    BAN_FAILED = "`Failed to ban this person`"
    CANNOT_UNBAN_SELF = "`I can't unban myself`"
    # user name, chat tile
    UNBAN_SUCCESS_REMOTE = "{} has been unbanned from **{}**"
    UNBAN_SUCCESS = "{} has been unbanned!"  # user name
    UNBAN_FAILED = "`Failed to unban this person`"
    CANNOT_KICK_SELF = "`I can't kick myself`"
    # user name, chat tile
    KICK_SUCCESS_REMOTE = "{} has been kicked from **{}**"
    KICK_SUCCESS = "{} has been kicked!"  # user name
    KICK_FAILED = "`Failed to kick this person`"
    PERSON_ANONYMOUS = "Person is anonymous"
    CANNOT_PROMOTE_CHANNEL = "I can't promote a channel!"
    NO_ONE_TO_PROMOTE = "`There is no one to promote`"
    NOT_USER = "`Given username or ID isn't an User`"
    CANNOT_PROMOTE_SELF = "`I can't promote myself`"
    ADMIN_ALREADY_SELF = "`I am immortal already`"
    ADMIN_ALREADY = "`This person is immortal already`"
    ADMIN_NOT_ENOUGH_PERMS = ("`I don't have enough admin rights to "
                              "promote this person`")
    ADD_ADMINS_REQUIRED = ("`Add admins permission is required to perform "
                           "this action`")
    PROMOTE_SUCCESS = "{} has been promoted with immortal power!"  # user name
    TOO_MANY_ADMINS = "`This chat has too many admins already`"
    EMOJI_NOT_ALLOWED = "`Emoji are not allowed in admin titles`"
    GET_ENTITY_FAILED = "Failed to fetch entity"
    PROMOTE_FAILED = "`Failed to promote this person`"
    CANNOT_DEMOTE_CHANNEL = "I can't demote a channel!"
    NO_ONE_TO_DEMOTE = "`There is no one to demote`"
    CANNOT_DEMOTE_SELF = "`I can't demote myself`"
    DEMOTED_ALREADY = "`This person is mortal already`"
    DEMOTE_SUCCESS = "{} has been demoted!"  # user name
    CANNOT_DEMOTE_ADMIN = "`I can't demote this admin`"
    DEMOTE_FAILED = "`Failed to demote this person`"
    NO_GROUP_ARGS = "`This chat or given chat isn't a group`"
    NOT_MUTE_SUB_CHAN = "`Unable to mute subscribers in a channel`"
    CANNOT_MUTE_SELF = "`I can't mute myself`"
    MUTE_SUCCESS_REMOTE = "{} has been muted in **{}**"  # user name, chat tile
    MUTE_SUCCESS = "Muted {}"  # user name
    MUTE_FAILED = "`Failed to mute this person`"
    NOT_UNMUTE_SUB_CHAN = "`Unable to unmute subscribers in a channel`"
    CANNOT_UNMUTE_SELF = "`I can't unmute myself`"
    # user name, chat tile
    UNMUTE_SUCCESS_REMOTE = "{} has been unmuted in **{}**"
    UNMUTE_SUCCESS = "Unmuted {}"  # user name
    UNMUTE_FAILED = "`Failed to unmute this person`"
    INVALID_ID = "`Invalid ID given`"
    INVALID_USERNAME = "`Invalid username or link given`"
    TRY_DEL_ACCOUNTS = "`Trying to remove deleted accounts...`"
    DEL_ACCS_COUNT = "`{} deleted accounts found in this chat`"
    DEL_ACCS_COUNT_REMOTE = "`{} deleted accounts found in {}`"
    REM_DEL_ACCS_COUNT = "`Removed {} deleted accounts`"
    REM_DEL_ACCS_COUNT_REMOTE = "`Removed {} deleted accounts in {}`"
    REM_DEL_ACCS_COUNT_EXCP = "`Couldn't remove {} deleted (admin) accounts`"
    NO_DEL_ACCOUNTS = "`No deleted accounts found in this chat`"
    NO_DEL_ACCOUNTS_REMOTE = "`No deleted accounts found in {}`"


class SystemToolsText(object):
    UBOT = "Userbot Project: "
    SYSTEM_STATUS = "System Status"
    VER_TEXT = "Version: "
    USR_TEXT = "User: "
    SAFEMODE = "Safe mode: "
    ON = "On"
    OFF = "Off"
    LANG = "Language: "
    RTT = "RTT: "
    TELETON_VER = "Telethon version: "
    PYTHON_VER = "Python version: "
    GITAPI_VER = "GitHub API Version: "
    COMMIT_NUM = "Revision: "
    ERROR = "ERROR!"
    DAYS = "day(s)"
    BOT_UPTIMETXT = "Bot uptime: "
    MAC_UPTIMETXT = "Server uptime: "
    SHUTDOWN = "`Powering off...`"
    SHUTDOWN_LOG = "Bot is powering off under user request!"
    SYSD_GATHER_INFO = "`Gathering system information...`"
    SYSD_NEOFETCH_REQ = ("`neofetch package is required to display system "
                         "information`")
    RESTART = "`Rebooting...`"
    RESTART_UNSUPPORTED = ("`Reboot isn't supported on Windows but heads "
                           "up! Ctrl+C still does the job`")
    RESTART_LOG = "Userbot is restarting!"
    RESTARTED = "Reboot complete!"
    GENERAL = "General"
    STORAGE = "Storage"
    STORAGE_TOTAL = "Total"
    STORAGE_USED = "Used"
    STORAGE_FREE = "Free"
    USED_BY_HYPERUBOT = "Used by HyperUBot"
    STORAGE_SYSTEM = "Built-in modules"
    STORAGE_USER = "User modules"
    STORAGE_USERDATA = "User data"
    STORAGE_TEMP_DL = "Temporary downloads"
    STORAGE_HDD = "HDD"
    UPLD_LOG = "`Uploading userbot log...`"
    SUCCESS_UPLD_LOG = "`HyperUBot Log successfully uploaded!`"
    FAILED_UPLD_LOG = "`Failed to upload log file`"


class DeletionsText(object):
    CANNOT_DEL_MSG = "`I can't delete this message`"
    DEL_MSG_FAILED = "`Failed to delete this message`"
    REPLY_DEL_MSG = "`Reply to someone's message to delete it`"
    NO_ADMIN_PURGE = "`Admin privileges are required to purge messages`"
    NO_DEL_PRIV = "`Delete messages permission is required to purge messages`"
    PURGE_MSG_FAILED = "`Failed to purge message(s)`"
    PURGE_COMPLETE = "Purge complete! Purged `{}` message(s)!"
    LOG_PURGE = "Purged `{}` message(s)"
    REPLY_PURGE_MSG = "`Reply to a message to start purge`"


class ChatInfoText(object):
    CHAT_ANALYSIS = "`Analysing the chat...`"
    EXCEPTION = "`An unexpected error has occurred!`"
    REPLY_NOT_CHANNEL = "`This message isn't from a channel`"
    CANNOT_GET_CHATINFO = "`I can't get chat information from '{}'!`"
    YES_BOLD = "<b>Yes</b>"
    NO_BOLD = "<b>No</b>"
    YES = "Yes"
    NO = "No"
    DELETED_ACCOUNT = "Deleted Account"
    CHATINFO = "<b>Chat info</b>\n\n"
    CHAT_ID = "ID: <code>{}</code>\n"
    CHANNEL = "Channel"
    GROUP = "Group"
    CHAT_TYPE = "Chat type: {} ({})\n"  # group/channel, private/public
    CHAT_NAME = "Chat name: {}\n"
    FORMER_NAME = "Former name: {}\n"
    CHAT_PUBLIC = "Public"
    CHAT_PRIVATE = "Private"
    GROUP_TYPE = "Group type"
    GROUP_TYPE_GIGAGROUP = "Broadcast group"
    GROUP_TYPE_SUPERGROUP = "Supergroup"
    GROUP_TYPE_NORMAL = "Normal"
    OWNER = "Owner: {}\n"
    OWNER_WITH_URL = "Owner: <a href=\"tg://user?id={}\">{}</a>\n"
    CREATED_NOT_NULL = "Created: <code>{} - {} {}</code>\n"
    CREATED_NULL = "Created: <code>{} - {} {}</code> {}\n"
    DCID = "Data Center ID: {}\n"
    VIEWABLE_MSG = "Viewable messages: <code>{}</code>\n"
    DELETED_MSG = "Deleted messages: <code>{}</code>\n"
    SENT_MSG = "Messages sent: <code>{}</code>\n"
    SENT_MSG_PRED = "Messages sent: <code>{}</code> {}\n"
    MEMBERS = "Members: <code>{}</code>\n"
    ADMINS = "Administrators: <code>{}</code>\n"
    BOT_COUNT = "Bots: <code>{}</code>\n"
    ONLINE_MEM = "Currently online: <code>{}</code>\n"
    RESTRICTED_COUNT = "Restricted users: <code>{}</code>\n"
    BANNEDCOUNT = "Banned users: <code>{}</code>\n"
    GRUP_STICKERS = "Chat stickers: <a href=\"t.me/addstickers/{}\">{}</a>\n"
    LINKED_CHAT = "Linked chat: {}\n"
    LINKED_CHAT_TITLE = "> Name: {}\n"
    SLW_MODE = "Slow mode: {}"
    SLW_MODE_TIME = ", <code>{}s</code>\n\n"
    RESTR = "Restricted: {}\n"
    PFORM = "> Platform: {}\n"
    REASON = "> Reason: {}\n"
    TEXT = "> Text: {}\n\n"
    SCAM = "Scam: <b>Yes</b>\n\n"
    VERFIED = "Verified by Telegram: {}\n\n"
    DESCRIPTION = "Description: \n<code>{}</code>\n"
    UNKNOWN = "Unknown"
    INVALID_CH_GRP = "Invalid channel/group!"
    PRV_BAN = "This is a private channel/group or I am banned from there!"
    NOT_EXISTS = "Channel or supergroup doesn't exist!"
    CID_TEXT = "This chat's id is `{}`"
    CID_NO_GROUP = "`This chat isn't a channel or group`"
    LINK_INVALID_ID = "`Given ID or link is invalid`"
    LINK_INVALID_ID_GROUP = "`Given ID or link isn't from a channel or group`"
    LINK_TEXT = "Here is the invite link for **{}**"
    NO_LINK = "`This chat has no invite link`"
    NO_ADMIN_PERM = "`Admin privileges are required to perform this action`"
    NO_INVITE_PERM = ("`Invite users permission is required to perform this "
                      "action`")
    UNABLE_GET_LINK = "`Unable to fetch chat's invite link`"


class MemberInfoText(object):
    SCAN = "`Scanning this member's information...`"
    FAIL_GET_MEMBER_CHAT = "`Failed to get member info: couldn't fetch chat`"
    FAIL_GET_MEMBER = "`Failed to get member info`"
    NOT_SUPERGROUP = "`This chat or given chat ID isn't a supergroup!`"
    INVALID_CHAT_ID = "`Invalid chat ID!`"
    ME_NOT_PART = "`I am not a participant of {}`"
    USER_NOT_PART = "`This user isn't a participant of {}`"
    FAIL_GET_PART = "`Failed to get participant info`"
    DELETED_ACCOUNT = "Deleted Account"
    TIME_FOREVER = "Forever"
    ME_NOT_MEMBER = "`I am not a member of {}`"
    USER_NOT_MEMBER = "`This user isn't a member of {}`"
    MEMBERINFO = "Member info"
    GENERAL = "General"
    MINFO_ID = "ID"
    FIRST_NAME = "First Name"
    USERNAME = "Username"
    GROUP = "Group"
    GROUP_NAME = "Name"
    STATUS = "Status"
    STATUS_OWNER = "Owner"
    STATUS_ADMIN = "Admin"
    STATUS_MEMBER = "Member"
    STATUS_BANNED = "Banned"
    STATUS_MUTED = "Muted"
    STATUS_RESTRICTED = "Restricted"
    STATUS_MUTED_NOT_MEMBER = "Not a member but muted"
    STATUS_RESTRICTED_NOT_MEMBER = "Not a member but restricted"
    STATUS_BANNED_UNTIL = "Banned until"
    STATUS_MUTED_UNTIL = "Muted until"
    STATUS_RESTRICTED_UNTIL = "Restricted until"
    STATUS_BANNED_BY = "Banned by"
    STATUS_MUTED_BY = "Muted by"
    STATUS_RESTRICTED_BY = "Restricted by"
    ADMIN_TITLE = "Title"
    PERMISSIONS = "Permissions"
    CHANGE_GROUP_INFO = "Change group info"
    DELETE_MESSAGES = "Delete messages"
    BAN_USERS = "Ban users"
    INVITE_USERS = "Add/Invite users"
    PIN_MESSAGES = "Pin messages"
    ADD_ADMINS = "Add new admins"
    MANAGE_CALLS = "Manage voice calls"
    ANONYMOUS = "Send Anonymously"
    ROOT_RIGHTS = "Root rights"
    SEND_MESSAGES = "Send messages"
    SEND_MEDIA = "Send media"
    SEND_GIFS_STICKERS = "Send stickers & gifs"
    SEND_POLLS = "Send polls"
    EMBED_LINKS = "Embed links"
    WARN_ADMIN_PRIV = ("Admin privileges are required to access non-default "
                       "permissions")
    PROMOTED_BY = "Promoted by"
    ADDED_BY = "Added by"
    JOIN_DATE = "Join date"


class MessagesText(object):
    NO_ADMIN = "`Admin privileges are required to perform this action`"
    FAIL_CHAT = "`Failed to fetch chat`"
    CANNOT_COUNT_DEL = "`Can't count messages from a deleted user`"
    CANNOT_QUERY_FWD = "`Can't query forwarded messages from a channel`"
    FAIL_COUNT_MSG = "`Can't query forwarded messages from a channel`"
    # userlink, msg count
    USER_HAS_SENT = "{} has sent `{}` messages in this chat"
    # userlink, msg count, chat title
    USER_HAS_SENT_REMOTE = "{} has sent `{}` messages in **{}**"
    CANNOT_COUNT_MSG = "`Can't count messages in this chat!`"
    CANNOT_COUNT_MSG_REMOTE = "`Can't count messages in {}!`"
    PIN_REPLY_TO_MSG = "`Reply to a message to pin it`"
    PIN_SUCCESS = "`Message pinned successfully`"
    PIN_FAILED = "`Failed to pin this message`"
    LOG_PIN_MSG_ID = "Message ID"
    UNPIN_REPLY_TO_MSG = ("`Reply to a message to unpin it or use "
                          "\".unpin all\" to unpin all messages`")
    UNPIN_ALL_SUCCESS = "`All messages unpinned successfully`"
    UNPIN_SUCCESS = "`Message unpinned successfully`"
    UNPIN_FAILED = "`Failed to unpin this message`"
    LOG_UNPIN_ALL_TEXT = "All messages unpinned"


class ScrappersText(object):
    NO_TEXT_OR_MSG = "`No text or message to translate`"
    TRANSLATING = "`Translating...`"
    SAME_SRC_TARGET_LANG = "`Source text language equals target language`"
    DETECTED_LANG = "Detected language"
    TARGET_LANG = "Target language"
    ORG_TEXT = "Original text"
    TRANS_TEXT = "Translated text"
    MSG_TOO_LONG = "`Translated text is too long!`"
    FAIL_TRANS_MSG = "`Failed to translate this message`"
    FAIL_TRANS_TEXT = "`Failed to translate given text`"
    MEDIA_FORBIDDEN = ("`Couldn't TTS: Uploading media isn't allowed in this "
                       "chat`")
    NO_TEXT_TTS = "`No text or message to text-to-speech`"
    FAIL_TTS = "`Failed to text-to-speech`"
    FAIL_API_REQ = "`API request failed`"
    INVALID_LANG_CODE = "`Invalid language code or language isn't supported`"
    NOT_EGH_ARGS = "`Not enough arguments given!`"
    INVALID_AMOUNT_FORMAT = "`Invalid amount format`"
    CC_ISO_UNSUPPORTED = "`'{}' unsupported country ISO currency`"
    CC_HEADER = "Currency converter"
    CFROM_CTO = "**{}** to **{}**"  # from cc iso, target cc iso
    INVALID_INPUT = "Invalid input"
    UNABLE_TO_CC = "`Unable to convert currency`"
    CC_LAST_UPDATE = "Last Updated"
    REPLY_TO_VM = "`Reply to a voice message`"
    WORKS_WITH_VM_ONLY = "`Works with voice messages only`"
    CONVERT_STT = "`Converting speech into text...`"
    FAILED_LOAD_AUDIO = "`Failed to load audio`"
    STT = "Speech-to-text"
    STT_TEXT = "Text"
    STT_NOT_RECOGNIZED = "`Couldn't recognize speech from audio`"
    STT_REQ_FAILED = "Request result from server failed"
    STT_OUTPUT_TOO_LONG = "`Speech-to-text output is too long!`"
    UNABLE_TO_STT = "`Unable to speech-to-text`"
    SCRLANG = "HyperUBot Scrappers module language is currently set to: `{}`"
    MULT_ARGS = "`Please use one argument!`"
    INV_CT_CODE = ("Invalid value! Use one of the following 2 letter "
                   "country codes!\n\nAvailable codes:\n{}")
    SUCCESS_LANG_CHANGE = "Language successfully changed to: `{}`"


class UserText(object):
    CANNOT_LEAVE = "`This chat doesn't seem to be a group or channel`"
    LEAVING = "`Leaving chat...`"
    STATS_PROCESSING = "`Computing stats...`"
    STATS_HEADER = "My Telegram stats"
    STATS_USERS = "PM chats with **{}** people"
    STATS_BLOCKED = "Blocked **{}** of them"
    STATS_BOTS = "Started **{}** bots"
    STATS_BLOCKED_TOTAL = "Blocked **{}** bots/people in total"
    STATS_GROUPS = "Participant in **{}** groups"
    STATS_SGC_OWNER = "Owning **{}** of them"
    STATS_GROUPS_ADMIN = "Admin in **{}** groups"
    STATS_SUPER_GROUPS = "Participant in **{}** supergroups"
    STATS_SG_ADMIN = "Admin in **{}** supergroups"
    STATS_CHANNELS = "Subscribed **{}** channels"
    STATS_CHAN_ADMIN = "Admin in **{}** channels"
    STATS_UNKNOWN = "**{}** unknown chats"
    STATS_TOTAL = "Total chats"
    FETCH_INFO = "`Getting user info...`"
    FAILED_FETCH_INFO = "`Failed to fetch user info`"
    UNKNOWN = "Unknown"
    DELETED_ACCOUNT = "Deleted Account"
    YES = "Yes"
    NO = "No"
    USR_NO_BIO = "This User has no Bio"
    USR_INFO = "User info"
    FIRST_NAME = "First Name"
    LAST_NAME = "Last Name"
    USERNAME = "Username"
    DCID = "Data Centre ID"
    PROF_PIC_COUNT = "Number of Profile Pics"
    PROF_LINK = "Permanent Link To Profile"
    ISBOT = "Bot"
    SCAMMER = "Scammer"
    ISRESTRICTED = "Restricted"
    ISVERIFIED = "Verified by Telegram"
    USR_ID = "ID"
    BIO = "Bio"
    COMMON_SELF = "Common chats... oh look it's me!"
    COMMON = "Common chats"
    UNABLE_GET_IDS = "`Unable to get user ID(s) from this message`"
    ORIGINAL_AUTHOR = "Original author"
    FORWARDER = "Forwarder"
    # name of person, ID
    DUAL_HAS_ID_OF = "{} has an ID of `{}`"
    MY_ID = "My ID is `{}`"
    DEL_HAS_ID_OF = "Deleted Account has an ID of `{}`"
    ID_NOT_ACCESSIBLE = "the ID from {} is not accessible"
    # name of person, ID
    ORG_HAS_ID_OF = "The original author {} has an ID of `{}`"


class SystemUtilitiesText(object):
    CMD_STOPPED = "{} has stopped!"


class GeneralMessages(object):
    ERROR = "ERROR!"
    CHAT_NOT_USER = "`Channels are not User objects`"
    FAIL_FETCH_USER = "`Failed to fetch user`"
    ENTITY_NOT_USER = "`Entity is not an User object`"
    PERSON_ANONYMOUS = "Person is anonymous"
    CANT_FETCH_REQ_AS_USER = "`Couldn't fetch entity '{}' as an user`"
    LOG_USER = "User"
    LOG_USERNAME = "Username"
    LOG_USER_ID = "User ID"
    LOG_CHAT_TITLE = "Chat title"
    LOG_CHAT_LINK = "Link"
    LOG_CHAT_ID = "Chat ID"
    UNKNOWN = "Unknown"


class ModulesUtilsText(object):
    INVALID_ARG = "`Invalid argument \"{}\"`"
    USAGE = "Usage"
    AVAILABLE_MODULES = "Available modules"
    DISABLED_MODULES = "Disabled modules"
    NAME_MODULE = "**{} module**"
    MISSING_NUMBER_MODULE = "`Missing number of module`"
    MODULE_NOT_AVAILABLE = "`Module number \"{}\" not available`"
    MODULE_NO_DESC = "__No description available__"
    MODULE_NO_USAGE = "__No usage available__"
    ASTERISK = "Uninstallable user module"
    NOT_RUNNING_INFO = "Not running"
    UNKNOWN = "Unknown"
    SYSTEM = "Built-in"
    SYSTEM_MODULES = "Built-in modules"
    USER = "User"
    USER_MODULES = "User modules"
    PKG_NAME = "Package name"
    MODULE_TYPE = "Module type"
    AUTHORS = "Author(s)"
    VERSION = "Version"
    SIZE = "Size"
    INSTALL_DATE = "Installation date"
    LISTCMDS_TITLE = "All available commands"
    LISTCMDS_USAGE = ("Use '{} <name of command>' to get further information "
                      "about a specific command.")
    ARGS_NOT_REQ = "no arguments required"  # lower if possible
    ARGS_NOT_AVAILABLE = "no arguments available"  # lower if possible
    CMD_NOT_FOUND = "Command '{}' not found!"
    MOD_HELP = "Need help? Type {}"
    MOD_UTILS = "Modules"


class WebToolsText(object):
    PING_SPEED = "Round-Trip Time: "
    DCMESSAGE = ("Country : `{}`\n"
                 "This Datacenter : `{}`\n"
                 "Nearest Datacenter : `{}`")
    BAD_ARGS = "`Bad arguments!`"
    INVALID_HOST = "`There was a problem parsing the IP/Hostname`"
    PINGER_VAL = "DNS: `{}`\nPing Speed: `{}`"
    SPD_TEST_SELECT_SERVER = "Selecting best server"
    SPD_TEST_DOWNLOAD = "Testing download speed"
    SPD_TEST_UPLOAD = "Testing upload speed"
    SPD_PROCESSING = "Processing"
    SPD_FAILED = "Speedtest failed"
    SPD_NO_RESULT = "No result"
    SPD_NO_MEMORY = "Out of memory"
    SPD_FAIL_SEND_RESULT = "`Failed to send speedtest result`"
    SPD_MEGABITS = "Mbit/s"
    SPD_MEGABYTES = "MB/s"
    SPD_TIME = "Time"
    SPD_DOWNLOAD = "Download speed"
    SPD_UPLOAD = "Upload speed"
    SPD_PING = "Ping"
    SPD_ISP = "My ISP"
    SPD_HOSTED_BY = "Hosted by"


class GitHubText(object):
    INVALID_URL = "Invalid user/repo combo"
    NO_RELEASE = "The specified release could not be found"
    AUTHOR_STR = "<b>Author:</b> <a href='{}'>{}</a>\n"
    RELEASE_NAME = "<b>Release Name:</b> "
    ASSET = "<b>Asset:</b> \n"
    SIZE = "Size: "
    DL_COUNT = "\nDownload Count: "
    INVALID_ARGS = ("Invalid arguments! Make sure you are typing a valid "
                    "combination of user/repo")


class TerminalText(object):
    BASH_ERROR = ("There has been an unspecified error, likely bad "
                  "arguments or that command does not exist")
    BASH_CRT_FILE_FAILED_RO = ("Failed to create shell output as a file. "
                               "Read-only filesystem?")
    BASH_CRT_FILE_FAILED = "Failed to create shell output as a file"
    BASH_SEND_FILE_MTLO = ("Can't shell output as a file as send media "
                           "isn't allowed in this chat")
    BASH_SEND_FILE_FAILED = "Unable to send shell output as a file"


class MiscText(object):
    COIN_LANDED_VAL = "The coin landed on: "
    THRWING_COIN = "`Throwing coin...`"
    HEADS = "Heads"
    TAILS = "Tails"
    RAND_INVLD_ARGS = ("`Invalid arguments, make sure you have "
                       "exactly 2 numbers`")
    FRST_LIMIT_INVALID = "`The first value is not a valid number!`"
    SCND_LIMIT_INVALID = "`The second value is not a valid number!`"
    RAND_NUM_GEN = "Your generated number between `{}` and `{}`: **`{}`**"


class PackageManagerText(object):
    REPO_LIST_EMPTY = ("List of repositories is empty! Use "
                       "`.pkg update <owner/repo>` to add a new repository "
                       "or add them to your COMMUNITY_REPOS config")
    PACKAGES_UPDATER = "Packages updater"
    INVALID_REPO_URL = "Invalid repo URL format"
    UPDATING = "Updating '{}'..."
    UPDATE_SUCCESS = "Got latest data from '{}'"
    UPDATE_FAILED = "Failed to fetch '{}'"
    UPDATER_FINISHED = "Updater finished"
    LIST_OF_PACKAGES = "List of packages"
    INSTALLED_MODULES = "Installed modules"
    NO_MODULES_INSTALLED = "No user modules installed"
    MODULES_IN = "Modules in {}"
    AUTHOR = "Author"
    VERSION = "Version"
    REPO_NO_MODULES = "This repository has no modules"
    REPOS_NO_DATA = "No repository data. You may need to use {}"
    INSTALLED = "Installed"
    INSTALLED_NOTLOADED = "Installed but not loaded"
    UPGRADEABLE = "Upgradeable"
    START_FAILED = "Failed to start"
    DISABLED = "Disabled"
    EQUAL_NAME = "Equal name"
    NEVER = "Never"
    LAST_UPDATED = "Last updated"
    INSTALL_EMPTY = "No module names given to install"
    PACKAGE_INSTALLER = "Package installer"
    NO_REPO_URL = "No repo URL given to install from!"
    INSTALL_EMPTY_REPO = "No module names given to install from specific repo!"
    UNKNOWN_REPO_URL = "Unknown repo URL given!"
    UNKNOWN_MODULES = "Unknown module(s)"
    DOWNLOADING = "Downloading '{}'..."
    DOWN_FAILED = "Failed to download '{}'"
    INSTALL_FAILED = "Failed to install '{}'"
    INSTALL_SUCCESS = "Installed '{}'"
    UPDATE_DATA_FAIL = "Failed to update data for '{}'"
    NO_INSTALL_QUEUED = "No installation queued"
    INSTALLER_FINISHED = "Installer finished"
    UNINSTALL_EMPTY = "No module names given to uninstall"
    PACKAGE_UNINSTALLER = "Package uninstaller"
    UNINSTALL_FAILED = "Failed to uninstall '{}'"
    UNINSTALL_SUCCESS = "Uninstalled '{}'"
    UNINSTALL_DATA = "Uninstalled '{}' but failed to remove data"
    MODULE_NOT_INSTALL = "'{}' not installed"
    UNINSTALLER_FINISHED = "Uninstaller finished"
    NO_REPO_NAMES = "No repo names given to remove"
    NO_REPO_REMOVE = "No repositories to remove"
    REPO_REMOVER = "Repo remover"
    CANNOT_REMOVE_REPO = "Can't remove '{}' (protected)"
    REMOVING = "Removing '{}'..."
    REMOVE_SUCCESS = "'{}' has been removed"
    REMOVE_FAILED = "Failed to remove '{}'"
    UNKNOWN_REPO = "Unknown repo"
    REMOVER_FINISHED = "Remover finished"
    LOAD_PGKS = "Loading package lists..."
    CANNOT_INSTALL_MODULES = "Can't install user modules in safe mode"
    PACKAGE_MANAGER = "Package Manager"
    UNKNOWN_OPTION = "Unknown option '{}'"
    NO_OPTION = "No option given"
    PKG_HELP = "Need help? Type {}"
    TEXT_TOO_LONG = ("The list is too long to display it here. The list is "
                     "printed in your bot's terminal")


class UpdaterText(object):
    CHECKING_UPDATES = "Checking for updates..."
    GIT_REPO = "HyperUBot's directory is a local git repository"
    DOWNLOADING_RELEASE = "Downloading latest release..."
    UPDATE_FAILED = "Update failed"
    UPDATE_INTERNAL_FAILED = "Internal error occurred"
    START_RECOVERY_FAILED = "Failed to start recovery"
    ALREADY_UP_TO_DATE = "HyperUBot is up-to-date already"
    LATEST = "Latest"
    CURRENT = "Current"
    UPDATE_AVAILABLE = "Update available"
    RELEASE_DATE = "Release date"
    CHANGELOG_AT = "Changelog at {}"
    DOWNLOAD_SUCCESS = ("Download successful. Shutting down bot to "
                        "install the update package...")
    DOWNLOAD_SUCCESS_WIN = ("Download successful and ready. Please "
                            "shutdown the bot and follow the instructions "
                            "in your terminal to apply the update package "
                            "manually")
    UPDATE_QUEUED = ("Use `.update upgrade` to download and install "
                     "the update package now")
    UPDATE_SUCESS = "HyperUBot updated to {} successfully!"
    UPDATE_FAIL = "Failed to update HyperUBot to {}"


class SideloaderText(object):
    NOT_PY_FILE = "This is not a valid .py file! Cannot sideload this!"
    DLOADING = "`Downloading...`"
    MODULE_EXISTS = ("There is already a userspace module named `{}`. "
                     "If you wish to overwrite this, please run the "
                     "command with the `force` argument!")
    SUCCESS = "Successfully installed `{}`!"
    LOG = "The module `{}` was sideloaded successfully!"
    REBOOT_INFO = "Please reboot HyperUBot now to load the sideloaded module"
    INVALID_FILE = "Please reply to a valid file!"


class FeatureMgrText(object):
    DISABLE_FTR = "Name a command or feature to disable it!"
    DISABLE_FTR_FAIL = "Seems like I can't disable this command or feature"
    DISABLE_FTR_SUCCESS = "Command or feature '`{}`' has been disabled"
    DISABLED_FTRS = "Disabled features"
    NO_DISABLED_FTRS = "No features disabled"
    ENABLE_FTR = "Name a command or feature to enable it!"
    ENABLE_FTR_FAIL = "Seems like I can't enable this command or feature"
    ENABLE_FTR_SUCCESS = "Command or feature '`{}`' has been enabled"


class WelcomeText(object):
    WELCOME_TO_HYPERUBOT = "Welcome to HyperUBot!"
    INFO = ("You made it to run HyperUBot on your machine successfully. So "
            "what's next? The following commands will help you to understand "
            "your new userbot better and what options, features etc. "
            "HyperUBot does offer for you")
    INFO_STATUS = ("get the current status of HyperUBot such as the "
                   "version, uptime etc. Useful to check if the bot is "
                   "actually online.")
    INFO_OR = "or"
    INFO_HELP = ("lists all available commands and features from all "
                 "modules to use. Pass the name of a command or feature "
                 "(e.g. {}) to get the usage of the specific command or "
                 "feature.")
    INFO_MODULES = ("lists all built-in and user modules at one place. "
                    "This command takes arguments to get further "
                    "information of a module such as the description "
                    "or usage.")
    INFO_PKG = ("our package manager allows you to install new modules. "
                "We made some user modules which can be downloaded with the "
                "help of this command to allow the user to get new modules "
                "without waiting for new updates for the bot. FYI there are "
                "also modules made by the community. So make sure to check "
                "them out too!")
    INFO_SUPPORT = ("Questions about HyperUBot? Read our {} or "
                    "feel free to chat with us in our {}!")
    INFO_SUPPORT_LINK = "support group"
    INFO_SUPPORT_WIKI = "wiki page"
    INFO_FUN = "Have fun!"


# Save your eyes from what may become the ugliest part of this userbot.
class ModuleDescriptions(object):
    ADMIN_DESC = ("A module to help you to manage your or a "
                  "friend's group easier. Includes common commands such as "
                  "ban, unban, promote, etc.\n\n"
                  "Note: most commands in this module require admin "
                  "privileges to work properly.")
    CHATINFO_DESC = ("Get most various information from a channel, group "
                     "or supergroup such as creation date, message counts, "
                     "deletions, former name, etc.")
    DELETIONS_DESC = ("This module allows you to delete your or in groups "
                      "messages faster. Someone spammed your group? Use "
                      "purge command to delete them all!\n"
                      "All commands in this module require admin privileges "
                      "to delete other people's messages.\n\n"
                      "**Important: don't abuse this module to delete "
                      "someone's else whole group history**, for real, "
                      "just don't...")
    MEMBERINFO_DESC = ("Provides information from a specific group "
                       "participant like permissions, restriction date, "
                       "join date, etc.\n\n"
                       "Note: requires admin privileges to access other "
                       "member's permissions.")
    MESSAGES_DESC = ("This module includes commands that work only with "
                     "messages, such as msgs or pin.")
    SCRAPPERS_DESC = ("Not exactly what it sounds like, but still this "
                      "module includes useful features like translation "
                      "or text-to-speech.")
    SYSTOOLS_DESC = ("This module contains a set of system tools for the "
                     "bot. It allows you to check the bot uptime, the "
                     "server uptime, the versions of all the bot's "
                     "components, the specifications of the server system, "
                     "and some bot power controls.")
    USER_DESC = ("Provides information about any user, your statistics, "
                 "and contains the kickme tool.")
    WEBTOOLS_DESC = ("This module contains most, if not all, of the bot's "
                     "webtools, such as ping, speedtest, RTT calculator "
                     "and the current datacenter.")
    GITHUB_DESC = ("A module that takes use of the GitHub API. This "
                   "module allows you to check for releases from a "
                   "specific user and repository.")
    TERMINAL_DESC = ("This module provides tools to run directly shell "
                     "commands, in the host machine.\n\n"
                     "**Attention:** Running shell commands in the bot "
                     "can and will make permanent changes to the host "
                     "system. **Bad things will happen if you run the bot "
                     "as sudo/root!**")
    MISC_DESC = ("The miscellaneous module contains a small set of tools "
                 "that did not quite fit any of the other modules, but "
                 "at the same time were too simple to have their own "
                 "module. Check the help for more details.")
    PACKAGE_MANAGER_DESC = ("The package manager module allows a user "
                            "to manage extra apps, from external repos, "
                            "either official, such as the modules-universe "
                            "repo, or from external sources. It provides a "
                            "way for users to customize their bots more "
                            "than stock.")
    UPDATER_DESC = ("The updater module allows the user to check for bot "
                    "updates and to update the bot, if new updates exist.")
    SIDELOADER_DESC = ("The sideloader module allows you to sideload python "
                       "files with ease. To do such, all you have to do is "
                       "reply to a .py file sent in the chat as a "
                       "document!\n\n"
                       "**INFORMATION**: These files must be written to "
                       "work with the bot. Attempting to load unknown "
                       "files might result in a 'soft brick' of the bot, "
                       "requiring you to manually delete the bad user "
                       "space module!\n\n"
                       "**CRITICAL WARNING**: Some malicious files could "
                       "send some of your information (namely API Key and/or "
                       "String Session) to a malicious hacker! Only "
                       "sideload modules if you trust the source!")
    FEATURE_MGR_DESC = ("The Feature Manager module allows the user "
                        "to enable/disable a command or feature in "
                        "real time and no, the enable and disable "
                        "commands cannot be disabled.")


class ModuleUsages(object):
    # KEEP CORRECT DICT FORMAT!!
    # {"cmd": {"args": ARGUMENTS, "usage": USAGE}} edit ARGUMENTS and
    # USAGE only!
    ADMIN_USAGE = {"adminlist": {"args": "[optional: <link/id>]",
                                 "usage": ("lists all admins from a "
                                           "channel or group (remotely). "
                                           "Requires admin privileges in "
                                           "channels.")},
                   "ban": {"args": ("[optional: <username/id> <chat "
                                    "(id or link)>] or reply"),
                           "usage": ("Ban a certain user from a chat "
                                     "(remotely). Requires admin privileges "
                                     "with ban permission.")},
                   "unban": {"args": ("[optional: <username/id> <chat "
                                      "(id or link)>] or reply"),
                             "usage": ("Unban a certain user from a chat "
                                       "(remotely). Requires admin "
                                       "privileges with ban permission.")},
                   "kick": {"args": ("[optional: <username/id> <chat "
                                     "(id or link)>] or reply"),
                            "usage": ("Kick a certain user from a chat "
                                      "(remotely). Requires admin "
                                      "privileges with ban permission.")},
                   "promote": {"args": ("[optional: <username/id> and/or "
                                        "<title>] or reply"),
                               "usage": ("Promote an user with immortal "
                                         "power! Requires admin privileges "
                                         "with at least add admin "
                                         "permission and a second "
                                         "admin permission as promote "
                                         "never promotes an user with "
                                         "add admin permission. Title "
                                         "length must be <= 16 characters.")},
                   "demote": {"args": "[optional: <username/id>] or reply",
                              "usage": ("Demote an user to a mortal user. "
                                        "Requires admin privileges with add "
                                        "admin permission. Works with admins "
                                        "only which are promoted by you.")},
                   "mute": {"args": ("[optional: <username/id> <chat "
                                     "(id or link)>] or reply"),
                            "usage": ("Mute a certain user from a chat "
                                      "(remotely). Requires admin "
                                      "privileges with ban permission.")},
                   "unmute": {"args": ("[optional: <username/id> <chat "
                                       "(id or link)>] or reply"),
                              "usage": ("Unmute a certain user from a chat "
                                        "(remotely). Requires admin "
                                        "privileges with ban permission.")},
                   "delaccs": {"args": "[optional: <chat id or link>]",
                               "usage": ("Tries to remove deleted accounts "
                                         "automatically in a chat if admin "
                                         "privileges with ban permission "
                                         "are present. Else it reports the "
                                         "amount of deleted accounts it "
                                         "the specific chat.")}}

    CHATINFO_USAGE = {"chatinfo": {"args": ("[optional: <chat_id/link>] or "
                                            "reply (if channel)"),
                                   "usage": ("Gets info about a chat. "
                                             "Some info might be limited "
                                             "due to missing permissions.")},
                      "chatid": {"args": None,
                                 "usage": ("Gets the ID of a channel or "
                                           "group.")},
                      "getlink": {"args": "[optional: <chat_id/link>]",
                                  "usage": ("Fetch the invite link from a "
                                            "channel or group to share it "
                                            "with other people. Requires "
                                            "admin privileges with invite "
                                            "users permission.")}}

    DELETIONS_USAGE = {"del": {"args": None,
                               "usage": "Deletes the replied message."},
                       "purge": {"args": None,
                                 "usage": ("Purges all messages between "
                                           "the latest and replied message. "
                                           "Admin privileges with delete "
                                           "permission are required if "
                                           "purge is being used in channels "
                                           "or groups.\n"
                                           "**Note: Please don't abuse this "
                                           "feature to delete whole group "
                                           "histories from other people!**")}}

    MEMBERINFO_USAGE = {"minfo": {"args": ("[optional: <tag/id> <group>] or "
                                           "reply"),
                                  "usage": ("Get (remotely) info of a member "
                                            "in a supergroup.")}}

    MESSAGES_USAGE = {"msgs": {"args": ("[optional: <username/id> <group>] "
                                        "or reply"),
                               "usage": ("Gets the amount of sent messages "
                                         "from an user (includes any "
                                         "message like text messages, voice "
                                         "notes, videos etc.).\n"
                                         "Works remotely too.")},
                      "pin": {"args": ("[optional argument \"loud\" to "
                                       "notify all members] or reply"),
                              "usage": ("Reply to someone's message to pin "
                                        "it in the chat.")},
                      "unpin": {"args": "[optional argument \"all\"] or reply",
                                "usage": ("Reply to someone's message to "
                                          "unpin it or send \".unpin all\" to "
                                          "unpin all messages in a chat.")}}

    SCRAPPERS_USAGE = {"trt": {"args": "[optional: <text>] or reply",
                               "usage": ("Translates given text or replied "
                                         "message to the bot's target "
                                         "language.")},
                       "tts": {"args": "[optional: <text>] or reply",
                               "usage": ("Converts text or replied message "
                                         "into spoken voice output "
                                         "(text-to-speech).")},
                       "stt": {"args": "reply only",
                               "usage": ("Converts a replied voice message "
                                         "into text (speech-to-text).")},
                       "scrlang": {"args": None,
                                   "usage": ("Shows which is the current "
                                             "language that bot will "
                                             "translate or TTS to")},
                       "setlang": {"args": "[ISO value]",
                                   "usage": ("Sets a new language from the "
                                             "ISO value list")},
                       "currency": {"args": ("<amount> <From ISO> "
                                             "[optional: <To ISO>]"),
                                    "usage": ("Converts input currency to "
                                              "target currency (default: "
                                              "USD). Requires Country ISO "
                                              "(EUR, USD, JPY etc.).")}}

    SYSTOOLS_USAGE = {"status": {"args": None,
                                 "usage": ("Type .status to check various "
                                           "bot information and if it is "
                                           "up and running.")},
                      "shutdown": {"args": None,
                                   "usage": ("Type .shutdown to shutdown "
                                             "the bot.")},
                      "reboot": {"args": None,
                                 "usage": "Reboots the bot!"},
                      "storage": {"args": None,
                                  "usage": ("Shows info on bot server "
                                            "HDD storage.")},
                      "sysd": {"args": None,
                               "usage": ("Type .sysd to get system details. "
                                         "(Requires neofetch installed)")},
                      "sendlog": {"args": None,
                                  "usage": ("Uploads the log file to the "
                                            "current chat.")}}

    USER_USAGE = {"info": {"args": "[optional: <username/id>] or reply",
                           "usage": "Gets info of an user."},
                  "stats": {"args": None,
                            "usage": "Gets your stats."},
                  "kickme": {"args": None,
                             "usage": "Makes you leave the group."},
                  "userid": {"args": "[optional: <username>] or reply",
                             "usage": ("Get the ID from an user. If "
                                       "replied to a forwarded message, "
                                       "it gets the IDs from both, "
                                       "forwarder and original author.")}}

    WEBTOOLS_USAGE = {"dc": {"args": None,
                             "usage": ("Finds the near datacenter to "
                                       "your userbot host.")},
                      "ping": {"args": "<DNS/IP>",
                               "usage": "Pings a specific DNS or IP address."},
                      "rtt": {"args": None,
                              "usage": "Gets the current Round Trip Time"},
                      "speedtest": {"args": "[optional argument \"pic\"]",
                                    "usage": ("Performs a speedtest and "
                                              "shows the result as text. "
                                              "Passing \"pic\" as argument "
                                              "will change the result to a "
                                              "picture.")}}

    GITHUB_USAGE = {"git": {"args": "<user>/<repo>",
                            "usage": ("Checks for releases on the "
                                      "specified user/repo combination.")}}

    MODULES_UTILS_USAGE = {"listcmds": {"args": ("[optional: <name of "
                                                 "command>]"),
                                        "usage": ("Lists all available and "
                                                  "registered commands.")},
                           "modules": {"args": ("<-option> [number of module "
                                                "from the list]"),
                                       "usage": ("\n`.modules -d [number of "
                                                 "module from the list]`\n"
                                                 "Shows the description of "
                                                 "the specific module. "
                                                 "Maybe some hidden "
                                                 "information are there, "
                                                 "who knows?\n\n"
                                                 "`.modules -i [number of "
                                                 "module from the list]`\n"
                                                 "Shows information about "
                                                 "the specific module like "
                                                 "the name, author, version "
                                                 "etc.\n\n"
                                                 "`.modules -u [number of "
                                                 "module from the list]`\n"
                                                 "Reveals the secrets and "
                                                 "the usage of the specific "
                                                 "module")}}

    TERMINAL_USAGE = {"shell": {"args": "<command>",
                                "usage": ("Executes in the server machine "
                                          "shell prompt (bash, powershell "
                                          "or zsh) the specified command.\n\n"
                                          "**WARNING: if the userbot process "
                                          "is running as root, this could "
                                          "potentially break your system "
                                          "irreversibly! Proceed with "
                                          "caution!**")}}

    MISC_USAGE = {"coinflip": {"args": None,
                               "usage": ("Flips a coin and returns heads "
                                         "or tails, depending on "
                                         "the result.")},
                  "dice": {"args": None,
                           "usage": ("This will send the dice emoji, "
                                     "telegram will take care of the value, "
                                     "totally random.")},
                  "rand": {"args": "<lower limit> <upper limit>",
                           "usage": ("Given an upper and lower limit "
                                     "(both integers), the bot will "
                                     "generate a random number in between.")}}

    PACKAGE_MANAGER_USAGE = {"pkg": {"args": ("<option> [optional: "
                                              "<arguments>]"),
                                     "usage": ("\n`.pkg update "
                                               "[optional: <list of "
                                               "owner/repo combos>]`\n"
                                               "Updates data of all "
                                               "repositories. If repo urls "
                                               "are given e.g '.pkg update "
                                               "nunopenim/module-universe' "
                                               "then only the specific "
                                               "repo(s) will be updated. "
                                               "This command can also be "
                                               "used to add new repos by "
                                               "using the <owner/repo> "
                                               "combo.\n\n"
                                               "`.pkg list [optional: "
                                               "<-installed or -repos>]`\n"
                                               "Lists all installed modules "
                                               "and all modules from known "
                                               "repositories. Use the "
                                               "-installed option to show "
                                               "installed modules only or "
                                               "the -repos option to show "
                                               "modules from repositories "
                                               "only.\n\n"
                                               "`.pkg install <list of "
                                               "modules>`\nor\n"
                                               "`.pkg install -repo "
                                               "<owner/repo> <list of "
                                               "modules>`\n"
                                               "Installs the list of "
                                               "modules from given argument. "
                                               "If you want to install "
                                               "modules from a specific "
                                               "repo only, use the -repo "
                                               "option and pass the "
                                               "owner/repo combo along with "
                                               "the list of modules as "
                                               "argument.\n\n"
                                               "`.pkg uninstall/remove <list "
                                               "of modules>`\n"
                                               "Uninstalls modules from "
                                               "given list.\n\n"
                                               "`.pkg rmrepo <list of "
                                               "owner/repo combos>`\n"
                                               "Removes repos from given "
                                               "list of owner/repo combos "
                                               "from data.")}}

    UPDATER_USAGE = {"update": {"args": "upgrade",
                                "usage": ("Checks for updates, and if "
                                          "avaliable, displays "
                                          "the changelog.\n"
                                          "If the user has checked for "
                                          "updates, it will update the bot "
                                          "to the latest version.")}}

    SIDELOADER_USAGE = {"sideload": {"args": "<argument>",
                                     "usage": ("Sideloads a python script "
                                               "file sent as a document to "
                                               "the chat. Reply to such. "
                                               "You can use the `force` "
                                               "argument to force "
                                               "installation, if a user "
                                               "space module with the same "
                                               "name already exists.\n\n"
                                               "**INFORMATION**: These "
                                               "files must be written to "
                                               "work with the bot. "
                                               "Attempting to load unknown "
                                               "files might result in a "
                                               "'soft brick' of the bot, "
                                               "requiring you to manually "
                                               "delete the bad user space "
                                               "module!\n\n"
                                               "**CRITICAL WARNING**: Some "
                                               "malicious files could send "
                                               "some of your information "
                                               "(namely API Key and/or "
                                               "String Session) to a "
                                               "malicious hacker! Only "
                                               "sideload modules if you "
                                               "trust the source!")}}

    FEATURE_MGR_USAGE = {"disable": {"args": ("<name of command/alias or "
                                              "feature>"),
                                     "usage": ("Disable the given command "
                                               "or feature. Works with "
                                               "aliases too")},
                         "disabled": {"args": None,
                                      "usage": ("Lists all disabled "
                                                "features")},
                         "enable": {"args": ("<name of command/alias or "
                                             "feature>"),
                                    "usage": ("Enable the given command "
                                              "or feature. Works with "
                                              "aliases too")}}
