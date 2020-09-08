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
        await upd.edit("Basically here upgrades")
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
            await upd.edit("Bot is up to date")
            return
        if changelog:
            await upd.edit(changelog)
            return

