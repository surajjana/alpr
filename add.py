from subprocess import call
import numpy as np
import cv2
import MySQLdb
import time

cap = cv2.VideoCapture(1)
db = MySQLdb.connect("localhost","root","root123","test")
cursor = db.cursor()

while(True):

    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	cv2.imwrite('test_snap.png',frame)
        cap.release()
        cv2.destroyAllWindows()
        break

doj = str(time.time())
status = 0
status_time = "NULL"

call("alpr -c eu -n 1 test_snap.png > out.txt", shell=True)
fo = open("out.txt", "r+")
data = fo.read()
if data == 'No license plates found.\n':
  print "Invalid image..."
else:
  data = data.split("-")
  data = data[1].split("\t")
  data = data[0].split(" ")
  data = data[1]

  uname = raw_input("Enter User Name : ")
  email = raw_input("Enter Email : ")
  phone = raw_input("Enter Phone No. : ")
  dept = raw_input("Enter Department : ")
  lnum = str(data)

  sql = "INSERT INTO alpr(uname,email,phone,doj,dept,lnum,status,status_time) VALUES('"+uname+"','"+email+"','"+phone+"','"+doj+"','"+dept+"','"+lnum+"',"+str(status)+",'"+status_time+"')"
  try:
    cursor.execute(sql)
    db.commit()
    #data = cursor.fetchall()
    print "Vehicle added!!"
  except:
    print "Error... :("
  db.close()