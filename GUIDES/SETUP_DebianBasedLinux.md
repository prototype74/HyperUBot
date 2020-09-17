# HyperUBot Guide - Set up in a Debian Based Distro
## 0. Pre-requisites

Before starting up, make sure you have the following packages installed: ``python3 git neofetch ffmpeg flac net-tools``.

It is required to have at least python3.8. To install the following packages, run the following command:

``sudo apt-get update && sudo apt-get install python3 git neofetch ffmpeg flac net-tools``

The prefered distros to work are Ubuntu 18.04 and Ubuntu 20.04 (flavours like Kubuntu, Xubuntu and Lubuntu, and variants like Linux Mint, work too!), but other Debian based distros (including Debian itself) should work.

## 1. Clone the userbot repo.

After having the needed packages installed, you will need to clone the bot repo. You can do such with the following command:

``git clone --recursive https://github.com/nunopenim/HyperUBot.git``

After the command runs, you should have a folder named HyperUBot in the current working directory. Change directory to it, so we advance to the next step:

``cd HyperUBot``

## 2. Installing the dependencies.

In the bot's main directory (the HyperUBot folder that you cloned in the previous step), run the following command:

``python3 -m pip install -r requirements.txt``

This should install all the bot's requirements. After this command is done, and if it ran well, you are ready to advance to #3.

## 3. Configuring the bot.

The bot relies on a config.py file. You can find a sample_config.py file inside "HyperUBot/userbot". This file is **NOT** to be used and just serves as a demonstration file, with descriptions of the supported fields. Some modules downloaded from community repos might require you to add extra configuration fields or classes for them to properly work! To create a new config file, run the following command:

``nano userbot/config.py``

This will open the nano text editor, inside you can copy the following template:

``
class ConfigClass(object):
    API_KEY = ""
    API_HASH = ""
    STRING_SESSION = ""
    UBOT_LANG = "en"
    LOGGING = False
    LOGGING_CHATID = 0
    TEMP_DL_DIR = "./downloads"
    COMMUNITY_REPOS = []
``

Save it, by doing Ctrl + O, then Enter/Return key, and then Ctrl + X, to exit the editor. To get the API_KEY and API_HASH values, you will need to login to the [Telegram API](https://my.telegram.org/). Here you can create an App, in the API Development Tools page. After creating an App, your API_KEY is the "App api_id" value, and your API_HASH is the "App api_hash". Don't share these values with anyone! By running the same command as before, to open the text editor, you can copy and paste these values to between the "" in each of these fields. 

### (Recommended) Generating a String Session

We have included, in the root folder of the userbot, a python script to generate a string session. This is recommended, as you no longer need to log in everytime. To do such, you can run the command:

``python3 generate_session.py``

It will ask you for your phone number and the login code message. After obtaining the String session, you can copy the value, and the paste it in the configuration field, between the ""

### (Optional) Logging, Language and Community Repos

Setting up logging is easy, all you need is a designated log group (Do not use public groups, or you could be banned for spam!). Having the log group, you need to find it's ID. You can do such by using a Group Manager Bot, or if your userbot is working already, by the .chatinfo command. Copy this ID and put it in the LOGGING_CHATID field, then change LOGGING to True. That's it!

To set up a language, you will need to change the UBOT_LANG parameter, to any of the supported languages inside "HyperUBot/translations". Just replace "en" by any other language code (no need to include the .py part of the file).

Community repos are also easy to set up. All you need is the name of the repository and the author, in GitHub. Then add it, between "", to between the [] in the COMMUNITY_REPOS field. If you need to add more repositories, separate them by commas (for example ["nunopenim/repo1", "nunopenim/repo2"]).

## 4. Running the bot!

If your configuration is valid, and everything has been set-up correctly, you are ready to start! Do such by running the following command:

``python3 -m userbot``

In the first execution, it can ask for a phone number and for the confirmation codes/2 step auth password. This is normal, and we do not register this information.

Have fun!
