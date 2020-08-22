# This is the english language file! As an early version,
# if you want to translate, copy this file then rename all
# the imports in the language processor module
# for your language. I will think of a better implementation
# system in future revisions. - Penim

class AdminText(object): # Admin module
    NOT_ADMIN = "I am not admin! I need admin permissions to perform this action!"
    BANNING_USER = "`Banning user...`"
    NO_PERMS = "I do not have sufficient permissions to execute this action!"
    NO_MSG_DEL_PERMS = "I do not have permissions to delete messages, so I cannot delete whatever this user sent."
    BANNED_SUCCESSFULLY = "`{}` was banned!"
    UNBANNING_USER = "`Unbanning user...`"
    UNBANNED_SUCCESSFULLY = "Successfully unbanned!"
    USERID_INVALID = "Invalid UserID!"
    FAILED_FETCH_USER = "Couldn't fetch user."
    KICKING_USER = "`Kicking user...`"
    KICKED_SUCCESSFULLY = "{} has been kicked!"
    ONLY_CHAN_GROUPS = "I can only perform this action in Groups or channels!"
    NOT_USER = "This entity is not a User!"
    PROMT_SELF = "I can't promote myself!"
    ADM_ALRD = "This user is already Admin!"
    PROMTING_USER = "`Promoting user...`"
    NO_ADD_ADM_RIGHT = "I am admin, but I do not have permission to add other admins!"
    PRMT_SUCCESS = "Successfully promoted!"
    TOO_MANY_ADM = "There are too many administrators in this chat!"
    ALREADY_NOT_ADM = "This user is already not an Admin!"
    DMT_MYSELF = "I can't demote myself!"
    DMTING_USER = "`Demoting user...`"
    DMTED_SUCCESSFULLY = "Successfully demoted!"
    NO_DEl_USERS = "No deleted accounts detected!"
    SEARCHING_DEL_USERS = "`Searching for deleted accounts...`"
    FOUND_DEL_ACCS = "Found `{}` deleted accounts! Use .delusers clean to clean them!"
    DELETING_ACCS = "`Removing deleted accounts...`"
    NO_BAN_PERMS = "I have no permissions to ban users!"
    DEL_ALL_SUCCESFULLY = "Successfully removed `{}` deleted accounts!"
    DEL_SOME_SUCCESSFULLY = "Successfully removed `{}` deleted accounts! `{}` admin accounts could not be removed!"
    BANLOG = "#BAN\nUser: [{}]({})\nChat: [{}]({})"
    UNBANLOG = "#UNBAN\nUser: [{}]({})\nChat: [{}]({})"
    KICKLOG = "#KICK\nUser: [{}]({})\nChat: [{}]({})"
    CLEAN_DELACC_LOG = "#DELUSERS\nRemoved `{}` deleted accounts!"
    PROMT_LOG = "#PROMOTE\nUser: [{}]({})\nChat: [{}]({})"
    DMT_LOG = "#DEMOTE\nUser: [{}]({})\nChat: [{}]({})"
    MUTING_USR = "`Muting user...`"
    USER_MUTED = "Successfully muted!"
    UNMUTING_USR = "`Unmuting user...`"
    USER_UNMUTED = "Successfully unmuted!"
    MUTE_LOG = "#MUTE\nUser: [{}]({})\nChat: [{}]({})"
    UNMUTE_LOG = "#UNMUTE\nUser: [{}]({})\nChat: [{}]({})"
    MSG_NOT_FOUND_PIN = "`Reply to a message to pin it!`"
    PINNED_SUCCESSFULLY = "Sucessfully pinned!"

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
    SHUTDOWN_LOG = "#SHUTDOWN\nBot is powering off under user request!"

class DeletionsText(object):
    PURGE_COMPLETE = "Purge complete! Deleted `{}` messages!"
    DEL_FAILED = "I cannot delete this message!"
    PURGE_LOG = "#PURGE\nPurged {} messages successfully!"

class ChatInfoText(object):
    CHAT_ANALYSIS = "`Analysing the chat...`"
    EXCEPTION = "`An unexpected error has occurred!`"
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
    SCAN_CHANNEL_FAIL = "`Cannot check channels for member info`"
    FAIL_GET_MEMBER_CHAT = "`Failed to get member info: couldn't fetch chat`"
    FAIL_GET_MEMBER_ARGS = "`Failed to get member info: invalid arguments given`"
    INVALID_USER_ID = "`Invalid user ID!`"
    FAIL_GET_MEMBER_DIV = "Failed to get member info"
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

class UserText(object):
    LEAVING = "`Leaving chat...`"
    KICKME_LOG = "#KICKME\nSuccessfully left [{}]({})!"
    STATS_PROCESSING = "`Computing stats...`"
    STATS_USERS = "Users: **{}**\n"
    STATS_GROUPS = "Groups: **{}**\n"
    STATS_SUPER_GROUPS = "Super Groups: **{}**\n"
    STATS_CHANNELS = "Channels: **{}**\n"
    STATS_BOTS = "Bots: **{}**\n"
    FETCH_INFO = "`Getting user info...`"
    NO_PROF_PIC = "This user has no profile picture."
    UNKNOWN = "Unknown"
    USR_NO_BIO = "This User has no Bio"
    USR_INFO = "<b>USER INFO:</b>\n\n"
    FIRST_NAME = "First Name: {}\n"
    LAST_NAME = "Last Name: {}\n"
    USERNAME = "Username: {}\n"
    DCID = "Data Centre ID: {}\n"
    PROF_PIC_COUNT = "Number of Profile Pics: {}\n"
    PROF_LINK = "Permanent Link To Profile: "
    ISBOT = "Bot: {}\n"
    ISRESTRICTED = "Restricted: {}\n"
    ISVERIFIED = "Verified by Telegram: {}\n"
    USR_ID = "ID: <code>{}</code>\n\n"
    BIO = "Bio: \n<code>{}</code>\n\n"
    COMMON = "Common chats: {}\n"

class GeneralMessages(object):
    ERROR = "ERROR!"
    GET_USER_FROM_EVENT_FAIL = "Invalid user specified!"

class HelpText(object):
    INVALID_NAME = "Please specify a valid module name."
    DEFAULT = "Please specify which module do you want help for !!\nSyntax: .help <module name>\n\nModules available:\n\n"

class WebToolsText(object):
    PING_SPEED = "Ping speed is: "
    DCMESSAGE = "Country : `{}`\nThis Datacenter : `{}`\nNearest Datacenter : `{}`"
    BAD_ARGS = "`Bad arguments!`"
    INVALID_HOST = "`There was a problem parsing the IP/Hostname`"
    PINGER_VAL = "DNS: `{}`\nPing Speed: `{}`"
    SPD_START = "`Running speed test...`"
    SPD_END = "Started at: {}\nDownload: `{}`\nUpload: `{}`\nPing: `{}`\nISP: `{}`"

# Save your eyes from what may become the ugliest part of this userbot.
class HelpDesignations(object):
    ADMIN_HELP = "`.ban` \
                 \nUsage: Reply to someone's message with .ban to ban them. \
                 \n\n`.unban` \
                 \nUsage: Reply to someone's message with .unban to unban them. \
                 \n\n`.kick` \
                 \nUsage: Reply to someone's message with .kick to kick them. \
                 \n\n`.promote` \
                 \nUsage: Reply to someone's message with .promote to promote them. \
                 \n\n`.demote` \
                 \nUsage: Reply to someone's message with .demote to demote them. \
                 \n\n`.delusers`\
                 \nUsage: Searches for deleted accounts in a group. Use '.delusers clean' to remove deleted accounts from the group. \
                 \n\n`.mute` \
                 \nUsage: Reply to someone's message with .mute to mute them. \
                 \n\n`.unmute` \
                 \nUsage: Reply to someone's message with .unmute to unmute them. \
                 \n\n`.pin` \
                 \nUsage: Reply to someone's message to pin it in the chat."

    CHATINFO_HELP = "`.chatinfo` [optional: <chat_id>] \
                 \nUsage: Gets info about a chat. Some info might be limited due to missing permissions."

    DELETIONS_HELP = "`.purge`\
         \nUsage: Purges all messages starting from the reply.\
         \n\n`.del`\
         \nUsage: Deletes the message replied to."

    MEMBERINFO_HELP = "`.minfo` [optional: <tag/id> <group>] or reply\
          \nUsage: Get (remotely) info of a member in a supergroup."

    SYSTOOLS_HELP = "`.status`\
         \nUsage: Type .status to check various bot information and if it is up and running.\
         \n\n`.shutdown`\
         \nUsage: Type .shutdown to shutdown the bot. \
         \n\n`.sysd`\
         \nUsage: Type .sysd to get system details. (Requires neofetch installed)"

    USER_HELP = "`.info ` [optional: <username>]\
        \nUsage: Gets info of an user.\
        \n\n`.stats`\
        \nUsage: Gets your stats.\
        \n\n`.kickme`\
        \nUsage: Makes you leave the group."
