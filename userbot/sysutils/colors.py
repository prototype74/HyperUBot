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
    return color + text + Color.END

def setColorTextBG(text: str, colorbg: ColorBG) -> str:
    return colorbg + text + ColorBG.END
