from tg_userbot.watcher import watcher
from tg_userbot.languages.english import testModuleText as msgRep

@watcher(outgoing=True, pattern=r"^\.test$")
async def tester(msg):
    await msg.edit(msgRep.TEST_MESSAGE)