# -*- coding: utf-8 -*-

import re
import subprocess

from khasbaht.helpers import cmd_builder, cmd_runner
from slackbot.bot import listen_to, respond_to


@respond_to('^ping (.*)')
def ping(message, params):
    """Ping specified host specified times. Flags accepted."""
    cmd = cmd_builder('ping', params)
    cmd_runner(cmd, message)

@respond_to('^traceroute (.*)')
def traceroute(message, params):
    """Perform a traceroute against the specified host."""
    cmd = cmd_builder('traceroute', params)
    cmd_runner(cmd, message)

@respond_to('^What is your external IP?', re.IGNORECASE)
def get_external_ip(message):
    """The bot will respond with the host machine's external IP."""
    cmd = [ "dig", "+short", "myip.opendns.com", "@resolver1.opendns.com" ]
    cmd_runner(cmd, message)

# TODO: This needs to be updated
@respond_to('^What is your internal IP?', re.IGNORECASE)
def get_internal_ip(message):
    """
    The bot will repsond with all internal IP addresses.
    Note: 127.0.0.1 will be excluded from the results. Cause, duh.
    """
    cmd = [ "ifconfig" ]
    results = subprocess.run(cmd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, universal_newlines=True, shell=False)
    if results.stdout:
        for line in results.stdout.split('\n'):
            if re.search('inet ', line):
                ip = line.split(' ')[1]
                if ip != "127.0.0.1":
                    message.reply("```{}```".format(ip))
    if results.stderr:
        message.reply("```{}```".format(results.stderr))
