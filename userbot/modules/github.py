# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.language_processor import (GitHubText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
import userbot.include.git_api as api

ehandler = EventHandler()


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


@ehandler.on(command="git", hasArgs=True, outgoing=True)
async def get_release(event):
    commandArgs = event.text.split(" ")
    if len(commandArgs) != 2 or "/" not in commandArgs[1]:
        await event.edit(msgRep.INVALID_ARGS)
        return
    index = 0  # later will support going back in time!
    url = commandArgs[1]
    text = getData(url, index)
    await event.edit(text, parse_mode="html")
    return


@ehandler.on(command="gitrate", alt="gitlimit", outgoing=True)
async def rate_limit(event):
    data = api.getRateLimit()
    if not data:
        await event.edit(msgRep.GITRATE_NO_DATA)
        return

    api_naming = {
        "core": "REST API",
        "search": "Search API",
        "graphql": "GraphQL API",
        "integration_manifest": "GitHub App Manifest"
    }

    text = "**GitHub API Rate Limit**\n\n"
    for key, value in data.items():
        limit = value.get("limit", 0)
        remaining = value.get("remaining", 0)
        api_name = api_naming.get(key, "Unknown")
        text += f"{api_name}: {remaining}/{limit}\n"
    await event.edit(text)
    return


for cmd in ("git", "gitrate"):
    register_cmd_usage(
        cmd,
        usageRep.GITHUB_USAGE.get(cmd, {}).get("args"),
        usageRep.GITHUB_USAGE.get(cmd, {}).get("usage")
    )

register_module_desc(descRep.GITHUB_DESC)
register_module_info(
    name="GitHub",
    authors="nunopenim, prototype74",
    version=VERSION
)
