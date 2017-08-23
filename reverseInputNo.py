num = int(raw_input('Please input a num: '))
res = ''
while num > 0:
	temp = num % 10
	num = num / 10
	res = res + str(temp)
print res