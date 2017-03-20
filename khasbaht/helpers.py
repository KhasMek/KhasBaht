# -*- coding: utf-8 -*-

import os
import re

from slackbot import settings
from slackbot.utils import create_tmp_file


def cmd_builder(cmd, params):
    cmd = [ cmd ]
    if params:
        for param in params.split():
            param = url_checker(param)
            cmd.append(param)
    return cmd

def url_checker(param):
    url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(url, param):
        param = param.split('|', 1)[-1]
        return param[:-1]
    else:
        return param

def check_response(message, response):
    max_message_length = settings.MAX_MESSAGE_LENGTH if hasattr(settings,
        'MAX_MESSAGE_LENGTH') else 50
    if len(response.split('\n')) > max_message_length:
        fname = re.sub('-+', '-', re.sub('[^\w]', '-', message.body['text']))
        response = response.lstrip('```').rstrip('```')
        with create_tmp_file(content=bytes(response, 'utf-8')) as tmpf:
            message.channel.upload_file(fname, tmpf)
        return "Output of {c} has been uploaded as a file due to length.".format(
            c=message.body['text'])
    else:
        return response

def format_response(message, **kwargs):
    default_username = settings.DEFAULT_USERNAME if hasattr(settings,
        'DEFAULT_USERNAME') else True
    response_set = ''
    null_response = ("```No Response (it probably completely quietly).```")
    if kwargs.get('stdout'):
        response_set = True
        response = str("```{}```".format(kwargs.get('stdout')))
        if response is None:
            response = null_response
        return check_response(message, response), default_username
    if kwargs.get('stderr'):
        response_set = True
        response = str("```{}```".format(kwargs.get('stderr')))
        if response is None:
            response = null_response
        return check_response(message, response), default_username
    if kwargs.get('data'):
        response_set = True
        response = kwargs.get('data')
        return check_response(message, response), default_username
    if not response_set:
        return null_response, default_username
