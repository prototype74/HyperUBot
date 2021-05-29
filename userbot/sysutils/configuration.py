# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from inspect import currentframe, getouterframes
from logging import getLogger
from os.path import basename, join

log = getLogger(__name__)


class AccessError(Exception):
    __module__ = Exception.__module__

    def __init__(self, message="Access denied", *args, **kwargs):
        """
        Custom Exception to inform about inaccessibility
        """
        self.message = message
        super().__init__(self.message, *args, **kwargs)


class _SysConfigurations:
    def __init__(self):
        """
        Initialize HyperUBot's global configurations.
        SysConfigurations allows to store configs into a dictionary
        to access them later with getConfig (see below).

        Certain configs may be inaccessible due to security reasons
        """
        self.__botconfigs = {"REBOOT": False, "REBOOT_SAFEMODE": False,
                             "START_RECOVERY": False, "UPDATE_COMMIT_ID": None}
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
        module_caller = (getouterframes(currentframe(), 2)[2].filename
                         if getouterframes(
                             currentframe(), 2)[2].filename.endswith(
                                 join("userbot", "__init__.py")) else
                         getouterframes(currentframe(), 2)[1].filename)
        if not module_caller.endswith(join("userbot", "__init__.py")):
            raise AccessError("Access to configurations denied")
        if config in self.__protect_configs:
            raise AccessError(f"Access to '{config}' denied")
        if config not in self.__botconfigs.keys():
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
        special_caller = [join("userbot", "modules", "systools.py"),
                          join("userbot", "modules", "updater.py"),
                          join("userbot", "modules", "package_manager.py"),
                          join("userbot", "modules", "sideloader.py")]
        valid_caller = False
        for caller in special_caller:
            if getouterframes(currentframe(), 2)[2].filename.endswith(caller):
                valid_caller = True
                break
        module_caller = (getouterframes(currentframe(), 2)[2].filename
                         if valid_caller else
                         getouterframes(currentframe(), 2)[1].filename)
        valid_caller = False
        for caller in special_caller:
            if module_caller.endswith(caller):
                valid_caller = True
                break
        if not valid_caller:
            raise AccessError("Access to configurations denied")
        if config == "UPDATE_COMMIT_ID" and \
           not module_caller.endswith(
               join("userbot", "modules", "updater.py")):
            raise AccessError("Access to {config} denied")
        if config in self.__botconfigs.keys():
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
        module_caller = (getouterframes(currentframe(), 2)[2].filename
                         if not getouterframes(
                             currentframe(), 2)[2].filename.endswith(
                                 __name__) else
                         getouterframes(currentframe(), 2)[1].filename)
        if not config:
            return default
        if config in self.__protect_configs:
            raise AccessError(f"Access to '{config}' denied "
                              f"(requested by {basename(module_caller)})")
        if config in self.__botconfigs.keys():
            for key, value in self.__botconfigs.items():
                if config == key:
                    return value
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
