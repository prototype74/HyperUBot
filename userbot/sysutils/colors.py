# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

class Color:
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    VIOLET ="\033[35m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    END = "\033[0m"

class ColorBG:
    BLUE = "\033[44m"
    CYAN = "\033[46m"
    GREEN = "\033[42m"
    VIOLET ="\033[45m"
    RED = "\033[41m"
    YELLOW = "\033[43m"
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
    return colorbg + text + ColorBG.END
