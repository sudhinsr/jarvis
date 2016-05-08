import re
import MySQLdb as mdb

WORDS = ["SWITCH","ON"]

def handle(mic):
	con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
	with con:
		cur=con.cursor()
		cur.execute("INSERT INTO switch (s_id,status) VALUES ('1','1')")
		con.commit()		
	if con:
		con.close()
	mic.say("Switch turning on")


def isValid(text):
	return bool(re.search(r'\bswitch on\b', text, re.IGNORECASE))
