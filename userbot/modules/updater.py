# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient, PROJECT, log

# Telethon stuff
from telethon.events import NewMessage

# Misc stuff
from git import Repo
from subprocess import check_output, CalledProcessError
from sys import executable

BOT_REPO_URL = "https://github.com/nunopenim/HyperUBot"
RAN = False
FOUND_UPD = False

@tgclient.on(NewMessage(pattern=r"^\.update(?: |$)(.*)$", outgoing=True))
async def updater(upd):
    global RAN
    global FOUND_UPD
    args = upd.pattern_match.group(1)
    if args == "upgrade":
        if not RAN:
            await upd.edit("Please run just .update to check for updates first!")
            return
        if not FOUND_UPD:
            await upd.edit("No updates queued. If you suspect a new update has been released, please run .update to queue it.")
            return
        try:
            await upd.edit("`Updating...`")
            gitpull = check_output("git pull", shell=True).decode()
            log.info(gitpull)
            pip = check_output(executable + " -m pip install -r requirements.txt", shell=True).decode()
            log.info(pip)
        except CalledProcessError:
            await upd.edit("An unspecified error has occured, the common issue is not having git installed as a system package, please make sure you do.")
            return
        await upd.edit("Userbot updated! Please reboot now!")
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
            await upd.edit("{} is already running on the latest version!".format(PROJECT))
            RAN = True
            return
        if changelog:
            retText = "**UPDATES AVALIABLE!**\n\n**Changelog:**\n"
            retText += changelog
            retText += "\nPlease run `.update upgrade` to update now!"
            await upd.edit(retText)
            RAN = True
            FOUND_UPD = True
            return

