print ("                    Basic Calculator")

while True:

	A= int(input("Enter your first number: "))
	op= input("Enter Operation: ")
	B= int(input("Enter your second number:"))

	if op =="+":
		print("The sum of ",A, "and", B, "is ",A+	B,)
	
	elif op =="-":
		print("The difference between", A,			"and",B, "is ",A-B)
	
	elif op =="*":
		print("The product of", A,"and",B, "is ",	A*B)
	
	elif op =="/":
		if B  != 0:
			print("The quotient of", A,"and",B, "is ",	A/B)
			
		else:
			print("Division by 0 is not possible")
		
		
	else:
		print("Wrong Operation!", "Please enter,+,-,*,or,/")
			
	print("       ")
		
	choice = input("Do you want to calculate more: Yes or No:    ")

	if choice == "Yes":
		print("                     Calculator ")
	
	elif choice =="No":
		print("Calculator Closed")
		break
		