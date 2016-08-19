# *****************************************************************************************
# Version:     2016.08.19 
# Author:      Archer Huang
# License:     MIT
# Description: finger guess
# *****************************************************************************************

#!/usr/bin/python

import random

def type1(choice):
	typeList = ["stone", "scissors", "cloth"]
	return typeList[choice]

def computer():
	randomComputer = random.randint(0,2)
	print("computer is: ", randomComputer)
	type1(randomComputer)
	return randomComputer

def getResult(me, computerNo):

	#           scissors cloth    stone
	# scissors     0       1       -1
	# cloth       -1       0        1     
	# stone        1      -1        0

	array = [["0", "1", "-1"], ["-1", "0", "1"], ["1", "-1", "0"]]
	return array[me][computerNo]

def whoWin(result):
	print('whoWin: ', result)
	if int(result) == -1:
		print('you lose')
	elif int(result) == 0:
		print('equal')
	elif int(result) == 1:
		print('you win')

choice = int(input('Please input a num (0:stone 1:scissors 2:cloth):'))
print("me: ", type1(choice))

computerType = computer()
compareResult = getResult(choice, computerType)
whoWin(compareResult)

