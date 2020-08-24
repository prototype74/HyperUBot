# tguserbot stuff
from tg_userbot import NOT_LOAD_MODULES

# Misc
from glob import glob
from os.path import dirname, basename, isfile


def __list_all_modules() -> list:
    module_paths = glob(dirname(__file__) + "/*.py")
    modules = []
    for module in module_paths:
        if isfile(module) and module.endswith(".py") and not module.endswith("__init__.py"):
            try:
                if not basename(module)[:-3] in NOT_LOAD_MODULES:
                    modules.append(basename(module)[:-3])
            except:
                modules.append(basename(module)[:-3])

    return modules

ALL_MODULES = sorted(__list_all_modules())
