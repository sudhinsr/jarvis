# -*- coding: utf-8-*-
import datetime
import re
from semantic.dates import DateService

WORDS = ["TIME"]


def handle(mic):
    
    now = datetime.datetime.now()
    service = DateService()
    response = service.convertTime(now)
    mic.say("It is %s right now." % response)


def isValid(text):
    
    return bool(re.search(r'\btime\b', text, re.IGNORECASE))
