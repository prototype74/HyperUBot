# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from importlib.util import find_spec
from inspect import currentframe, getouterframes
from logging import getLogger
from os.path import basename
from pkg_resources import get_distribution
from subprocess import check_call, DEVNULL
from sys import executable

log = getLogger(__name__)


def checkPkgByDist(dist_name: str) -> bool:
    """
    Check if given distribution name is installed

    Args:
        dist_name (string): name of distribution

    Example:
        if checkPkgByDist("requests"):
            print("package request installed")
        else:
            print("package request not installed")

    Returns:
        True if distribution is installed else False
    """
    try:
        get_distribution(dist_name)
        return True
    except:
        pass
    return False


def checkPkgByImport(import_name: str) -> bool:
    """
    Checks if the importable name of the distribution exists

    Args:
        import_name (string): name of importable package

    Example:
        if checkPkgByImport("requests"):
            print("package request installed")
        else:
            print("package request not installed")

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
        ver = get_distribution(dist_name)
        ver = str(ver).split()[1]
        return ver
    except:
        pass
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
            print("package request installed already")

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
            check_call([py_exec, "-m", "pip", "install", "--upgrade",
                        dist_name], stdout=DEVNULL, stderr=DEVNULL)
            log.info(f"Package '{dist_name}' upgraded successfully ({caller})")
        else:
            log.info(f"Package '{dist_name}' installed already ({caller})")
        return True
    except Exception as e:
        log.error(f"Failed to install package '{dist_name}' ({caller})",
                  exc_info=True)
    return False
