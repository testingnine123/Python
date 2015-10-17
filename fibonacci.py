def fib(list, n):
	for i in range(0,n):
		a = list[i] + list[i+1]
		list.append(a)
	print list
list = [0, 1]
n = input('Enter value of N ') 
fib(list, n)
