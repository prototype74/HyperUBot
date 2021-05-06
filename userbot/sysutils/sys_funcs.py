# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

import platform
import os
import sys

def isLinux() -> bool:
    return True if platform.system().lower() == "linux" or \
           sys.platform.startswith("linux") else False

def isMacOS() -> bool:
    return True if platform.system().lower() == "darwin" or \
           sys.platform == "darwin" else False

def isWindows() -> bool:
    return True if platform.system().lower() == "windows" or \
           os.name == "nt" or sys.platform.startswith("win") else False
