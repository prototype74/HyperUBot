# Copyright 2021-2023 nunopenim @github
# Copyright 2021-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from sys import version_info

if (version_info.major, version_info.minor) < (3, 8):
    print("Python v3.8+ is required to start Recovery System! "
          "Please update Python to v3.8 or newer "
          "(current version: {}.{}.{}).".format(
              version_info.major, version_info.minor, version_info.micro))
    quit(1)

from glob import glob  # noqa: E402
from json import loads  # noqa: E402
from platform import system  # noqa: E402
from shutil import copytree, rmtree  # noqa: E402
from subprocess import check_call, DEVNULL  # noqa: E402
from sys import argv, executable, platform  # noqa: E402
from urllib.request import urlopen, urlretrieve  # noqa: E402
from zipfile import (BadZipFile, LargeZipFile,
                     ZipFile, ZIP_DEFLATED)  # noqa: E402
import ast  # noqa: E402
import os  # noqa: E402

RECOVERY_NAME = os.path.basename(__file__)
VERSION = "2.4.0"
BACKUP_DIR = os.path.join(".", "backup")
GIT = os.path.join(".", ".git")
GITIGNORE = os.path.join(".", ".gitignore")
RELEASE_DIR = os.path.join(".", "releases")
UPDATE_PACKAGE = os.path.join(RELEASE_DIR, "update.zip")
PY_EXEC = executable if " " not in executable else '"' + executable + '"'
IS_WINDOWS = (True if system().lower() == "windows" or
              os.name == "nt" or platform.startswith("win") else False)

if IS_WINDOWS:
    try:
        import colorama
        colorama.init()
        WIN_COLOR_ENABLED = True
    except (ImportError, ModuleNotFoundError):
        WIN_COLOR_ENABLED = False
    except Exception as e:
        WIN_COLOR_ENABLED = False
        print(f"Exception: {e}")


class Colors:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GRAY = "\033[90m"
    CYAN_BG = "\033[46m"
    GREEN_BG = "\033[102m"
    RED_BG = "\033[101m"
    YELLOW_BG = "\033[103m"
    END = "\033[0m"


def setColorText(text: str, color: Colors) -> str:
    if IS_WINDOWS and not WIN_COLOR_ENABLED:
        return text  # don't use ANSI codes
    return f"{color}{text}{Colors.END}"


class _Recovery:
    def __init__(self):
        self.__recovery_mode = "NORMAL"

    def start_userbot(self, option: str = ""):
        try:
            if option in ("safemode", "safemode2", "nomods"):
                tcmd = [PY_EXEC, "-m", "userbot", f"-{option}"]
            else:
                tcmd = [PY_EXEC, "-m", "userbot"]
            os.execle(PY_EXEC, *tcmd, os.environ)
        except Exception as e:
            print(setColorText(
                f"Failed to start HyperUBot: {e}", Colors.RED))
        return

    def userbot_installed(self) -> bool:
        if os.path.exists(os.path.join(".", "userbot")) and \
           os.path.exists(os.path.join(".", "userbot", "__init__.py")) and \
           os.path.exists(os.path.join(".", "userbot", "__main__.py")):
            return True
        return False

    def _list_dirs(self, source: str, ignore: list = []) -> list:
        do_not_list = [BACKUP_DIR, RELEASE_DIR, GIT]
        listed_dirs = []
        if ignore:
            for element in ignore:
                if isinstance(element, str):
                    do_not_list.append(element)
        for name in os.listdir(source):
            srcname = os.path.join(source, name)
            if srcname not in do_not_list:
                listed_dirs.append(srcname)
                if os.path.isdir(srcname):
                    for elem in self._list_dirs(srcname, ignore):
                        listed_dirs.append(elem)
        return listed_dirs

    def _fix_paths(self, rules_paths: list) -> list:
        paths = []
        try:
            for path in rules_paths:
                if IS_WINDOWS:
                    path = path.replace("/", "\\")
                else:
                    path = path.replace("\\", "/")
                if "*" in path:
                    for name in glob(path):
                        dir_name = os.path.dirname(name)
                        dir_name = os.path.join(".", dir_name)
                        if dir_name not in paths:
                            paths.append(dir_name)
                        paths.append(os.path.join(".", name))
                        if os.path.isdir(name):
                            for elem in self._list_dirs(name):
                                paths.append(os.path.join(".", elem))
                elif os.path.isdir(path):
                    paths.append(os.path.join(".", path))
                    for elem in self._list_dirs(path):
                        paths.append(os.path.join(".", elem))
                else:
                    paths.append(os.path.join(".", path))
        except Exception as e:
            print(setColorText(e, Colors.RED))
        return paths

    def _install_requirements(self):
        try:
            check_call(
               [PY_EXEC, "-m", "pip", "install", "-r", "requirements.txt"])
        except Exception as e:
            print(setColorText(
                f"Failed to install pip requirements: {e}", Colors.RED))
        return

    @property
    def recovery_mode(self) -> str:
        return self.__recovery_mode

    @recovery_mode.setter
    def recovery_mode(self, new_mode: str):
        self.__recovery_mode = new_mode

    def _remove(self, dirs: list = [], ignore: list = []):
        def name_in_list(name_to_check, list_to_check) -> bool:
            # only exact path names should be ignored
            for name in list_to_check:
                if name == name_to_check:
                    return True
            return False
        for name in reversed(dirs):
            if not name_in_list(name, ignore):
                if os.path.isfile(name):
                    os.remove(name)
                elif os.path.isdir(name):
                    os.rmdir(name)
        return

    def _remove_extracted_update_package(self, package_path: str):
        try:
            rmtree(package_path)
        except Exception as e:
            print(
                setColorText(f"Failed to remove extracted update package: {e}",
                             Colors.RED))
        return

    def userbot_version(self) -> str:
        ver_py = os.path.join(".", "userbot", "version.py")
        version = None
        try:
            ver_attr = {}
            if os.path.exists(ver_py) and os.path.isfile(ver_py):
                with open(ver_py, "r") as ver_file:
                    code = ast.parse(ver_file.read())
                    exec(compile(code, "", "exec"), ver_attr)
                ver_file.close()
            version = ver_attr.get(
                "VERSION", setColorText("Unknown", Colors.YELLOW))
        except Exception:
            version = setColorText("Unknown", Colors.YELLOW)
        return version

    def detect_git(self) -> int:
        try:
            check_call(["git", "rev-parse", "--git-dir"],
                       stderr=DEVNULL, stdout=DEVNULL)
            return 2
        except Exception:
            if os.path.exists(GIT) and os.path.isdir(GIT):
                return 1
        return 0


class _Backup(_Recovery):
    def __init__(self):
        super().__init__()

    def backup_exists(self, name: str) -> bool:
        bkName = os.path.join(BACKUP_DIR, name + ".hbotbk")
        if os.path.exists(bkName):
            return True
        return False

    def generate_backup(self, bk_name: str):
        if not os.path.exists(BACKUP_DIR):
            try:
                os.mkdir(BACKUP_DIR)
            except Exception as e:
                print(setColorText(
                    f"Failed to create backup directory: {e}", Colors.RED))
                return
        try:
            bkName = os.path.join(BACKUP_DIR, bk_name + ".hbotbk")
            print("Generating backup...")
            paths = open(os.path.join(".", "list.paths"), "w")
            list_paths = self._list_dirs(".")
            for name in list_paths:
                if not name == os.path.join(".", "list.paths"):
                    paths.write(f"{name}\n")
            paths.close()
            with ZipFile(bkName, "w", ZIP_DEFLATED) as bkZIP:
                for name in list_paths:
                    bkZIP.write(name)
            bkZIP.close()
            os.remove(os.path.join(".", "list.paths"))
            print(setColorText("Backup generated successfully.", Colors.GREEN))
        except BadZipFile as bze:
            print(setColorText(
                f"Bad zip archive: {bze}", Colors.RED))
        except LargeZipFile as lze:
            print(setColorText(
                f"Zip archive too large (>64): {lze}", Colors.RED))
        except Exception as e:
            print(setColorText(
                f"Failed to generate backup archive: {e}", Colors.RED))
        return


class _Cache(_Recovery):
    def __init__(self):
        super().__init__()

    def clear(self):
        pyc_list = []
        ubot_dir = self._list_dirs(os.path.join(".", "userbot"))
        for name in ubot_dir:
            if "__pycache__" in name:
                pyc_list.append(name)
        try:
            print("Clearing caches...")
            self._remove(pyc_list)
        except Exception as e:
            print(
                setColorText(f"Failed to clear caches: {e}", Colors.RED))
            return
        if all(True if not os.path.exists(name) else False
               for name in pyc_list):
            print(setColorText("Caches cleaned.", Colors.GREEN))
        else:
            print(setColorText("Failed to clear caches.", Colors.RED))
        return


class _Installer(_Recovery):
    def __init__(self):
        self.__download_successful = False
        self.__installation_successful = False
        self.__package_path = None
        super().__init__()

    def __extract_update_package(self):
        try:
            contents = None
            with ZipFile(UPDATE_PACKAGE, "r") as zipObject:
                contents = zipObject.namelist()
                zipObject.extractall(RELEASE_DIR)
            zipObject.close()
            if contents and len(contents) > 0:
                root_dir = contents[0][:-1]
                self.__package_path = os.path.join(RELEASE_DIR, root_dir)
        except BadZipFile as bze:
            print(setColorText(
                f"Bad zip archive: {bze}", Colors.RED))
        except LargeZipFile as lze:
            print(setColorText(
                f"Zip archive too large (>64): {lze}", Colors.RED))
        except Exception as e:
            print(setColorText(
                f"Failed to extract update package: {e}", Colors.RED))
        return

    def __get_latest_release(self):
        if not os.path.exists(RELEASE_DIR):
            try:
                os.mkdir(RELEASE_DIR)
            except Exception as e:
                print(f"Failed to create release directory: {e}")
                return

        try:
            print("Parsing latest release data...")
            repo_url = urlopen("https://api.github.com/repos/prototype74/"
                               "HyperUBot/releases/latest")
            repo_data = loads(repo_url.read().decode())
            dw_url = repo_data.get("zipball_url")
            if not dw_url:
                print(setColorText("Failed to parse download URL", Colors.RED))
                return
        except Exception as e:
            print(
                setColorText(f"Failed to parse latest release: {e}",
                             Colors.RED))
            return

        try:
            print("Downloading latest release...")
            urlretrieve(dw_url, UPDATE_PACKAGE)
        except Exception as e:
            print(
                setColorText(f"Unable to download latest release: {e}",
                             Colors.RED))
            return

        if os.path.exists(UPDATE_PACKAGE):
            self.__download_successful = True
            print("Download completed.")
        else:
            print(
                setColorText("Unable to find update package", Colors.RED))
        return

    def install_update_package(self):
        self.__get_latest_release()

        if not self.__download_successful:
            print(setColorText("Installation aborted.", Colors.YELLOW))
            return

        print("Extracting update package...")
        self.__extract_update_package()

        if not self.__package_path:
            print(
                setColorText("Extracted update package not found",
                             Colors.YELLOW))
            return

        try:
            print("Removing current environment...")
            self._remove(self._list_dirs("."),
                         [os.path.join(".", RECOVERY_NAME)])
        except Exception as e:
            print(
                setColorText(f"Failed to remove old environment: {e}",
                             Colors.RED))
            self._remove_extracted_update_package(self.__package_path)
            return

        try:
            print("Installing update package...")
            copytree(self.__package_path, ".", dirs_exist_ok=True)
        except Exception as e:
            print(
                setColorText(f"Failed to install update package: {e}",
                             Colors.RED))
            self._remove_extracted_update_package(self.__package_path)
            return

        print("Installing pip requirements...")
        self._install_requirements()

        try:
            print("Cleaning up...")
            self._remove_extracted_update_package(self.__package_path)
            self._remove(self._fix_paths(["releases"]))
        except Exception as e:
            print(
                setColorText(f"Failed to clean updater environment: {e}",
                             Colors.YELLOW))

        self.__installation_successful = True
        print(setColorText("Installation completed.", Colors.GREEN))
        return

    def getInstallationSuccessful(self):
        return self.__installation_successful


class _Restore(_Recovery):
    def __init__(self):
        super().__init__()

    def list_backups(self) -> dict:
        bk_dict = {}
        if not os.path.exists(BACKUP_DIR):
            return bk_dict
        try:
            num = 1
            for name in os.listdir(BACKUP_DIR):
                if os.path.isfile(os.path.join(BACKUP_DIR, name)) and \
                   name.endswith(".hbotbk"):
                    srcname = os.path.join(BACKUP_DIR, name)
                    bk_dict[str(num)] = {"bkname": name.split(".hbotbk")[0],
                                         "source": srcname}
                    num += 1
        except Exception as e:
            print(setColorText(
                f"Failed to list backup directory: {e}", Colors.RED))
        return bk_dict

    def __getListPaths(self, content: bytes) -> list:
        paths = []
        try:
            byte_to_str = "".join(map(chr, content))
        except Exception:
            return paths
        split_str = "\r\n" if byte_to_str.endswith("\r\n") else "\n"
        for name in byte_to_str.split(split_str):
            if name:
                paths.append(name.replace("/", "\\")
                             if IS_WINDOWS else name.replace("\\", "/"))
        return paths

    def __comparePaths(self, zipNamelist: list, list_paths: list) -> bool:
        zipNamelist_fixed = []
        for name in zipNamelist:
            if not name == "list.paths":
                if name.endswith("/") or name.endswith("\\"):
                    name = name[:-1]
                zipNamelist_fixed.append(
                    os.path.join(".", name.replace("/", "\\") if IS_WINDOWS
                                 else name))
        if sorted(zipNamelist_fixed) == sorted(list_paths):
            return True
        return False

    def restore(self, name: dict):
        if not name:
            print(setColorText("Name empty!", Colors.YELLOW))
            return

        bkName = name.get("bkname", "HyperUBot")
        bkSource = name.get("source")
        bkName += ".hbotbk"

        if not os.path.exists(bkSource):
            print(
                setColorText(f"{bkSource}: No such file or directory",
                             Colors.YELLOW))
            return

        try:
            contents = None
            userbot = ["userbot/", "userbot/__init__.py",
                       "userbot/__main__.py"]
            bkZIP = ZipFile(bkSource, "r")
            contents = bkZIP.namelist()
            lpfile = None
            for x in contents:
                if x == "list.paths":
                    lpfile = bkZIP.read(x)
                    break
            list_paths = self.__getListPaths(lpfile)
            result = 0
            for y in contents:
                for uname in userbot:
                    if uname == y:
                        result += 1
            if not self.__comparePaths(contents, list_paths) or \
               not result == len(userbot):
                print(setColorText(f"{bkSource}: Invalid archive format!",
                                   Colors.RED))
                return

            try:
                print("Removing current environment...")
                self._remove(self._list_dirs("."),
                             [os.path.join(".", RECOVERY_NAME)])
            except Exception as e:
                print(
                    setColorText(f"Failed to remove current environment: {e}",
                                 Colors.RED))
                return

            print("Restoring backup archive...")
            bkZIP.extractall(path=".", members=[z for z in contents
                                                if not z == "list.paths"])
            bkZIP.close()
            print(setColorText("Restore completed.", Colors.GREEN))
        except BadZipFile as bze:
            print(setColorText(
                f"Bad zip archive: {bze}", Colors.RED))
        except LargeZipFile as lze:
            print(setColorText(
                f"Zip archive too large (>64): {lze}", Colors.RED))
        except Exception as e:
            print(setColorText(
                f"Failed to restore backup archive: {e}", Colors.RED))
        return


class _Updater(_Recovery):
    def __init__(self, commit_id: str):
        self.__commit_id = commit_id
        self.__package_path = None
        self.__id_mismatch = False
        self.__modify_started = False
        self.__successful = False
        super().__init__()

    def __find_update_package(self) -> bool:
        if os.path.exists(UPDATE_PACKAGE):
            return True
        return False

    def __extract_update_package(self):
        try:
            contents = None
            root_dir = None
            with ZipFile(UPDATE_PACKAGE, "r") as zipObject:
                print("Update package found")
                contents = zipObject.namelist()
                if contents and len(contents) > 0:
                    try:
                        root_dir = contents[0][:-1]
                        self.__package_path = os.path.join(RELEASE_DIR,
                                                           root_dir)
                    except Exception:
                        print(setColorText(
                            "Failed to extract package path", Colors.RED))
                if not root_dir or \
                   not root_dir.split("-")[-1] == self.__commit_id:
                    self.__id_mismatch = True
                    return
                print("Extracting update package...")
                zipObject.extractall(RELEASE_DIR)
            zipObject.close()
        except BadZipFile as bze:
            print(setColorText(
                f"Bad zip archive: {bze}", Colors.RED))
        except LargeZipFile as lze:
            print(setColorText(
                f"Zip archive too large (>64): {lze}", Colors.RED))
        except Exception as e:
            print(setColorText(
                f"Failed to extract update package: {e}", Colors.RED))
        return

    def __parse_gitignore(self) -> list:
        ignore_paths = []
        try:
            with open(GITIGNORE, "r") as git:
                for line in git.readlines():
                    if not line.startswith("#") and not line == "\n" and \
                       "__pycache__" not in line:
                        line = line.split("#")[0].rstrip()
                        if IS_WINDOWS:
                            line = line.replace("/", "\\")
                        if "*" in line:
                            for name in glob(line):
                                dir_name = os.path.dirname(name)
                                dir_name = os.path.join(".", dir_name)
                                if dir_name not in ignore_paths:
                                    ignore_paths.append(dir_name)
                                ignore_paths.append(os.path.join(".", name))
                                if os.path.isdir(name):
                                    for elem in self._list_dirs(name):
                                        ignore_paths.append(
                                            os.path.join(".", elem))
                        elif os.path.isdir(line):
                            ignore_paths.append(os.path.join(".", line))
                            for elem in self._list_dirs(line):
                                ignore_paths.append(os.path.join(".", elem))
                        else:
                            ignore_paths.append(
                                os.path.join(".", line.replace("\n", "")))
            git.close()
        except Exception as e:
            print(setColorText(e, Colors.RED))
        return ignore_paths

    def install_update_package(self):
        if not self.__find_update_package():
            print(setColorText("Update package not found", Colors.YELLOW))
            return

        self.__extract_update_package()

        if self.__id_mismatch:
            print(setColorText("Commit ID mismatch!", Colors.YELLOW))
            return

        if not self.__package_path:
            print(
                setColorText("Extracted update package not found",
                             Colors.YELLOW))
            return

        try:
            import releases.rules as rules
        except ImportError:
            print(setColorText("Unable to find updater rules!", Colors.YELLOW))
            self._remove_extracted_update_package(self.__package_path)
            return
        except Exception as e:
            print(setColorText(f"Invalid format for updater rules: {e}",
                               Colors.RED))
            self._remove_extracted_update_package(self.__package_path)
            print(setColorText("Update cancelled", Colors.YELLOW))
            return

        always_ignore = [os.path.join(".", "userbot"),
                         os.path.join(".", "userbot", "modules_user"),
                         os.path.join(".", "userbot", "userdata"),
                         os.path.join(".", "userbot", "config.env"),
                         os.path.join(".", "userbot", "config.ini"),
                         os.path.join(".", "userbot", "config.py"),
                         os.path.join(".", "userbot", "secure_config"),
                         os.path.join(".", RECOVERY_NAME)]
        for name in self._fix_paths(["__pycache__/*"]):
            always_ignore.append(name)
        parse_gitignore = (rules.PARSE_GITIGNORE
                           if hasattr(rules, "PARSE_GITIGNORE") and
                           isinstance(rules.PARSE_GITIGNORE, bool) else False)
        force_delete = (rules.DEL if hasattr(rules, "DEL") and
                        isinstance(rules.DEL, list) else [])
        rules_ignore = (rules.IGNORE if hasattr(rules, "IGNORE") and
                        isinstance(rules.IGNORE, list) else [])

        if force_delete:
            force_delete = self._fix_paths(force_delete)

        if rules_ignore:
            rules_ignore = self._fix_paths(rules_ignore)
            for name in rules_ignore:
                always_ignore.append(name)

        ignore = []
        if parse_gitignore:
            try:
                print("Parsing gitignore...")
                if os.path.exists(GITIGNORE):
                    git_ignore = self.__parse_gitignore()
                    for elem in git_ignore:
                        if not elem == os.path.join(".", "userbot"):
                            ignore.append(elem)
            except Exception as e:
                print(
                    setColorText(f"Failed to parse gitgignore: {e}",
                                 Colors.YELLOW))

        # Everything afterwards will modify bot files/directories
        self.__modify_started = True

        try:
            print("Removing old environment...")
            self._remove(
                self._list_dirs(".", ignore), always_ignore)
        except Exception as e:
            print(
                setColorText(f"Failed to remove old environment: {e}",
                             Colors.RED))
            self._remove_extracted_update_package(self.__package_path)
            return

        if force_delete:
            try:
                print("Force deleting specific directories/files...")
                self._remove(force_delete, rules_ignore)
            except Exception as e:
                print(
                    setColorText(
                        f"Failed to delete specific directories/files: {e}",
                        Colors.YELLOW))

        try:
            print("Installing update package...")
            copytree(self.__package_path, ".", dirs_exist_ok=True)
        except Exception as e:
            print(
                setColorText(f"Failed to install update package: {e}",
                             Colors.RED))
            self._remove_extracted_update_package(self.__package_path)
            return

        print("Installing pip requirements...")
        self._install_requirements()

        try:
            print("Cleaning up...")
            self._remove_extracted_update_package(self.__package_path)
            self._remove(self._fix_paths(["releases"]))
        except Exception as e:
            print(
                setColorText(f"Failed to clean updater environment: {e}",
                             Colors.YELLOW))

        self.__successful = True
        print(setColorText("Update completed.", Colors.GREEN))
        return

    def getModifyStarted(self) -> bool:
        return self.__modify_started

    def getSuccessful(self) -> bool:
        return self.__successful

_option_table = {
    # status can be 0=ok, 1=warn or 2=error
    "boot":      {"enabled": True,
                  "status": 0,
                  "name": "Start HyperUBot",
                  "func": (lambda r: _start_userbot_options(r))},
    "clear":     {"enabled": True,
                  "status": 0,
                  "name": "Clear caches",
                  "func": (lambda: _clear_caches())},
    "update":    {"enabled": True,
                  "status": 0,
                  "name": "Apply update",
                  "func": (lambda: _apply_update(False))},
    "backup":    {"enabled": True,
                  "status": 0,
                  "name": "Backup current version",
                  "func": (lambda: _create_backup())},
    "restore":   {"enabled": True,
                  "status": 0,
                  "name": "Restore",
                  "func": (lambda: _restore_backup())},
    "reinstall": {"enabled": True,
                  "status": 0,
                  "name": "Reinstall HyperUBot",
                  "func": (lambda: _reinstall_userbot())},
    "terminate": {"enabled": True,
                  "status": 0,
                  "name": "Exit",
                  "func": "X"}
    }


def _get_option(name, val):
    return _option_table.get(name, {}).get(val)


def _update_option_table(recovery: _Recovery):
    bot_installed = recovery.userbot_installed()
    is_git_repo = recovery.detect_git()
    for i, (key, val) in enumerate(_option_table.items(), start=1):
        if key in ("boot", "clear", "update", "backup"):
            if not bot_installed:
                if val.get("enabled"):
                    _option_table[key]["enabled"] = False
                    _option_table[key]["status"] = 2
            elif not val.get("enabled"):  # reset error
                _option_table[key]["enabled"] = True
                _option_table[key]["status"] = 0
        if IS_WINDOWS and key == "boot":
            # Disable boot options as os.execle isn't working
            # well on Windows due to missing fork+exec support.
            # More info: https://bugs.python.org/issue9148
            if val.get("enabled"):
                _option_table[key]["enabled"] = False
                _option_table[key]["status"] = 2
        if key in ("update", "restore", "reinstall"):
            # status 2 is preferred
            if is_git_repo and not val.get("status") == 2:
                _option_table[key]["status"] = 1
            elif (val.get("status") and
                  not val.get("status") == 2):  # reset warning
                _option_table[key]["status"] = 0
        if not val.get("num"):
            _option_table[key]["num"] = str(i)
    return


def _update_info(recovery: _Recovery, show_version: bool = True):
    bot_installed = recovery.userbot_installed()
    git_type = recovery.detect_git()
    if show_version or not bot_installed or git_type:
        print()
    if show_version:
        print(f"HyperUBot version: {recovery.userbot_version()}")
    if not bot_installed:
        print(setColorText("HyperUBot is not installed", Colors.RED))
    if git_type == 2:
        print(setColorText("Directory is a local git repository",
                           Colors.YELLOW))
    elif git_type == 1:
        print(setColorText("Directory might be git initialized",
                           Colors.YELLOW))
    return


_modified = False  # in case of modifications


def _start_userbot_options(recovery: _Recovery):
    start_options = {
        "1": {"name": "Normal", "option": None},
        "2": {"name": "Safe mode", "option": "safemode"},
        "3": {"name": "Advanced safe mode", "option": "safemode2"},
        "4": {"name": "Core only mode", "option": "nomods"},
    }
    option_text = ""
    for key, val in start_options.items():
        name = val.get("name")
        option_text += f"[{key}] {name}\n"
    print(option_text)
    temp = None
    try:
        while True:
            temp = input("Your input (or 'X' to cancel): ")
            if temp.lower() == "x":
                raise KeyboardInterrupt
            if temp.isnumeric():
                if temp in start_options.keys():
                    break
            print(
                setColorText("Invalid input. Try again", Colors.YELLOW))
    except KeyboardInterrupt:
        print()
        return
    selected_option = start_options.get(temp, {}).get("option")
    if selected_option:
        recovery.start_userbot(selected_option)
    else:
        # default start option
        recovery.start_userbot()
    return


def _apply_update(auto: bool, commit_id=None):
    cid = commit_id
    if not auto:
        try:
            while True:
                cid = input("Commit ID (or 'X' to cancel): ")
                if cid:
                    break
                else:
                    print(
                        setColorText("Invalid input. Try again",
                                     Colors.YELLOW))
        except KeyboardInterrupt:
            print()
            return
        if cid.lower() == "x":
            return
    updater = _Updater(cid)
    updater.install_update_package()
    if auto and updater.getSuccessful():
        if IS_WINDOWS:  # No auto-start on Windows
            print("Run the following command to start HyperUBot: " +
                  setColorText("python -m userbot", Colors.CYAN))
        else:
            print("Starting HyperUBot...")
            updater.start_userbot()
    elif updater.getSuccessful():
        global _modified
        _modified = True
    elif updater.getModifyStarted():
        print(setColorText("Update failed", Colors.RED_BG))
        print(setColorText("Important data might be lost. "
                           "Please restore a backup if available or "
                           "reinstall HyperUBot!",
                           Colors.RED))
    return


def _clear_caches(is_cli: bool = False):
    if not is_cli:
        try:
            while True:
                temp = input("Do you want to clear all caches? (y/n): ")
                if temp.lower() in ("yes", "y"):
                    break
                elif temp.lower() in ("no", "n"):
                    raise KeyboardInterrupt
                else:
                    print(
                        setColorText("Invalid input. Try again",
                                     Colors.YELLOW))
        except KeyboardInterrupt:
            print()
            return
    cache = _Cache()
    cache.clear()
    return


def _create_backup(is_cli: bool = False, option: str = ""):
    backup = _Backup()
    if not backup.userbot_installed():
        print(setColorText("Failed to backup current version: "
                           "HyperUBot not installed", Colors.RED))
        return

    if not is_cli:
        temp = None
        try:
            while True:
                temp = input("Do you want to backup the current version? "
                             "(y/n): ")
                if temp.lower() in ("yes", "y"):
                    break
                elif temp.lower() in ("no", "n"):
                    raise KeyboardInterrupt
                else:
                    print(
                        setColorText("Invalid input. Try again",
                                     Colors.YELLOW))
        except KeyboardInterrupt:
            print()
            return
    bkName = "HyperUBot-" + backup.userbot_version()
    if backup.backup_exists(bkName):
        if not is_cli:
            try:
                while True:
                    temp = input(f"A backup of '{bkName}' exists already.\n"
                                 "Overwrite? (y/n): ")
                    if temp.lower() in ("yes", "y"):
                        break
                    elif temp.lower() in ("no", "n"):
                        raise KeyboardInterrupt
                    else:
                        print(
                            setColorText("Invalid input. Try again",
                                         Colors.YELLOW))
            except KeyboardInterrupt:
                print()
                return
        elif option.lower() != "-f":
            print(setColorText(f"A backup of '{bkName}' exists already. "
                               "Add option '-f' to force overwrite it",
                               Colors.YELLOW))
            return
    backup.generate_backup(bkName)
    return


def _restore_backup(is_cli: bool = False, bk_name: str = ""):
    restore = _Restore()
    backups = restore.list_backups()
    if not backups:
        print(setColorText("No backups found!", Colors.YELLOW))
        return
    if not is_cli:
        listed_backups = "Select a backup to restore\n\n"
        for key, value in backups.items():
            bkName = value.get("bkname")
            listed_backups += f"[{key}] {bkName}\n"
        print(listed_backups)
        temp = None
        try:
            while True:
                temp = input("Your input (or 'X' to cancel): ")
                if temp.lower() == "x":
                    raise KeyboardInterrupt
                if temp.isnumeric():
                    if temp in backups.keys():
                        break
                print(
                    setColorText("Invalid input. Try again",
                                 Colors.YELLOW))
        except KeyboardInterrupt:
            print()
            return
        selected_backup = None
        for key, value in backups.items():
            if temp == key:
                selected_backup = value
                break
        bkName = selected_backup.get("bkname")
        print(f"Are you sure you want to restore '{bkName}'?\n" +
              setColorText("THIS PROCESS CANNOT BE UNDONE!", Colors.RED))
        try:
            while True:
                temp = input("Your input (y/n): ")
                if temp.lower() in ("yes", "y"):
                    break
                elif temp.lower() in ("no", "n"):
                    raise KeyboardInterrupt
                else:
                    print(
                        setColorText("Invalid input. Try again",
                                     Colors.YELLOW))
        except KeyboardInterrupt:
            print()
            return
    else:
        if not bk_name:
            print(setColorText("Backup filename is not given", Colors.YELLOW))
            return
        for val in backups.values():
            if bk_name.split(".hbotbk")[0] == val.get("bkname"):
                selected_backup = val
                break
        else:
            print(setColorText(f"Backup '{bk_name}' not found", Colors.YELLOW))
            return
    restore.restore(selected_backup)
    if not is_cli:
        global _modified
        _modified = True
    return


def _reinstall_userbot():
    print(
        setColorText("This process will delete all downloaded user modules, "
                     "your configurations including your string "
                     "session and any other data in HyperUBot's root "
                     "directory. Please backup your data before you continue. "
                     "At last, the latest release will be "
                     "installed automatically.",
                     Colors.YELLOW))
    print(
        setColorText("THIS PROCESS CANNOT BE UNDONE!", Colors.RED))
    try:
        while True:
            temp = input("Continue? (y/n): ")
            if temp.lower() in ("yes", "y"):
                break
            elif temp.lower() in ("no", "n"):
                raise KeyboardInterrupt
            else:
                print(
                    setColorText("Invalid input. Try again",
                                 Colors.YELLOW))
    except KeyboardInterrupt:
        print()
        return

    installer = _Installer()
    installer.install_update_package()

    if not installer.getInstallationSuccessful():
        print(setColorText("Reinstallation not successful.", Colors.YELLOW))

    global _modified
    _modified = True
    return


def _print_table():
    for key in _option_table.keys():
        num = _get_option(key, "num")
        name = _get_option(key, "name")
        if not _get_option(key, "enabled"):
            print(setColorText(f"[-] {name}", Colors.GRAY))
        elif _get_option(key, "status") == 1:
            print(setColorText(f"[{num}] {name}", Colors.YELLOW))
        else:
            print(f"[{num}] {name}")
    return


def _get_available_opt(opt_length: int):
    options_str = ""
    min_num = ""
    max_num = ""

    def add_to_str():
        nonlocal min_num, max_num, options_str
        if min_num and max_num:
            if options_str:
                options_str += "|"
            options_str += f"{min_num}-{max_num}"
        elif min_num:
            if options_str:
                options_str += "|"
            options_str += f"{min_num}"
        min_num = ""
        max_num = ""
        return

    for i, val in enumerate(_option_table.values(), start=1):
        is_enabled = val.get("enabled")
        number = val.get("num")
        if not min_num and is_enabled:
            min_num = number
        elif is_enabled:
            max_num = number
            if i == opt_length:  # last element
                add_to_str()
        else:
            add_to_str()
    return options_str


def _menues(recovery: _Recovery):
    while True:
        # update table
        global _modified
        _update_option_table(recovery)
        _update_info(recovery, _modified)
        _modified = False
        #################
        print()
        print("Main Menu")
        _print_table()
        print()
        opt_length = len(_option_table)
        if opt_length >= 1:
            try:
                num = input(f"Your input [{_get_available_opt(opt_length)}]: ")
            except KeyboardInterrupt:
                print()
                raise KeyboardInterrupt
        else:
            print(setColorText("No options available!", Colors.RED))
            return
        for key in _option_table.keys():
            if num == _get_option(key, "num") and \
               _get_option(key, "enabled"):
                func = _get_option(key, "func")
                if callable(func):
                    opt_name = _get_option(key, "name")
                    print(f"\nMain Menu > {opt_name}")
                    if key == "boot":
                        func(recovery)
                    else:
                        func()
                elif func.lower() == "x":
                    raise KeyboardInterrupt
                break
        else:
            print(setColorText("Invalid input!", Colors.YELLOW))
    return


def main():
    # INIT
    args = argv
    if len(args) > 1:  # CLI
        if args[1].lower() == "-clearcache":
            _clear_caches(True)
            return
        if args[1].lower() == "-backup":
            try:
                _cli_option = args[2]
            except IndexError:
                _cli_option = ""
            _create_backup(True, _cli_option)
            return
        if args[1].lower() == "-restore":
            try:
                _cli_bk_name = args[2]
            except IndexError:
                _cli_bk_name = ""
            _restore_backup(True, _cli_bk_name)
            return
    auto_updater = False
    print(setColorText("HyperUBot Recovery System", Colors.CYAN))
    print(f"Recovery version: {VERSION}")
    recovery = _Recovery()
    if len(args) > 1:  # CLI
        if args[1].lower() == "-autoupdate":
            auto_updater = True
            recovery.recovery_mode = setColorText("AUTO UPDATE", Colors.CYAN)
    print(f"HyperUBot version: {recovery.userbot_version()}")
    print(f"Mode: {recovery.recovery_mode}")
    if auto_updater:
        try:
            commit_id = args[2]
        except IndexError:
            print(setColorText("Commit ID required!", Colors.YELLOW))
            return
        if not recovery.userbot_installed():
            print(setColorText("HyperUBot is not installed", Colors.RED))
            return
        _apply_update(True, commit_id)
        return

    # MAIN
    _menues(recovery)
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
    except (BaseException, Exception) as e:
        print(
            setColorText(f"Recovery has stopped: {e}", Colors.RED_BG))
        quit(1)
    quit()
