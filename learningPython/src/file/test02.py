print("Give me two numbers: ")
print("Enter 'q' to quit")
while True:
	first_number = int(input("first_number: "))
	if first_number == 'q':
		break
	second_number = int(input("second_number: "))
	if second_number == 'q':
		break
	result = 0
	try:
		result = first_number / second_number
	except ZeroDivisionError:
		print("You canit devide by 0")
	else:
		print(result)
