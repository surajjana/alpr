from subprocess import call

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
		print "Coming soon... :)"
	else :
		print "Exit.. :-D"
else:
	print "Invalid Credentials"