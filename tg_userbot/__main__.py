from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from sys import argv
from tg_userbot import bot

try:
    bot.start()
except PhoneNumberInvalidError:
    print("Invalid PhoneNumber")
    exit(1)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
