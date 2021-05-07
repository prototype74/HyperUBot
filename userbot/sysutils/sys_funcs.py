# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.version import VERSION
from subprocess import check_output
import platform
import os
import sys

def requiredVersion(min_ver: str, max_ver: str, empty_func: bool = False):
    """
    Wraps a given function and returns it only if current
    HyperUBot version is between min and max version. If version
    does not match required versions, a non callable type (None)
    will be returned instead.
    Ideal if you want to limit your functions or features
    to certain versions only

    Args:
        min_ver (string): minimum required version
        max_ver (string): maximum required version
        empty_func (bool): if a callable empty function should
                           be returned instead of None

    Note:
        if used together with EventHandler (example below) and
        empty_func set to True, EventHandler will still register
        the commands but without content

    Examples:
        from userbot.sysutils.event_handler import EventHandler
        from userbot.sysutils.sys_funcs import requiredVersion

        ehandler = EventHandler()

        @ehandler.on(command="example", outgoing=True)
        @requiredVersion("1.1.0", "3.0.0")
        async def example(event):
             await event.edit("I'm an example function!")
             return

        @ehandler.on(command="example2", outgoing=True)
        @requiredVersion("1.2.0", "1.2.0")  # should match exactly v1.2.0
        async def example2(event):
             await event.edit("I'm an example2 function!")
             return

    Returns:
        a callable function with it's original content else
        depending on 'empty_func' a callable empty function or None
    """
    def wrapper(function):
        if empty_func:
            efunc = lambda *args, **kwargs: None
        else:
            efunc = None
        try:
            ver_tuple = tuple(map(int, VERSION.split(".")))
            min_tuple = tuple(map(int, min_ver.split(".")))
            max_tuple = tuple(map(int, max_ver.split(".")))
        except:
            return efunc
        if not min_ver <= max_ver:  # min should be lower or equal to max
            return efunc
        if ver_tuple >= min_tuple and \
           ver_tuple <= max_tuple:
            def func(**args):
                return function(**args)
            return func
        return efunc
    return wrapper

def isLinux() -> bool:
    return True if platform.system().lower() == "linux" or \
           sys.platform.startswith("linux") else False

def isMacOS() -> bool:
    return True if platform.system().lower() == "darwin" or \
           sys.platform == "darwin" else False

def isWindows() -> bool:
    return True if platform.system().lower() == "windows" or \
           os.name == "nt" or sys.platform.startswith("win") else False

def isAndroid() -> bool:
    if not isLinux():
        return False

    try:
        android_sdk = check_output(["getprop", "ro.build.version.sdk"],
                                   universal_newlines=True).replace("\n", "")
        android_ver = check_output(["getprop", "ro.build.version.release"],
                                   universal_newlines=True).replace("\n", "")

        if android_sdk or android_ver:
            return True
    except:
        pass

    return False
