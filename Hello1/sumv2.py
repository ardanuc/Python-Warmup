#!/usr/bin/python3
# htis program is pretty cool
# Just type sumv2.py < data.txt
print ("Type  integers followed by Enter or ^D")
count=0
total=0

while True:
	try:
		line=input()
		if line:
			number=int(line)
			count +=1
			total +=number
	except ValueError as ValueError:
		print(ValueError)
		continue
	except EOFError:
		break

if count:
	print ("count= ",count,"sum= ",total,"mean=", total/count)




