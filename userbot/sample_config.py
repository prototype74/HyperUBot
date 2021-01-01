# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import log
from os.path import basename 

if basename(__file__).startswith("config") or basename(__file__).startswith("sample_config"):
    log.error("Please do not just use this sample config as your main config. Create a new config.py in the same directory with a proper ConfigClass.")
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


    ### Optional configurations
    #
    # Userbot display language. Default is english ('en')
    #
    UBOT_LANG = "en"  # must match language code

    #
    # Logs any bot event to the specific chat
    #
    LOGGING = False  # Enable or disable logging
    LOGGING_CHATID = None  # Chat ID. Must be an integer

    #
    # To store downloaded file(s) (temporary)
    #
    TEMP_DL_DIR = "./downloads"  # Default

    #
    # Skips load specific module(s) e.g. ["admin"]
    #
    NOT_LOAD_MODULES = []  # must be a list or config will not work

    #
    # Community extra repos, leave as list of strings (or not)
    # The format of the repo should be "<github_username>/<github_repo>"
    # Example: "nunopenim/modules-universe", although this is not a community repo :)
    #
    COMMUNITY_REPOS = []

