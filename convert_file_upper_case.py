inp = raw_input('Enter file name:')
file = open(inp)
for i in file:
	i = i.rstrip().upper()
	print i