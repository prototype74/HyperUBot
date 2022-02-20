# Copyright 2021-2022 nunopenim @github
# Copyright 2021-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .sys_funcs import isWindows, strlist_to_list
from userbot._core.access_controller import _protectedAccess
from configparser import ConfigParser
from inspect import currentframe, getouterframes
from logging import getLogger
import os
import sys

log = getLogger(__name__)


class Properties:
    def __init__(self, name: str):
        """
        Initializes the properties from given filename. Name should be a
        string. Illegal characters in filenames are not allowed.

        Args:
            name (str): filename
        """
        if not isinstance(name, str):
            raise TypeError("Name should be a string and not "
                            f"'{type(name).__name__}'")
        for char in list(name):
            if char in ("/", "\\", "\r", "\n", "\t", "<", ">", ":", "?",
                        "*", "\"", "|"):
                raise ValueError("Name contains illegal characters")
        if name.lower() == "sysprops":
            raise ValueError("Name used by core already")
        self.__parser = ConfigParser()
        self.__filename = name.replace(" ", "_")
        self.__path = os.path.join(".", "userbot", "userdata",
                                   f"{self.__filename}.ini")
        self.__sections = []
        self.__prop_present = False

    def __create_props(self, caller, sections=None):
        """
        Apparently creates a prop file :)
        """
        self.__parser["DEFAULT"] = {"source": caller.replace(os.getcwd(), ".")}
        if sections and isinstance(sections, (list, tuple)):
            for section in sections:
                if section and isinstance(section, str):
                    section = section.upper()
                    if not section == "DEFAULT" and \
                       section not in self.__sections:
                        self.__parser[section] = {}
                        self.__sections.append(section)
        try:
            with open(self.__path, "w") as propfile:
                self.__parser.write(propfile)
            propfile.close()
            self.__prop_present = True
        except Exception:
            log.error("Failed to create props "
                      f"(requested by {os.path.basename(caller)})",
                      exc_info=True)
        return

    def init_props(self, sections=None):
        """
        Setup the prop file and checks if the file isn't already used by a
        different program. There is always a DEFAULT section. New sections
        are addable by passing a list or tuple to 'sections' arg

        Args:
            sections (list or tuple): list of section names. Default None

        Example:
            from userbot.sysutils.properties import Properties

            props = Properties("myprops")
            props.init_props(["MySection1", "MySection2"])
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if not os.path.exists(self.__path):
            self.__create_props(caller, sections)
            return
        if os.path.exists(self.__path) and os.path.isfile(self.__path):
            self.__parser.read(self.__path)
            source = self.__parser["DEFAULT"].get("source", fallback="")
            if not source:
                log.error(f"[INIT] Re-initializing prop '{self.__path}' "
                          f"(requested by {os.path.basename(caller)})")
                self.__create_props(caller, sections)
                return
            # switch slashes if OS changed
            if "/" in source and isWindows():
                source = source.replace("/", "\\")
            elif "\\" in source and not isWindows():
                source = source.replace("\\", "/")
            if source == caller.replace(os.getcwd(), "."):
                self.__prop_present = True
            if self.__prop_present:
                props_modified = False
                # update prop file if sections differs
                if sections and isinstance(sections, (list, tuple)):
                    # load current given sections
                    for section in sections:
                        if section and isinstance(section, str):
                            section = section.upper()
                            if section not in self.__sections:
                                self.__sections.append(section)
                    # compare
                    temp_sections = self.__parser.sections()
                    for section in temp_sections:
                        if section not in self.__sections:
                            self.__parser.remove_section(section)
                            if not props_modified:
                                props_modified = True
                    temp_sections = self.__parser.sections()  # update list
                    for section in self.__sections:
                        if section not in temp_sections:
                            self.__parser[section] = {}
                            if not props_modified:
                                props_modified = True
                else:
                    # if a list of sections was given in past but now removed,
                    # all sections will be removed from file except DEFAULT too
                    temp_sections = self.__parser.sections()
                    for section in temp_sections:
                        if not section == "DEFAULT":
                            self.__parser.remove_section(section)
                            if not props_modified:
                                props_modified = True
                if props_modified:
                    try:
                        with open(self.__path, "w") as propfile:
                            self.__parser.write(propfile)
                        propfile.close()
                    except Exception:
                        log.error("[INIT] Failed to update props "
                                  f"(requested by {os.path.basename(caller)})",
                                  exc_info=True)
                        self.__prop_present = False
            else:
                log.error(f"[INIT] Prop '{self.__path}' exists but used "
                          "by a different program already "
                          f"(requested by {os.path.basename(caller)})")
        elif os.path.exists(self.__path) and os.path.isdir(self.__path):
            log.error(f"[INIT] '{self.__path}' exists as directory, not as "
                      f"file (requested by {os.path.basename(caller)})")
        else:
            log.error(f"[INIT] Prop '{self.__path}' not found "
                      f"(requested by {os.path.basename(caller)})")
        return

    def setprop(self, key: str, value, section=None) -> bool:
        """
        Add or update an (existing) key with a new value. Key will always be
        stored to DEFAULT section if no 'section' is given or doesn't exist.

        Args:
            key (str): existing/new key
            value: new value
            section (str): name of section. Default None

        Example:
            from userbot.sysutils.properties import Properties

            props = Properties("myprops")
            props.init_props(["MySection1", "MySection2"])
            props.setprop("testKey1", "testValue1")  # DEFAULT
            props.setprop("testKey2", True, "MySection1")

        Returns:
            True if action was successful else False
        """
        caller = getouterframes(currentframe(), 2)[1].filename
        if not self.__prop_present:
            return False
        self.__parser.read(self.__path)
        target_section = "DEFAULT"
        prop_set = False
        if section and isinstance(section, str):
            section = section.upper()
            if section in self.__sections:
                target_section = section
        if key.lower() == "source" and target_section == "DEFAULT":
            return False
        value = str(value)
        if value.lower() == "false":
            value = "no"
        elif value.lower() == "true":
            value = "yes"
        try:
            try:
                self.__parser[target_section][key.lower()] = value
            except KeyError:
                return False
            with open(self.__path, "w") as propfile:
                self.__parser.write(propfile)
            propfile.close()
            prop_set = True
        except Exception:
            log.error(f"[SETPROP] Failed to update prop '{self.__path}' "
                      f"(requested by {os.path.basename(caller)})",
                      exc_info=True)
        return True if prop_set else False

    def getprop(self, key: str, section=None):
        """
        Load the value from given key. getprop will always check in DEFAULT
        section if no 'section' is given or doesn't exist.

        Args:
            key (str): existing key
            section (str): name of section. Default None

        Example:
            from userbot.sysutils.properties import Properties

            props = Properties("myprops")
            props.init_props(["MySection1", "MySection2"])
            props.setprop("testKey1", "testValue1")  # DEFAULT
            props.setprop("testKey2", True, "MySection1")

            if props.getprop("testKey2", "MySection1"):
                # do stuff

        Returns:
            the value from key else None if key doesn't exist
        """
        if not self.__prop_present:
            return None
        self.__parser.read(self.__path)
        target_section = "DEFAULT"
        if section and isinstance(section, str):
            section = section.upper()
            if section in self.__sections:
                target_section = section.upper()
        try:
            value = self.__parser[target_section].get(key.lower(),
                                                      fallback=None)
        except KeyError:
            return None
        if value:
            if value.startswith("[") and value.endswith("]"):
                value = strlist_to_list(value)
            elif value.lower() == "no":
                value = False
            elif value.lower() == "yes":
                value = True
            else:
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
        return value


class _SysProperties:
    def __init__(self):
        self.__parser = ConfigParser()
        self.__path = os.path.join(".", "userbot", "userdata", "sysprops.ini")
        self.__prop_present = False

    def __create_props(self):
        """
        Creates the system properties with default keys and values
        """
        self.__parser["DEFAULT"] = {"source": "HyperUBot"}
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
            else:
                try:  # integer
                    value = int(value)
                except ValueError:
                    try:  # float
                        value = float(value)
                    except ValueError:
                        pass
        return value


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=["_SysProperties"],
    warn_msg="SysProp reserved for core service only (requested by {1}:{2})",
    mlogger=log
)
