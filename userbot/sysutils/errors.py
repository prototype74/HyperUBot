# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

class AccessError(Exception):
    __module__ = Exception.__module__

    def __init__(self, message: str = "Access denied", *args, **kwargs):
        self.message = message
        super().__init__(self.message, *args, **kwargs)


class UnauthorizedAccessError(Exception):
    __module__ = Exception.__module__

    def __init__(self, message: str = "Unauthorized access denied",
                 *args, **kwargs):
        self.message = message
        super().__init__(self.message, *args, **kwargs)
