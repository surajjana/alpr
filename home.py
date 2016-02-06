from subprocess import call
import MySQLdb

db = MySQLdb.connect("localhost","root","hack123","test")
cursor = db.cursor()

uid = raw_input("Enter User ID : ")
pwd = raw_input("Enter Password : ")

if uid == 'admin' and pwd == '12345':
	print "1. Add vehicle"
	print "2. Vehicle status"
	print "3. Delete vehicle"
	print "4. Exit"

	r = raw_input("Enter your choice : ")

	if r == '1':
		call("python add.py",shell=True)
	elif r == '2':
		print "Coming soon... :)"
	elif r == '3':
		dname = raw_input("Enter User Name : ")

		sql = "SELECT * FROM alpr WHERE uname='"+dname+"'"
		try:
		  cursor.execute(sql)
		  db.commit()
		  data = cursor.fetchall()
		  #print data[0][0]
		  print "User Name : ",data[0][0]
		  print "DOJ : ",data[0][3]
		  print "Department : ",data[0][4]
		  print "Vehicle No. : ",data[0][5]
		  val = raw_input("\nDo you want to delete user?(y/n) : ")
		  if val == 'y' or val == 'Y':
		  	try:
		  		sql = "DELETE FROM alpr WHERE uname='"+dname+"'"
		  		cursor.execute(sql)
		  		db.commit()
		  		print "Vehicle removed..."
		  	except:
		  		print "Error... :("
		  else:
		  	print "Vehicle not removed..."
		except:
		  print "Error... :("
	else :
		print "Exit.. :-D"
else:
	print "Invalid Credentials"