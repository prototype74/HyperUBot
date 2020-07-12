import tg_userbot.languages.english as en

# Language processor!

class AdminText(object): # Admin module
    NOT_ADMIN = en.AdminText.NOT_ADMIN
    BANNING_USER = en.AdminText.BANNING_USER
    NO_PERMS = en.AdminText.NO_PERMS
    NO_MSG_DEL_PERMS = en.AdminText.NO_MSG_DEL_PERMS
    BANNED_SUCCESSFULLY = en.AdminText.BANNED_SUCCESSFULLY
    UNBANNING_USER = en.AdminText.UNBANNING_USER
    UNBANNED_SUCCESSFULLY = en.AdminText.UNBANNED_SUCCESSFULLY
    USERID_INVALID = en.AdminText.USERID_INVALID
    FAILED_FETCH_USER = en.AdminText.FAILED_FETCH_USER
    KICKING_USER = en.AdminText.KICKING_USER
    KICKED_SUCCESSFULLY = en.AdminText.KICKED_SUCCESSFULLY
    ONLY_CHAN_GROUPS = en.AdminText.ONLY_CHAN_GROUPS
    NOT_USER = en.AdminText.NOT_USER
    PROMT_SELF = en.AdminText.PROMT_SELF
    ADM_ALRD = en.AdminText.ADM_ALRD
    PROMTING_USER = en.AdminText.PROMTING_USER
    NO_ADD_ADM_RIGHT = en.AdminText.NO_ADD_ADM_RIGHT
    PRMT_SUCCESS = en.AdminText.PRMT_SUCCESS
    TOO_MANY_ADM = en.AdminText.TOO_MANY_ADM
    ALREADY_NOT_ADM = en.AdminText.ALREADY_NOT_ADM
    DMT_MYSELF = en.AdminText.DMT_MYSELF
    DMTING_USER = en.AdminText.DMTING_USER
    DMTED_SUCCESSFULLY = en.AdminText.DMTED_SUCCESSFULLY
    NO_DEl_USERS = en.AdminText.NO_DEl_USERS
    SEARCHING_DEL_USERS = en.AdminText.SEARCHING_DEL_USERS
    FOUND_DEL_ACCS = en.AdminText.FOUND_DEL_ACCS
    DELETING_ACCS = en.AdminText.DELETING_ACCS
    NO_BAN_PERMS = en.AdminText.NO_BAN_PERMS
    DEL_ALL_SUCCESFULLY = en.AdminText.DEL_ALL_SUCCESFULLY
    DEL_SOME_SUCCESSFULLY = en.AdminText.DEL_SOME_SUCCESSFULLY

class StatusText(object):
    UBOT = en.StatusText.UBOT
    SYSTEM_STATUS = en.StatusText.SYSTEM_STATUS
    ONLINE = en.StatusText.ONLINE
    VER_TEXT = en.StatusText.VER_TEXT
    USR_TEXT = en.StatusText.USR_TEXT
    RTT = en.StatusText.RTT
    TELETON_VER = en.StatusText.TELETON_VER
    PYTHON_VER = en.StatusText.PYTHON_VER
    GITAPI_VER = en.StatusText.GITAPI_VER
    CASAPI_VER = en.StatusText.CASAPI_VER
    COMMIT_NUM = en.StatusText.COMMIT_NUM
    ERROR = en.StatusText.ERROR

class GeneralMessages(object):
    ERROR = en.GeneralMessages.ERROR
    GET_USER_FROM_EVENT_FAIL = en.GeneralMessages.GET_USER_FROM_EVENT_FAIL

# Remove before official release!
class TestModuleText(object): #test module
    TEST_MESSAGE = en.TestModuleText.TEST_MESSAGE