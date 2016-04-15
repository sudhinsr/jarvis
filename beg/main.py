from flask import Flask, request, render_template, redirect, url_for,Response
from flaskext.mysql import MySQL
from tts import TTS
from selection import Selection
from camera import VideoCamera

tts=TTS()
s=Selection(tts)
mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='whyte'
app.config['MYSQL_DATABASE_DB']='jarvis'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

data = None
@app.route("/",methods=['GET','POST'])
def auth():
	cursor=mysql.connect().cursor()
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
	data = request.args['name']
	def rconv(device):
		if (device=="switchOn"):
			s_id='1'
			status='1'

		elif (device=="switchOff"):
			s_id='1'
			status='0'

		elif (device=="lightOn"):
			s_id='2'
			status='1'

		elif (device=="lightOff"):
			s_id='2'
			status='0'

		con=mysql.connect()
		cursor=con.cursor()
		cursor.execute("INSERT INTO switch (s_id,status,user) VALUES ('"+s_id+"','"+status+"','"+data+"')")
		con.commit()



	if request.method == 'POST':
		device=request.form["device"]
		if(device != None):
			rconv(device)


	cursor=mysql.connect().cursor()
	cursor.execute("select humidity,temperature from sensor order by id desc")
	sensor=cursor.fetchone()
	cursor.execute("select s_id,status from switch where s_id='1' order by id desc")
	switch=cursor.fetchone()
	cursor.execute("select s_id,status from switch where s_id='2' order by id desc")
	light=cursor.fetchone()
		
	def conv(n):
		if n == '0':
			return "On"
		else:
			return "Off"

	return render_template('home.html',data=data,humidity=sensor[0],temperature=sensor[1],switch=conv(switch[1]),light=conv(light[1]))

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video')
def video_feed():
	return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')





if __name__ == '__main__':
	app.debug = True
	app.run(host="localhost")