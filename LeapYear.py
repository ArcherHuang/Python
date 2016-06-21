#!/usr/bin/python
# *****************************************************************************************
# Version:     2016.06.21 
# Author:      Archer Huang
# License:     MIT
# Description: 9 * 9
# *****************************************************************************************
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

leapYear = raw_input('Give me an leap year: ')
print leapYear

if int(leapYear) % 400 == 0 or ((int(leapYear) % 4 ==0 ) and (int(leapYear) % 100 != 0)):
	print "leap year"
else:
	print "common year"
