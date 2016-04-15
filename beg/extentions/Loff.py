import re
import MySQLdb as mdb

WORDS = ["LIGHT","OFF"]

def handle(mic):
	con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
	with con:
		cur=con.cursor()
		cur.execute("INSERT INTO switch (s_id,status) VALUES ('2','0')")
		con.commit()		
	if con:
		con.close()
	mic.say("light turning off")


def isValid(text):
	return bool(re.search(r'\blight off\b', text, re.IGNORECASE))
