# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# This file serves the purpose of adding configuration classes for userspace modules,
# downloaded from the Userbot's universe repo, extra repos, or manually sideloaded
# by the user or developer. You should organize it in classes with understandable names.
# An example of this could be the (future) weather module, as we will require a key. Just
# create a new WeatherConfigClass and import it from there (You can do such by doing
# "from userbot.external_configs import WeatherConfigClass as Config"), then use it (for any
# field inside the class, use "Config.FIELD", to obtain it's value). Down bellow there is a class
# DummyConfigClass, for python rookies that are learning how this works, and want to make
# a module.

class DummyConfigClass(object):
    DUMMY = False
    DUMMY_API_KEY = "OurHardWorkIsUsedAlsoToTeach" # Usually API Keys come in string format.
