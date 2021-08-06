# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from .configuration import addConfig, getConfig
from getpass import getpass
from inspect import currentframe, getouterframes
from logging import getLogger
from pyAesCrypt import decryptFile
import os


log = getLogger(__name__)


class _ConfigLoader:
    def __init__(self):
        """
        Initialize supported configs by HyperUBot
        """
        self.__supported_configs = [os.path.join(".", "userbot", "config.env"),
                                    os.path.join(".", "userbot", "config.py")]
        self.__curr_config = None
        self.__configs_loaded = False

    def _initialize_config(self):
        """
        Set optional config. Leaves current config to None if no optional
        config has been found
        """
        caller = os.path.join("userbot", "sysutils", "config_loader.py")
        if not getouterframes(currentframe(), 2)[1].filename.endswith(caller):
            log.warning("Not a valid caller")
            return
        for c in self.__supported_configs:
            if os.path.exists(c):
                self.__curr_config = c
                break
        return

    def __config_available(self) -> bool:
        """
        Check if config is available

        Returns:
            True if path exists else False
        """
        if self.__curr_config:
            return True
        return False

    def __load_env(self, is_safemode: bool):
        """
        Loads all configurations from config.env file

        Args:
            is_safemode (bool): if HyperUBot is currently in safe mode
        """
        from userbot.include.aux_funcs import strlist_to_list, str_to_bool
        from dotenv import load_dotenv
        len_before = len(os.environ.items())
        load_dotenv(self.__curr_config)
        loaded_env = {key: value
                      for key, value in list(os.environ.items())[len_before:]}
        if not is_safemode:
            for key, value in loaded_env.items():
                if key not in ("API_KEY", "API_HASH", "STRING_SESSION"):
                    if value.startswith("[") and value.endswith("]"):
                        addConfig(key, strlist_to_list(value))
                    elif value in ("True", "true", "False", "false"):
                        addConfig(key, str_to_bool(value))
                    else:  # default case
                        addConfig(key, int(value)
                                  if value.isnumeric() else value)
        if getConfig("SAMPLE_CONFIG", None):
            log.warning("Please remove SAMPLE_CONFIG from config.env!")
        if is_safemode:
            addConfig("UBOT_LANG", loaded_env.get("UBOT_LANG", "en"))
        os.environ["API_KEY"] = "0"
        os.environ["API_HASH"] = "None"
        os.environ["STRING_SESSION"] = "None"
        self.__configs_loaded = True
        return

    def __load_py(self, is_safemode: bool):
        """
        Loads all configurations from config.py file

        Args:
            is_safemode (bool): if HyperUBot is currently in safe mode
        """
        cfg_loadable = False
        try:
            import userbot.config as cfg
            cfg_loadable = True
        except (IndentationError, NameError,
                TypeError, ValueError, SyntaxError):  # totally F
            log.warning("config.py file isn't well-formed. Please make sure "
                        "your config file matches expected python script "
                        "formation", exc_info=True)
        except Exception as e:
            log.warning(f"Unable to load configs: {e}", exc_info=True)
        try:
            if not is_safemode:
                from inspect import getmembers, isclass, isfunction
        except Exception as e:
            log.warning(f"Couldn't import config components: {e}",
                        exc_info=True)
            if cfg_loadable:
                cfg_loadable = False
        if not is_safemode and cfg_loadable:
            for name, cfgclass in getmembers(cfg, isclass):
                for attr_name in vars(cfgclass):
                    attr_val = getattr(cfgclass, attr_name)
                    if not attr_name.startswith("__") and \
                       not isfunction(attr_val):
                        if attr_name not in ("API_KEY", "API_HASH",
                                             "STRING_SESSION"):
                            addConfig(attr_name, attr_val)
        if is_safemode and cfg_loadable:
            addConfig("UBOT_LANG",
                      (cfg.ConfigClass.UBOT_LANG
                       if hasattr(cfg.ConfigClass, "UBOT_LANG") else "en"))
        try:
            del cfg
        except:
            pass
        self.__configs_loaded = True
        return

    def _load_configs(self, is_safemode: bool):
        """
        Searches for config.env and config.py (config.env preferred if both
        exist) and starts to load the target config file

        Args:
            is_safemode (bool): if HyperUBot is currently in safe mode
        """
        caller = getouterframes(currentframe(), 2)[2].filename
        valid_caller = os.path.join("userbot", "__init__.py")
        if not caller.endswith(valid_caller):
            log.warning("Not a valid caller "\
                        f"(requested by {os.path.basename(caller)}")
            return
        if not self.__config_available():
            log.info("No optional configs found")
            return
        if self.__configs_loaded:
            log.info("Optional configs loaded already")
            return
        if self.__curr_config.endswith(".env"):
            self.__load_env(is_safemode)
        elif self.__curr_config.endswith(".py"):
            self.__load_py(is_safemode)
        return


class _SecureConfigLoader:
    def __init__(self):
        """
        Initialize secure config paths
        """
        self.__secure_config = os.path.join(".", "userbot", "secure_config")
        self.__temp = os.path.join(".", "userbot", "userdata", "_temp.py")
        self.__configs_loaded = False

    def _check_secure_config(self) -> bool:
        """
        Check if secure config exists
        """
        if os.path.exists(self.__secure_config) and \
           os.path.isfile(self.__secure_config):
            return True
        return False

    def __decrypt_config(self) -> bool:
        """
        Decrypt secure config

        Returns:
            True if decryption was successful else False
        """
        password = ""
        pwd_confm = False
        attempts = 0
        while True:
            try:
                decryptFile(infile=self.__secure_config,
                            outfile=self.__temp,
                            passw=password,
                            bufferSize=(64 * 1024))
                break
            except ValueError as e:
                if "wrong password" in str(e).lower() and \
                   attempts < 5:
                    if not pwd_confm:
                        log.info("Password required for secure config")
                    else:
                        log.warning("Invalid password. Try again...")
                    try:
                        while True:
                            password = getpass("Please enter your password: ")
                            if not pwd_confm:
                                pwd_confm = True
                            break
                    except KeyboardInterrupt:
                        return False
                    attempts += 1
                else:
                    log.error("Unable to read secure config")
                    return False
            except Exception:
                log.error("Unable to read secure config")
                return False
        return True

    def _get_secure_config(self) -> tuple:
        """
        Reads the secure config and returns the sensitive data.

        Returns:
            A tuple of the sensitive data else an empty tuple
        """
        caller = getouterframes(currentframe(), 2)[2].filename
        valid_caller = os.path.join("userbot", "__init__.py")
        if not caller.endswith(valid_caller):
            log.critical("Unauthorized access to secure config blocked "\
                         f"(requested by {os.path.basename(caller)})")
            return (None, None, None)
        if self.__configs_loaded:
            log.info("Secure config loaded already")
            return (None, None, None)
        if not self._check_secure_config():
            log.error("Secure config not found")
            return (None, None, None)
        if not self.__decrypt_config():
            return (None, None, None)
        try:
            import userbot.userdata._temp as s_cfg
            api_key = s_cfg.API_KEY
            api_hash = s_cfg.API_HASH
            string_session = s_cfg.STRING_SESSION
            self.__configs_loaded = True
        except Exception:
            log.error("Unable to read secure config")
            return (None, None, None)
        finally:
            if os.path.exists(self.__temp):
                os.remove(self.__temp)
            if os.path.exists(os.path.join(".", "userbot",
                                           "userdata", "__pycache__")) and \
               os.path.isdir(os.path.join(".", "userbot",
                                          "userdata", "__pycache__")):
                for name in os.listdir(
                     os.path.join(".", "userbot", "userdata", "__pycache__")):
                    if name.startswith("_temp.cpython-") and \
                       name.endswith(".pyc"):
                        os.remove(
                            os.path.join(".", "userbot", "userdata",
                                         "__pycache__", name))
                        break
        del s_cfg
        return (api_key, api_hash, string_session)


_cfg_loader = _ConfigLoader()
_scfg_loader = _SecureConfigLoader()
_cfg_loader._initialize_config()


def check_secure_config() -> bool:
    """
    Check if secure config exists
    """
    return _scfg_loader._check_secure_config()


def get_secure_config() -> tuple:
    """
    Reads the secure config and returns the sensitive data.

    Returns:
        A tuple of the sensitive data else an empty tuple
    """
    return _scfg_loader._get_secure_config()


def load_configs(is_safemode: bool):
    """
    Searches for config.env and config.py (config.env preferred if both
    exist) and starts to load the target config file

    Args:
        is_safemode (bool): if HyperUBot is currently in safe mode
    """
    _cfg_loader._load_configs(is_safemode)
    return
