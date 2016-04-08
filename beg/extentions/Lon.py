import re
import MySQLdb as mdb

WORDS = ["LIGHT","ON"]

def handle(mic):
	con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
	with con:
		cur=con.cursor()
		cur.execute("INSERT INTO switch (s_id,status) VALUES ('2','1')")
		con.commit()		
	if con:
		con.close()
	mic.say("light turning on")


def isValid(text):
	return bool(re.search(r'\blight on\b', text, re.IGNORECASE))
