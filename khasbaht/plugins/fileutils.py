# -*- coding: utf-8 -*-

import re

from khasbaht.helpers import format_response
from slackbot.bot import respond_to


@respond_to('^touch (.*)', re.IGNORECASE)
def touch(message, file):
    with open(file, 'a'):
        response, default_username = format_response(message,
            data="```{f} created successfully!```".format(f=file))
        message.reply_webapi(response, as_user=default_username)
