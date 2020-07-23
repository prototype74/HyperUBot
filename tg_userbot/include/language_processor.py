

import tg_userbot.translations.english as text

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

class DeletionsText(object):
    PURGE_COMPLETE = text.DeletionsText.PURGE_COMPLETE
    DEL_FAILED = text.DeletionsText.DEL_FAILED

class GeneralMessages(object):
    ERROR = text.GeneralMessages.ERROR
    GET_USER_FROM_EVENT_FAIL = text.GeneralMessages.GET_USER_FROM_EVENT_FAIL

# Remove before official release!
class TestModuleText(object): #test module
    TEST_MESSAGE = text.TestModuleText.TEST_MESSAGE