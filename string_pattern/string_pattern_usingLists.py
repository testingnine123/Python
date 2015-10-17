count = 0
inp = raw_input('Enter file name: ')
try:
	file = open(inp)
except:
	print 'File not found'
	exit()
for i in file:
	i = i.rstrip()
	#searching for the line starting with 'From (space)''
	if i.startswith('From '):
		count = count + 1
		#creating a list from that string
		lst = i.split()
		if i == []: continue
		#the second element in the list is what we need
		print lst[1]
print "There were", count, "lines in the file with From as the first word"
print lst
