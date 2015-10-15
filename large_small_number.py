largest = None
smallest = None
while True:
	inp = raw_input('Num: ')
	if inp == 'done': break
	if len(inp) < 1: break
	try:
		num_int = int(inp)
	except:
		print 'Invalid input'
		
	if largest is None: largest = num_int
	if largest < num_int: largest = num_int
	
	if smallest is None: smallest = num_int
	if smallest > num_int: smallest = num_int
	
print 'Maximum is', largest
print 'Minimum is', smallest