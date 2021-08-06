# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from sys import version_info

if (version_info.major, version_info.minor) < (3, 8):
    print("Python v3.8+ is required! Please update "
          "Python to v3.8 or newer "
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
import os  # noqa: E402

RECOVERY_NAME = os.path.basename(__file__)
VERSION = "2.1.0"
BACKUP_DIR = os.path.join(".", "backup")
GIT = os.path.join(".", ".git")
GITIGNORE = os.path.join(".", ".gitignore")
RELEASE_DIR = os.path.join(".", "releases")
UPDATE_PACKAGE = os.path.join(RELEASE_DIR, "update.zip")
PY_EXEC = executable if " " not in executable else '"' + executable + '"'
IS_WINDOWS = (True if system().lower() == "windows" or
              os.name == "nt" or platform.startswith("win") else False)
WIN_COLOR_ENABLED = False

try:
    if IS_WINDOWS:
        import colorama
        colorama.init()
        WIN_COLOR_ENABLED = True
except:
    pass


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

    def run_userbot(self, safemode: bool = False):
        try:
            if safemode:
                tcmd = [PY_EXEC, "-m", "userbot", "-safemode"]
            else:
                tcmd = [PY_EXEC, "-m", "userbot"]
            os.execle(PY_EXEC, *tcmd, os.environ)
        except Exception as e:
            print(setColorText(
                f"Failed to run HyperUBot: {e}", Colors.RED))
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
                setColorText("Failed to remove extracted update package",
                             Colors.RED))
        return

    def userbot_version(self) -> str:
        ver_py = os.path.join(".", "userbot", "version.py")
        version = setColorText("Unknown", Colors.YELLOW)
        try:
            with open(ver_py, "r") as script:
                for line in script.readlines():
                    if not line.startswith("#") and not line == "\n" and \
                       line.startswith("VERSION = "):
                        if line.split(" = ")[1]:
                            version = line.split(" = ")[1]
                            version = version.replace("\n", "")
                        break
            if '"' in version:
                version = version.replace('"', "")
            script.close()
        except:
            pass
        return version

    def detect_git(self) -> int:
        try:
            check_call(["git", "rev-parse", "--git-dir"],
                       stderr=DEVNULL, stdout=DEVNULL)
            return 2
        except:
            pass
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
            repo_url = urlopen("https://api.github.com/repos/nunopenim/"
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
                setColorText(f"Unable to find update package: {e}",
                             Colors.RED))
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
        try:
            byte_to_str = "".join(map(chr, content))
        except:
            return []
        return [name for name in byte_to_str.split(
            "\r\n" if IS_WINDOWS else "\n") if name]

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
            for name in contents:
                if name == "list.paths":
                    lpfile = bkZIP.read(name)
                    break
            list_paths = self.__getListPaths(lpfile)
            result = 0
            for name in contents:
                for uname in userbot:
                    if uname == name:
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
            bkZIP.extractall(path=".", members=[name for name in contents
                                                if not name == "list.paths"])
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
                    except:
                        pass
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
                         os.path.join(".", "userbot", "config.py"),
                         os.path.join(".", "userbot", "secure_config"),
                         os.path.join(".", "userbot", "package_lists.hbot"),
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
                  "name": "Run HyperUBot",
                  "func": (lambda r: r.run_userbot())},
    "boot_safe": {"enabled": True,
                  "status": 0,
                  "name": "Run HyperUBot (safe mode)",
                  "func": (lambda r: r.run_userbot(True))},
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
        if key in ("boot", "boot_safe", "clear", "update", "backup"):
            if not bot_installed:
                if val.get("enabled"):
                    _option_table[key]["enabled"] = False
                    _option_table[key]["status"] = 2
            elif not val.get("enabled"):  # reset error
                _option_table[key]["enabled"] = True
                _option_table[key]["status"] = 0
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
    print() if show_version or not bot_installed or git_type else None
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
            pass
        if cid.lower() == "x":
            return
    updater = _Updater(cid)
    updater.install_update_package()
    if auto and updater.getSuccessful():
        print("Booting HyperUBot...")
        updater.run_userbot()
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


def _clear_caches():
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
        return
    cache = _Cache()
    cache.clear()
    return


def _create_backup():
    backup = _Backup()
    if not backup.userbot_installed():
        print(setColorText("Failed to backup current version: "
                           "HyperUBot not installed", Colors.RED))
        return

    temp = None
    try:
        while True:
            temp = input("Do you want to backup the current version? (y/n): ")
            if temp.lower() in ("yes", "y"):
                break
            elif temp.lower() in ("no", "n"):
                raise KeyboardInterrupt
            else:
                print(
                    setColorText("Invalid input. Try again",
                                 Colors.YELLOW))
    except KeyboardInterrupt:
        return
    bkName = "HyperUBot-" + backup.userbot_version()
    if backup.backup_exists(bkName):
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
            return
    backup.generate_backup(bkName)
    return


def _restore_backup():
    restore = _Restore()
    backups = restore.list_backups()
    if not backups:
        print(setColorText("No backups found!", Colors.YELLOW))
        return
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
            elif temp.isnumeric():
                if temp in backups.keys():
                    break
            print(
                setColorText("Invalid input. Try again",
                             Colors.YELLOW))
    except KeyboardInterrupt:
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
        return
    restore.restore(selected_backup)
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
            opt_min = list(_option_table.items())[0][-1].get("num")
            if opt_length == 1:
                num = input(f"Your input [{opt_min}]: ")
            else:
                opt_max = list(_option_table.items())[-1][-1].get("num")
                num = input(f"Your input [{opt_min}-{opt_max}]: ")
        else:
            print(setColorText("No options available!", Colors.RED))
            return
        for key in _option_table.keys():
            if num == _get_option(key, "num") and \
               _get_option(key, "enabled"):
                if key in ("boot", "boot_safe"):
                    _get_option(key, "func")(recovery)
                    return  # leave menu
                else:
                    func = _get_option(key, "func")
                    if callable(func):
                        opt_name = _get_option(key, "name")
                        print(f"\nMain Menu > {opt_name}")
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
    auto_updater = False
    print("HyperUBot Recovery System")
    print(f"Recovery version: {VERSION}")
    recovery = _Recovery()
    if len(args) > 1:
        if args[1].lower() == "-autoupdate":
            auto_updater = True
            recovery.recovery_mode = setColorText("AUTO UPDATE", Colors.CYAN)
    print(f"HyperUBot version: {recovery.userbot_version()}")
    print(f"Mode: {recovery.recovery_mode}")
    if auto_updater:
        try:
            commit_id = args[2]
        except:
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
