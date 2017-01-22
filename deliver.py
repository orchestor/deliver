#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '1700e1c5921a4b12b7c4c1c4579d8f61'


def deliver(query):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = query

    response = request.getresponse()
    j = json.loads(response.read())

    s = j["result"]["parameters"]
    res = "food:" + s["food"] + ", " + " address:" +  s["address"]
    return res
