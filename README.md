# Open ALPR Based Enhanced System

### Operating System : Ubuntu 14.04, 64-bit

### Setting up the openalpr

	wget -O - http://deb.openalpr.com/openalpr.gpg.key | sudo apt-key add -
	echo "deb http://deb.openalpr.com/master/ openalpr main" | sudo tee /etc/apt/sources.list.d/openalpr.list
	sudo apt-get update
	sudo apt-get install openalpr openalpr-daemon openalpr-utils libopenalpr-dev

### Setting up python libraries

	sudo apt-get update
	sudo apt-get install python-pip
	sudo apt-get install python-opencv
	sudo apt-get install python-numpy
	sudo apt-get install python-mysqldb

### Setting Up MySQL Server

	sudo apt-get install mysql-server