# Copyright 2021-2023 nunopenim @github
# Copyright 2021-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot._core.access_controller import _protectedAccess
from userbot.include.language_processor import (FeatureMgrText as msgRep,
                                                ModuleDescriptions as descRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.feature_manager import (_disable_feature,
                                              _enable_feature,
                                              _get_disabled_features)
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from logging import getLogger
import sys

log = getLogger(__name__)
ehandler = EventHandler(log)


@ehandler.on(command="disable", hasArgs=True, outgoing=True)
async def disable_feature(event):
    feature = event.pattern_match.group(1)
    if not feature:
        await event.edit(msgRep.DISABLE_FTR)
        return
    result = _disable_feature(feature)
    if not result:
        log.warn(f"Feature '{feature}' can't be disabled or "
                 "it's not a feature")
        await event.edit(msgRep.DISABLE_FTR_FAIL)
        return
    log.info(f"Feature '{feature}' disabled")
    await event.edit(msgRep.DISABLE_FTR_SUCCESS.format(feature))
    return


@ehandler.on(command="disabled", outgoing=True)
async def disabled_features(event):
    text = f"**{msgRep.DISABLED_FTRS}**\n\n"
    result = _get_disabled_features()
    text += result if result else f"__{msgRep.NO_DISABLED_FTRS}__"
    await event.edit(text)
    return


@ehandler.on(command="enable", hasArgs=True, outgoing=True)
async def enable_feature(event):
    feature = event.pattern_match.group(1)
    if not feature:
        await event.edit(msgRep.ENABLE_FTR)
        return
    result = _enable_feature(feature)
    if not result:
        log.warn(f"Feature '{feature}' can't be enabled or it's not a feature")
        await event.edit(msgRep.ENABLE_FTR_FAIL)
        return
    log.info(f"Feature '{feature}' enabled")
    await event.edit(msgRep.ENABLE_FTR_SUCCESS.format(feature))
    return


for cmd in ("disable", "disabled", "enable"):
    register_cmd_usage(
        cmd,
        usageRep.FEATURE_MGR_USAGE.get(cmd, {}).get("args"),
        usageRep.FEATURE_MGR_USAGE.get(cmd, {}).get("usage")
    )


register_module_desc(descRep.FEATURE_MGR_DESC)
register_module_info(
    name="Feature Manager",
    authors="nunopenim, prototype74",
    version=VERSION
)


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=["_disable_feature", "_enable_feature", "_get_disabled_features"],
    warn_msg=("Access to protected attribute from Feature Manager denied"
              "(requested by {1}:{2})"),
    mlogger=log
)
