# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient

# Telethon stuff
from telethon.events import NewMessage

# Misc stuff
from git import Repo

BOT_REPO_URL = "https://github.com/nunopenim/HyperUBot"

@tgclient.on(NewMessage(pattern=r"^\.update(?: |$)(.*)$", outgoing=True))
async def updater(upd):
    args = upd.pattern_match.group(1)
    if args == "upgrade":
        await upd.edit("`LMAO PRANKED! I AM STILL BROKEN`")
        return
    else:
        repo = Repo()
        branch = repo.active_branch.name
        if not (branch in ['master', 'staging']):
            await upd.edit("Unrecognized branch. Likely you are running a modified source.")
            return
        try:
            repo.create_remote('upstream', BOT_REPO_URL)
        except BaseException:
            pass
        repo.remote('upstream').fetch(branch)
        changelog = ''
        counter = 1
        for commit in repo.iter_commits("HEAD..upstream/"+branch):
            changelog += "{}. [{}] > `{}`\n".format(counter, commit.author, commit.summary)
            counter += 1
        if not changelog:
            await upd.edit("HyperUBot is already running on the latest version!")
            return
        if changelog:
            retText = "**UPDATES AVALIABLE!**\n\n**Changelog:**\n"
            retText += changelog
            retText += "\n\nPlease run `.update upgrade` to update now!"
            await upd.edit(retText)
            return
