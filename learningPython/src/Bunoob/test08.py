
while True:
	print("input you name:")
	name = input("you name: ")
	if name != 'Joe':
		continue # 结束本次循环
	password = input("password:")
	if password == 'xiaohu':
		break  # 结束剩下的循环

print("Access granted")
