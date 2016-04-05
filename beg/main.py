from flask import Flask, request, render_template, redirect, url_for
from flaskext.mysql import MySQL
from tts import TTS
from selection import Selection

tts=TTS()
s=Selection(tts)
mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='whyte'
app.config['MYSQL_DATABASE_DB']='jarvis'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)
cursor=mysql.connect().cursor()
data = None
@app.route("/",methods=['GET','POST'])
def auth():
	if request.method == 'POST':
		email=request.form["email"]
		passw=request.form["passw"]
		
		cursor.execute("select * from users where email='"+email+"' and password='"+passw+"'")
		data = cursor.fetchone()

		if data is None:
			return " Error"
		else:
			return redirect(url_for('home',name=data[0]))
	return render_template('index.html')

@app.route("/speech",methods=['GET','POST'])
def speech():
	qry=[]
	txt=request.args.get('txt')
	qry.append(txt)
	s.select(qry)
	return 


@app.route("/home",methods=['GET','POST'])
def home():
	if request.method == 'POST':
		switch1=request.form["switch1"]
		switch2=requst.form["switch2"]
		"""switch1=op(switch1)
		switch2=op(switch2)"""
		print switch1
		print switch2

	def op(val):
		if val == 1:
			return 0
		else:
			return 1

	data = request.args['name']
	cursor.execute("select humidity,temperature from sensor order by id desc")
	sensor=cursor.fetchone()
	cursor.execute("select s_id,status from switch where s_id='1' order by id desc")
	switch1=cursor.fetchone()
	cursor.execute("select s_id,status from switch where s_id='2' order by id desc")
	switch2=cursor.fetchone()

	return render_template('home.html',data=data,humidity=sensor[0],temperature=sensor[1],switch1=switch1[1],switch2=switch2[1])

if __name__ == '__main__':
	app.debug = True
	app.run(host="192.168.0.110")