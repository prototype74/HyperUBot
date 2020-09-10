# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

class AdminText(object): # Admin module
    FAIL_CHAT = "`Failed to fetch chat`"
    NO_GROUP_CHAN = "`This chat isn't a group or channel`"
    NO_GROUP_CHAN_ARGS = "`This chat or given chat isn't a group or channel`"
    NO_ADMIN = "`Admin privileges are required to perform this action`"
    NO_BAN_PRIV = "`Ban permission is required to perform this action`"
    DELETED_ACCOUNT = "Deleted Account"
    CANNOT_BAN_SELF = "`I can't ban myself`"
    CANNOT_BAN_ADMIN = "`I can't ban this admin`"
    BAN_SUCCESS_REMOTE = "{} has been banned from **{}**"  # user name, chat tile
    BAN_SUCCESS = "{} has been banned!"  # user name
    BAN_FAILED = "`Failed to ban this person`"
    CANNOT_UNBAN_SELF = "`I can't unban myself`"
    UNBAN_SUCCESS_REMOTE = "{} has been unbanned from **{}**"  # user name, chat tile
    UNBAN_SUCCESS = "{} has been unbanned!"  # user name
    UNBAN_FAILED = "`Failed to unban this person`"
    CANNOT_KICK_SELF = "`I can't kick myself`"
    KICK_SUCCESS_REMOTE = "{} has been kicked from **{}**"  # user name, chat tile
    KICK_SUCCESS = "{} has been kicked!"  # user name
    KICK_FAILED = "`Failed to kick this person`"
    NOONE_TO_PROMOTE = "`There is no one to promote`"
    NOT_USER = "`Given username or ID isn't an User`"
    CANNOT_PROMOTE_SELF = "`I can't promote myself`"
    ADMIN_ALREADY_SELF = "`I am immortal already`"
    ADMIN_ALREADY = "`This person is immortal already`"
    ADMIN_NOT_ENOUGH_PERMS = "`I don't have enough admin rights to promote this person`"
    ADD_ADMINS_REQUIRED = "`Add admins permission is required to perform this action`"
    PROMOTE_SUCCESS = "{} has been promoted with immortal power!"  # user name
    TOO_MANY_ADMINS = "`This chat has too many admins already`"
    EMOJI_NOT_ALLOWED = "`Emoji are not allowed in admin titles`"
    GET_ENTITY_FAILED = "Failed to fetch entity"
    PROMOTE_FAILED = "`Failed to promote this person`"
    NOONE_TO_DEMOTE = "`There is no one to demote`"
    CANNOT_DEMOTE_SELF = "`I can't demote myself`"
    DEMOTED_ALREADY = "`This person is mortal already`"
    DEMOTE_SUCCESS = "{} has been demoted!"  # user name
    CANNOT_DEMOTE_ADMIN = "`This chat has too many admins already`"
    DEMOTE_FAILED = "`Failed to demote this person`"
    NO_GROUP_ARGS = "`This chat or given chat isn't a group`"
    NOT_MUTE_SUB_CHAN = "`Unable to mute subscribers in a channel`"
    CANNOT_MUTE_SELF = "`I can't mute myself`"
    MUTE_SUCCESS_REMOTE = "{} has been muted in **{}**"  # user name, chat tile
    MUTE_SUCCESS = "Muted {}"  # user name
    MUTE_FAILED = "`Failed to mute this person`"
    NOT_UNMUTE_SUB_CHAN = "`Unable to unmute subscribers in a channel`"
    CANNOT_UNMUTE_SELF = "`I can't unmute myself`"
    UNMUTE_SUCCESS_REMOTE = "{} has been unmuted in **{}**"  # user name, chat tile
    UNMUTE_SUCCESS = "Unmuted {}"  # user name
    UNMUTE_FAILED = "`Failed to unmute this person`"
    TRY_DEL_ACCOUNTS = "`Trying to remove deleted accounts...`"
    DEL_ACCS_COUNT = "`{} deleted accounts found in this chat`"
    REM_DEL_ACCS_COUNT = "`Removed {} of {} deleted accounts`"  # rem count, total count
    NO_DEL_ACCOUNTS = "`No deleted accounts found in this chat`"
    REPLY_TO_MSG = "`Reply to a message to pin it`"
    PIN_SUCCESS = "`Message pinned successfully`"
    PINNED_ALREADY = "`This message is pinned already`"
    PIN_FAILED = "`Failed to pin this message`"
    LOG_PIN_MSG_ID = "Message ID"

class StatusText(object):
    UBOT = "Userbot Project: "
    SYSTEM_STATUS = "System Status: "
    ONLINE = "Online!"
    VER_TEXT = "Version: "
    USR_TEXT = "User: "
    RTT = "RTT: "
    TELETON_VER = "Telethon version: "
    PYTHON_VER = "Python version: "
    GITAPI_VER = "GitHub API Version: "
    CASAPI_VER = "CAS API Version: "
    COMMIT_NUM = "Revision: "
    ERROR = "ERROR!"
    DAYS = "days"
    BOT_UPTIMETXT = "Bot uptime: "
    MAC_UPTIMETXT = "Server uptime: "
    SHUTDOWN = "`Powering off...`"
    SHUTDOWN_LOG = "Bot is powering off under user request!"
    SYSD_NEOFETCH_REQ = "`neofetch package is required to display system information`"
    RESTART = "`Rebooting...`"
    RESTART_LOG = "Userbot is restarting!"
    RESTARTED = "Reboot complete!"

class DeletionsText(object):
    CANNOT_DEL_MSG = "`I can't delete this message`"
    UNABLE_DEL_MSG = "`Unable to delete this message`"
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
    CANNOT_GET_CHATINFO = "`I can't get information from this chat!`"
    YES_BOLD = "<b>Yes</b>"
    NO_BOLD = "<b>No</b>"
    YES = "Yes"
    NO = "No"
    CHATINFO = "<b>CHAT INFO:</b>\n"
    CHAT_ID = "ID: <code>{}</code>\n"
    CHATTYPE = "Chat type: {}\n"
    CHAT_NAME = "Chat name: {}\n"
    FORMER_NAME = "Former name: {}\n"
    CHAT_TYPE_PUBLIC = "Chat type: Public\n"
    CHAT_TYPE_PRIVATE = "Chat type: Private\n"
    CREATOR = "Creator: {}\n"
    CREATOR_WITH_URL = "Creator: <a href=\"tg://user?id={}\">{creator_firstname}</a>\n"
    CREATED_NOT_NULL = "Created: <code>{} - {} {}</code>\n"
    CREATED_NULL = "Created: <code>{} - {} {}</code> {}\n"
    DCID = "Data Center ID: {}\n"
    CHAT_LEVEL = "Chat level: <code>{}</code>\n"
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
    SPER_GRP = "Supergroup: {}\n\n"
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
    MEMBERINFO = "MEMBER INFO"
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
    ROOT_RIGHTS = "Root rights"
    SEND_MESSAGES = "Send messages"
    SEND_MEDIA = "Send media"
    SEND_GIFS_STICKERS = "Send stickers & gifs"
    SEND_POLLS = "Send polls"
    EMBED_LINKS = "Embed links"
    WARN_ADMIN_PRIV = "Admin privileges are required to access non-default permissions"
    PROMOTED_BY = "Promoted by"
    ADDED_BY = "Added by"
    JOIN_DATE = "Join date"

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
    MEDIA_FORBIDDEN = "`Couldn't TTS: Uploading media isn't allowed in this chat`"
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

class UserText(object):
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
    STATS_SUPER_GROUPS = "Participant in **{}** super groups"
    STATS_SG_ADMIN = "Admin in **{}** super groups"
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
    USR_INFO = "USER INFO"
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

class GeneralMessages(object):
    ERROR = "ERROR!"
    CHAT_NOT_USER = "`Channels are not User objects`"
    FAIL_FETCH_USER = "`Failed to fetch user`"
    ENTITY_NOT_USER = "`Entity is not an User object`"
    CALL_UREQ_FAIL = "`Call User request failed`"
    LOG_USER = "User"
    LOG_USERNAME = "Username"
    LOG_USER_ID = "User ID"
    LOG_CHAT_TITLE = "Chat title"
    LOG_CHAT_LINK = "Link"
    LOG_CHAT_ID = "Chat ID"

class HelpText(object):
    INVALID_ARG = "`Invalid argument \"{}\"`"
    USAGE = "Usage"
    NAME_OF_MODULE = "name of module"  # lower if possible
    AVAILABLE_MODULES = "Available modules"
    DISABLED_MODULES = "Disabled modules"
    NAME_MODULE = "**{} module**"
    MISSING_NAME_MODULE = "`Missing name of module`"
    MODULE_NOT_FOUND = "`Module \"{}\" not found`"
    MODULE_NO_DESC = "__No description available__"
    MODULE_NO_USAGE = "__No usage available__"
    ASTERISK = "__* Uninstallable user module__"

class WebToolsText(object):
    PING_SPEED = "Round-Trip Time: "
    DCMESSAGE = "Country : `{}`\nThis Datacenter : `{}`\nNearest Datacenter : `{}`"
    BAD_ARGS = "`Bad arguments!`"
    INVALID_HOST = "`There was a problem parsing the IP/Hostname`"
    PINGER_VAL = "DNS: `{}`\nPing Speed: `{}`"
    SPD_START = "`Running speed test...`"
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

class CasIntText(object):
    FAIL = "Failed to extract a user from given data"
    USER_HEADER = "<b>USER DATA</b>\n\n"
    USER_ID = "ID: "
    FIRST_NAME = "First name: "
    LAST_NAME = "Last name: "
    USERNAME = "Username: @"
    CAS_DATA = "\n<b>CAS DATA</b>\n\n"
    RESULT = "Result: "
    OFFENSES = "Total of Offenses: "
    DAY_ADDED = "Day added: "
    TIME_ADDED = "\nTime added: "
    UTC_INFO = "\n\nAll times are in UTC"
    USERS_DETECTED = "Warning! `{}` of `{}` users are CAS Banned:\n"
    NO_USRS = "No CAS Banned users found!"
    NO_ADM = "`CAS check failed: Admin privileges are required`"
    CAS_CHECK_FAIL = "`CAS check failed`"

class GitHubText(object):
    INVALID_URL = "Invalid user/repo combo"
    NO_RELEASE = "The specified release could not be found"
    AUTHOR_STR = "<b>Author:</b> <a href='{}'>{}</a>\n"
    RELEASE_NAME = "<b>Release Name:</b> "
    ASSET = "<b>Asset:</b> \n"
    SIZE = "Size: "
    DL_COUNT = "\nDownload Count: "
    INVALID_ARGS = "Invalid arguments! Make sure you are typing a valid combination of user/repo"

class StickersText(object):
    FAIL_FETCH_INFO = "This command can only be used as a reply to something!"
    NOT_STICKER = "Reply to a sticker to get the pack details!"
    FETCHING_STICKER_DETAILS = "`Fetching details...`"
    STICKER_INFO_OUTPUT = "**Sticker Title:** `{}`\n**Sticker Short Name:** `{}`\n**Official:** `{}`\n**Archived:** `{}`\n**Stickers In Pack:** `{}`\n**Emojis In Pack:**\n{}"

class TerminalText(object):
    BASH_ERROR = "There has been an unspecified error, likely bad arguments or that command does not exist"

class MiscText(object):
    COIN_LANDED_VAL = "The coin landed on: "
    THRWING_COIN = "`Throwing coin...`"
    HEADS = "Heads"
    TAILS = "Tails"
    RAND_INVLD_ARGS = "`Invalid arguments, make sure you have exactly 2 numbers`"
    FRST_LIMIT_INVALID = "`The first value is not a valid number!`"
    SCND_LIMIT_INVALID = "`The second value is not a valid number!`"
    RAND_NUM_GEN = "Your generated number between `{}` and `{}`: **`{}`**"

class PackageManagerText(object):
    INVALID_ARG = "Invalid argument! Make sure it is **update**, **list**, **install** or **uninstall**!"
    UPDATE_COMPLETE = "Modules list has been updated from the universe(s): **{}**"
    EMPTY_LIST = "The modules list is empty! Please run `.pkg update` first!"
    FILES_IN = "\n\n **Files in {}:**\n"
    FILE_DSC = "{}. [{}]({}) - {}\n"
    NO_PKG = "`No specified package to install! Process halted!`"
    MOD_NOT_FOUND_INSTALL = "No module named `{}` was found in the release repo! Aborting!"
    DONE_RBT = "`Rebooting userbot...`"
    NO_UNINSTALL_MODULES = "No uninstallable modules present! Process halted!"
    NO_UN_NAME = "Please specify a module name, I cannot uninstall __nothing__!"
    MULTIPLE_NAMES = "For safety reasons, you can only uninstall one module at a time, please give a single name!"
    NOT_IN_USERSPACE = "`{}` is not a valid Userspace module name! Process halted!"
    UNINSTALLING = "`Uninstalling {}...`"
    REBOOT_DONE_INS = "Done! Module(s) installed: `{}`"
    REBOOT_DONE_UNINS = "Done! Uninstalled `{}`!"
    INSTALL_LOG = "Userbot rebooted! Module(s) installed: `{}`"
    UNINSTALL_LOG = "Userbot rebooted! Module uninstalled: `{}`"
    INSTALLED = "**INSTALLED MODULES:**\n"

class UpdaterText(object):
    UPDATES_NOT_RAN = "Please run just .update to check for updates first!"
    NO_UPDATES = "No updates queued. If you suspect a new update has been released, please run .update to queue it."
    UPDATING = "`Updating...`"
    UPD_ERROR = "An unspecified error has occured, the common issue is not having git installed as a system package, please make sure you do."
    UPD_SUCCESS = "Userbot updated! Rebooting..."
    UNKWN_BRANCH = "Unrecognized branch. Likely you are running a modified source."
    LATS_VERSION = "{} is already running on the latest version!"
    UPD_AVAIL = "**UPDATES AVALIABLE!**\n\n**Changelog:**\n"
    RUN_UPD = "\nPlease run `.update upgrade` to update now!"
    CHLG_TOO_LONG = "New updates avaliable, however the changelist is too long to be displayed!\n\nPlease run `.update upgrade` to update now!"
    RBT_COMPLETE = "Update complete!"
    UPD_LOG = "Userbot has successfully been updated and has rebooted!"

# Save your eyes from what may become the ugliest part of this userbot.
class ModuleDescriptions(object):
    ADMIN_DESC = "A module to help you to manage your or a friend's group easier. Includes common commands such as ban, unban, promote etc.\
                 \n\nNote: most commands in this module require admin privileges to work properly."
    CHATINFO_DESC = "Get most various information from a channel, group or super group such as creation date, message counts, deletions, former name etc."
    DELETIONS_DESC = "This module allows you to delete your or in groups messages faster. Someone spammed your group? use purge command to delete them all!\
                     \nAll commands in this module require admin privileges to delete other people's messages.\
                     \n\n**Important: don't abuse this module to delete someone's else whole group history**, for real, just don't..."
    MEMBERINFO_DESC = "Provides information from a specific group participant like permissions, restriction date, join date etc.\
                     \n\nNote: requires admin privileges to access other member's permissions."
    SCRAPPERS_DESC = "Not as it sounds like to be but still this module includes useful features like translation or text-to-speech."
    SYSTOOLS_DESC = "This module contains a set of system tools for the bot. It allows you to check the bot uptime, the server uptime, the versions of all the bot's \
                    components, the specifications of the server system, and some bot power controls."
    USER_DESC = "Provides information about any user, your statistics, and contains the kickme tool."
    WEBTOOLS_DESC = "This module contains most, if not all, of the bot's webtools, such as ping, speedtest, rtt calculator and the current datacenter."
    CAS_INTERFACE_DESC = "The interface for the Combot Anti-Spam System API. It allows you to check a specific user for CAS bans or an entire group, via the designated commands."
    GITHUB_DESC = "A module that takes use of the GitHub API. This allows you to check for releases from a specific user and repository."
    TERMINAL_DESC = "This module provides tools to run directly shell commands, in the host machine.\
                    \n\n**Attention:** Running shell commands in the bot can and will make permanent changes to the host system. **Bad things will happen if you run the bot as sudo/root!**"
    MISC_DESC = "The miscelaneous module contains a small set of tools that did not quite fit any of the other modules, but at the same time were too simple to have their own module. Check the help for more details."
    PACKAGE_MANAGER_DESC = "The package manager module allows a user to manage extra apps, from external repos, either official, such as the modules-universe repo, or from external sources. It provides a way for users to customize their bots more than stock."
    UPDATER_DESC = "The updater module allows the user to check for bot updates and to update the bot, if new updates exist."

class ModuleUsages(object):
    ADMIN_USAGE = "`.ban` [optional: <username/id> <chat (id or link)>] or reply\
                 \nUsage: Ban a certain user from a chat (remotely). Requires admin privileges with ban permission.\
                 \n\n`.unban` [optional: <username/id> <chat (id or link)>] or reply\
                 \nUsage: Unban a certain user from a chat (remotely). Requires admin privileges with ban permission.\
                 \n\n`.kick` [optional: <username/id> <chat (id or link)>] or reply\
                 \nUsage: Kick a certain user from a chat (remotely). Requires admin privileges with ban permission.\
                 \n\n`.promote` [optional: <username/id> and/or <title>] or reply\
                 \nUsage: Promote an user with immortal power! Requires admin privileges with at least add admin permission and a second\
                 \nadmin permission as promote never promotes an user with add admin permission. Title length must be <= 16 characters.\
                 \n\n`.demote` [optional: <username/id>] or reply\
                 \nUsage: Demote an user to a mortal user. Requires admin privileges with add admin permission. Works with admins only which are promoted by you.\
                 \n\n`.mute` [optional: <username/id> <chat (id or link)>] or reply\
                 \nUsage: Mute a certain user from a chat (remotely). Requires admin privileges with ban permission.\
                 \n\n`.unmute` [optional: <username/id> <chat (id or link)>] or reply\
                 \nUsage: Unmute a certain user from a chat (remotely). Requires admin privileges with ban permission.\
                 \n\n`.delaccs`\
                 \nUsage: Tries to remove deleted accounts automatically in a chat if admin privileges with ban permission are present.\
                 \nElse it reports the amount of deleted accounts it the specific chat.\
                 \n\n`.pin` [optional argument \"loud\" to notify all members] or reply\
                 \nUsage: Reply to someone's message to pin it in the chat."

    CHATINFO_USAGE = "`.chatinfo` [optional: <chat_id>] \
                 \nUsage: Gets info about a chat. Some info might be limited due to missing permissions."

    DELETIONS_USAGE = "`.del`\
         \nUsage: Deletes the replied message.\
         \n\n`.purge`\
         \nUsage: Purges all messages between the latest and replied message. Admin privileges with delete permission are required if purge is being used in channels or groups.\
         \n**Note: Please don't abuse this feature to delete whole group histories from other people!**"

    MEMBERINFO_USAGE = "`.minfo` [optional: <tag/id> <group>] or reply\
          \nUsage: Get (remotely) info of a member in a supergroup."

    SCRAPPERS_USAGE = "`.trt` [optional: <text>] or reply\
          \nUsage: Translates given text or replied message to the bot's target language.\
          \n\n`.tts` [optional: <text>] or reply\
          \nUsage: Converts text or replied message into spoken voice output (text-to-speech).\
          \n\n`.stt` reply only\
          \nUsage: Converts a replied voice message into text (speech-to-text).\
          \n\n`.currency` <amount> <From ISO> [optional: <To ISO>] \
          \nUsage: Converts input currency to target currency (default: USD). Requires Country ISO (EUR, USD, JPY etc.)."

    SYSTOOLS_USAGE = "`.status`\
         \nUsage: Type .status to check various bot information and if it is up and running.\
         \n\n`.shutdown`\
         \nUsage: Type .shutdown to shutdown the bot. \
         \n\n`.reboot`\
         \nUsage: Reboots the bot! \
         \n\n`.sysd`\
         \nUsage: Type .sysd to get system details. (Requires neofetch installed)"

    USER_USAGE = "`.info ` [optional: <username>]\
        \nUsage: Gets info of an user.\
        \n\n`.stats`\
        \nUsage: Gets your stats.\
        \n\n`.kickme`\
        \nUsage: Makes you leave the group."

    WEBTOOLS_USAGE = "`.rtt` \
                    \nUsage: Gets the current Round Trip Time\
                    \n\n`.dc` \
                    \nUsage: Finds the near datacenter to your userbot host. \
                    \n\n`.ping` <DNS/IP> \
                    \nUsage: Pings a specific DNS or IP address. \
                    \n\n`.speedtest` [optional argument \"pic\"] \
                    \nUsage: Performs a speedtest and shows the result as text. Passing \"pic\" as argument will change the result to a picture."

    CAS_INTERFACE_USAGE = "`.cascheck` [optional: <username>]\
                    \nUsage: Checks if a user is CAS Banned\
                    \n\n`.groupcheck` \
                    \nUsage: Checks the whole group for CAS Banned users "

    GITHUB_USAGE = "`.git` <user>/<repo> \
                  \nUsage: Checks for releases on the specified user/repo combination."

    TERMINAL_USAGE = "`.shell` <command> \
                  \nUsage: Executes in the server machine shell prompt (bash, powershell or zsh) the specified command. \
                  \n\n**WARNING: if the userbot process is running as root, this could potentially break your system irreversibly! Proceed with caution!**"

    MISC_USAGE = "`.coinflip` \
                 \nUsage: Flips a coin and returns heads or tails, depending on the result.\
                 \n\n`.dice` \
                 \nUsage: This will send the dice emoji, telegram will take care of the value, totally random.\
                 \n\n`.rand` <lower limit> <upper limit>\
                 \nUsage: Given an upper and lower limit (both integers), the bot will generate a random number in between."

    PACKAGE_MANAGER_USAGE = "`.pkg update` \
                 \nUsage: Updates the Modules List with info from the repos. \
                 \n\n`.pkg list` \
                 \nUsage: Lists the list of available modules for installation (can be outdated!) \
                 \n\n`.pkg install <module name 1> <module name 2 (optional)> <...>` \
                 \nUsage: Installs the list of modules given as argument. \
                 \n\n`.pkg uninstall <module name>` \
                 \nUsage: Uninstalls the specified module. For security measures, it only works with a single module name."

    UPDATER_USAGE = "`.update` \
                 \nUsage: Checks for updates, and if avaliable, displays the changelog. \
                 \n\n`.update upgrade` \
                 \nUsage: If the user has checked for updates, it will update the bot to the latest version."