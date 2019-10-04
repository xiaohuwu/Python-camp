'''
四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少
'''
array = [1, 2, 3, 4]
for item in array:
	other = array[:]
	other.remove(item)
	for x in other:
		anthoer = other[:]
		anthoer.remove(x)
		for y in anthoer:
			print(str(item) + str(x) + str(y))
