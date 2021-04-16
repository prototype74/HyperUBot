# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from platform import system

_WIN_COLOR_ENABLED = False

try:
    if system().lower().startswith("win"):
        import colorama
        colorama.init()
        _WIN_COLOR_ENABLED = True
except:
    pass

class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA ="\033[95m"
    CYAN = "\033[96m"
    RED_DARK = "\033[31m"
    GREEN_DARK = "\033[32m"
    YELLOW_DARK = "\033[33m"
    BLUE_DARK = "\033[34m"
    MAGENTA_DARK = "\033[35m"
    CYAN_DARK = "\033[36m"
    END = "\033[0m"

class ColorBG:
    RED = "\033[101m"
    GREEN = "\033[102m"
    YELLOW = "\033[103m"
    BLUE = "\033[104m"
    MAGENTA ="\033[105m"
    CYAN = "\033[106m"
    RED_DARK = "\033[41m"
    GREEN_DARK = "\033[42m"
    YELLOW_DARK = "\033[43m"
    BLUE_DARK = "\033[44m"
    MAGENTA_DARK = "\033[45m"
    CYAN_DARK = "\033[46m"
    END = "\033[0m"

def setColorText(text: str, color: Color) -> str:
    """
    (Terminal only) Wrap the given string with a color

    Args:
        text (str): text to color
        color (Color): color type from class Color

    Example:
        setColorText("Hello", Color.BLUE)

    Returns:
        Given string with wrapped color
    """
    if system().lower().startswith("win") and not _WIN_COLOR_ENABLED:
        return text
    return color + text + Color.END

def setColorTextBG(text: str, colorbg: ColorBG) -> str:
    """
    (Terminal only) Wrap the given string with a background color

    Args:
        text (str): text to color
        colorbg (ColorBG): color type from class ColorBG

    Example:
        setColorTextBG("Hello", ColorBG.BLUE)

    Returns:
        Given string with wrapped background color
    """
    if system().lower().startswith("win") and not _WIN_COLOR_ENABLED:
        return text
    return colorbg + text + ColorBG.END
