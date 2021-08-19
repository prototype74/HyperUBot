# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .sys_funcs import strlist_to_list
from configparser import ConfigParser
from inspect import currentframe, getouterframes
from logging import getLogger
import os

log = getLogger(__name__)


class _SysProperties:
    def __init__(self):
        self.__parser = ConfigParser()
        self.__path = os.path.join(".", "userbot", "userdata", "sysprops.ini")
        self.__prop_present = False

    def __create_props(self):
        """
        Creates the system properties with default keys and values
        """
        self.__parser["SYSTEM"] = {}
        try:
            with open(self.__path, "w") as propfile:
                self.__parser.write(propfile)
            propfile.close()
            self.__prop_present = True
        except Exception:
            log.error("Failed to create sysprops", exc_info=True)
        return

    def _init_props(self):
        """
        Initializes the sysprops file and check if the required section is
        present. Resets the file if it's missing. Only __init__ can run
        this function.
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = os.path.join("userbot", "__init__.py")
        if not caller.endswith(valid_caller):
            log.warning("Not a valid caller "
                        f"(requested by {os.path.basename(caller)})")
            return
        if os.path.exists(self.__path) and os.path.isfile(self.__path):
            self.__parser.read(self.__path)
            sections = self.__parser.sections()
            if "SYSTEM" in sections:
                self.__prop_present = True
                return
            # section not found
            log.warning("Resetting system properties")
        self.__create_props()
        return

    def _setprop(self, key: str, value) -> bool:
        """
        Creates or sets a (new) value to given key. Regardless which datatype
        value has, it will always be stored as a string.

        Returns:
            True if action was successful else False
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if os.path.dirname(caller).endswith(os.path.join("userbot",
                                                         "modules_user")):
            log.warning("User modules are not allowed to access sysprops "
                        f"(requested by {os.path.basename(caller)})")
            return False
        if not self.__prop_present:
            log.warning("System properties not found "
                        f"(requested by {os.path.basename(caller)})")
            return False
        prop_set = False
        section_found = False
        self.__parser.read(self.__path)
        for section in self.__parser.sections():
            if section == "SYSTEM":
                section_found = True
                value = str(value)
                if value.lower() == "false":
                    value = "no"
                elif value.lower() == "true":
                    value = "yes"
                try:
                    self.__parser["SYSTEM"][key.lower()] = value
                    with open(self.__path, "w") as propfile:
                        self.__parser.write(propfile)
                    propfile.close()
                    prop_set = True
                except Exception:
                    log.error("Failed to update sysprops "
                              f"(requested by {os.path.basename(caller)})",
                              exc_info=True)
                break
        if not section_found:
            log.warning(f"prop '{key}' not set as system properties "
                        "file may be corrupted (requested by "
                        f"{os.path.basename(caller)})")
        return True if prop_set else False

    def _getprop(self, key: str):
        """
        Get the value from given key. Auto cast the value to proper
        Python datatype (if supported) else always as string.

        Returns:
            the value from key else None if key doesn't exist
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if os.path.dirname(caller).endswith(os.path.join("userbot",
                                                         "modules_user")):
            log.warning("User modules are not allowed to access sysprops "
                        f"(requested by {os.path.basename(caller)})")
            return None
        if not self.__prop_present:
            log.warning("System properties not found "
                        f"(requested by {os.path.basename(caller)})")
            return None
        self.__parser.read(self.__path)
        value = None
        for section in self.__parser.sections():
            if section == "SYSTEM":
                section_found = True
                value = self.__parser["SYSTEM"].get(key.lower())
                break
        if value:
            # cast to proper datatype
            if value.startswith("[") and value.endswith("]"):
                value = strlist_to_list(value)  # list
            elif value.lower() == "no":
                value = False  # bool
            elif value.lower() == "yes":
                value = True  # bool
            elif value.isnumeric():
                value = int(value)  # integer
        return value
