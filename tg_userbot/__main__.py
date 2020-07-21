from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from sys import argv
from tg_userbot import bot, LOGS, PROJECT, VERSION
from importlib import import_module
from tg_userbot.modules import ALL_MODULES

try:
    bot.start()
except PhoneNumberInvalidError:
    print("Invalid PhoneNumber")
    exit(1)

for module in ALL_MODULES:
    imported_module = import_module("tg_userbot.modules." + module)

LOGS.info(PROJECT + " " + VERSION + ": operational!")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
