thistuple = ("apple", "banana", "cherry")  # note the double round-brackets
print(type(thistuple))

array = ["apple", "banana", "cherry", "banana"]

thisset = set(array)
print(type(thisset)) # 判断数据类型

print(set(array)) # set 无序且不重复的集合
if 'apple' in thisset:
	print("Yes apple is a friut!")

thisset.remove("apple")
if 'apple' in thisset:
	print("Yes apple is a friut!")


x = thisset.pop()
print(x)
print(thisset)



