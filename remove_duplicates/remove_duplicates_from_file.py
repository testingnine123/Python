lst = list()
inp = raw_input('Enter file name: ')
try:
	file = open(inp)
except:
	print 'File not found'
	exit()
for i in file:
    #this creates a list for the row
	i = i.split()
	#funtion to check duplicates in each line
	for j in i:
		if j not in lst:
			lst.append(j)
lst.sort()
print lst
