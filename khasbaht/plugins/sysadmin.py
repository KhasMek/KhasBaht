# -*- coding: utf-8 -*-

import re
import subprocess

from khasbaht.helpers import cmd_builder, format_response
from slackbot.bot import respond_to


@respond_to('^shell-cmd (.*)')
def exec_cmd(message, cmd):
    if len(cmd.split(' ')) > 1:
        cmd = cmd_builder(cmd.split(' ')[0], str(cmd.split(' ', 1)[1]))
    results = subprocess.run(cmd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, universal_newlines=True, shell=False)
    response, default_username = format_response(message,
        stdout=results.stdout, stderr=results.stderr)
    message.reply_webapi(response, as_user=default_username)
