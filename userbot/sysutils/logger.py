# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .colors import Color, ColorBG, setColorText, setColorTextBG
from .sys_funcs import os_name
from userbot.version import VERSION
from inspect import currentframe, getouterframes
from platform import platform, machine, processor
import logging
import os


class LogFileFormatter(logging.Formatter):
    def format(self, logtype):
        """
        (Log file only) Register logging levels with the help of
        logging.Formatter class. Debug level is not included.
        This function overwrites the original format function from Formatter.
        """
        LOG_FORMAT = ("[%(asctime)s] %(process)d %(levelname).1s: "
                      "%(name)s: %(funcName)s: %(message)s "
                      "[%(filename)s:%(lineno)d]")
        LOG_LEVELS = {"INFO": LOG_FORMAT,
                      "WARNING": LOG_FORMAT,
                      "ERROR": LOG_FORMAT,
                      "CRITICAL": LOG_FORMAT}
        get_type = LOG_LEVELS.get(logtype.levelname)  # get current level
        formatter = logging.Formatter(get_type,
                                      "%Y-%m-%d %H:%M:%S").format(logtype)
        return formatter


class LogColorFormatter(logging.Formatter):
    def format(self, logtype):
        """
        (Terminal only) Register logging levels with the help of
        logging.Formatter class. Sets colors to warning (yellow),
        error (red) and critical (red background) levels. Info level
        remains plain text. Debug level is not included. This function
        overwrites the original format function from Formatter.
        """
        LOG_FORMAT = "[%(asctime)s] %(levelname).1s: %(name)s: %(message)s"
        LOG_COLORS = {"INFO": LOG_FORMAT,  # plain text
                      "WARNING": setColorText(LOG_FORMAT, Color.YELLOW),
                      "ERROR": setColorText(LOG_FORMAT, Color.RED),
                      "CRITICAL": setColorTextBG(LOG_FORMAT, ColorBG.RED)}
        get_type = LOG_COLORS.get(logtype.levelname)
        formatter = logging.Formatter(get_type,
                                      "%Y-%m-%d %H:%M:%S").format(logtype)
        return formatter


class _UserbotLogger:
    def __init__(self, logger):
        self.__logfile = "hyper.log"
        self.__log = logger
        self.__fhandler = None
        self.__shandler = None

    def _setup_logger(self):
        caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = os.path.join("userbot", "__init__.py")
        if not caller.endswith(valid_caller):
            return
        self.__fhandler = logging.FileHandler(self.__logfile)
        self.__fhandler.setFormatter(LogFileFormatter())
        self.__shandler = logging.StreamHandler()
        self.__shandler.setFormatter(LogColorFormatter())
        logging.basicConfig(handlers=[self.__fhandler, self.__shandler],
                           level=logging.INFO)
        return

    def _initialize_logfile(self, project_name: str, is_safemode: bool,
                            python_version, telethon_version):
        caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = os.path.join("userbot", "__init__.py")
        if not caller.endswith(valid_caller):
            log.warning("Not a valid caller "\
                        f"(requested by {os.path.basename(caller)}")
            return
        try:
            if os.path.exists(self.__logfile):
                os.remove(self.__logfile)
        except:
            pass
        try:
            sys_string = "======= SYS INFO\n\n"
            sys_string += "Project: {}\n".format(project_name)
            sys_string += "Version: {}\n".format(VERSION)
            sys_string += "Safe mode: {}\n".format("On"
                                                   if is_safemode else "Off")
            sys_string += "Operating System: {}\n".format(os_name())
            sys_string += "Platform: {}\n".format(platform())
            sys_string += "Machine: {}\n".format(machine())
            sys_string += "Processor: {}\n".format(processor())
            sys_string += "Python: v{}.{}.{}\n".format(python_version.major,
                                                       python_version.minor,
                                                       python_version.micro)
            sys_string += "Telethon: v{}\n\n".format(
                telethon_version.__version__)
            sys_string += "======= TERMINAL LOGGING\n\n"
            with open(self.__logfile, "w") as file:
                file.write(sys_string)
            file.close()
        except Exception as e:
            self.__log.warning("Unable to write system information "
                               "into log: {}".format(e))
        return

    def _stop_logging(self):
        caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = os.path.join("userbot", "__main__.py")
        if not caller.endswith(valid_caller):
            self.__log.warning("Not a valid caller "\
                               f"(requested by {os.path.basename(caller)}")
            return
        if self.__fhandler:
            self.__fhandler.close()
        if self.__shandler:
            self.__shandler.close()
        return
