# ![HyperUBot](https://github.com/prototype74/HyperUBot/wiki/resources/hyperanim2021final_KebapciEBY.gif)

A customizable, modular Telegram userbot, with innovative components.

Copyright (C) 2020-2021 nunopenim\
Copyright (C) 2020-2021 prototype74

> Licensed under [PEL](https://github.com/prototype74/HyperUBot/blob/master/LICENSE.md)

All rights reserved.

## What is this?

HyperUBot is a modular Telegram userbot written in Python which uses 
[Telethon](https://github.com/LonamiWebs/Telethon)'s API library by 
[LonamiWebs](https://github.com/LonamiWebs). It does not require any form of 
database. It has support to be fully translatable, contains it's own package manager, 
with an [official community repo](https://github.com/nunopenim/module-universe) 
and the possibility to configure multiple extra community repos. It contains 
also a sideloader for `.py` files sent in chat. The aim of this userbot is to 
become an extension of it's own user. Instead of coming cluttered with all 
kinds of packages, it is fully customizable, aiming to be fast.

## Compatibility

HyperUBot works with Linux based systems, macOS and Windows. It doesn't matter 
on which platform you'll setup HyperUBot, it's setup will be easy on all of 
them. However, at least [Python](https://www.python.org/) v3.8 will be required 
regardless on which platform you want to host HyperUBot.

### Supported platforms

- Alpine Linux
- Android (with Termux)
- Arch Linux Based Distros (Arch Linux, Manjaro, etc.)
- Debian Based Distros (Linux Mint, Ubuntu, etc.)
- Docker* (Cloud platforms or local machine)
- macOS (Catalina (10.15) or newer)
- Red Hat Based Distros (AlmaLinux, Fedora, etc.)
- Windows 10/11 (with PowerShell (5.0 or newer) or WSL)

> \* Docker will reset the environment after it's stopped which will also reset 
HyperUBot's saved data and settings. So it's recommended to use 
[docker-volume](https://docs.docker.com/storage/volumes/) or 
[bind mounts](https://docs.docker.com/storage/bind-mounts/) to keep your data 
permanently.

## Install HyperUBot

Follow the instructions in our 
[Setup wiki](https://github.com/prototype74/HyperUBot/wiki/Installation-and-setup) 
to install HyperUBot on your device. Follow the steps meant for your 
**Operating System** where you want to install HyperUBot.

> **Important notice**: Do not git clone the repository to install HyperUBot as 
changes pushed to the repository may not be stable for normal usage. Clone the 
project only if you want to take own changes to the source. Our stable releases 
are available in our [Releases](https://github.com/prototype74/HyperUBot/releases) 
section which will be automatically picked by the installers in setup wiki and 
by the updater in userbot.

## Read the wiki!

We made a [GitHub wiki](https://github.com/prototype74/HyperUBot/wiki) which 
should help users to understand more how HyperUBot works and which features it 
does offer. Feel free to check it out!

## Reporting a bug

### How to proper report a bug

A bug report can be done either in the 
[Issues](https://github.com/prototype74/HyperUBot/issues) section of this 
repository or in our Telegram Support Group. In order to solve the bug or issue 
report from you as fast as possible, please answer the following requirements 
as detailed as possible (this can be used as a template):

- Which HyperUBot, Python and Telethon versions are you running?
- On which platform(s) did you run it?
- Describe the bug or issue as good as possible
- Provide the log which the bot did generate!

HyperUBot generates a log `hyper.log` in the bot's root directory automatically 
everytime you run the bot. Follow 
[this guide](https://github.com/prototype74/HyperUBot/wiki/Logging#get-or-view-hyperlog-file) 
to view or get the log.\
Bugs or issues caused by user modules from 
[HyperUBot's modules universe](https://github.com/nunopenim/module-universe) should 
be reported in [it's Issues](https://github.com/nunopenim/module-universe/issues) 
section.

### What we don't accept as a bug

We **DO NOT** provide support, if the bug or issue was caused by modules from 
[community repos](https://github.com/prototype74/HyperUBot/wiki/Community-Repos) 
or other type of modules e.g. ported modules from other userbots. Expect that we 
will ignore such bug reports if you report it anyway.

## Support

Currently we have a [News Channel](https://t.me/HyperUBotNews) (Click to join). 
Here you can find news about bot updates, changes in modules and releases in the 
[module-universe](https://github.com/nunopenim/module-universe).

We also have a [Support Group](https://t.me/HyperUBotSupport) (Click to join), 
where we will be there to discuss about the bot, fix some issues, and help you 
set up the bot, if you are stuck in a specific step.

## Maintainers

- [nunopenim](https://github.com/nunopenim)
- [prototype74](https://github.com/prototype74)

## Credits

### People, who also contributed to this project

- [AndrzejDwo](https://github.com/AndrzejDwo)
- [soulr344](https://github.com/soulr344)
- [Watn3y](https://github.com/Watn3y)

### Special thanks

- [KebapciEBY](https://github.com/KebapciEBY) [banner, ideas]

### Translators

- [nunopenim](https://github.com/nunopenim) [Portuguese translation]
- [prototype74](https://github.com/prototype74) [German translation]
