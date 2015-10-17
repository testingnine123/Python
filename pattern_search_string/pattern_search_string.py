inp = raw_input('Enter filename: ')
try:
	file = open(inp)
except:
	print 'File can not be opened'
	quit()
count = 0
sum = 0
for i in file:
	i = i.rstrip()
	if i.startswith('X-DSPAM-Confidence'):
		#count the number of times the above word occurs
		count = count + 1
		#break the sentence to find only the confidence number
		pos = i.find(':')
		#sum all the confidence number obtained
		sum = sum + float(i[(pos+1):len(i)])
#print sum		
#print count
print'Average confidence is: ', sum / count
