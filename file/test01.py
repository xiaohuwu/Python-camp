# 读文件
file_name = '../day09/pi_digits.txt'

# 读文件
with open(file_name) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)

# 写文件

with open(file_name, 'w') as file_object:
	file_object.write("hello world\n")
	file_object.write("good study")




