inp = raw_input('Enter file name:')
try:
	if len(inp) < 1 : inp = 'mbox-short.txt'
except:
	print 'File not found'

fh = open(inp)

for line in fh:
	if not line.startswith('From:') : continue
	line = line.strip()
	
	#this will print all line starting by "From:"
	if re.search('^From:',line) : print line

	#this will print all line starting by "From:"
	email = re.findall('^From.*', line)
	#print email

	#this will print only the domain name
	domain = re.findall('@([^ ]*)',line)
	print domain