import serial
import MySQLdb as mdb
import time
con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
ser=serial.Serial('/dev/ttyUSB1',9600)
ot=0
while True:
	time.sleep(2)
	con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
	data=ser.readline()
	pieces=data.split("\t")
	print data
	with con:
		cur=con.cursor()
		cur.execute("select status from switch where s_id = 1 order by time desc limit 1")
		s1 = cur.fetchone()
		cur.execute("select status from switch where s_id = 2 order by time desc limit 1")
		s2 = cur.fetchone()
		if(ot != pieces[1]):
			ot=pieces[1]
			cur.execute("INSERT INTO sensor (humidity,temperature) VALUES (%s,%s)",(pieces[0],pieces[1]))
	con.commit()		
	if con:
		con.close()

	if(s1[0]=='0'):
		ser.write('1')
		#print '1'
	elif(s1[0]=='1'):
		ser.write('2')
		#print '2'
	ser.write('\n')
	if(s2[0]=='0'):
		ser.write('3')
		#print '3'
	elif(s2[0]=='1'):
		ser.write('4')
		#print '4'

	ser.write('\n')
