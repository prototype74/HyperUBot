# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.version import VERSION_TUPLE
from logging import getLogger
from subprocess import check_output
from json import loads
import platform
import os
import sys

log = getLogger(__name__)


def strlist_to_list(strlist: str) -> list:
    """
    Casting string formatted list to a real list

    Args:
        strlist (string): a string formatted list

    Example:
        mystr = "[25, 100, 'example']"
        mylist = strlist_to_list(mystr)
        for elem in mylist:
            print(elem)

    Returns:
        a real list from string
    """
    try:
        list_obj = loads(strlist)
    except Exception:
        list_obj = []
    return list_obj


def str_to_bool(strbool: str) -> bool:
    """
    Casting string formatted boolean to a real boolean

    Args:
        strbool (string): a string formatted boolean

    Example:
        mystr = "true"
        mybool = str_to_bool(mystr)
        if mybool:
            print("it's true")
        else:
            print("it's not true")

    Returns:
        a real bool from string
    """
    if strbool in ("True", "true"):
        return True
    if strbool in ("False", "false"):
        return False
    raise ValueError(f"{strbool} is not a bool")


def isLinux() -> bool:
    """
    Returns True if current machine runs with a Linux (based)
    system else False
    """
    return (True if platform.system().lower() == "linux" or
            sys.platform.startswith("linux") else False)


def isMacOS() -> bool:
    """
    Returns True if current machine runs with macOS else False
    """
    return (True if platform.system().lower() == "darwin" or
            sys.platform == "darwin" else False)


def isWindows() -> bool:
    """
    Returns True if current machine runs with Windows else False
    """
    return (True if platform.system().lower() == "windows" or
            os.name == "nt" or sys.platform.startswith("win") else False)


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
    except Exception:
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


def getDistro() -> str:
    """
    Tries to get the distro/debian name of a Linux based
    system. Returns an empty string if os-release doesn't
    exist or include the name
    """
    name = ""
    if not isLinux():
        return name

    if os.path.exists(os.path.abspath(
            os.path.join(os.sep, "etc", "os-release"))):
        rel_path = os.path.abspath(os.path.join(os.sep, "etc", "os-release"))
        try:
            with open(rel_path, "r") as release:
                for line in release.readlines():
                    if not line.startswith("#") and not line == "\n" and \
                       line.startswith("PRETTY_NAME="):
                        if line.split("=")[1]:
                            name = line.split("=")[1]
                            name = name.replace("\n", "")
                        break
            if '"' in name:
                name = name.replace('"', "")
            release.close()
        except Exception:
            return ""  # in case 'name' got modified but unfinished
    return name


def os_name() -> str:
    """
    Get and return the name of the current operating system.
    Might return an empty string if OS is unknown.
    """
    if isAndroid():
        return "Android"
    if isMacOS():
        return "macOS"
    if isWSL():
        dist_name = getDistro()
        if dist_name:
            return f"{dist_name} (WSL)"
        return "Windows Subsystem for Linux"
    if isLinux():
        dist_name = getDistro()
        if dist_name:
            return dist_name
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
    verAsTuple("15") -> (15, 0)
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
    if len(version) >= 1 and "." not in version:
        try:
            if int(version):
                # assume it's just a digit
                return tuple(map(int, f"{version}.0".split(".")))
        except ValueError:
            pass
        return ()

    try:
        # version only includes integers
        return tuple(map(int, version.split(".")))
    except ValueError:
        pass

    ver_list = version.split(".")
    new_list = []
    first_elem_int = False  # first element should be a digit

    for elem in ver_list:
        try:  # integer cases
            elem = int(elem)
            first_elem_int = True  # first element is a digit
            new_list.append(elem)
        except Exception:  # word (with integer) cases
            if not first_elem_int:
                # first element was not a digit (not well-formed)
                break
            if "-" in elem:
                temp = elem.split("-")
                for new_elem in temp:
                    try:
                        new_elem = int(new_elem)
                    except ValueError:
                        pass
                    new_list.append(new_elem)
            else:
                new_list.append(elem)
    return tuple(new_list)


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
            def efunc(*args, **kwargs):
                return
        else:
            efunc = None
        try:
            ver_tuple = VERSION_TUPLE
            min_tuple = verAsTuple(min_ver)
            max_tuple = verAsTuple(max_ver)
        except Exception:
            return efunc
        if not min_ver <= max_ver:  # min should be lower or equal to max
            return efunc
        if ver_tuple >= min_tuple and \
           ver_tuple <= max_tuple:
            return function
        return efunc
    return wrapper
