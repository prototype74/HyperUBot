from tg_userbot import LOGS
from os.path import basename 

if basename(__file__).startswith("config") or basename(__file__).startswith("sample_config"):
    LOGS.error("Please do not just use this sample config as your main config. Create a new config.py in the same directory with a proper ConfigClass.")
    quit(1)

class ConfigClass(object):
    ### Required configurations
    #
    # API KEY and HASH are 2 identification numbers to log in into your Telegram API appliaction-
    # If you don't have any yet, create a new application at https://my.telegram.org
    # and put your API IDs to the corresponding configs below
    #
    # Note: Do NOT share your API KEY and HASH with anyone else!
    #
    API_KEY = ""  #  Your API KEY
    API_HASH = ""  #  Your API HASH

    #
    # Needed to log in into your user account
    #
    STRING_SESSION = ""  # Your string session

    #
    # Required to store downloaded file(s) (temporary)
    #
    TEMP_DL_DIR = "./downloads"  # Default

    #
    # Userbot display language. Default is english ('en')
    #
    UBOT_LANG = "en"  # must match language code


    ### Optional configurations
    #
    # Logs any bot event to the specific chat
    #
    BOTLOG = False  # Enable or disable logging
    BOTLOG_CHATID = None  # Chat ID. Must be an integer

