import re
import MySQLdb as mdb

WORDS = ["SWITCH","OFF"]

def handle(mic):
	con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
	with con:
		cur=con.cursor()
		cur.execute("INSERT INTO switch (s_id,status) VALUES ('1','0')")
		con.commit()		
	if con:
		con.close()
	mic.say("light turning off")


def isValid(text):
	return bool(re.search(r'\bswitch off\b', text, re.IGNORECASE))
