lst = []
count = None
email = None
d = dict()
#read file
inp = raw_input('Enter a file:')
try:
	if len(inp) < 1:
		inp = 'mbox-short.txt'
	file = open(inp)
except:
	print 'File not found'
	exit()
#iterate through the file and find the string pattern and store it in a list
for i in file:
	if i.startswith('From '):
		i = i.split()
		lst.append(i[1])
#store the list in a dictionary along with the frequency of sender as value
for words in lst:
	d[words] = d.get(words,0) + 1
#print the key in the dictionary with the maximum value
for key,value in d.items():
	if email == None or value > count:
		email = key
		count = value
print email,count