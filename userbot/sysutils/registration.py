# Copyright 2021-2023 nunopenim @github
# Copyright 2021-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot._core.access_controller import _protectedAccess
from inspect import getfile, currentframe, getouterframes
from logging import getLogger
from os.path import basename, join
import sys

log = getLogger(__name__)


class _RegisterModules:
    def __init__(self):
        self.__all_modules = []
        self.__built_in_modules = []
        self.__load_modules = {}
        self.__user_modules = []
        self.__module_desc = {}
        self.__module_info = {}
        self.__handlers = {}

    def _update_all_modules(self, name_of_module: str, remove: bool = False):
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return
        if remove:
            if name_of_module in self.__all_modules:
                self.__all_modules.remove(name_of_module)
        else:
            if name_of_module not in self.__all_modules:
                self.__all_modules.append(name_of_module)
        return

    def _update_built_in_modules(self, name_of_module: str,
                                 remove: bool = False):
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return
        if remove:
            if name_of_module in self.__built_in_modules:
                self.__built_in_modules.remove(name_of_module)
        else:
            if name_of_module not in self.__built_in_modules:
                self.__built_in_modules.append(name_of_module)
        return

    def _update_load_modules(self, name_of_module: str,
                             is_running: bool, remove: bool = False):
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return
        if remove:
            if name_of_module in self.__load_modules:
                try:
                    self.__load_modules.pop(name_of_module)
                except KeyError:
                    pass
        else:
            if name_of_module not in self.__load_modules:
                self.__load_modules[name_of_module] = is_running
        return

    def _update_handlers(self, name_of_module: str,
                         handler, remove: bool = False):
        special_caller = [join("userbot", "_core", "module_loader.py"),
                          join("userbot", "sysutils", "event_handler.py")]
        sys_caller = getouterframes(currentframe(), 2)[2].filename
        valid_caller = False
        for caller in special_caller:
            if sys_caller.endswith(caller):
                valid_caller = True
                break
        if not valid_caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
        if remove:
            if name_of_module in self.__handlers:
                try:
                    self.__handlers.pop(name_of_module)
                except KeyError:
                    pass
            return
        if name_of_module in self.__handlers:
            handlers = self.__handlers.get(name_of_module)
            if handler not in handlers:
                handlers.append(handler)
                self.__handlers[name_of_module] = handlers
        else:
            self.__handlers[name_of_module] = [handler]
        return

    def _update_user_modules(self, name_of_module: str, remove: bool = False):
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return
        if remove:
            if name_of_module in self.__user_modules:
                self.__user_modules.remove(name_of_module)
        else:
            if name_of_module not in self.__built_in_modules:
                self.__user_modules.append(name_of_module)
        return

    def _register_module_desc(self, description: str):
        caller = basename(getouterframes(currentframe(), 2)[2].filename)[:-3]
        if not isinstance(description, str):
            log.warning("Invalid attribute type for 'description'. "
                        "Instance should be type of str. "
                        f"Module description for '{caller}' not registered")
            return

        if caller not in self.__module_desc:
            self.__module_desc[caller] = description
        else:
            log.warning(f"Module description for '{caller}' "
                        "registered already")
        return

    def _register_module_info(self, name: str,
                              authors=None, version=None):
        caller = basename(getouterframes(currentframe(), 2)[2].filename)[:-3]
        if not isinstance(name, str):
            log.warning("Invalid attribute type for 'name'. "
                        "Instance should be type of str. "
                        f"Module info for '{caller}' not registered")
            return
        if authors and not isinstance(authors, str):
            log.warning("Invalid attribute type for 'authors'. "
                        "Instance should be type of str. "
                        f"Module info for '{caller}' not registered")
            return
        if not isinstance(version, str):
            log.warning("Invalid attribute type for 'version'. "
                        "Instance should be type of str. "
                        f"Module info for '{caller}' not registered")
            return

        if caller not in self.__module_info:
            self.__module_info[caller] = {"name": name, "authors": authors,
                                          "version": version}
        else:
            log.warning(f"Module info for '{caller}' registered already")
        return

    def _unregister_module_desc(self, module: str):
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return
        try:
            self.__module_desc.pop(module)
        except KeyError:
            pass
        return

    def _unregister_module_info(self, module: str):
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return
        try:
            self.__module_info.pop(module)
        except KeyError:
            pass
        return

    def _getHandlers(self) -> dict:
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            return {}
        return self.__handlers

    def _getAllModules(self) -> list:
        return self.__all_modules

    def _getBuiltInModules(self) -> list:
        return self.__built_in_modules

    def _getLoadModules(self) -> dict:
        return self.__load_modules

    def _getUserModules(self) -> list:
        return self.__user_modules

    def _getModuleDesc(self) -> dict:
        return self.__module_desc

    def _getModuleInfo(self) -> dict:
        return self.__module_info


class _RegisterCMD:
    def __init__(self):
        """
        Initialize the dictionary for registered commands/features.
        This class avoids any duplicated commands/patterns.
        Scheme: {"cmd": {"alt_cmd": "alternative way to trigger the cmd",
                         "hasArgs": "whether the command takes arguments",
                         "prefix": "the prefix used at the beginning of
                                    cmd (pattern)",
                         "no_space_arg": "remove space between command/feature
                                          and argument",
                         "no_cmd": "if cmd is not actually a command",
                         "args": "argument(s) of the cmd",
                         "usage": "how to use the cmd?",
                         "module_name": "Where is it defined?"
                                        (_pre_register_cmd() auto generates it)
                         "success": True (present if cmd usage has been
                                    registered in_register_cmd_usage())}}
        """
        self.__registered_cmds = {}

    def _pre_register_cmd(self, cmd: str, alt_cmd: str,
                          hasArgs: bool, prefix: str,
                          no_space_arg: bool, no_cmd: bool, func) -> bool:
        """
        Pre-registers commands and checks if cmd/pattern isn't
        registered already to avoid duplicated cmds/patterns

        Args:
            cmd (string): command/pattern to pre-register
            alt_cmd (string): alternative command to 'cmd'
            hasArgs (bool): whether 'cmd' takes arguments
            prefix (string): the prefix used at the beginning of cmd (pattern)
            no_space_arg (bool): tell modules utils to remove space
                                 between cmd and arg
            no_cmd (bool): if cmd is not actually a command
            func (Function): the function where the cmd is being used

        Note:
            Callable in EventHandler only

        Returns:
            True if pre-registered successfully or False if
            unauthorized caller calls this function or cmd is
            pre-registered already
        """
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "sysutils", "event_handler.py"))
                  else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return False
        module_name = basename(getfile(func)[:-3])
        if cmd not in self.__registered_cmds:
            for key, value in self.__registered_cmds.items():
                val = value.get("alt_cmd")
                loc = value.get("module_name")
                if cmd == val:
                    log.warning(f"Command '{cmd}' in module '{module_name}' "
                                "registered as alternative command "
                                f"for command '{key}' already "
                                f"(in module '{loc}')")
                    return False
                if alt_cmd and alt_cmd == val:
                    log.warning(f"Alternative command '{alt_cmd}' in module "
                                f"'{module_name}' registered as "
                                "alternative command for primary command "
                                f"'{key}' already (in module '{loc}')")
                    alt_cmd = None
                    break
                if alt_cmd and alt_cmd == key:
                    log.warning(f"Alternative command '{alt_cmd}' in module "
                                f"'{module_name}' registered as "
                                f"primary command already (in module '{loc}')")
                    alt_cmd = None
                    break
            self.__registered_cmds[cmd] = {"alt_cmd": alt_cmd,
                                           "hasArgs": hasArgs,
                                           "prefix": prefix,
                                           "no_space_arg": no_space_arg,
                                           "no_cmd": no_cmd,
                                           "args": None, "usage": None,
                                           "module_name": module_name}
            return True
        loc = self.__registered_cmds.get(cmd, {}).get("module_name")
        log.warning(f"Command/feature '{cmd}' in module '{module_name}' "
                    f"registered in module '{loc}' already")
        return False

    def _register_cmd_usage(self, cmd: str, args=None, usage=None):
        """
        Registers the usage of a command if the specific command is
        pre-registered

        Args:
            cmd (string): cmd to register usage
            args (string): arguments of the command (must be None)
            usage (string): usage of the command (must be None)

        Note:
            Passed parameters attribute type should match strings
        """
        caller = getouterframes(currentframe(), 2)[2]
        caller_name = basename(caller.filename)[:-3]
        line = caller.lineno
        caller = f"{caller_name}:{line}"
        if not isinstance(cmd, str):
            log.warning("Invalid attribute type for 'cmd'. "
                        "Instance should be type of str. "
                        f"CMD usage not registered ({caller})")
            return
        if args and not isinstance(args, str):
            log.warning("Invalid attribute type for 'args'. "
                        "Instance should be type of str. "
                        f"CMD usage of '{cmd}' not registered ({caller})")
            return
        if usage and not isinstance(usage, str):
            log.warning("Invalid attribute type for 'usage'. "
                        "Instance should be type of str. "
                        f"CMD usage of '{cmd}' not registered ({caller})")
            return
        if cmd in self.__registered_cmds:
            val = self.__registered_cmds.get(cmd)
            if val.get("success"):
                log.warning(f"Register usage of command '{cmd}' is "
                            f"present already ({caller})")
                return
            val["args"] = args
            val["usage"] = usage
            val["success"] = True
            self.__registered_cmds[cmd] = val
            return
        log.warning("Register command usage failed as command/feature "
                    f"'{cmd}' is not pre-registered ({caller})")
        return

    def _unregister_cmd(self, cmd: str):
        caller = (True
                  if getouterframes(currentframe(), 2)[2].filename.endswith(
                      join("userbot", "_core", "module_loader.py")) else False)
        if not caller:
            caller = getouterframes(currentframe(), 2)[2]
            log.warning("Not a valid caller "
                        f"({basename(caller.filename)}:{caller.lineno})")
            return
        try:
            self.__registered_cmds.pop(cmd)
        except KeyError:
            pass
        return

    def _getRegisteredCMDs(self) -> dict:
        """
        Returns all registered commands/features in a sorted dictionary
        """
        return dict(sorted(self.__registered_cmds.items()))


_reg_mod = _RegisterModules()


def update_all_modules(name_of_module: str, remove: bool = False):
    _reg_mod._update_all_modules(name_of_module, remove)
    return


def update_built_in_modules(name_of_module: str, remove: bool = False):
    _reg_mod._update_built_in_modules(name_of_module, remove)
    return


def update_load_modules(name_of_module: str,
                        is_running: bool, remove: bool = False):
    _reg_mod._update_load_modules(name_of_module, is_running, remove)
    return


def update_user_modules(name_of_module: str, remove: bool = False):
    _reg_mod._update_user_modules(name_of_module, remove)
    return


def update_handlers(name_of_module: str, handler, remove: bool = False):
    _reg_mod._update_handlers(name_of_module, handler, remove)
    return


def register_module_desc(description: str):
    """
    Registers the description of a module

    Args:
        description (string): (detailed) description of a module
    """
    _reg_mod._register_module_desc(description)
    return


def register_module_info(name: str, authors=None, version=None):
    """
    Registers the information of a module

    Args:
        name (string): name of module
        authors (string): name of author(s) (must be None)
        version (string): version of module (must be None)
    """
    _reg_mod._register_module_info(name, authors, version)
    return


def unregister_module_desc(module: str):
    _reg_mod._unregister_module_desc(module)
    return


def unregister_module_info(module: str):
    _reg_mod._unregister_module_info(module)
    return


def getHandlers() -> dict:
    return _reg_mod._getHandlers()


def getAllModules() -> list:
    return _reg_mod._getAllModules()


def getBuiltInModules() -> list:
    return _reg_mod._getBuiltInModules()


def getLoadModules() -> dict:
    return _reg_mod._getLoadModules()


def getUserModules() -> list:
    return _reg_mod._getUserModules()


def getModuleDesc() -> dict:
    return _reg_mod._getModuleDesc()


def getModuleInfo() -> dict:
    return _reg_mod._getModuleInfo()


_reg_cmd = _RegisterCMD()


def pre_register_cmd(cmd: str, alt_cmd: str,
                     hasArgs: bool, prefix: str,
                     no_space_arg: bool, no_cmd: bool, func) -> bool:
    """
    Pre-registers commands and checks if cmd isn't registered
    already to avoid duplicated cmds

    Args:
        cmd (string): command to pre-register
        alt_cmd (string): alternative command to 'cmd'
        hasArgs (bool): whether 'cmd' takes arguments
        func (Function): the function where the cmd is being used

    Returns:
        True if pre-registered successfully or False if unauthorized
        caller calls this function or cmd is pre-registered already
    """
    return _reg_cmd._pre_register_cmd(cmd, alt_cmd, hasArgs,
                                      prefix, no_space_arg, no_cmd, func)


def register_cmd_usage(cmd: str, args=None, usage=None):
    """
    Registers the usage of a command if the specific command is pre-registered

    Args:
        cmd (string): cmd to register usage
        args (string): arguments of the command (must be None)
        usage (string): usage of the command (must be None)

    Example:
        from userbot.sysutils.register_cmd import register_cmd_usage

        register_cmd_usage("example",
                           "[optional: <ID>] or reply",
                           "Gets the ID of an user")
    """
    _reg_cmd._register_cmd_usage(cmd, args, usage)
    return


def unregister_cmd(cmd: str):
    _reg_cmd._unregister_cmd(cmd)
    return


def getRegisteredCMDs():
    """
    Returns all registered commands in a sorted dictionary
    """
    return _reg_cmd._getRegisteredCMDs()


sys.modules[__name__] = _protectedAccess(
    sys.modules[__name__],
    attrs=[
        "update_all_modules", "update_built_in_modules", "update_load_modules",
        "update_user_modules", "update_handlers", "unregister_module_desc",
        "unregister_module_info", "getHandlers", "unregister_cmd",
        "_RegisterModules", "_RegisterCMD", "_reg_mod", "_reg_cmd",
        "pre_register_cmd"
    ],
    warn_msg=("Illegal access to core attribute '{0}' blocked "
              "(requested by {1}:{2})"),
    mlogger=log
)
