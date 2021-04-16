# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from json import loads

def strlist_to_list(strlist: str) -> list:
    try:
        list_obj = loads(strlist)
    except:
        list_obj = []
    return list_obj

def str_to_bool(strbool: str) -> bool:
    if strbool in ("True", "true"):
        return True
    elif strbool in ("False", "false"):
        return False
    raise ValueError(f"{strbool} is not a bool")
