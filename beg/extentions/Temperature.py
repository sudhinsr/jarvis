# -*- coding: utf-8-*-
import MySQLdb as mdb
import re

WORDS = ["TEMPERATURE"]


def handle(mic):

    con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
    cur=con.cursor()
    cur.execute("select temperature from sensor order by date desc")
    temp=cur.fetchone()
    temp=str(temp)
    mic.say("It is %s degree celcius." %temp)


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\btemperature\b', text, re.IGNORECASE))
