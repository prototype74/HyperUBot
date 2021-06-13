# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .registration import getRegisteredCMDs
from inspect import currentframe, getouterframes
from logging import getLogger
import os
import json

log = getLogger(__name__)


class _FeatureManager:
    def __init__(self):
        self.__filename = os.path.join(".", "userbot", ".dsbld_features.json")
        self.__disabled_features = {}
        self.__init_failed = False

    def __init_json(self):
        try:
            with open(self.__filename, "w") as js:
                json.dump({}, js)
            js.close()
        except Exception:
            log.error("Failed to initialize JSON", exc_info=True)
            if not self.__init_failed:
                self.__init_failed = True
        return

    def __check_json(self):
        if not os.path.exists(self.__filename) and \
           not os.path.isfile(self.__filename):
            self.__init_json()
        return

    def _read_json(self):
        caller = os.path.join("userbot", "sysutils", "feature_manager.py")
        if not getouterframes(currentframe(), 2)[1].filename.endswith(caller):
            log.warning("Not a valid caller")
            return
        self.__check_json()
        try:
            with open(self.__filename, "r") as js:
                try:
                    self.__disabled_features = json.load(js)
                except:
                    log.error("JSON file is invalid. Resetting...")
                    if not self.__init_failed:
                        self.__init_json()
                    self.__disabled_features = {}
            js.close()
        except Exception:
            log.error("Failed to read JSON", exc_info=True)
            self.__disabled_features = {}
        return

    def __save_json(self):
        try:
            if not self.__init_failed:
                with open(self.__filename, "w") as js:
                    json.dump(self.__disabled_features, js,
                              sort_keys=True, indent=4)
                js.close()
            else:
                log.warning("Unable to save JSON as previous "
                            "initialization failed")
        except Exception as e:
            log.error("Failed to write JSON", exc_info=True)
        return

    def _disable_feature(self, feature) -> bool:
        caller = os.path.join("userbot", "modules", "_feature_manager.py")
        if not getouterframes(currentframe(), 2)[2].filename.endswith(caller):
            log.warning("Not a valid caller")
            return False
        if feature in ("enable", "disable"):
            return False
        for key, val in self.__disabled_features.items():
            if feature == key or (val and feature == val):
                return False
        for key, val in getRegisteredCMDs().items():
            if feature == key or (val.get("alt_cmd") and
                                  feature == val.get("alt_cmd")):
                self.__disabled_features[key] = val.get("alt_cmd")
                self.__save_json()
                return True
        return False

    def _enable_feature(self, feature) -> bool:
        caller = os.path.join("userbot", "modules", "_feature_manager.py")
        if not getouterframes(currentframe(), 2)[2].filename.endswith(caller):
            log.warning("Not a valid caller")
            return False
        if feature in ("enable", "disable"):
            return False
        for key, val in self.__disabled_features.items():
            if feature == key or (val and feature == val):
                self.__disabled_features.pop(key, None)
                self.__save_json()
                return True
        return False

    def _is_active(self, feature) -> bool:
        if feature in ("enable", "disable"):
            return True
        for key, val in self.__disabled_features.items():
            if feature == key or (val and feature == val):
                return False
        return True


_featureMgr = _FeatureManager()
_featureMgr._read_json()  # initialize json


def _disable_feature(feature) -> bool:
    return _featureMgr._disable_feature(feature)


def _enable_feature(feature) -> bool:
    return _featureMgr._enable_feature(feature)


def _is_active(feature) -> bool:
    return _featureMgr._is_active(feature)
