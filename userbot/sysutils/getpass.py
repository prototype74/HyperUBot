# Copyright 2021-2022 nunopenim @github
# Copyright 2021-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .sys_funcs import isWindows
import sys

if isWindows():
    import msvcrt
else:
    import termios
    import tty


def _GetwchPOSIX():
    if isWindows():
        return ""
    # based on: https://docs.python.org/3/library/termios.html#example
    fd = sys.stdin.fileno()
    prev_attr = termios.tcgetattr(fd)
    try:
        tty.setraw(fd, termios.TCSAFLUSH)
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, prev_attr)
    return char


_getwch = msvcrt.getwch if isWindows() else _GetwchPOSIX


def getpass(prompt):
    print(prompt, end="", flush=True)
    password_chars = []
    while True:
        char = _getwch()
        if ord(char) in (10, 13):
            break
        elif ord(char) in (8, 127):  # Windows: 8, POSIX: 127
            if len(password_chars) > 0:
                password_chars.pop()
                print("\b \b", end="", flush=True)
        elif ord(char) in (3,):
            raise KeyboardInterrupt
        else:
            password_chars.append(char)
            print("*", end="", flush=True)
    print()
    password = "".join(password_chars)
    return password
