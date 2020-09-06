# tguserbot stuff
from tg_userbot import tgclient, ALL_MODULES, LOAD_MODULES, NOT_LOAD_MODULES, MODULE_DESC, MODULE_DICT
from tg_userbot.include.language_processor import HelpText as msgRep

# Telethon stuff
from telethon.events import NewMessage

# Misc
from os.path import basename


def modules_listing(error_text: str = None) -> str:
    if error_text:
        modules_listed = f"{error_text}\n\n"
        modules_listed += f"{msgRep.USAGE}:\n`.modules -d, --desc, --description [{msgRep.NAME_OF_MODULE}]\n.modules -u, --usage [{msgRep.NAME_OF_MODULE}]`\n\n"

    num = 1
    if not error_text:
        modules_listed = f"{msgRep.AVAILABLE_MODULES}:\n"
    else:
        modules_listed += f"{msgRep.AVAILABLE_MODULES}:\n"
    for module in LOAD_MODULES:
        if not module == basename(__file__)[:-3]:  # exclude this module
            modules_listed += f"`{str(num)}. {module}`\n"
            num += 1

    if NOT_LOAD_MODULES:
        num = 1
        for module in NOT_LOAD_MODULES:
            if module in ALL_MODULES:
                modules_listed += "\n"
                modules_listed += f"{msgRep.DISABLED_MODULES}:\n"
                break
        for module in sorted(NOT_LOAD_MODULES):
            if module in ALL_MODULES:
                modules_listed += f"`{str(num)}. {module}`\n"
                num += 1
    return modules_listed


def module_desc(module: str) -> str:
    if module in LOAD_MODULES:
        if module in MODULE_DESC.keys():
            return msgRep.NAME_MODULE.format(module.capitalize()) + "\n\n" + MODULE_DESC.get(module)
        else:
            return msgRep.NAME_MODULE.format(module.capitalize()) + "\n\n" + msgRep.MODULE_NO_DESC
    else:
        raise IndexError


def module_usage(module: str) -> str:
    if module in LOAD_MODULES:
        if module in MODULE_DICT.keys():
            return msgRep.NAME_MODULE.format(module.capitalize()) + "\n\n" + MODULE_DICT.get(module)
        else:
            return msgRep.NAME_MODULE.format(module.capitalize()) + "\n\n" + msgRep.MODULE_NO_USAGE
    else:
        raise IndexError


@tgclient.on(NewMessage(pattern=r"^\.modules(?: |$)(.*)", outgoing=True))
async def modules(event):
    args_from_event = event.pattern_match.group(1).split(" ", 1)
    if len(args_from_event) == 2:
        first_arg, sec_arg = args_from_event
    else:
        first_arg, sec_arg = args_from_event[0], None

    desc, usage = (False,)*2

    if not first_arg:
        await event.edit(modules_listing())
        return

    if first_arg.lower() in ("-d, --desc, --description"):
        desc = True
    elif first_arg.lower() in ("-u, --usage"):
        usage = True
    else:
        await event.edit(modules_listing(msgRep.INVALID_ARG.format(first_arg)))
        return

    if not sec_arg:
        await event.edit(modules_listing(msgRep.MISSING_NAME_MODULE))
        return

    if sec_arg:
        try:
            if desc:
                await event.edit(module_desc(sec_arg.lower()))
            elif usage:
                await event.edit(module_usage(sec_arg.lower()))
        except IndexError:
            await event.edit(modules_listing(msgRep.MODULE_NOT_FOUND.format(sec_arg)))

    return

