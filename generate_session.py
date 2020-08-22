# Telethon Stuff
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Misc
from sys import version_info

color_yellow = "\033[33m"
color_red = "\033[31m"
color_end = "\033[0m"

if (version_info.major, version_info.minor) < (3, 8):
    print(color_yellow + "Required Python 3.8!" + color_end)
    quit()

con_confirmed, valid_api_key, valid_api_hash = (False,)*3

print("Welcome!\n\
Get a new string session from your Telegram account with the help of this script.\n\n\
Important: If not done yet, please go to https://my.telegram.org and\n\
-> log in into your account\n\
-> create a new application\n\
-> get your API KEY and HASH (do NOT share these IDs with anyone else!)\n\n\
Please keep the following requirements ready to obtain a new string session:\n\
- Your Telegram application's API KEY and HASH (to access your application)\n\
- Your Phone Number (required to log in into your account)\n\
- Your Account's password (Two-Step Verification; if enabled)\n")

try:
    while not con_confirmed:
        con = input("Continue (y/n)?: ")
        if con.lower() in ("y", "yes"):
            con_confirmed = True
        elif con.lower() in ("n", "no"):
            print("Terminating...")
            quit()
        else:
            print(color_red + "Invalid input. Try again..." + color_end)

    while not valid_api_key:
        API_KEY = input("Please enter your API KEY: ")
        try:
            API_KEY = int(API_KEY)
            valid_api_key = True
        except:
            print(color_yellow + "Invalid integer format. Try again..." + color_end)

    while not valid_api_hash:
        API_HASH = input("Please enter your API HASH: ")
        if len(API_HASH) == 32:
            valid_api_hash = True
        else:
            print(color_yellow + "Invalid hash format. Try again..." + color_end)
except KeyboardInterrupt:
    print("Keyboard interruption. Terminating...")
    quit()

try:
    client = TelegramClient(StringSession(), API_KEY, API_HASH)
    with client:
        print("This long string below is your new string session:\n\n")
        print(client.session.save())
        print("\n\nPlease keep this string to a safe place and copy it to your bot's config.* file")
except KeyboardInterrupt:
    print("Keyboard interruption. Terminating...")
    quit()
except Exception as e:
    print(color_red + f"Unable to obtain new string session: {e}" + color_end)
    quit(1)
