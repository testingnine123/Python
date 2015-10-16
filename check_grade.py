score = raw_input('Enter score between 0.0 and 1.0')
try:
    sr = float(score)
except ValueError:
    print 'That was not a number'
    quit()
if sr >=0.9:
    print 'A'
elif sr >= 0.8:
    print 'B'
elif sr >=0.7:
    print 'C'
elif sr >= 0.6:
    print 'D'
else:
    print 'F'