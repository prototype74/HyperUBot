# HyperUBot Guide - Hosting your own community repo

## 0. Requirements, rules and advices

### 0.1 - Requirements:

    - GitHub account
    - Some module(s) you developed.

### 0.2 - Rules:

Besides the common sense rules, such as "don't host malware", the modules you make and upload should not share the same name as the modules that are by default distributed with the bot and the modules in modules-universe. You cannot use existing commands in the modules universe and bot. There is already a [taken commands list](https://github.com/nunopenim/module-universe/blob/master/TAKEN_COMMANDS.md) in this repo's root directory (Soon there will be a bot one).

### 0.3 - Advices:

If you create your own repo, you should also create a channel to release information in how to install, updates and the requirements of such modules (pip dependencies). If your module needs extra pip dependencies, you should tell users to install them via the req_install module, available in the modules-universe. If you want to go more exotic, pip can be imported into your module. You could create some function to check if there is a dependency missing. Be creative :)
You should also include the licenses under which your modules (or the modules you are redistributing) in a separate "Licenses" folder. The source codes should also be available in a src folder.
Last but not least, if you want to make an extension of official modules (such as admin.py), you should name them admin_ext.py. You could include commands here such as tban or tmute, that we didn't implement.

## 1. How to host, and how hosting system works.

The bot gets modules via the "releases" system of GitHub. You should create a new release there. The tag and title should be the name of what you want your repo to be known as (since this is where the bot will get the names). You can write a description if you want, but it is not needed. In the files to be added, you need to exclusively drop .py files. When the release is published, there should be only .py files (and the 2 source code archives made automatically, but bot ignores these!). Any other file could possibly break the bot.
