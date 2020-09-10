# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# My stuff
from userbot import tgclient, PROJECT, log
from userbot.include.language_processor import UpdaterText as msgRep

# Telethon stuff
from telethon.events import NewMessage
from telethon.errors.rpcerrorlist import MessageTooLongError

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
            await upd.edit(msgRep.UPDATES_NOT_RAN)
            return
        if not FOUND_UPD:
            await upd.edit(msgRep.NO_UPDATES)
            return
        try:
            await upd.edit(msgRep.UPDATING)
            gitpull = check_output("git pull", shell=True).decode()
            log.info(gitpull)
            pip = check_output(executable + " -m pip install -r requirements.txt", shell=True).decode()
            log.info(pip)
        except CalledProcessError:
            await upd.edit(msgRep.UPD_ERROR)
            return
        await upd.edit(msgRep.UPD_SUCCESS)
        return
    else:
        repo = Repo()
        branch = repo.active_branch.name
        if not (branch in ['master', 'staging']):
            await upd.edit(msgRep.UNKWN_BRANCH)
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
            await upd.edit(msgRep.LATS_VERSION.format(PROJECT))
            RAN = True
            return
        if changelog:
            try:
                retText = msgRep.UPD_AVAIL
                retText += changelog
                retText += msgRep.RUN_UPD
                await upd.edit(retText)
            except MessageTooLongError:
                retText = msgRep.CHLG_TOO_LONG
                await upd.edit(retText)
            RAN = True
            FOUND_UPD = True
            return
