#!/usr/bin/python3
# This file prints digis from the system arguement
import sys
numberstring=sys.argv

digit_zero= (" 0 0", " 0 0")
digit_one=(" 1 1", " 1 1")
digit_two=(" 2 2", " 2 2")
digit_three=(" 3 3", " 3 3")
digit_four=(" 4 4", " 4 4")
digit_five=(" 5 5", " 6 6")
digit_six=(" 6 6", " 6 6")
digit_seven=(" 7 7", " 7 7")
digit_eight=(" 8 8", " 8 8")
digit_nine=(" 9 9", " 9 9")

alldigits=(digit_zero, digit_one, digit_two, digit_three, digit_four, digit_five,\
digit_six,digit_seven,digit_eight,digit_nine )

n_rows=len(digit_zero)
print("Number of rows is", n_rows)

number=[]
if numberstring[1]:
	try:
		number=int(numberstring[1])
	except ValueError as ValueError:
		print(ValueError)

if number:		
	print("System argument is ", numberstring, "number is :",number)
	for x in range(1,n_rows+1):
		currentline=''
		for digit in numberstring[1]:
			currentline+=alldigits[int(digit)][x-1]
			currentline+='  '
		print(currentline)

