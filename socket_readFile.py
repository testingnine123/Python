import socket

#the below line is like "open", what we used to do in file handling.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
	#receive 128 characters of data at a time
	data = mysock.recv(128)
	#get out of loop when EOF reached
	if (len(data) < 1): break
	print data

mysock.close()