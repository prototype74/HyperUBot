# Copyright 2021-2022 nunopenim @github
# Copyright 2021-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.sys_funcs import verAsTuple
from importlib.util import find_spec
from inspect import currentframe, getouterframes
from logging import getLogger
from os.path import basename
from pkg_resources import get_distribution
from subprocess import check_call, check_output, DEVNULL
from sys import executable
import json

log = getLogger(__name__)


def checkPkgByDist(dist_name: str) -> bool:
    """
    Check if given distribution name is installed

    Args:
        dist_name (string): name of distribution

    Example:
        if checkPkgByDist("requests"):
            print("package requests installed")
        else:
            print("package requests not installed")

    Returns:
        True if distribution is installed else False
    """
    try:
        get_distribution(dist_name)
        return True
    except Exception:
        return False

def checkPkgByImport(import_name: str) -> bool:
    """
    Checks if the importable name of the distribution exists

    Args:
        import_name (string): name of importable package

    Example:
        if checkPkgByImport("requests"):
            print("package requests installed")
        else:
            print("package requests not installed")

    Returns:
        True if name is importable else False
    """
    if find_spec(import_name):
        return True
    return False


def getVersionFromDist(dist_name):
    """
    Get the version of the distribution

    Args:
        dist_name (string): name of distribution

    Example:
        version = getVersionFromDist("telethon")
        if version:
            print(f"version of package telethon is {version}")
        else:
            print("package telethon not installed")

    Returns:
        the version as string if distribution is installed else None
    """
    try:
        py_exec = (executable if " " not in executable else
                   '"' + executable + '"')
        out = check_output([py_exec, "-m", "pip", "list", "--format", "json"])
        out_json = json.loads(out)
        for elem in out_json:
            if elem.get("name").lower() == dist_name.lower():
                return elem.get("version")
    except Exception:
        log.error(f"Failed to get version of the distribution '{dist_name}'",
                  exc_info=True)
    return


def installPkg(dist_name, upgrade: bool = False) -> bool:
    """
    Installs the given name of the distribution

    Args:
        dist_name (string): name of distribution
        upgrade (bool): if the distribution should be upgraded instead.
                        This works only if the distribution is installed

    Example:
        if not checkPkgByDist("requests"):
            installPkg("requests")
        else:
            print("package requests installed already")

    Returns:
        True if installation was successful or not required
        else False if errors occurred
    """
    caller = getouterframes(currentframe(), 2)[1]
    caller = f"{basename(caller.filename)}:{caller.lineno}"
    try:
        py_exec = (executable if " " not in executable else
                   '"' + executable + '"')
        if not checkPkgByDist(dist_name):
            check_call([py_exec, "-m", "pip", "install", dist_name],
                       stdout=DEVNULL, stderr=DEVNULL)
            log.info(f"Package '{dist_name}' installed successfully "
                     f"({caller})")
        elif upgrade:
            curr_ver = verAsTuple(getVersionFromDist(dist_name))
            check_call([py_exec, "-m", "pip", "install", "--upgrade",
                        dist_name], stdout=DEVNULL, stderr=DEVNULL)
            new_ver = verAsTuple(getVersionFromDist(dist_name))
            if(curr_ver and new_ver and curr_ver == new_ver):
                log.info(f"Package '{dist_name}' is up-to-date already "
                         f"({caller})")
            else:
                # default case
                log.info(f"Package '{dist_name}' upgraded successfully "
                         f"({caller})")
        else:
            log.info(f"Package '{dist_name}' installed already ({caller})")
        return True
    except Exception as e:
        log.error(f"Failed to install package '{dist_name}' ({caller})",
                  exc_info=True)
    return False
