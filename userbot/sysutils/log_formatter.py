# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .colors import Color, ColorBG, setColorText, setColorTextBG
from logging import Formatter, INFO, WARNING, ERROR, CRITICAL

class LogFileFormatter(Formatter):
    def format(self, logtype):
        """
        (Log file only) Register logging levels with the help of logging.Formatter
        class. Debug level is not included. This function overwrites the original
        format function from Formatter.
        """
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
        """
        (Terminal only) Register logging levels with the help of logging.Formatter
        class. Sets colors to warning (yellow), error (red) and critical (red background) levels.
        Info level remains plain text. Debug level is not included. This function overwrites the
        original format function from Formatter.
        """
        LOG_FORMAT = "[%(asctime)s] %(levelname).1s: %(name)s: %(message)s"
        LOG_COLORS = {"INFO": LOG_FORMAT,  # plain text
                      "WARNING": setColorText(LOG_FORMAT, Color.YELLOW),
                      "ERROR": setColorText(LOG_FORMAT, Color.RED),
                      "CRITICAL": setColorTextBG(LOG_FORMAT, ColorBG.RED)}
        get_type = LOG_COLORS.get(logtype.levelname)
        formatter = Formatter(get_type, "%Y-%m-%d %H:%M:%S").format(logtype)
        return formatter

