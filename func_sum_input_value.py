def sum(num1):
	sumV = 0
	while 1<=int(num1):
		sumV += int(num1)
		num1 = num1 - 1
	return sumV

num = int(input('Please input a num:'))
print "sum: " + str(sum(num))

