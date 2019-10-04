file_name = '../day09/pi_digits.txt'
try:
	with open(file_name) as file_object:
		contents = file_object.readline()
except FileNotFoundError:
	print("file not find")
else:
	print(contents)
	words = contents.split()
	num_words = len(words)
	print("The file name " + file_name + "has about " + str(num_words))

print("My name is %s and weight is %d kg!" % ('Zara', 21))
