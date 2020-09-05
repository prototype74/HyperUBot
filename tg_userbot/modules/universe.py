# My stuff
from tg_userbot import tgclient

# Telethon stuff
from telethon.events import NewMessage

# Misc imports
import pygit2
import stat

UNIVERSE_URL = "https://github.com/nunopenim/module-universe.git"

# Auxiliary test functions
def add_tree(repo, tree, prefix, files):
    for file in tree:
        fullname = '%s/%s' % (prefix, file.name)
        if stat.S_ISDIR(file.filemode):
            add_tree(repo, file.to_object(), fullname, files)
        else:
            files[fullname] = 1

def list_all_files(repo_path):
    repo = pygit2.Repository(repo_path)
    walker = repo.walk(repo.head.hex, pygit2.GIT_SORT_NONE)
    files = {}
    for ref in repo.listall_references():
        if not ref.startswith('refs/heads'):
            continue
        walker.push(repo.lookup_reference(ref).hex)
    for ref in walker:
        add_tree(repo, ref.tree, '', files)
    files = files.keys()
    files.sort()
    return files

# Maybe add just a single command, but multiple arguments?
@tgclient.on(NewMessage(pattern=r"^\.universe$", outgoing=True))
async def universe_checker(msg):
    files = list_all_files(UNIVERSE_URL)
    await msg.edit(files)
    return