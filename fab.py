# fab(10) = 55

def fab(n):
    fn_1 = 1
    fn_2 = 0
    i = 2
    tmp = 0
    if n <= 1: 
        return n
    for i in range(2, n+1):
    	tmp = fn_1
        fn_1 = fn_1 + fn_2
        fn_2 = tmp  
   
    return fn_1;

num = int(input('Please input a num:'))
print "fab: " + str(fab(num))

