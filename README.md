# ![](https://github.com/prototype74/HyperUBot/wiki/resources/hyperanim2021final_KebapciEBY.gif)

A customizable, modular Telegram userbot, with innovative components.

Copyright (C) 2020-2021 nunopenim\
Copyright (C) 2020-2021 prototype74

> Licensed under [PEL](https://github.com/prototype74/HyperUBot/blob/master/LICENSE.md)

All rights reserved.

## What is this?

HyperUBot is a modular Telegram userbot written in Python which uses 
[Telethon](https://github.com/LonamiWebs/Telethon)'s API library by [LonamiWebs](https://github.com/LonamiWebs).
It does not require any form of database. It has support to be fully translatable, contains it's own package manager,
with an [official repo](https://github.com/nunopenim/module-universe) and the possibility to configure multiple extra community repos.
It contains also a sideloader for `.py` files sent in chat. The aim of this userbot is to become an extension of it's own user.
Instead of coming cluttered with all kinds of packages, it is fully customizable, aiming to be fast.

## Compatibility

HyperUBot works with Windows _(PowerShell and WSL)_, macOS, Linux _(Ubuntu, Arch linux etc.)_ and Android. We recommend using `Ubuntu 18.04` or `20.04`, as it's setup is a lot easier, and straight forward (there is no need of installing a package manager, such as apt-get, since it comes by default.)

### Supported platforms

- Android (Termux)
- Debian Based Distros (Native Linux, WSL)
- Red Hat Based Distros (Native Linux)
- macOS
- Windows (PowerShell)

> Cloud platforms like Heroku are **not** supported by us, as these platforms can't handle shell commands, some of our shell based commands (`.ping`, `.rtt` etc.) do need to work properly. Also some cloud platforms may reset the environment which will also reset HyperUBot's saved data and settings.

## Install HyperUBot

Follow the instructions on our [Setup wiki](https://github.com/prototype74/HyperUBot/wiki/Download-and-setup) to install HyperUBot on your device. Follow the steps meant for your **Operating System** where you want to install HyperUBot.

> **Warning**: Do not git clone the repository to download HyperUBot as changes pushed to the repo may not be stable for normal usage. Git clone it only if you want take own changes to the source. Our stable releases are available in our [Releases](https://github.com/prototype74/HyperUBot/releases) of this repository.

## Read the wiki!

We made a [GitHub wiki](https://github.com/prototype74/HyperUBot/wiki) which should help users to understand more how HyperUBot works and which features it does offer. Feel free to check it out!

## Reporting a bug

### How to proper report a bug

A bug report can be done either in the [Issues](https://github.com/prototype74/HyperUBot/issues) section of this repository or
in our Telegram Support Group. In order to solve the bug or issue report from you as fast as possible, please answer the following requirements as detailed as possible (this can be used as a template):

- Which HyperUBot, Python and Telethon versions are you running?
- On which platform(s) did you run it?
- Describe the bug or issue as good as possible
- Provide the log which the bot did generate!

HyperUBot generates a log `hyper.log` in the bot's root directory automatically everytime you run the bot.
Please provide us this log, as it helps us a lot to figure out the bug or issue faster.\
Bugs or issues caused by user modules from [HyperUBot's modules universe](https://github.com/nunopenim/module-universe)
should be reported in [it's Issues](https://github.com/nunopenim/module-universe/issues) section.

### What we don't accept as a bug

We **DO NOT** provide support, if the bug or issue was caused by modules from [Community repos](https://github.com/prototype74/HyperUBot/wiki/Community-Repos) or other type of modules e.g. ported modules from other userbots. Expect that we will ignore such bug reports if you report it anyway.

## Support

Currently we have a [News Channel](https://t.me/HyperUBotNews) (Click to join). Here you can find news about bot updates, changes in modules and releases in the [module-universe](https://github.com/nunopenim/module-universe).

We also have a [Support Group](https://t.me/HyperUBotSupport) (Click to join), where we will be there to discuss about the bot, fix some issues, and help you set up the bot, if you are stuck in a specific step.

## Maintainers

- [nunopenim](https://github.com/nunopenim)
- [prototype74](https://github.com/prototype74)

## Credits

### Special thanks

- [KebapciEBY](https://github.com/KebapciEBY), for the amazing banner! Also for the support and ideas he gave during development.

### Translators

- [nunopenim](https://github.com/nunopenim), for the Portuguese translation
- [prototype74](https://github.com/prototype74), for the German translation
