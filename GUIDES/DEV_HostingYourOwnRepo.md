# HyperUBot Guide - Hosting your own community repo

## Requirements

- GitHub account
- Repository (public)
- Your modules you'd like to share with the world

## Basic structure of your community repo

```
Your repo
|
+--Licence 
|     Your license, PEL if based on our code
|
+--src
|     module1.py
|     module2.py
|     module3.py
|     module4.py
|     etc.
|
+--other stuff
```

There is no unique structure how your repository should look like, it's enough if there is a README file, a license if needed (required if your modules are based on our code: falls under **PEL**) and maybe some credits. The only important thing is that your modules are in the `Releases` section of your repository.

## Rules? I don't think so!

But still do us a favor and follow the basic rules:
- Don't share harmful modules
- Try to set names which are **not** used by our modules in HyperUBot and in [module-universe](https://github.com/nunopenim/module-universe) already
- Avoid duplicate commands, HyperUBot does not load equal commands. We have made a [list of taken commands](https://github.com/prototype74/HyperUBot/blob/master/GUIDES/DEV_TakenCommandsReference.md) to check if a command isn't taken already
- Don't create modules that do spam too much, don't forget, the more a module does spam on Telegram the higher the chance the user who uses the module get (temporary) banned. A first symptome is a [FloodWaitError](https://docs.telethon.dev/en/latest/concepts/errors.html#avoiding-limits) in terminal.

Well we can't check if you actually did follow the rules, neither we can take down modules from GitHub that does do harmful stuff but take our advice, no one will use hardmful modules, so don't even bother to create some. However you are free to do whatever you want to your community repo. Create nice modules no one did made before, people will surely to use and like them!

## Release the kraken... your modules!

To release your modules, locate to `Release` section and hit the `Draft a new releae` button. There you can upload your modules to the footer as assets. This is also how HyperUBot's Package Manager does check for your community repos: it checks for assets in the latest release on GitHub.

> Note: Don't forget to set a proper version (tag of release). It will be visible in Package Manager!

## Adding your community repo to Package Manager

Adding a repo is pretty easy. Just run `.pkg update <owner/repo>` in any chat where `owner` is your GitHub's account name and `repo` the name of your community repository. Check the upper-left corner of this site, you will know what we mean then.

Alternative you can add the <owner/repo>-combo in your `COMMUNITY_REPO` config e.g. `COMMUNITY_REPO = ["example/example_repo"]` and run `.pkg update` in any chat later.

Once the repo is added you can finally install your own modules in HyperUBot using the `.pkg install <your module name>` command. Run `.pkg list` before just to ensure your repo is actually added.

## Tips and Tricks

### 1. Tell us, how your modules work

It might be possible that your modules work different than ours and may need a special requirement or instruction. Let us know about that, as it will surely make it easier to use your creations!

### 2. Let them know there are updates!

Updates are great and people get excited if they know there are updates soon. So let them know that by creating a Telegram update channel for example, and posting a status update there.

### 3. Follow the development

HyperUBot gets improvements, changes and additions which might be possible that some features were removed, you do use in your modules. The consequence is your module may fail to load it. Always follow the current development, to adapt your modules to the changes we made faster. How to follow the development you ask? Check out our [Telegram channel](https://t.me/HyperUBotNews) or check the last [commits](https://github.com/prototype74/HyperUBot/commits/master) we made.

---

> Note: Always keep in mind that you take the full responsibility  about your repo and the modules you offer. We don't give support to users who facing issues with your modules.
