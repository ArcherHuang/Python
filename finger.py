#-*-coding:utf-8-*-
import random

def type1(choice):
	typeList = ["石頭", "剪刀", "布"]
	return typeList[choice]

def computer():
	randomComputer = random.randint(0,2)
	print "電腦出: " + type1(randomComputer)
	return randomComputer

def result(me, computerNo):
	array = [["0", "1", "-1"], ["-1", "0", "1"], ["1", "-1", "0"]]
	return array[me][computerNo]

def whoWin(result):
	#print('whoWin: ', result)
	if int(result) == -1:
		print('結果  : 我輸')
	elif int(result) == 0:
		print('結果  : 沒輸贏')
	elif int(result) == 1:
		print('結果  : 我贏')

choice = int(raw_input('Please input a num (0:石頭 1:剪刀 2:布):'))
print "我出  : " + type1(choice)
whoWin(result(choice, computer()))