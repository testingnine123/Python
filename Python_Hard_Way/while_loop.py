from sys import argv

i = 0
numbers = []
max_limit = 6
script, add_value = argv
print add_value

while i < max_limit:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + int (add_value)
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num