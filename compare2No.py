def compare2no (num1, num2):
	if num1 == num2:
		return (num1,' equal ',num2)
	elif num1 < num2:
		return (num1,' Less than ',num2)
	else:
		return (num1,' more than ',num2)

num1 = int(input('Please input a num1:'))
num2 = int(input('Please input a num2:'))

print compare2no(num1, num2)
