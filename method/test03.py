def make_pizza(size, *toppings):
	print("\n Making a "+ str(size) + "-inch pizza with the follow Toppings:")
	for item in toppings:
		print(item)
make_pizza(3,'good','bye','hellow')

#  from module_name import function_name 导入模块指定的函数
