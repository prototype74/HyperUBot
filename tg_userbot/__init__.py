from telethon import TelegramClient
from telethon.sessions import StringSession
from logging import basicConfig, INFO, getLogger
from sys import version_info #check python version
from dotenv import load_dotenv
import os

load_dotenv("config.env")

#For now, static, there is also a DEBUG one
basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO)

LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6: #for now python 3.6
    LOGS.error("Required Python 3.6")
    quit(1)

ENV = bool(os.environ.get('ENV', False)) #check if environment vars

if ENV:
    API_KEY = os.environ.get("API_KEY", None)
    API_HASH = os.environ.get("API_HASH", None)
    BOTLOG = os.environ.get("BOTLOG", False)
    BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", "0"))
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
else:
    from tg_userbot.config import ConfigClass  # Import here, otherwise error, if ENV!

    #Add some checks for API_KEY and API_HASH, they are requirements!
    API_KEY = ConfigClass.API_KEY
    API_HASH = ConfigClass.API_HASH
    BOTLOG = ConfigClass.BOTLOG
    BOTLOG_CHATID = ConfigClass.BOTLOG_CHATID
    STRING_SESSION = ConfigClass.STRING_SESSION

#add something for stringsession
if STRING_SESSION:
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    bot = TelegramClient("tguserbot", API_KEY, API_HASH)

#SYSVARS
PROJECT = "tguserbot-X"
VERSION = "0.0.1-DEV_PREV"