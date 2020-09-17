# HyperUBot Guide - Set up in the Termux environment
## 0. Pre-requisites

Before starting up, make sure you have the following packages installed: `python git neofetch ffmpeg flac nano`.

It is required to have at least python3.8. To install the following packages, run the following command:

`pkg update && pkg install python git neofetch ffmpeg flac nano`

## 1. Clone the userbot repo.

After having the needed packages installed, you will need to clone the bot repo. You can do such with the following command:

`git clone --recursive https://github.com/nunopenim/HyperUBot.git`

After the command runs, you should have a folder named HyperUBot in the current working directory.
Change directory to it, so we advance to the next step:

`cd HyperUBot`

## 2. Installing the dependencies.

In the bot's main directory (the HyperUBot folder that you cloned in the previous step), run the following command:

`python -m pip install -r requirements.txt`

This should install all the bot's requirements. After this command is done, and if it ran well, you are ready to advance to #3.

## 3. Configuring the bot.

The bot relies on a config file, either `.env` or `.py`. You can find the sample configs inside "HyperUBot/userbot".
Sample configs are **NOT** to be used and just serves as demonstration files, with descriptions of the supported fields.
Some modules downloaded from community repos might require you to add extra configuration fields or classes for them to properly work!

### Setup config using ENV
To create a new config `.env` file, run the following command:

`nano userbot/config.env`

This will open the nano text editor, inside you can copy the following template:

```
# Required configs
API_KEY = ""
API_HASH = ""
STRING_SESSION = ""
UBOT_LANG = "en"

# Optional configs
LOGGING = False
LOGGING_CHATID = 0
TEMP_DL_DIR = "./downloads"
COMMUNITY_REPOS = []
```

### Setup config using py script
To create a new config `.py` file, run the following command:

`nano userbot/config.py`

This will open the nano text editor, inside you can copy the following template:

```python
class ConfigClass(object):
    # Required configs
    API_KEY = ""
    API_HASH = ""
    STRING_SESSION = ""
    UBOT_LANG = "en"

    # Optional configs
    LOGGING = False
    LOGGING_CHATID = 0
    TEMP_DL_DIR = "./downloads"
    COMMUNITY_REPOS = []
```

Save it, by doing Ctrl + O, then Enter/Return key, and then Ctrl + X, to exit the editor.
To get the API_KEY and API_HASH values, you will need to login to [My Telegram](https://my.telegram.org/).
Here you can create an App, in the API Development Tools page.
After creating an App, your API_KEY is the "App api_id" value, and your API_HASH is the "App api_hash".
Don't share these values with anyone! By running the same command as before,
to open the text editor, you can copy and paste these values to between the "" in each of these fields.

Note: Only one config file, either `.env` or `.py`, should be configured in "userbot" directory.
If both are configured there, then only `config.env` will be loaded.

### (Recommended) Generating a String Session

We have included, in the root folder of the userbot, a python script to generate a string session.
This is recommended, as you no longer need to log in everytime. To do such, you can run the command:

`python generate_session.py`

It will ask you for your phone number and the login code message. After obtaining the String session,
you can copy the value, and the paste it in the configuration field, between the ""

### (Optional) Logging, Language and Community Repos

Setting up logging is easy, all you need is a designated log group (Do not use public groups, or you could be banned for spam!).
Having the log group, you need to find it's ID. You can do such by using a Group Manager Bot,
or if your userbot is working already, by the .chatinfo command.
Copy this ID and put it in the LOGGING_CHATID field, then change LOGGING to True. That's it!

To set up a language, you will need to change the UBOT_LANG parameter,
to any of the supported languages inside "HyperUBot/userbot/translations".
Just replace "en" by any other language code (no need to include the .py part of the file).

Community repos are also easy to set up. All you need is the name of the repository and the author,
in GitHub. Then add it, between "", to between the [] in the COMMUNITY_REPOS field.
If you need to add more repositories, separate them by commas (for example ["nunopenim/repo1", "nunopenim/repo2"]).

## 4. Running the bot!

If your configuration is valid, and everything has been set-up correctly, you are ready to start!
Do such by running the following command:

`python -m userbot`

In the first execution, it can ask for a phone number and for the confirmation codes/2 step auth password.
This is normal, and we do not register this information.

Have fun!
