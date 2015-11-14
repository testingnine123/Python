#module to convert urls into files We don't need to use "socket" module.
import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
	#no header files from the html page would be sent
	print line.strip()