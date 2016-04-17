# -*- coding: utf-8-*-
import MySQLdb as mdb
import re
import datetime
from semantic.dates import DateService

WORDS = ["NOTIFICATION"]


def handle(mic):
    c=datetime.datetime.now()
    con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
    cur=con.cursor()
    cur.execute("select * from notif where date > '"+str(c)+"' order by date limit 5")
    temp=cur.fetchall()
    service = DateService()
    
    for item in temp:
    	time = service.convertTime(item[2])
    	mic.say(str(item[1])+" on "+str(time))
    con.close()

def isValid(text):
    
    return bool(re.search(r'\bnotifications\b', text, re.IGNORECASE))

