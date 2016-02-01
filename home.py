from subprocess import call

print "1. Add vehicle"
print "2. Search vehicle"
print "3. Delete vehicle"
print "4. Vehicle status"
print "5. Exit"

r = raw_input("Enter your choice : ")

if r == '1':
	call("python add.py",shell=True)

no prblm 
