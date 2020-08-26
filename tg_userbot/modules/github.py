# My stuff
from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import GitHubText as msgRep
import tg_userbot.include.git_api as api

def getData(url, index):
    if not api.getData(url):
        return msgRep.INVALID_URL
    recentRelease = api.getReleaseData(api.getData(url), index)
    if recentRelease is None:
        return msgRep.NO_RELEASE
    author = api.getAuthor(recentRelease)
    authorUrl = api.getAuthorUrl(recentRelease)
    assets = api.getAssets(recentRelease)
    releaseName = api.getReleaseName(recentRelease)
    message = msgRep.AUTHOR_STR.format(authorUrl, author)
    message += "RELEASE_NAME" + releaseName + "\n\n"
    for asset in assets:
        message += "ASSET"
        fileName = api.getReleaseFileName(asset)
        fileURL = api.getReleaseFileURL(asset)
        assetFile = "<a href='{}'>{}</a>".format(fileURL, fileName)
        sizeB = ((api.getSize(asset)) / 1024) / 1024
        size = "{0:.2f}".format(sizeB)
        downloadCount = api.getDownloadCount(asset)
        message += assetFile + "\n"
        message += "SIZE" + size + " MB"
        message += "DL_COUNT" + str(downloadCount) + "\n\n"
    return message


@watcher(pattern=".git(?: |$)(.*)", outgoing=True)
async def get_release(event):
    commandArgs = event.text.split(" ")
    if len(commandArgs) != 2 or not "/" in commandArgs[1]:
        await event.edit("INVALID_ARGS")
        return
    index = 0  # later will support going back in time!
    url = commandArgs[1]
    text = getData(url, index)
    await event.edit(text, parse_mode="html")