from Tkinter import *
import MySQLdb as mdb

class App:
	def __init__(self,window):
		self.con = mdb.connect('localhost', 'root', 'whyte', 'jarvis')
		self.cur=self.con.cursor()
		self.window=window
		self.flag=False
		self.window.resizable(width=FALSE, height=FALSE)
		self.window.title("JARVIS")
		self.window.geometry("300x350")
		self.status="Enter details"
		self.create()

	def register(self):
		fname=self.u5.get()
		lname=self.u7.get()
		phn=self.u9.get()
		email=self.u11.get()
		pasw=self.u13.get()
		rpasw=self.u15.get()
		if(pasw == rpasw):
			try:
				self.cur.execute("insert into users (fname,lname,email,phone,password) values ('"+fname+"','"+lname+"','"+email+"','"+phn+"','"+pasw+"')")
				self.con.commit()
				self.status="Registration Completed"
				self.regreset()
				self.reg()
			except self.con.IntegrityError as err:
				print("Error: {}".format(err))
		else:
			self.regreset()
			self.reg()
	
	def set(self):
		user = self.u5.get()
		pasw = self.u7.get()
		self.reset()
		self.cur.execute("select * from users where email = '"+user+"' and password = '"+ pasw +"'")

		if self.cur.rowcount > 0 :
			row = self.cur.fetchone()
			self.name=row[1]
			self.index()

		else:
			self.status="Incorrect Details"
			self.create()

	def index(self):
		def stat(n):
			if(n == '1'):
				return "On"
			else:
				return "Off"

		self.cur.execute("select humidity,temperature from sensor order by date desc")
		sen = self.cur.fetchone()
		self.cur.execute("select status from switch where s_id = 1 order by time desc")
		s1 = self.cur.fetchone()
		self.cur.execute("select status from switch where s_id = 2 order by time desc")
		s2 = self.cur.fetchone()
		temp="Temperature"+str(sen[1])
		hum="Humidity"+str(sen[0])
		self.u3 = Label(self.window, text= "JARVIS")
		self.u4 = Label(self.window, text= "Hi"+self.name)
		self.u5 = Label(self.window, text=temp)
		self.u6 = Label(self.window, text=hum)
		self.u7 = Label(self.window, text="Switch 1"+stat(s1[0]))
		self.u8 = Label(self.window, text="Switch 2"+stat(s2[0]))
		self.u9 = Button(text="Logout", command=self.logout)

		self.u3.pack()
		self.u4.pack()
		self.u5.pack()
		self.u6.pack()
		self.u7.pack()
		self.u8.pack()
		self.u9.pack()

		


	def logout(self):
		self.u3.pack_forget()
		self.u4.pack_forget()
		self.u5.pack_forget()
		self.u6.pack_forget()
		self.u7.pack_forget()
		self.u8.pack_forget()
		self.u9.pack_forget()
		self.create()


	
	def reset(self):
		self.u3.pack_forget()
		self.u4.pack_forget()
		self.u5.pack_forget()
		self.u6.pack_forget()
		self.u7.pack_forget()
		self.u8.pack_forget()
		self.u9.pack_forget()

	def  regreset(self):
		self.u3.pack_forget()
		self.u4.pack_forget()
		self.u5.pack_forget()
		self.u6.pack_forget()
		self.u7.pack_forget()
		self.u8.pack_forget()
		self.u9.pack_forget()
		self.u10.pack_forget()
		self.u11.pack_forget()
		self.u12.pack_forget()
		self.u13.pack_forget()
		self.u14.pack_forget()
		self.u15.pack_forget()
		self.u16.pack_forget()
		self.u17.pack_forget()

	def login(self):
		self.regreset()
		self.create()

	def reg(self):
		self.reset()
		self.u3 = Label(self.window, text=self.status)
		self.u4 = Label(self.window, text="First Name:")
		self.u5 = Entry(self.window)
		self.u6 = Label(self.window, text="Last Name:")
		self.u7 = Entry(self.window)
		self.u8 = Label(self.window, text="Phone No:")
		self.u9 = Entry(self.window)
		self.u10 = Label(self.window, text="Email:")
		self.u11 = Entry(self.window)
		self.u12 = Label(self.window, text="Password :")
		self.u13 = Entry(self.window, show="*")
		self.u14 = Label(self.window, text="Re Password :")
		self.u15 = Entry(self.window, show="*")
		self.u16 = Button(text="Register", command=self.register)
		self.u17 = Button(text="Login", command=self.login)

		self.u3.pack()
		self.u4.pack()
		self.u5.pack()
		self.u6.pack()
		self.u7.pack()
		self.u8.pack()
		self.u9.pack()
		self.u10.pack()
		self.u11.pack()
		self.u12.pack()
		self.u13.pack()
		self.u14.pack()
		self.u15.pack()
		self.u16.pack()
		self.u17.pack()


	def create(self):
		self.u3 = Label(self.window, text=self.status)
		self.u4 = Label(self.window, text="Email:")
		self.u5 = Entry(self.window)
		self.u6 = Label(self.window, text="Password:")
		self.u7 = Entry(self.window, show="*")
		self.u8 = Button(text="Login", command=self.set)
		self.u9 = Button(text="Register", command=self.reg)

		self.u3.pack()
		self.u4.pack()
		self.u5.pack()
		self.u6.pack()
		self.u7.pack()
		self.u8.pack()
		self.u9.pack()


root = Tk() 
app=App(root)
root.mainloop()