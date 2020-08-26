from telethon import events

from tg_userbot import tgclient

def watcher(**args): #bot command processor, maybe later for edited messages
    command = args.get('command', None)
    #disable_edited = args.get('disable_edited', False)
    if command is not None and not command.startswith('(?i)'):
        args['pattern'] = '(?i)' + command

    def starter(func):
        tgclient.add_event_handler(func, events.MessageEdited(**args))
        tgclient.add_event_handler(func, events.NewMessage(**args))
        return func

    return starter
