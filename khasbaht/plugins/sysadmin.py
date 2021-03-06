# -*- coding: utf-8 -*-

from khasbaht.helpers import cmd_builder, cmd_runner
from slackbot.bot import respond_to


@respond_to('^shell-cmd (.*)')
def exec_cmd(message, cmd):
    """
    Run any shell command on the host machine. This can be very risky.
    But, also enables one to run exactly what they want to on the host
    machine, regardless of OS type.
    """
    if len(cmd.split(' ')) > 1:
        cmd = cmd_builder(cmd.split(' ')[0], str(cmd.split(' ', 1)[1]))
    cmd_runner(cmd, message)