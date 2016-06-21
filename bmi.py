#!/usr/bin/python
# *****************************************************************************************
# Version:     2016.06.21 
# Author:      Archer Huang
# License:     MIT
# Description: BMI                                                                                 #
# *****************************************************************************************
# BMI =  weight(kg) / height (m) ^ 2
# Underweight : BMI < 18.5
# Overweight  : BMI >= 25
# Normal      : BMI >= 18.5 and BMI < 25
# *****************************************************************************************

heightNumber = raw_input('Give me an integer height: ')
print heightNumber
weightNumber = raw_input('Give me an integer weight: ')
print weightNumber

bmi = float(weightNumber)/((float(heightNumber)/100)**2)
print "BMI: " + str(bmi)
    
if bmi < 18.5:
	print "Underweight"
elif bmi >= 25:
	print "Overweight"
else:
	print "Normal"
