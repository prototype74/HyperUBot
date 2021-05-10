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

def isLinux() -> bool:
    """
    Returns True if current machine runs with a Linux (based)
    system else False
    """
    return True if platform.system().lower() == "linux" or \
           sys.platform.startswith("linux") else False

def isMacOS() -> bool:
    """
    Returns True if current machine runs with macOS else False
    """
    return True if platform.system().lower() == "darwin" or \
           sys.platform == "darwin" else False

def isWindows() -> bool:
    """
    Returns True if current machine runs with Windows else False
    """
    return True if platform.system().lower() == "windows" or \
           os.name == "nt" or sys.platform.startswith("win") else False

def isAndroid() -> bool:
    """
    Returns True if current machine runs with an Android system
    else False
    """
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

def isWSL() -> bool:
    """
    Returns True if HyperUBot runs on WSL (2) which is a
    subfeature of Windows 10 else False
    """
    if not isLinux():
        return False
    if "microsoft" in platform.release().lower() and \
       os.path.exists("/mnt/c/Windows"):
        return True
    return False

def os_name() -> str:
    """
    Get and return the name of the current operating system.
    Might return an empty string if OS is unknown.
    """
    if isAndroid():
        return "Android"
    elif isMacOS():
        return "macOS"
    elif isWSL():
        return "Windows Subsystem for Linux"
    return platform.system()  # default case

def verAsTuple(version: str) -> tuple:
    """
    Converts a version string to a version tuple.
    String should be 'well-formed' e.g. '1.2.3' or
    '1.2.3-beta'.
    Useful to compare 2 different (or equal) versions
    for a possible case (e.g. limit a feature to a
    minimum required version)

    INPUT -> OUTPUT:
    verAsTuple("1.2.3") -> (1, 2, 3)
    verAsTuple("1.2.3-beta") -> (1, 2, 3, 'beta')
    verAsTuple("1.0") -> (1, 0)
    verAsTuple("1") -> (1, 0)
    verAsTuple("v1.0") -> () !!

    Args:
        version (string): a 'well-formed' version as string

    Examples:
        from userbot.sysutils.sys_funcs import verAsTuple

        MY_VERSION = "2.5"

        def example():
            if verAsTuple(MY_VERSION) >= (2, 5):
                import xyz_module as my_module
            else:
                import xyz_module_old as my_module
            return my_module.example_func()

    Returns:
        version as tuple if string is well-formed else an empty tuple
    """
    if not version:
        return ()
    if not isinstance(version, str):
        return ()

    # dot is the delimiter and it is required
    # return an empty tuple if version doesn't
    # include any dots (not well-formed)
    if len(version) > 1 and not "." in version:
        return ()

    try:
        if len(version) == 1 and int(version):
            # assume it's just a digit
            return tuple(map(int, f"{version}.0".split(".")))
    except:
        pass

    try:
        # version only includes integers
        return tuple(map(int, version.split(".")))
    except:
        pass

    ver_list = version.split(".")
    new_list = []
    first_elem_int = False  # first element should be a digit

    for elem in ver_list:
        try:  # integer cases
            elem = int(elem)
            first_elem_int = True  # first element is a digit
            new_list.append(elem)
        except:  # word (with integer) cases
            if not first_elem_int:
                # first element was not a digit (not well-formed)
                break
            if "-" in elem:
                temp = elem.split("-")
                for new_elem in temp:
                    try:
                        new_elem = int(new_elem)
                    except:
                        pass
                    new_list.append(new_elem)
            else:
                new_list.append(elem)
    return tuple(new_list)

def botVerAsTuple() -> tuple:
    """
    Returns the version of HyperUBot as tuple
    """
    return verAsTuple(VERSION)

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
            def func(*args, **kwargs):
                return function(*args, **kwargs)
            return func
        return efunc
    return wrapper
