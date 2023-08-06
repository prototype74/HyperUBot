# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .errors import AccessError
from userbot._core.access_controller import _protectedAccess
from inspect import currentframe, getouterframes
from logging import getLogger
from os.path import basename, join
import sys

log = getLogger(__name__)


class _SysConfigurations:
    def __init__(self):
        """
        Initialize HyperUBot's global configurations.
        SysConfigurations allows to store configs into a dictionary
        to access them later with getConfig (see below).

        Certain configs may be inaccessible due to security reasons
        """
        self.__botconfigs = {"REBOOT": False, "REBOOT_SAFEMODE": False,
                             "START_RECOVERY": False, "UPDATE_COMMIT_ID": None,
                             "USERDATA": join(".", "userbot", "userdata")}
        self.__protect_configs = ("API_KEY", "API_HASH", "STRING_SESSION")

    def _addConfiguration(self, config: str, value):
        """
        Add new config to global configurations. Nothing will be added
        if config exist already. Function protected to use at init only.

        Args:
            config (str): config ID
            value: any value to pass (int, string, list etc.)

        Example:
            addConfiguration("EXAMPLE_INT", 5)
            addConfiguration("EXAMPLE_STR", "Test")
            addConfiguration("EXAMPLE_LIST", [25, "test"])
        """
        special_caller = [join("userbot", "__init__.py"),
                          join("userbot", "sysutils", "config_loader.py")]
        sys_caller = getouterframes(currentframe(), 2)[2].filename
        valid_caller = False
        for caller in special_caller:
            if sys_caller.endswith(caller):
                valid_caller = True
                break
        if not valid_caller:
            raise AccessError("Access to configurations denied "
                              f"(requested by {basename(sys_caller)})")
        if config in self.__protect_configs:
            raise AccessError(f"Access to '{config}' denied "
                              f"(requested by {basename(sys_caller)})")
        if config not in self.__botconfigs:
            self.__botconfigs[config] = value
        return

    def _setConfiguration(self, config: str, value):
        """
        Update an existing config. Only special caller can use this function.

        Args:
            config (str): config ID
            value: any value to pass (int, string, list etc.)

        Example:
            setConfiguration("EXAMPLE_INT", 5)
            setConfiguration("EXAMPLE_STR", "Test")
            setConfiguration("EXAMPLE_LIST", [25, "test"])
        """
        special_caller = [join("userbot", "modules", "_systools.py"),
                          join("userbot", "modules", "_updater.py")]
        module_caller = getouterframes(currentframe(), 2)[2].filename
        valid_caller = False
        for caller in special_caller:
            if module_caller.endswith(caller):
                valid_caller = True
                break
        if not valid_caller:
            raise AccessError("Access to configurations denied "
                              f"(requested by {basename(module_caller)})")
        if config == "UPDATE_COMMIT_ID" and \
           not module_caller.endswith(
               join("userbot", "modules", "_updater.py")):
            raise AccessError(f"Access to '{config}' denied "
                              f"(requested by {basename(module_caller)})")
        if config in self.__botconfigs:
            self.__botconfigs[config] = value
        return

    def _getConfiguration(self, config: str, default):
        """
        Get a config from global configurations.

        Args:
            config (str): config ID
            default: default value to return if config doesn't exist

        Example:
            test_var = getConfiguration("EXAMPLE_BOOL", False)
            if test_var:
                print("EXAMPLE is True")

        Returns:
            the value from config, default if config doesn't exist
        """
        module_caller = getouterframes(currentframe(), 2)[2].filename
        if not config:
            return default
        if config in self.__protect_configs:
            raise AccessError(f"Access to '{config}' denied "
                              f"(requested by {basename(module_caller)})")
        if config in self.__botconfigs:
            return self.__botconfigs.get(config)
        return default

_sysconfigs = _SysConfigurations()


def addConfig(config: str, value):
    """
    Add new config to global configurations. Nothing will be added
    if config exist already. Function protected to use at init only.
    (see addConfiguration)
    """
    try:
        return _sysconfigs._addConfiguration(config, value)
    except AccessError as ae:
        log.warning(ae)
    return


def setConfig(config: str, value):
    """
    Update an existing config. Only special caller can use this function
    """
    try:
        return _sysconfigs._setConfiguration(config, value)
    except AccessError as ae:
        log.warning(ae)
    return


def getConfig(config: str, default=None):
    """
    Get a config from global configurations.

    Args:
        config (str): config ID
        default: default value to return if config doesn't exist

    Example:
        from userbot.sysutils.configuration import getConfig

        test_var = getConfig("EXAMPLE_BOOL", False)
        if test_var:
            print("EXAMPLE is True")

    Returns:
        the value from config, default if config doesn't exist
    """
    try:
        return _sysconfigs._getConfiguration(config, default)
    except AccessError as ae:
        log.warning(ae)
    return default


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=["_sysconfigs", "_SysConfigurations", "addConfig", "setConfig"],
    warn_msg=("Unauthorized access to protected attribute blocked "
              "(requested by {1}:{2})"),
    allowed=(join("userbot", "modules", "_systools.py"),
             join("userbot", "modules", "_updater.py")),
    mlogger=log
)
