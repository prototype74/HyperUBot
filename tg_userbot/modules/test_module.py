from tg_userbot.watcher import watcher

@watcher(outgoing=True, pattern=r"^\.test$")
async def tester(msg):
    await msg.edit("`This is a test - I am working`")