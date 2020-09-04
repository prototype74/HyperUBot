# Misc
from logging import Formatter, INFO, WARNING, ERROR, CRITICAL

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

class LogColorFormatter(Formatter):
    def format(self, logtype):
        logging = "[%(asctime)s] %(levelname).1s: %(name)s: %(message)s"
        LOG_COLORS = {"INFO": logging,  # plain text
                      "WARNING": Color.YELLOW + logging + Color.END,
                      "ERROR": Color.RED + logging + Color.END,
                      "CRITICAL": ColorBG.RED + logging + ColorBG.END}
        get_type = LOG_COLORS.get(logtype.levelname)  # get current level
        formatter = Formatter(get_type, "%Y-%m-%d %H:%M:%S").format(logtype)
        return formatter
