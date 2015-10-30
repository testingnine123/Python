#import regular expression module
import re

lst = list()

inp = raw_input('Enter file:')
try:
	if len(inp) < 1 : inp = 'regex_sum_171694.txt'
	file = open(inp)
except:
	print 'File not found'
	exit()
for line in file:
	line = line.rstrip()

	#find all the numbers in each line
	num = re.findall('[0-9]+',line)
	
	#sum all the numbers found in each line and store it as int in a list
	sum_line = sum(int (i) for i in num)
	lst.append(sum_line)

	#method 2 to sum all numbers
	"""for i in num:
		lst.append(int(i))"""

#print the sum of all the numbers in the list
print sum(lst)
