# gcd(54, 24) = 6

def gcd(x, y):
	tmp = 0
	while x % y != 0:
		tmp = y
		y = x % y
		x = tmp
    
	return y;

num1 = int(input('Please input a num1:'))
num2 = int(input('Please input a num2:'))
print "gcd: " + str(gcd(num1, num2))

