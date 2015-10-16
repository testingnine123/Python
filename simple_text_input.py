while True:
	line = raw_input('Enter text ("done" to exit> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print line
print 'Done!'

