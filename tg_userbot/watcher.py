from telethon import events

from tg_userbot import bot

def watcher(**args): #bot command processor, maybe later for edited messages
    command = args.get('command', None)
    if command is not None and not command.startswith('(?i)'):
        args['pattern'] = '(?i)' + command

    def starter(func):
        bot.add_event_handler(func, events.NewMessage(**args))
        return func

    return starter
