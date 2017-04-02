# KHASBAHT

My other terminal emulator is Slack.

---

## DAFUQ IS KHASBAHT?

KhasBaht is a bot for [Slack](https://slack.com) (technically a plugin for [slackbot](https://github.com/lins05/slackbot)) that enables one to interact with the host system that KhasBaht is installed on. This has been tested on Linux and MacOS (10.12.x) but should™ work on any OS that supports Python 3.x.

### KNOWN ISSUES

Some shit don't work. Go figure...

- File attachments are only uploaded by the primary name of the bot (not the spoofed name, if enabled). The current way to manage it is to have the spoofed named bot post the name of the file to help a little in tracking the origin.
- You'll tell me.

### TODO

- [x] setting for max output length -> crop and add output as file if longer
- [ ] network utilities module (ifconfig, ping, print routing info, traceroute)
- [ ] self updater (pull, rebase and restart/reload from git?)
- [ ] file utils module (touch, cat file, etc)
- [x] dynamic naming/calling of tmpfile
- [ ] silent mode that only confirms that the command ran (and logs output locally)

---

## INSTALLATION

Clone the damn repo

`git clone https://github.com/KhasMek/KhasBaht.git`

Make sure the dependencies are installed

- Python 3.x
- slackbot
    + If you wish to use the username spoofing option, you'll need to install my fork of slackbot, found [here](https://github.com/KhasMek/slackbot/tree/username-wip)
    + `pip install slackbot`

---

## RUN DOE?

Get yourself an [api key](https://api.slack.com/web) by filling out some options. Next, copy `local_settings.example` to `local_settings.py` and add that api key from Slack otherwise shit won't work. You can add optional settings, or slackbot plugins as well. See below. Invite that baht into whatever channels you want it in.

### SETTINGS

#### Required Settings

```
API_TOKEN = ''
PLUGINS = [
    'khasbaht.plugins'
]
```

#### Optional Settings

```
DEBUG = ''
DEFAULT_REPLY = ''
ERRORS_TO = ''
BOT_ICON = ''
DEFAULT_USERNAME = True/False
BOT_USERNAME = ''
MAX_MESSAGE_LENGTH = 20
```

### I SAID RUN DOE

You can run in the current terminal session with `python khasbaht.py`, although you may want to kick it into a background screen session or something with `screen -dmS khasbaht python run.py`.

---

## LISTENERS & RESPONDERS

Things you can say to KhasBaht and things it listens for.

**Listener** - Will respond whenever the phrase is seen, regardless of who it is directed to. These have no affect in Direct Messages.

**Responder** - Will respond only if the phrase is directed at the bot, either via PM or invoking the bots name.

#### Trigger Phrases

|            Phrase           |                           Options                           |    Type   |                                                                Details                                                                 |
| --------------------------- | ----------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| \^Be a parrot (.**)         | responses to parrot                                         | Listener  | All the bots will parrot whatever options you post. This is basic and helpful for troubleshooting.                                     |
| \^Everyone check in         |                                                             | Listener  | All of the bots in the channel will respond with the hostname of the machine they're running on and the username they're running under |
| \^ls (args optional)        | arguments are optional, if not '.' will be the assumed path | Responder | List files and directories                                                                                                             |
| \^mkdir                     | directory name                                              | Responder | Create a new directory                                                                                                                 |
| \^ping (.*)                 | -c $AMOUNT $HOST                                            | Responder | Pings specified host X times. You will have a bad time if you don't specify a number of pings with the -c flag                         |
| \^rm                        | $file(s) or $dir(s)                                         | Responder | Delete specified file(s)/dir(s)                                                                                                        |
| \^shell-cmd (.*)            | shell-command & flags                                       | Responder | Execute the specified shell command on the host machine                                                                                |
| \^touch (.*)                | $filename(s)                                                | Responder | Create an empty file with the specified name and extension                                                                             |
| \^traceroute                | $domain                                                     | Responder | Perform a traceroute to specified domain                                                                                               |
| \^What is your external IP? |                                                             | Responder | Responds with the hosts external IP                                                                                                    |
| \^What is your internal IP? |                                                             | Responder | Responds with hosts internal IP address(es)                                                                                            |

#### Regex Legend

| Symbol |               Meaning                |
| ------ | ------------------------------------ |
| `^`    | Message starts with                  |
| `(.*)` | Body of message after trigger phrase |

---
