#!/usr/bin/python
# *****************************************************************************************
# Version:     2016.06.21 
# Author:      Archer Huang
# License:     MIT
# Description: finger guess
# *****************************************************************************************

import random

def type1(choice):
	typeList = ["stone", "scissors", "cloth"]
	return typeList[choice]

def computer():
	randomComputer = random.randint(0,2)
	print("computer is: ", randomComputer)
	type1(randomComputer)
	return randomComputer

def result(me, computerNo):
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
whoWin(result(choice, computer()))