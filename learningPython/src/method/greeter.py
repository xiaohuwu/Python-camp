def get_formatted_name(first_name,last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

while True:
	print("Please tell me your name")
	f_name = input("first name:")
	if f_name == 'q':
		break
	l_name = input("Last name")
	format_name = get_formatted_name(f_name,l_name)
	print("\n Hello, "+format_name+"!")

