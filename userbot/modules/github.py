# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO, VERSION
from userbot.include.aux_funcs import module_info
from userbot.include.language_processor import GitHubText as msgRep, ModuleDescriptions as descRep, ModuleUsages as usageRep
import userbot.include.git_api as api
from telethon.events import NewMessage
from os.path import basename

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
    message += msgRep.RELEASE_NAME + releaseName + "\n\n"
    for asset in assets:
        message += msgRep.ASSET
        fileName = api.getReleaseFileName(asset)
        fileURL = api.getReleaseFileURL(asset)
        assetFile = "<a href='{}'>{}</a>".format(fileURL, fileName)
        sizeB = ((api.getSize(asset)) / 1024) / 1024
        size = "{0:.2f}".format(sizeB)
        downloadCount = api.getDownloadCount(asset)
        message += assetFile + "\n"
        message += msgRep.SIZE + size + " MB"
        message += msgRep.DL_COUNT + str(downloadCount) + "\n\n"
    return message

@tgclient.on(NewMessage(pattern=r"^\.git(?: |$)(.*)", outgoing=True))
async def get_release(event):
    commandArgs = event.text.split(" ")
    if len(commandArgs) != 2 or not "/" in commandArgs[1]:
        await event.edit(msgRep.INVALID_ARGS)
        return
    index = 0  # later will support going back in time!
    url = commandArgs[1]
    text = getData(url, index)
    await event.edit(text, parse_mode="html")
    return

MODULE_DESC.update({basename(__file__)[:-3]: descRep.GITHUB_DESC})
MODULE_DICT.update({basename(__file__)[:-3]: usageRep.GITHUB_USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="GitHub", version=VERSION)})
