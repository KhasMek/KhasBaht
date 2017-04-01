# -*- coding: utf-8 -*-

import re
import subprocess

from khasbaht.helpers import cmd_builder, format_response
from slackbot.bot import listen_to, respond_to


@respond_to('^What is your external IP?', re.IGNORECASE)
def get_external_ip(message):
    cmd = [ "dig", "+short", "myip.opendns.com", "@resolver1.opendns.com" ]
    external_ip = subprocess.run(cmd, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, universal_newlines=True, shell=False)
    response, default_username = format_response(message,
        data="```{}```".format(external_ip.stdout))
    message.reply_webapi(response, as_user=default_username)

# TODO: This needs to be updated
@respond_to('^What is your internal IP?', re.IGNORECASE)
def get_internal_ip(message):
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

@respond_to('^ping (.*)')
def ping(message, params):
    cmd = cmd_builder('ping', params)
    results = subprocess.run(cmd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, universal_newlines=True, shell=False)
    response, default_username = format_response(message,
        stdout=results.stdout, stderr=results.stderr)
    message.reply_webapi(str(response), as_user=default_username)
