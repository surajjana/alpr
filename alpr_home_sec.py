from Tkinter import *
import tkMessageBox
from subprocess import call
import MySQLdb
import time

db = MySQLdb.connect("localhost","root","hack123","test")
cursor = db.cursor()

master = Tk()
master.title("ALPR")
master.geometry("300x300")

l = Label(master, text="\nALPR Home Security\n\n")
l.pack()


def addVehicle():
	m = Tk()
	m.title("ALPR")
	m.geometry("300x300")

	l = Label(m, text="\nAdd Vehicle\n\n")
	l.pack()
	l1 = Label(m, text="License Plate No.")
	l1.pack()
	e1 = Entry(m)
	e1.pack()
	e1.focus_set()
	l2 = Label(m, text="User Name")
	l2.pack()
	e2 = Entry(m)
	e2.pack()
	e2.focus_set()
	l3 = Label(m, text="Email ID")
	l3.pack()
	e3 = Entry(m)
	e3.pack()
	e3.focus_set()
	l4 = Label(m, text="Phone No")
	l4.pack()
	e4 = Entry(m)
	e4.pack()
	e4.focus_set()
	l5 = Label(m, text="Department")
	l5.pack()
	e5 = Entry(m)
	e5.pack()
	e5.focus_set()

	def submitInfo():
		doj = str(time.time())
		status = 0
		status_time = "NULL"
		lnum = e1.get()
		uname = e2.get()
		email = e3.get()
		phone = e4.get()
		dept = e5.get()
		sql = "INSERT INTO alpr(uname,email,phone,doj,dept,lnum,status,status_time) VALUES('"+uname+"','"+email+"','"+phone+"','"+doj+"','"+dept+"','"+lnum+"',"+str(status)+",'"+status_time+"')"
		cursor.execute(sql)
		db.commit()
		tkMessageBox.showinfo( "ALPR", "Vehicle Added!!")
		exit(0)  

	b = Button(m, text="Submit", width=10, command=submitInfo)
	b.pack()
	mainloop()
	exit(0)

def searchVehicle():
	m = Tk()
	m.title("ALPR")
	m.geometry("300x300")

	l = Label(m, text="\nSearch Vehicle\n\n")
	l.pack()
	l1 = Label(m, text="User Name")
	l1.pack()
	e1 = Entry(m)
	e1.pack()
	e1.focus_set()

	def searchInfo():
		sql = "SELECT * FROM alpr WHERE uname='"+e1.get()+"'"
		try:
			cursor.execute(sql)
			data = cursor.fetchall()
			a = int(float(data[0][3]))
			tkMessageBox.showinfo( "ALPR Vehicle Info", "User Name : "+data[0][0]+"\nDOJ : "+time.strftime("%D %H:%M", time.localtime(int(str(a))))+"\nDepartment : "+data[0][4]+"\nVehicle No. : "+data[0][5])
		except:
			tkMessageBox.showinfo("ALPR Vehicle Info", "Error!!")
		exit(0)  

	b = Button(m, text="Submit", width=10, command=searchInfo)
	b.pack()
	mainloop()
	exit(0)

def deleteVehicle():
	m = Tk()
	m.title("ALPR")
	m.geometry("300x300")

	l = Label(m, text="\nDelete Vehicle\n\n")
	l.pack()
	l1 = Label(m, text="User Name")
	l1.pack()
	e1 = Entry(m)
	e1.pack()
	e1.focus_set()

	def deleteInfo():
		sql = "DELETE FROM alpr WHERE uname='"+e1.get()+"'"
		try:
			cursor.execute(sql)
			db.commit()
			tkMessageBox.showinfo( "ALPR Vehicle Info", "Vehicle removed!!")
		except:
			tkMessageBox.showinfo("ALPR Vehicle Info", "Error!!")
		exit(0)  

	b = Button(m, text="Submit", width=10, command=deleteInfo)
	b.pack()
	mainloop()
	exit(0)

def vehicleStatus():
	m = Tk()
	m.title("ALPR")
	m.geometry("300x300")

	l = Label(m, text="\nVehicle Status\n\n")
	l.pack()
	l1 = Label(m, text="User Name")
	l1.pack()
	e1 = Entry(m)
	e1.pack()
	e1.focus_set()

	def checkStatus():
		sql = "SELECT status,status_time FROM alpr WHERE uname='"+e1.get()+"'"
		try:
			cursor.execute(sql)
			data = cursor.fetchall()
			db.commit()
			status = ""
			if data[0][0] == 0:
				status = "Checked Out"
			else:
				status = "Checked In"
			if data[0][1]:
				time = "NULL"
			else:
				a = int(float(data[0][1]))
				time = time.strftime("%D %H:%M", time.localtime(int(str(a))))
			tkMessageBox.showinfo( "ALPR Vehicle Status", "Status : "+status+"\nTime : "+time)
		except:
			tkMessageBox.showinfo("ALPR Vehicle Status", "Error!!")
		exit(0)

	b = Button(m, text="Submit", width=10, command=checkStatus)
	b.pack()
	mainloop()
	exit(0)

def checkIn_Out():
	m = Tk()
	m.title("ALPR")
	m.geometry("300x300")

	l = Label(m, text="\nVehicle Status\n\n")
	l.pack()
	l1 = Label(m, text="User Name")
	l1.pack()
	e1 = Entry(m)
	e1.pack()
	e1.focus_set()

	def checkIn():
		sql = "select status from alpr where uname='"+e1.get()+"'"
		try:
			cursor.execute(sql)
			data = cursor.fetchall()
			if data[0][0] == 0:
				sql = "update alpr set status=1 where uname='"+e1.get()+"'"
				cursor.execute(sql)
				db.commit()
				tkMessageBox.showinfo( "ALPR Vehicle Status", "Checked In!!")	
			else:
				tkMessageBox.showinfo( "ALPR Vehicle Status", "Already Checked In!!")		
		except:
			tkMessageBox.showinfo("ALPR Vehicle Status", "Error!!")
		exit(0)
	def checkOut():
		sql = "select status from alpr where uname='"+e1.get()+"'"
		try:
			cursor.execute(sql)
			data = cursor.fetchall()
			if data[0][0] == 1:
				sql = "update alpr set status=0 where uname='"+e1.get()+"'"
				cursor.execute(sql)
				db.commit()
				tkMessageBox.showinfo( "ALPR Vehicle Status", "Checked Out!!")	
			else:
				tkMessageBox.showinfo( "ALPR Vehicle Status", "Already Checked Out!!")		
		except:
			tkMessageBox.showinfo("ALPR Vehicle Status", "Error!!")
		exit(0)

	b1 = Button(m, text="Check In", width=10, command=checkIn)
	b1.pack()
	b2 = Button(m, text="Check Out", width=10, command=checkOut)
	b2.pack()
	mainloop()
	exit(0)

b1 = Button(master, text="Add Vehicle", width=10, command=addVehicle)
b1.pack()
b2 = Button(master, text="Search Vehicle", width=10, command=searchVehicle)
b2.pack()
b3 = Button(master, text="Delete Vehicle", width=10, command=deleteVehicle)
b3.pack()
b4 = Button(master, text="Vehicle Status", width=10, command=vehicleStatus)
b4.pack()
b5 = Button(master, text="Check-In/Out", width=10, command=checkIn_Out)
b5.pack()

mainloop()