# This is the english language file! As an early version,
# if you want to translate, copy this file then rename all
# the imports in the language processor module
# for your language. I will think of a better implementation
# system in future revisions. - Penim

class AdminText(object): # Admin module
    NOT_ADMIN = "`I am not admin!`"
    BANNING_USER = "`Banning user...`"
    NO_PERMS = "`I do not have sufficient permissions to execute this action!`"
    NO_MSG_DEL_PERMS = "`I do not have permissions to delete messages, so I cannot delete whatever this user wrote.`"
    BANNED_SUCCESSFULLY = "`{}` was banned!"
    UNBANNING_USER = "`Unbanning user...`"
    UNBANNED_SUCCESSFULLY = "Successfully unbanned!"
    USERID_INVALID = "Invalid UserID!"
    FAILED_FETCH_USER = "`Couldn't fetch user.`"
    KICKING_USER = "`Kicking user...`"
    KICKED_SUCCESSFULLY = "{} has been kicked!"

class TestModuleText(object): #test module
    TEST_MESSAGE = "`This is a test message! I am operational!`"