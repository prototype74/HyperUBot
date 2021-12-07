# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from glob import glob
from inspect import currentframe, getouterframes
from logging import getLogger
import os
import json

log = getLogger(__name__)


class _PackageManagerJSON:
    def __init__(self):
        self.__filename = os.path.join(".", "userbot", "userdata",
                                       "package_lists.json")
        self.__init_failed = False

    def _init_json(self, force_init: bool = False):
        special_caller = [os.path.join("userbot", "modules",
                                       "_package_manager.py"),
                          os.path.join("userbot", "sysutils",
                                       "package_manager.py")]
        sys_caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = False
        for caller in special_caller:
            if sys_caller.endswith(caller):
                valid_caller = True
                break
        if not valid_caller:
            log.warning("Not a valid caller "
                        f"(requested by {os.path.basename(caller)})")
            return
        if os.path.exists(self.__filename) and \
           os.path.isfile(self.__filename) and \
           not force_init:
            return
        try:
            with open(self.__filename, "w") as js:
                json.dump({"last_updated": None, "repos": [],
                           "module_sources": []},
                          js, indent=4)
            js.close()
        except Exception:
            log.error("Failed to initialize JSON", exc_info=True)
            if not self.__init_failed:
                self.__init_failed = True
        return

    def _read_json(self):
        caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = os.path.join("userbot", "modules",
                                    "_package_manager.py")
        if not caller.endswith(valid_caller):
            log.warning("Not a valid caller "
                        f"(requested by {os.path.basename(caller)})")
            return
        data = {}
        reread = False
        try:
            with open(self.__filename, "r") as js:
                try:
                    data = json.load(js)
                except Exception:
                    log.error("JSON file is invalid. Resetting...")
                    if not self.__init_failed:
                        self._init_json(True)
                        reread = True
            js.close()
            if not reread:
                return data
        except FileNotFoundError:
            if not self.__init_failed:
                log.error("JSON file not found. Initializing data...",
                          exc_info=True)
                self._init_json(True)
                reread = True
            else:
                log.error("JSON file not found", exc_info=True)
        except Exception:
            log.error("Failed to read JSON", exc_info=True)
        if reread:
            with open(self.__filename, "r") as js:
                try:
                    data = json.load(js)
                except Exception:
                    pass
            js.close()
            return data
        return {}

    def _save_json(self, new_data: dict):
        special_caller = [os.path.join("userbot", "modules",
                                       "_package_manager.py"),
                          os.path.join("userbot", "sysutils",
                                       "package_manager.py")]
        sys_caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = False
        for caller in special_caller:
            if sys_caller.endswith(caller):
                valid_caller = True
                break
        if not valid_caller:
            log.warning("Not a valid caller "
                        f"(requested by {os.path.basename(caller)})")
            return
        try:
            if not self.__init_failed:
                with open(self.__filename, "w") as js:
                    json.dump(new_data, js, indent=4)
                js.close()
            else:
                log.warning("Unable to save JSON as previous "
                            "initialization failed")
        except Exception as e:
            log.error("Failed to write JSON", exc_info=True)
        return

    def _check_packages(self, json_data: dict) -> dict:
        caller = getouterframes(currentframe(), 2)[1].filename
        valid_caller = os.path.join("userbot", "modules",
                                    "_package_manager.py")
        if not caller.endswith(valid_caller):
            log.warning("Not a valid caller "
                        f"(requested by {os.path.basename(caller)})")
            return json_data
        if not json_data:
            return json_data
        pkg_list = json_data
        module_sources = pkg_list.get("module_sources", [])
        user_module_list = []
        user_module_path = sorted(
            glob(os.path.join(".", "userbot", "modules_user", "*.py")))
        for module in user_module_path:
            if os.path.isfile(module) and \
               not os.path.basename(module).startswith("__") and \
               module.endswith(".py"):
                filename = os.path.basename(module)[:-3]
                user_module_list.append(filename)
        list_modified = False
        # check if modules are still installed
        indexes_to_remove = []  # mark the index to remove the target element
        for i, mod_source in enumerate(module_sources):
            mod_name = mod_source.get("name", "")
            if mod_name:
                if mod_name not in user_module_list:
                    indexes_to_remove.append(i)
        if indexes_to_remove:
            indexes_to_remove.reverse()
            for index in indexes_to_remove:
                module_sources.pop(index)
                if not list_modified:
                    list_modified = True
        # check if new modules are installed
        for module in user_module_list:
            for mod_source in module_sources:
                mod_name = mod_source.get("name", "")
                if module == mod_name:
                    break
            else:
                # new module installed but from unknown source
                module_sources.append({"name": module,
                                       "author": "Unknown",
                                       "repo": "Unknown",
                                       "version": "Unknown",
                                       "size": 0})
                if not list_modified:
                    list_modified = True
        if list_modified:
            # update list
            pkg_list["module_sources"] = module_sources
            self._save_json(pkg_list)
        return pkg_list
