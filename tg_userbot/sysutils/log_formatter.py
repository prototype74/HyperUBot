# tguserbot stuff
from .colors import Color, ColorBG

# Misc
from logging import Formatter, INFO, WARNING, ERROR, CRITICAL


class LogFileFormatter(Formatter):
    def format(self, logtype):
        LOG_FORMAT = "[%(asctime)s] %(process)d %(levelname).1s: %(name)s: %(funcName)s: %(message)s [%(filename)s:%(lineno)d]"
        LOG_LEVELS = {"INFO": LOG_FORMAT,
                      "WARNING": LOG_FORMAT,
                      "ERROR": LOG_FORMAT,
                      "CRITICAL": LOG_FORMAT}
        get_type = LOG_LEVELS.get(logtype.levelname)  # get current level
        formatter = Formatter(get_type, "%Y-%m-%d %H:%M:%S").format(logtype)
        return formatter

class LogColorFormatter(Formatter):
    def format(self, logtype):
        LOG_FORMAT = "[%(asctime)s] %(levelname).1s: %(name)s: %(message)s"
        LOG_COLORS = {"INFO": LOG_FORMAT,  # plain text
                      "WARNING": Color.YELLOW + LOG_FORMAT + Color.END,
                      "ERROR": Color.RED + LOG_FORMAT + Color.END,
                      "CRITICAL": ColorBG.RED + LOG_FORMAT + ColorBG.END}
        get_type = LOG_COLORS.get(logtype.levelname)
        formatter = Formatter(get_type, "%Y-%m-%d %H:%M:%S").format(logtype)
        return formatter

