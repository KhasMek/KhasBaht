# -*- coding: utf-8 -*-

import re

from khasbaht.helpers import cmd_builder, format_response, cmd_runner
from slackbot.bot import respond_to


@respond_to('^ls$')
@respond_to('^ls (.*)')
def ls(message, params='.'):
    """
    Return the contents of the current, or specified directory.
    Flags accepted.
    """
    cmd = cmd_builder('ls', params)
    cmd_runner(cmd, message)

@respond_to('^mkdir (.*)')
def mkdir(message, params):
    """Create a new directory in the specified path. Flags accepted."""
    cmd = cmd_builder('mkdir', params)
    cmd_runner(cmd, message)

@respond_to('^rm (.*)')
def rm(message, params):
    """Delete specified file or directory. Flags accepted."""
    cmd = cmd_builder('rm', params)
    cmd_runner(cmd, message)

@respond_to('^touch (.*)', re.IGNORECASE)
def touch(message, file):
    """Touch (create) an empty file with the specified name."""
    with open(file, 'a'):
        response, default_username = format_response(message,
            data="```{f} created successfully!```".format(f=file))
        message.reply_webapi(response, as_user=default_username)
