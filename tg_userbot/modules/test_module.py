from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import TestModuleText as msgRep

@watcher(outgoing=True, pattern=r"^\.test$")
async def tester(msg):
    await msg.edit(msgRep.TEST_MESSAGE)