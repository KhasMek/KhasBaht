# -*- coding: utf-8 -*-

import re
import subprocess

from khasbaht.helpers import cmd_builder, format_response
from slackbot.bot import listen_to, respond_to


@listen_to('^be a parrot (.*)', re.IGNORECASE)
def testing(message, cmd):
    response, default_username = format_response(message, data="{r}"
        .format(r=cmd))
    message.reply_webapi(response, as_user=default_username)

@listen_to('^Everyone check in', re.IGNORECASE)
def check_in(message):
    un = subprocess.run([ 'whoami' ], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True, shell=False)
    hn = subprocess.run([ 'hostname' ], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True, shell=False)
    response, default_username = format_response(message,
        data="```Running on System: {hn}\nRunning as User {un}```"
            .format(hn=hn.stdout, un=un.stdout))
    message.reply_webapi(response, as_user=default_username)
    message.react('+1')

@respond_to('^Troll me', re.IGNORECASE)
def trololol(message):
    response, default_username = format_response(message, data="Bitch Please.")
    message.reply_webapi(response, as_user=default_username)
