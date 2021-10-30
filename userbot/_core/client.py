# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from telethon import TelegramClient
from inspect import currentframe, getouterframes
from logging import getLogger
import glob
import os

log = getLogger(__name__)


class HyperClient(TelegramClient):
    def __init__(self, *args, **kwargs):
        """
        Initialize the Client. Equal to TelegramClient.
        """
        super().__init__(*args, **kwargs)

    def __getattribute__(self, attr):
        """
        Filter unwanted requests from the userbot. HyperUBot doesn't need
        these attributes in any way from the client after initialization.
        So if a program or module calls them after initialization then it
        could be for bad purposes. So block the access to these attributes.
        """
        if attr in ("session", "api_id", "api_hash", "_init_request",
                    "_sender"):
            all_pys = tuple(glob.glob(os.path.join("userbot", "*.py")) +
                            glob.glob(os.path.join("userbot", "*", "*.py")))
            caller = getouterframes(currentframe(), 2)[1]
            c_name = caller.filename
            c_line = caller.lineno
            if c_name.endswith(all_pys):
                protected_attrs = {"session": "String Session",
                                   "api_id": "App api_id",
                                   "api_hash": "App api_hash",
                                   "_init_request": "InitConnectionRequest",
                                   "_sender": "MTProtoSender"}
                blocked_attr = protected_attrs.get(attr)
                log.warning(f"Blocked access to '{blocked_attr}' (requested "
                            f"by {os.path.basename(c_name)}:{c_line})")
                return None
        return super(HyperClient, self).__getattribute__(attr)

    def __setattr__(self, attr, value):
        """
        Same way as in __getattribute__ but blocks the userbot to overwrite
        these attributes.
        """
        if attr in ("session", "api_id", "api_hash", "_init_request",
                    "_sender"):
            all_pys = tuple(glob.glob(os.path.join("userbot", "*.py")) +
                            glob.glob(os.path.join("userbot", "*", "*.py")))
            caller = getouterframes(currentframe(), 2)[1]
            c_name = caller.filename
            c_line = caller.lineno
            if c_name.endswith(all_pys):
                protected_attrs = {"session": "String Session",
                                   "api_id": "App api_id",
                                   "api_hash": "App api_hash",
                                   "_init_request": "InitConnectionRequest",
                                   "_sender": "MTProtoSender"}
                blocked_attr = protected_attrs.get(attr)
                log.warning(f"Blocked access to '{blocked_attr}' (requested "
                            f"by {os.path.basename(c_name)}:{c_line})")
                return
        super(HyperClient, self).__setattr__(attr, value)
        return
