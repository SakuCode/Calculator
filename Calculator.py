#Basic Calculator
#Author: Saku Linnankoski
#version: 1.1

calculate = True	#Calculator is on

while calculate:

	opetation = input("Enter add/sub/mul/div \n")
	
	#Check operation
	while (opetation == "add"
	or opetation == "sub" 
	or opetation == "mul" 
	or opetation == "div"):
		
		#Catch valueError
		try:
			x = int(input("Enter a number: \n"))
			y = int(input("Enter another number: \n"))
		except ValueError:
			print("Enter number!")
			continue
	
		if (opetation == "add"):	#Add operation
			print(x, "+" ,y, "=" , (x + y))
		
		elif (opetation == "sub"):	#Substract operation
			print(x, "-" , y, "=" , (x - y))
		
		elif (opetation == "mul"): #Multiply operation
			print(x, "*" ,y, "=" , (x * y))
		
		elif (opetation == "div"):	#Divide operation
			print(x, "/" ,y, "=" , (x / y))
	
		again = input("Calculate again?\n")
		
		while (again != "yes"):
			if (again == "no"):	#Stops calculating
				calculate = False
				break
			again = input("Calculate again?\n")
		
		break
