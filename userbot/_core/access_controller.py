# Copyright 2022-2023 nunopenim @github
# Copyright 2022-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.errors import UnauthorizedAccessError
from inspect import currentframe, getouterframes
from logging import getLogger, Logger
from os.path import basename, dirname, join
import sys


# based on: https://stackoverflow.com/a/922693
def _protectedAccess(module, attrs: list,
                     allowed: tuple = (), warn_msg: str = "", mlogger=None):
    if isinstance(mlogger, Logger):
        logger = mlogger
    else:
        logger = getLogger(__name__)

    all_attrs = ["_protectedAccess"] + attrs

    class FilterAccess():
        def __getattribute__(self, attr):
            if attr in all_attrs:
                caller = getouterframes(currentframe(), 2)[1]
                caller_name = caller.filename
                caller_line = caller.lineno
                if dirname(caller_name).endswith(
                    (join("userbot", "modules"),
                     join("userbot", "modules_user"))):
                    if not caller_name.endswith(allowed):
                        if warn_msg:
                            logger.warning(
                                warn_msg.format(
                                    attr, basename(caller_name), caller_line))
                        raise UnauthorizedAccessError()
            return getattr(module, attr)

        def __setattr__(self, attr, value):
            if attr in all_attrs:
                caller = getouterframes(currentframe(), 2)[1]
                caller_name = caller.filename
                caller_line = caller.lineno
                if dirname(caller_name).endswith(
                    (join("userbot", "modules"),
                     join("userbot", "modules_user"))):
                    if not caller_name.endswith(allowed):
                        if warn_msg:
                            logger.warning(
                                warn_msg.format(
                                    attr, basename(caller_name), caller_line))
                        raise UnauthorizedAccessError()
            return setattr(module, attr, value)
    return FilterAccess()


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=[],
    allowed=(join("userbot", "modules", "_feature_manager.py"),
             join("userbot", "modules", "_package_manager.py"),
             join("userbot", "modules", "_systools.py"),
             join("userbot", "modules", "_updater.py"),
             join("userbot", "modules", "sideloader.py")),
    warn_msg=("Modules are not allowed to use the "
              "Access Controller (requested by {1}:{2})")
)
