# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import (tgclient, ALL_MODULES, LOAD_MODULES, NOT_LOAD_MODULES, MODULE_DESC,
                     MODULE_DICT, MODULE_INFO, OS, USER_MODULES)
from userbot.include.aux_funcs import sizeStrMaker
from userbot.include.language_processor import HelpText as msgRep
from telethon.events import NewMessage
from os.path import basename, exists, getctime, getsize
from os import stat
from time import ctime

MODULES_LISTED = {}

def update_list() -> list:
    modules_list = []
    for module in sorted(LOAD_MODULES):
        if not module == basename(__file__)[:-3]:  # exclude this module
            if module in USER_MODULES:
                if module in MODULE_INFO.keys():
                    modules_list.append([MODULE_INFO.get(module, {}).get("name", msgRep.UNKNOWN), module])  # [Name of module, filename of module]
                else:
                    modules_list.append([module, module])
            else:
                if module in MODULE_INFO.keys():
                    modules_list.append([MODULE_INFO.get(module, {}).get("name", msgRep.UNKNOWN), module])
                else:
                    modules_list.append([module, module])

    global MODULES_LISTED

    if MODULES_LISTED:
        MODULES_LISTED = {}  # reset dict

    num = 1

    for module_name, module in sorted(modules_list):
        MODULES_LISTED[str(num)] = module
        num += 1
    return sorted(modules_list)

def modules_listing(error_text: str = None) -> str:
    modules_listed = f"**Modules**\n\n"

    if error_text:
        modules_listed += f"{error_text}\n\n"

    modules_listed += f"{msgRep.USAGE}:\n`.modules -d, --desc, --description [{msgRep.NUMBER_OF_MODULE}]`\n"\
                                       f"`.modules -i, --info, --information [{msgRep.NUMBER_OF_MODULE}]`\n"\
                                       f"`.modules -u, --usage [{msgRep.NUMBER_OF_MODULE}]`\n\n"

    num = 1
    modules_listed += f"{msgRep.AVAILABLE_MODULES}:\n"

    modules_list = update_list()

    for module_name, module in modules_list:
        if module in USER_MODULES:
            modules_listed += f"`({str(num)}) {module_name}* ({module})`\n"
        else:
            modules_listed += f"`({str(num)}) {module_name} ({module})`\n"
        num += 1

    if USER_MODULES:
        modules_listed += "\n" + msgRep.ASTERISK + "\n"

    if NOT_LOAD_MODULES:
        for module in NOT_LOAD_MODULES:
            if module in ALL_MODULES:
                modules_listed += "\n"
                modules_listed += f"{msgRep.DISABLED_MODULES}:\n"
                break
        for module in sorted(NOT_LOAD_MODULES):
            if module in ALL_MODULES:
                modules_listed += f"`- {module}`\n"
                num += 1
    return modules_listed

def module_desc(name_of_module: str, module: str) -> str:
    if module in LOAD_MODULES:
        if module in MODULE_DESC.keys():
            return msgRep.NAME_MODULE.format(name_of_module) + "\n\n" + MODULE_DESC.get(module)
        else:
            return msgRep.NAME_MODULE.format(name_of_module) + "\n\n" + msgRep.MODULE_NO_DESC
    else:
        raise IndexError

def module_info(name_of_module: str, module: str) -> str:
    if module in LOAD_MODULES:
        package_name, moduletype, installation_date = (msgRep.UNKNOWN,)*3
        size = 0
        version = MODULE_INFO.get(module, {}).get("version", 0)
        package_name = module
        module += ".py"
        if OS and OS.lower().startswith("win"):
            syspath = ".\\userbot\\modules\\"
            userpath = ".\\userbot\\modules_user\\"
        else:
            syspath = "./userbot/modules/"
            userpath = "./userbot/modules_user/"
        if exists(syspath + module):
            moduletype = msgRep.SYSTEM
            size = sizeStrMaker(getsize(syspath + module))
            if OS and OS.lower().startswith("win"):
                installation_date = getctime(syspath + module)
            elif OS and OS.lower().startswith("darwin"):
                installation_date = stat(syspath + module).st_birthtime
            else:
                installation_date = stat(syspath + module).st_ctime
        elif exists(userpath + module):
            moduletype = msgRep.USER
            size = sizeStrMaker(getsize(userpath + module))
            if OS and OS.lower().startswith("win"):
                installation_date = getctime(userpath + module)
            elif OS and OS.lower().startswith("darwin"):
                installation_date = stat(userpath + module).st_birthtime
            else:
                installation_date = stat(userpath + module).st_ctime
        result = f"{msgRep.PKG_NAME}: {package_name}\n"
        result += f"{msgRep.MODULE_TYPE}: {moduletype}\n"
        result += f"{msgRep.VERSION}: {version}\n"
        result += f"{msgRep.SIZE}: {size}\n"
        result += f"{msgRep.INSTALL_DATE}: {ctime(installation_date)}"
        return msgRep.NAME_MODULE.format(name_of_module).replace("_", " ") + "\n\n" + result
    else:
        raise IndexError

def module_usage(name_of_module: str, module: str) -> str:
    if module in LOAD_MODULES:
        if module in MODULE_DICT.keys():
            return msgRep.NAME_MODULE.format(name_of_module).replace("_", " ") + "\n\n" + MODULE_DICT.get(module)
        else:
            return msgRep.NAME_MODULE.format(name_of_module).replace("_", " ") + "\n\n" + msgRep.MODULE_NO_USAGE
    else:
        raise IndexError

@tgclient.on(NewMessage(pattern=r"^\.modules(?: |$)(.*)", outgoing=True))
async def modules(event):
    args_from_event = event.pattern_match.group(1).split(" ", 1)
    if len(args_from_event) == 2:
        first_arg, sec_arg = args_from_event
    else:
        first_arg, sec_arg = args_from_event[0], None

    desc, info, usage = (False,)*3

    if not first_arg:
        await event.edit(modules_listing())
        return

    if first_arg.lower() in ("-d", "--desc", "--description"):
        desc = True
    elif first_arg.lower() in ("-i", "--info", "--information"):
        info = True
    elif first_arg.lower() in ("-u", "--usage"):
        usage = True
    else:
        await event.edit(modules_listing(msgRep.INVALID_ARG.format(first_arg)))
        return

    if not sec_arg:
        await event.edit(modules_listing(msgRep.MISSING_NUMBER_MODULE))
        return

    if sec_arg:
        modules_list = update_list()
        global MODULES_LISTED
        name_of_module = None
        module_to_load = MODULES_LISTED.get(sec_arg)
        for module_name, module in modules_list:
            if module_to_load is module:
                name_of_module = module_name
                break
        try:
            if desc:
                await event.edit(module_desc(name_of_module, module_to_load))
            elif info:
                await event.edit(module_info(name_of_module, module_to_load))
            elif usage:
                await event.edit(module_usage(name_of_module, module_to_load))
        except IndexError:
            await event.edit(modules_listing(msgRep.MODULE_NOT_AVAILABLE.format(sec_arg)))

    return
