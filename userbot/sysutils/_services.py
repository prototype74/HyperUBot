# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .colors import Color, setColorText
from .sys_funcs import isWindows, os_name
from inspect import currentframe, getouterframes
from logging import getLogger, shutdown
from sys import executable
import os

log = getLogger(__name__)


class _SysServices:
    def __init__(self, hyper_logger):
        """
        Initialize system services with HyperUBot's logger
        """
        self.__hyper_logger = hyper_logger

    def __shutdown_logging(self):
        """
        Shutdown HyperUBot's logger
        """
        try:
            self.__hyper_logger._stop_logging()
            shutdown()
        except:
            pass
        return

    def __exec(self, commands: list):
        """
        Execute a python program from given list of commands

        Args:
            commands (list): given list of commands
        """
        caller = getouterframes(currentframe(), 2)[2].filename
        if not commands:
            log.warning("[EXEC] empty commands "
                        f"(requested by {os.path.basename(caller)})")
            return
        if isWindows():
            log.error(f"[EXEC] unsupported OS ({os_name()}) "
                      f"(requested by {os.path.basename(caller)})")
            return
        py_exec = (executable
                   if " " not in executable else '"' + executable + '"')
        tcmd = [py_exec]
        for cmd in commands:
            tcmd.append(cmd)
        cmds = " ".join(tcmd)
        self.__shutdown_logging()
        print()
        os.execle(py_exec, *tcmd, os.environ)
        return

    def _reboot(self, safemode: bool = False):
        """
        Reboot HyperUBot

        Args:
            safemode (bool): boot into safemode if True
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if os.path.dirname(caller).endswith(os.path.join("userbot",
                                                         "modules_user")):
            log.warning("User modules are not allowed to access services "
                        f"(requested by {os.path.basename(caller)})")
            return
        if safemode:
            log.info("[REBOOT] Rebooting HyperUBot into safemode...")
            self.__exec(["-m", "userbot", "-safemode"])
        else:
            log.info("[REBOOT] Rebooting HyperUBot...")
            self.__exec(["-m", "userbot"])
        return

    def _reboot_recovery(self, auto_update: bool, commit_id = None):
        """
        Reboot HyperUBot into recovery system

        Args:
            auto_update (bool): if auto updater should be started
            commit_id: commit id from release (default None). Should be
                       given if auto_update is set to True
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if os.path.dirname(caller).endswith(os.path.join("userbot",
                                                         "modules_user")):
            log.warning("User modules are not allowed to access services "
                        f"(requested by {os.path.basename(caller)})")
            return
        if auto_update:
            if not commit_id:
                log.warning("[REBOOT RECOVERY] Commit ID is missing "
                            f"(requested by {os.path.basename(caller)})")
                return
            log.info("[REBOOT RECOVERY] Starting auto update into recovery...")
            self.__exec(["recovery.py", "-autoupdate", commit_id])
            return
        log.info("[REBOOT RECOVERY] Starting recovery...")
        self.__exec(["recovery.py"])
        return

    def _start_setup_assistant(self):
        """
        Starts HyperUBot's Setup Assistant
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if os.path.dirname(caller).endswith(os.path.join("userbot",
                                                         "modules_user")):
            log.warning("User modules are not allowed to access services "
                        f"(requested by {os.path.basename(caller)})")
            return
        log.info("Starting setup assistant...")
        self.__exec(["setup.py"])
        return

    def _start_scfg_updater(self):
        """
        Starts HyperUBot's Secure Config Updater
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if os.path.dirname(caller).endswith(os.path.join("userbot",
                                                         "modules_user")):
            log.warning("User modules are not allowed to access services "
                        f"(requested by {os.path.basename(caller)})")
            return
        log.info("Starting secure config updater...")
        self.__exec(["update_secure_cfg.py"])
        return

    def _start_session_gen(self):
        """
        Starts HyperUBot's String Session Generator
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if os.path.dirname(caller).endswith(os.path.join("userbot",
                                                         "modules_user")):
            log.warning("User modules are not allowed to access services "
                        f"(requested by {os.path.basename(caller)})")
            return
        log.info("Starting string session generator...")
        self.__exec(["generate_session.py"])
        return

    def _suggest_options(self, options: list) -> int:
        """
        Creates an option table from list of 'options'.
        Prompts the user to select an option. The option table will always
        start at 1.
        Main idea is to create a suggestion table at init of HyperUBot
        to guide the user to fix a certain issue.

        Args:
            options (list): list of available options

        Returns:
            the selected option as integer else always 0.
            Consider 0 as error.
        """
        if not options:
            return 0
        temp_list = []
        text = "Suggestions:\n"
        for i, item in enumerate(options, start=1):
            if isWindows():
                text += f"- {item}\n"
            else:
                temp_list.append(str(i))
                text += f"[{i}] {item}\n"
        print()
        print(text)
        if not isWindows():
            options_size = len(temp_list)
            while True:
                inp = input(f"Your input [1-{options_size}]: ")
                for i in temp_list:
                    if inp == i:
                        return int(i)
                else:
                    print(setColorText("Invalid input. Try again...",
                                       Color.YELLOW))
        return 0
