from Tkinter import *
import tkMessageBox
from subprocess import call

master = Tk()
master.title("ALPR")
master.geometry("300x300")

l = Label(master, text="\nLogin\n\n")
l.pack()
l1 = Label(master, text="User Name")
l1.pack()
e1 = Entry(master)
e1.pack()
e1.focus_set()
l2 = Label(master, text="Password")
l2.pack()
e2 = Entry(master, show="*")
e2.pack()
e2.focus_set()
l0 = Label(master, text="\n\n")
l0.pack()

def callback():
	if e1.get() == "admin" and e2.get() == "12345":
		#tkMessageBox.showinfo( "ALPR", "Loged In!! :)")
		call("python ./alpr_home.py", shell=True)
		exit(0)
	elif e1.get() == "sec" and e2.get() == "12345":
		call("python ./alpr_home_sec.py", shell=True)
		exit(0)
	else:
		tkMessageBox.showinfo( "ALPR", "Invalid Credentials!!")
		exit(0)

b = Button(master, text="Log In", width=10, command=callback)
b.pack()

mainloop()