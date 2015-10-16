bigword = None
bigcount = None
inp = raw_input('Enter a file: ')
try:
	file = open(inp)
except:
	print 'File not found'
	exit()
#read the file and split it and store in one list
lst = []
for i in file:
	i = i.rstrip()
	i = i.split()
	for j in i:
		lst.append(j)
#create dictionary and store key-values
d = dict()
for words in lst:
	d[words] = d.get(words,0) + 1
#check the word with maximum value in the dictionary d
for key,value in d.items():
	if bigword == None or value > bigcount:
		bigword = key
		bigcount = value
print 'Word is', '"', bigword, '"', 'and count is ', bigcount